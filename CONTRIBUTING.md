# Guía de contribución

El informe se escribe en `report/`. `README.md` es el informe completo generado automáticamente. Cada integrante debe usar su propia identidad de Git y otro integrante debe revisar su Pull Request.

## Organización del informe

- `00–04`: carátula, registro de versiones, colaboración, contenido y Student Outcome.
- `11–17`: capítulos I–VII, con un Markdown por capítulo.
- `90–92`: conclusiones, bibliografía y anexos.
- `assets/capitulo-NN/`: imágenes del capítulo correspondiente. Las fotos del equipo van en el capítulo I y las evidencias de colaboración en el VII.
- `references/`: enunciado y documentos de referencia.

Los capítulos incluyen la estructura del enunciado. Se corrigieron sus saltos y duplicados de numeración manteniendo las secciones requeridas. Los bounded contexts se agregan como subsecciones dentro del capítulo V. Los sprints se documentan dentro del capítulo VII.

El README corresponde actualmente al **AV1, semana 4**: preliminares, capítulos I–IV y avances de conclusiones, bibliografía y anexos. Los capítulos V–VII conservan sus plantillas en `report/` para las próximas entregas, pero no aparecen en el README ni en su índice. El límite de capítulos se define con `LAST_CHAPTER = 4` en `scripts/build_report.py`; se actualiza y se regenera el README al ampliar el alcance de la entrega. Todas las fuentes se validan, incluidas las plantillas futuras.

## GitFlow

| Rama | Propósito | Origen | Destino |
| --- | --- | --- | --- |
| `main` | Versiones revisadas y entregadas | Inicialización | — |
| `develop` | Trabajo aprobado para la siguiente entrega | `main` | `release/...` |
| `feature/...` | Una sección o artefacto concreto | `develop` | `develop` |
| `release/X.Y.Z` | Preparación de una entrega | `develop` | `main` y `develop` |
| `hotfix/X.Y.Z` | Corrección urgente de una versión publicada | `main` | `main` y `develop` |

Las ramas de trabajo se nombran en inglés por tarea, por ejemplo `feature/ch02-interview-analysis`. Las versiones de entrega usan `X.Y.Z` y tags `vX.Y.Z`. El nombre del hito académico se registra en la descripción de la Release.

La inicialización del repositorio se registra en un único commit `chore(report): scaffold project report` en `main`, y `develop` parte de esa base. El scaffold incluye carátula, títulos, tablas pendientes y el generador configurado para AV1. El Registro de Versiones se actualiza en commits propios, por ejemplo `docs(report): add initial report version`. Los perfiles, fotos y aportes de integrantes se agregan desde `develop` en ramas como `feature/add-member-piero-sulca`, con commits como `docs(team): add piero sulca member profile`.

## Trabajo habitual

```bash
git switch develop
git pull --ff-only origin develop
git switch -c feature/ch02-interview-analysis
```

Edita los archivos de la sección y agrega las imágenes que necesites. Comprueba que el informe pueda compilarse sin modificar el README:

```bash
python3 -c 'from scripts.build_report import build; build()'
```

Registra tus cambios y publica la rama:

```bash
git add report/12-capitulo-02-requirements-elicitation-analysis.md assets/capitulo-02/
git commit -m "docs(ch02): analyze target segment interviews"
git push -u origin feature/ch02-interview-analysis
```

Abre un PR hacia `develop`. Explica las secciones modificadas y cómo verificaste los cambios. Otro integrante revisa redacción, contenido, fuentes e imágenes. Integra mediante **merge commit** para conservar los commits individuales.

Después del merge, GitHub Actions compila el informe y `github-actions[bot]` actualiza `README.md` si hay diferencias. Antes de comenzar otra tarea, actualiza tu `develop` para incluir ese commit.

## Conventional Commits

Formato: `type(scope): description`. Los mensajes de commit deben escribirse completamente en minúsculas y en inglés, incluida la descripción y los nombres propios.

```text
docs(ch01): add startup description
docs(ch02): analyze target segment interviews
docs(outcome): record delivery contributions
fix(assets): correct lean ux canvas path
chore(release): prepare release 0.1.0
```

Usa `docs` para el informe, `fix` para errores y `chore` para mantenimiento. El alcance identifica el capítulo, sección o componente modificado. Realiza commits por cambios coherentes y verificables.

## Markdown e imágenes

Usa encabezados ATX: `#` para el título de sección o capítulo, `##` para subsecciones, `###` y `####` para los niveles siguientes. El índice se genera hasta cuatro niveles. Evita duplicar encabezados innecesariamente.

`report/03-contenido.md` marca la ubicación del índice. Conserva su marcador `<!-- TABLE_OF_CONTENTS -->`; el script lo sustituye por los enlaces al compilar.

Desde cualquier archivo de `report/`, las imágenes se enlazan así:

```markdown
![Lean UX Canvas](../assets/capitulo-01/lean-ux-canvas.png)
```

Incluye una explicación del artefacto y su fuente cuando corresponda. Usa nombres descriptivos, en minúsculas y con guiones para imágenes. User Stories, Acceptance Criteria y backlogs se escriben como texto o tablas, acompañados de evidencias cuando corresponda.

## Generación y verificaciones locales

Se requiere Python 3.10 o superior; no se instalan paquetes adicionales.

```bash
python3 scripts/build_report.py
python3 scripts/build_report.py --check
python3 -m unittest discover -s scripts -p 'test_*.py'
```

El script lee los `.md` numerados de `report/` en orden, genera el índice y ajusta rutas de enlaces e imágenes para el README. Detecta archivos locales enlazados inexistentes y conflictos de Git pendientes. La comprobación de enlaces locales verifica la existencia del archivo; no consulta sitios externos ni valida sus fragmentos.

## Preparación de una entrega

1. Espera a que el bot termine de actualizar `develop` y actualiza tu rama local.
2. Crea `release/X.Y.Z` desde `develop`.
3. Revisa contenido, índice, imágenes, bibliografía y anexos. Actualiza Registro de Versiones, Collaboration Insights y Student Outcome con aportes reales por integrante.
4. Si cambias las fuentes en la rama de release, regenera el README y registra ese cambio. Ejecuta las verificaciones locales.
5. Abre un PR hacia `main`; la automatización exige que el README coincida con sus fuentes.
6. Tras integrar, crea el tag `vX.Y.Z` y la GitHub Release de la entrega. Integra también la rama de release en `develop`.

Para un hotfix, aplica el mismo criterio de revisión y compilación desde `main`, publica una versión de parche y devuelve la corrección a `develop`.

## Automatización

El workflow valida PR y pushes hacia `develop` y `main`. Solo el job de sincronización en `develop` tiene permiso de escritura y usa `GITHUB_TOKEN` para actualizar el README. No requiere una cuenta ni un token personal del bot.

Si se protege `develop`, la configuración de la rama debe permitir esta actualización automática; el permiso `contents: write` por sí solo no evita las restricciones de protección. `main` recibe las entregas mediante PR revisados.

Las versiones de las acciones utilizadas se documentan en [actions/checkout](https://github.com/actions/checkout) y [actions/setup-python](https://github.com/actions/setup-python).
