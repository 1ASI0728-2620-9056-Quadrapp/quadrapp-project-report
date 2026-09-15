#!/usr/bin/env python3
"""Compilar report/*.md en README.md usando solo la biblioteca estándar."""

import argparse
import html
import posixpath
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "<!-- Generado con python3 scripts/build_report.py. Editar report/*.md, no README.md. Guía: CONTRIBUTING.md -->"
TOC_MARKER = "<!-- TABLE_OF_CONTENTS -->"
# Alcance actual: AV1 (semana 4), capítulos I–IV.
LAST_CHAPTER = 4


def prose_blocks(text):
    """Keep fenced code examples intact when finding headings or rewriting links."""
    prose = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\n"))
        if fence:
            yield False, line
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match:
            if prose:
                yield True, "".join(prose)
                prose = []
            fence = match[1]
            yield False, line
        else:
            prose.append(line)
    if prose:
        yield True, "".join(prose)


def rewrite_links(text, source):
    def target(url):
        parts = urlsplit(html.unescape(url))
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
            return url
        path = posixpath.normpath(posixpath.join(source.parent.as_posix(), parts.path))
        local = ROOT / unquote(path)
        if not local.is_file():
            raise ValueError(f"{source}: archivo enlazado inexistente: {url}")
        return urlunsplit(("", "", path, parts.query, parts.fragment))

    def rewrite(block):
        # Mask inline code before rewriting HTML or Markdown links.
        code = []

        def protect(match):
            code.append(match[0])
            return f"\x00{len(code) - 1}\x00"

        block = re.sub(r"(`+).*?\1", protect, block)
        block = re.sub(
            r"(\b(?:src|href)\s*=\s*)([\"'])(.*?)(\2)",
            lambda m: m[1] + m[2] + target(m[3]) + m[4], block,
        )
        block = re.sub(
            r"(!?\[[^\]\n]*\]\()(<[^>\n]+>|[^\s)]+)",
            lambda m: m[1] + ("<" + target(m[2][1:-1]) + ">" if m[2].startswith("<") else target(m[2])),
            block,
        )
        block = re.sub(
            r"(?m)^( {0,3}\[[^\]\n]+\]:\s*)(<[^>\n]+>|\S+)",
            lambda m: m[1] + ("<" + target(m[2][1:-1]) + ">" if m[2].startswith("<") else target(m[2])),
            block,
        )
        return re.sub(r"\x00(\d+)\x00", lambda m: code[int(m[1])], block)

    return "".join(rewrite(block) if prose else block for prose, block in prose_blocks(text))


def headings(text):
    for prose, block in prose_blocks(text):
        if prose:
            for match in re.finditer(r"(?m)^ {0,3}(#{1,6})\s+(.+?)\s*$", block):
                title = re.sub(r"\s+#+\s*$", "", match[2])
                title = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", title)
                title = html.unescape(re.sub(r"<[^>]*>", "", title))
                title = re.sub(r"[*`~]", "", title)
                yield len(match[1]), title


def slug(title):
    return "".join(
        char for char in title.lower()
        if char in " -_" or unicodedata.category(char)[0] in "LNM"
    ).replace(" ", "-")


def build(last_chapter=LAST_CHAPTER):
    """Leer las fuentes en orden y sustituir el marcador por el índice real."""
    if last_chapter not in range(1, 8):
        raise ValueError("El último capítulo debe estar entre 1 y 7.")
    sources = sorted((ROOT / "report").glob("[0-9][0-9]-*.md"))
    if not sources:
        raise ValueError("No se encontraron fuentes en report/.")
    contents_file = ROOT / "report/03-contenido.md"
    if contents_file not in sources:
        raise ValueError("Falta report/03-contenido.md.")
    sections = []
    for source in sources:
        relative = source.relative_to(ROOT)
        text = source.read_text(encoding="utf-8")
        if re.search(r"(?m)^(<<<<<<< |=======\s*$|>>>>>>> )", text):
            raise ValueError(f"{relative}: conflicto de Git pendiente")
        markers = text.count(TOC_MARKER)
        if markers != (1 if source == contents_file else 0):
            raise ValueError(f"{relative}: marcador de contenido ausente, duplicado o fuera de lugar")
        text = rewrite_links(text, relative).strip()
        order = int(source.name[:2])
        if 11 <= order <= 17 and order - 10 > last_chapter:
            continue
        sections.append((source, text))

    used = set()
    toc = []
    for source, text in sections:
        for level, title in headings(text):
            base = slug(title)
            anchor = base
            count = 0
            while anchor in used:
                count += 1
                anchor = f"{base}-{count}"
            used.add(anchor)
            # Todos los títulos cuentan para los anclajes, incluso fuera del índice.
            if source.name == "00-caratula.md" or source == contents_file or level > 4:
                continue
            label = title.replace("[", "\\[").replace("]", "\\]")
            toc.append("  " * (level - 1) + f"- [{label}](#{anchor})")

    body = "\n\n---\n\n".join(text for _, text in sections)
    return NOTICE + "\n\n" + body.replace(TOC_MARKER, "\n".join(toc)) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Comprobar que README.md coincide con sus fuentes")
    args = parser.parse_args()
    try:
        report = build()
        output = ROOT / "README.md"
        if args.check:
            if not output.exists() or output.read_text(encoding="utf-8") != report:
                print("README.md desactualizado. Ejecutar: python3 scripts/build_report.py", file=sys.stderr)
                return 1
            print("README.md coincide con los archivos fuente.")
        else:
            output.write_text(report, encoding="utf-8")
            print("README.md generado.")
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
