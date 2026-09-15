"""Verificar compilación, anclajes y detección de fuentes inválidas."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_report


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "report").mkdir()
        (self.root / "assets").mkdir()
        self.write("00-caratula.md", "# Informe\n")
        self.write("02-collaboration-insights.md", "# Colaboración\n")
        self.write("03-contenido.md", "# Contenido\n\n<!-- TABLE_OF_CONTENTS -->\n")
        self.write("04-student-outcome.md", "# Student Outcome\n")
        root_patch = patch.object(build_report, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)

    def write(self, name, text):
        (self.root / "report" / name).write_text(text, encoding="utf-8")

    def test_order_toc_depth_and_duplicate_unicode_anchors(self):
        self.write("92-anexos.md", "# Anexos\n")
        self.write("17-capitulo-07.md", "# Capítulo VII\n\n## Revisión\n\n##### Revisión\n\n## Revisión\n\n#### 7.2.1.1. Sprint Planning\n\n```md\n# Invisible\n```\n")
        self.write("11-capitulo-01.md", "# Capítulo I\n")
        result = build_report.build(last_chapter=7)
        for first, second in (("Colaboración", "Contenido"), ("Contenido", "Student Outcome"), ("Student Outcome", "Capítulo I"), ("Capítulo I", "Capítulo VII"), ("Capítulo VII", "Anexos")):
            self.assertLess(result.index("\n# " + first + "\n"), result.index("\n# " + second + "\n"))
        self.assertIn("[Revisión](#revisión)", result)
        self.assertIn("[Revisión](#revisión-2)", result)
        self.assertNotIn("[Revisión](#revisión-1)", result)
        self.assertIn("[7.2.1.1. Sprint Planning](#7211-sprint-planning)", result)
        self.assertNotIn("[Invisible]", result)
        self.assertNotIn(build_report.TOC_MARKER, result)
        self.assertEqual(result, build_report.build(last_chapter=7))

    def test_avance_1_excludes_future_chapters_from_body_and_contents(self):
        for n in range(1, 8):
            self.write(f"{10 + n:02}-capitulo-{n:02}.md", f"# Capítulo {n}\n")
        for number, title in ((90, "Conclusiones"), (91, "Bibliografía"), (92, "Anexos")):
            self.write(f"{number}-{title}.md", "# " + title + "\n")
        result = build_report.build()
        for n in range(1, 5):
            self.assertIn(f"# Capítulo {n}\n", result)
            self.assertIn(f"[Capítulo {n}]", result)
        for n in range(5, 8):
            self.assertNotIn(f"Capítulo {n}", result)
        for title in ("Conclusiones", "Bibliografía", "Anexos"):
            self.assertIn("# " + title + "\n", result)

    def test_links_rebased_and_code_examples_untouched(self):
        (self.root / "assets/foto.png").write_bytes(b"image")
        self.write("11-capitulo-01.md", "# Capítulo I\n")
        text = '''![Foto](../assets/foto.png)
<img src="../assets/foto.png">
[Capítulo](11-capitulo-01.md#capítulo-i)
[Web](https://example.org)
[foto]: ../assets/foto.png "Foto"
`![Ejemplo](../assets/no-existe.png)`
```md
![Ejemplo](../assets/no-existe.png)
```
'''
        result = build_report.rewrite_links(text, Path("report/04-student-outcome.md"))
        self.assertIn("![Foto](assets/foto.png)", result)
        self.assertIn('<img src="assets/foto.png">', result)
        self.assertIn("[Capítulo](report/11-capitulo-01.md#capítulo-i)", result)
        self.assertIn('[foto]: assets/foto.png "Foto"', result)
        self.assertIn("[Web](https://example.org)", result)
        self.assertEqual(result.count("![Ejemplo](../assets/no-existe.png)"), 2)
        with self.assertRaisesRegex(ValueError, "archivo enlazado inexistente"):
            build_report.rewrite_links("![Foto](../assets/falta.png)", Path("report/11-capitulo-01.md"))

    def test_missing_marker_and_merge_conflict_fail(self):
        self.write("03-contenido.md", "# Contenido\n")
        with self.assertRaisesRegex(ValueError, "marcador"):
            build_report.build()
        self.write("03-contenido.md", "# Contenido\n\n<!-- TABLE_OF_CONTENTS -->\n")
        self.write("11-capitulo-01.md", "# Capítulo I\n<<<<<<< HEAD\nuno\n=======\ndos\n>>>>>>> branch\n")
        with self.assertRaisesRegex(ValueError, "conflicto de Git"):
            build_report.build()

    def test_check_detects_stale_readme(self):
        with patch("sys.argv", ["build_report.py"]):
            self.assertEqual(build_report.main(), 0)
        with patch("sys.argv", ["build_report.py", "--check"]):
            self.assertEqual(build_report.main(), 0)
            self.write("11-capitulo-01.md", "# Nuevo capítulo\n")
            self.assertEqual(build_report.main(), 1)


if __name__ == "__main__":
    unittest.main()
