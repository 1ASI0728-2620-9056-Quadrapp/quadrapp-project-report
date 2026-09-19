# Guía de contribución

El informe se escribe directamente en `README.md`, que es el informe completo. Cada integrante debe usar su propia identidad de Git y registrar su trabajo en una rama propia con su Pull Request hacia `develop`.

## Organización del informe

- `README.md`: informe completo en un solo archivo, con el orden del enunciado: carátula, registro de versiones, colaboración, contenido, Student Outcome, capítulos I–VII, conclusiones, bibliografía y anexos.
- `assets/capitulo-NN/`: imágenes del capítulo correspondiente. Las fotos del equipo van en el capítulo I y las evidencias de colaboración en el VII.
- `references/`: enunciado y documentos de referencia.

Los capítulos siguen la estructura del enunciado. Se corrigieron sus saltos y duplicados de numeración manteniendo las secciones requeridas. Los bounded contexts se agregan como subsecciones dentro del capítulo V. Los sprints se documentan dentro del capítulo VII.

El README corresponde actualmente al **AV1, semana 4**: preliminares, capítulos I–IV y avances de conclusiones, bibliografía y anexos. Los capítulos V–VII se agregan al ampliar el alcance de la entrega; sus plantillas originales quedan en el historial de Git (commit `91f2456`) y pueden recuperarse con `git show 91f2456:report/15-capitulo-05-tactical-level-software-design.md`.

Al editar un único archivo compartido, **los conflictos son la regla, no la excepción**. Trabaja solo en las secciones que te corresponden, actualiza tu rama con `develop` antes de abrir el PR y nunca reordenes ni reformatees secciones ajenas.

## GitFlow

| Rama | Propósito | Origen | Destino |
| --- | --- | --- | --- |
| `main` | Versiones revisadas y entregadas | Inicialización | — |
| `develop` | Trabajo aprobado para la siguiente entrega | `main` | `release/...` |
| `feature/...` | Una sección o artefacto concreto | `develop` | `develop` |
| `release/X.Y.Z` | Preparación de una entrega | `develop` | `main` y `develop` |
| `hotfix/X.Y.Z` | Corrección urgente de una versión publicada | `main` | `main` y `develop` |

Las ramas de trabajo se nombran en inglés y por tarea, no por persona: `feature/chapter-02-interview-analysis`, no `feature/pedro`. Las versiones de entrega usan `X.Y.Z` y tags `vX.Y.Z`. El nombre del hito académico se registra en la descripción de la Release.

Cada rama parte de `develop` actualizado y se integra apenas la sección esté completa. Una rama que se queda semanas sobre una base vieja acumula conflictos en el README y bloquea al resto.

## Trabajo habitual

```bash
git switch develop
git pull --ff-only origin develop
git switch -c feature/chapter-02-interview-analysis
```

Edita en `README.md` las secciones de tu tarea y agrega las imágenes que necesites. Antes de registrar los cambios, revisa tu propio diff:

```bash
git diff
```

Registra tus cambios y publica la rama:

```bash
git add README.md assets/capitulo-02/
git commit -m "docs(chapter-02): analyze target segment interviews"
git push -u origin feature/chapter-02-interview-analysis
```

Abre un PR hacia `develop` y créalo con el mensaje por default, que toma el título del commit:

```bash
gh pr create --fill --base develop
```

El equipo trabaja sin revisión cruzada: cada integrante integra su propio PR apenas termina su sección, sin esperar a nadie. Antes de hacerlo, revisa tu propio diff y confirma que no toca secciones de otros. Integra mediante **merge commit**, con el mensaje por default, para conservar los commits individuales:

```bash
gh pr merge <número> --merge
```

Antes de comenzar otra tarea, actualiza tu `develop`.

## Conventional Commits

Formato: `type(scope): description`. Los mensajes de commit deben escribirse completamente en minúsculas y en inglés, incluida la descripción y los nombres propios.

```text
docs(chapter-01): add startup description
docs(chapter-02): analyze target segment interviews
docs(outcome): record delivery contributions
fix(assets): correct lean ux canvas path
chore(release): prepare release 0.1.0
```

Usa `docs` para el informe, `fix` para errores y `chore` para mantenimiento. El alcance identifica el capítulo modificado con el mismo nombre que usan las ramas (`chapter-01`, `chapter-02`, …) o el componente afectado (`assets`, `outcome`, `release`). El mensaje es una sola línea: el detalle va en la descripción del Pull Request, no en el cuerpo del commit.

## Markdown e imágenes

Usa encabezados ATX: `#` para el título de sección o capítulo, `##` para subsecciones, `###` y `####` para los niveles siguientes. El índice del enunciado exige cuatro niveles de profundidad. Evita duplicar encabezados innecesariamente.

La sección Contenido se mantiene a mano: al agregar o renombrar un encabezado, actualiza su enlace en el índice. Los anclajes de GitHub se generan en minúsculas, con guiones en lugar de espacios y sin signos de puntuación.

Desde `README.md`, las imágenes se enlazan así:

```markdown
![Lean UX Canvas](assets/capitulo-01/lean-ux-canvas.png)
```

Usa formatos que GitHub renderice: `.png`, `.jpg` o `.webp`. Evita `.jfif`. Incluye una explicación del artefacto y su fuente cuando corresponda. Usa nombres descriptivos, en minúsculas y con guiones para las imágenes. User Stories, Acceptance Criteria y backlogs se escriben como texto o tablas, nunca como capturas de la herramienta, acompañados de evidencias cuando corresponda.

## Preparación de una entrega

1. Actualiza tu `develop` local e integra todas las ramas de la entrega.
2. Crea `release/X.Y.Z` desde `develop`.
3. Revisa contenido, índice, imágenes, bibliografía y anexos. Verifica la numeración de secciones contra el enunciado y la consistencia de los IDs entre capítulos: Epics, User Stories, Technical Stories, Quality Attribute Scenarios, Constraints y Architectural Drivers.
4. Actualiza Registro de Versiones, Collaboration Insights y Student Outcome con aportes reales por integrante.
5. Abre un PR hacia `main` y, si hay observaciones del equipo, corrígelas en la misma rama de release antes de integrar.
6. Tras integrar, crea el tag `vX.Y.Z` y la GitHub Release de la entrega. Integra también la rama de release en `develop`.

Para un hotfix, aplica el mismo criterio desde `main`, publica una versión de parche y devuelve la corrección a `develop`.

## Exportación del PDF

El entregable se exporta desde el repositorio. Abre el `README.md` de la entrega en GitHub e imprime a PDF, o usa una herramienta local de Markdown a PDF. Verifica que las imágenes y las tablas se rendericen completas antes de entregar.
