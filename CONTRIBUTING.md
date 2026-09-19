# Guía de contribución

## Organización del informe

- `README.md`: informe completo en un solo archivo, con el orden del enunciado: carátula, registro de versiones, colaboración, contenido, Student Outcome, capítulos, conclusiones, bibliografía y anexos.
- `assets/capitulo-NN/`: imágenes del capítulo correspondiente. Las fotos del equipo van en el capítulo I y las evidencias de colaboración en el VII.
- `references/`: enunciado y documentos de referencia.

Los capítulos siguen la estructura y la numeración del enunciado. Los bounded contexts se agregan como subsecciones dentro del capítulo V y los sprints dentro del capítulo VII.

El README corresponde actualmente al **Primer Hito, semana 4**: preliminares, capítulos I–IV y avances de conclusiones, bibliografía y anexos. Los capítulos V–VII se agregan al ampliar el alcance de la entrega; sus plantillas originales quedan en el historial de Git (commit `91f2456`).

Al editar un único archivo compartido, **los conflictos son la regla, no la excepción**. Trabaja solo en las secciones que te corresponden y nunca reordenes ni reformatees secciones ajenas.

## GitFlow

| Rama | Propósito | Origen | Destino |
| --- | --- | --- | --- |
| `main` | Versiones entregadas | Inicialización | — |
| `develop` | Trabajo integrado para la siguiente entrega | `main` | `main` |
| `feature/...` | Una sección o artefacto concreto | `develop` | `develop` |

Las ramas se nombran en inglés y por tarea, no por persona: `feature/chapter-02-interview-analysis`, no `feature/pedro`. Cada rama parte de `develop` actualizado y se integra apenas la sección esté completa: una rama que envejece sobre una base vieja acumula conflictos en el README y bloquea al resto.

## Trabajo habitual

```bash
git switch develop
git pull --ff-only origin develop
git switch -c feature/chapter-02-interview-analysis
```

Edita en `README.md` las secciones de tu tarea y agrega las imágenes que necesites. Registra los cambios y publica la rama:

```bash
git add README.md assets/capitulo-02/
git commit -m "docs(chapter-02): analyze target segment interviews"
git push -u origin feature/chapter-02-interview-analysis
```

Abre un Pull Request hacia `develop` con el título y la descripción por default e intégralo con **merge commit**, para conservar los commits individuales.

## Conventional Commits

Formato: `type(scope): description`. Los mensajes se escriben completamente en minúsculas y en inglés, incluida la descripción y los nombres propios, en una sola línea.

```text
docs(chapter-01): add startup description
docs(chapter-02): analyze target segment interviews
docs(outcome): record delivery contributions
fix(assets): correct lean ux canvas path
```

Usa `docs` para el informe, `fix` para errores y `chore` para mantenimiento. El alcance identifica el capítulo modificado con el mismo nombre que usan las ramas (`chapter-01`, `chapter-02`, …) o el componente afectado (`assets`, `outcome`). Realiza commits por cambios coherentes y verificables.

## Markdown e imágenes

Usa encabezados ATX: `#` para el título de sección o capítulo, `##` para subsecciones, `###` y `####` para los niveles siguientes. El índice del enunciado exige cuatro niveles de profundidad.

La sección Contenido se mantiene a mano: al agregar o renombrar un encabezado, actualiza su enlace en el índice. Los anclajes de GitHub se generan en minúsculas, con guiones en lugar de espacios y sin signos de puntuación.

Desde `README.md`, las imágenes se enlazan así:

```markdown
![Lean UX Canvas](assets/capitulo-01/lean-ux-canvas.png)
```

Usa formatos que GitHub renderice: `.png`, `.jpg` o `.webp`. Evita `.jfif`. Usa nombres descriptivos, en minúsculas y con guiones. Incluye una explicación del artefacto cuando corresponda. User Stories, Acceptance Criteria y backlogs se escriben como texto o tablas, nunca como capturas de la herramienta.

## Preparación de una entrega

1. Integra en `develop` todas las ramas de la entrega.
2. Revisa contenido, índice e imágenes. Verifica la numeración de secciones contra el enunciado y la consistencia de los IDs entre capítulos: Epics, User Stories, Technical Stories, Quality Attribute Scenarios, Constraints y Architectural Drivers.
3. Actualiza Registro de Versiones, Collaboration Insights y Student Outcome con los aportes reales de cada integrante.
4. Integra `develop` en `main` mediante Pull Request.

## Exportación del PDF

El entregable se exporta desde el repositorio. Abre el `README.md` de la entrega en GitHub e imprime a PDF, o usa una herramienta local de Markdown a PDF. Verifica que las imágenes y las tablas se rendericen completas antes de entregar.
