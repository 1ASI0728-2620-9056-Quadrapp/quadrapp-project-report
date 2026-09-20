<!-- Generado con python3 scripts/build_report.py. Editar report/*.md, no README.md. Guía: CONTRIBUTING.md -->

# Informe de Trabajo Final

<div align="center">
  <img src="assets/capitulo-01/upc-logo.png" alt="Universidad Peruana de Ciencias Aplicadas" width="120">
</div>

| Campo | Información |
| --- | --- |
| Universidad | Universidad Peruana de Ciencias Aplicadas |
| Carrera | Ingeniería de Software |
| Ciclo | 202620 |
| Curso | 1ASI0728 — Arquitecturas de Software Emergentes |
| Sección | 9056 |
| Profesor | Enrique Alejandro Valdivia Verde |
| Startup | Integra Labs |
| Producto | Quadrapp |
| Mes y año | Setiembre, 2026 |

**Integrantes**

| Nombres y apellidos | Código de estudiante |
| --- | --- |
| Becerra Tejeda, Alessandra Nicole | Por completar |
| Bejarano Martinez, Alvaro Leandro | Por completar |
| Melgarejo Gomez, Marcia Victoria | Por completar |
| Nanfuñay Liza, Pedro Jesus | Por completar |
| Sulca Sanchez, Piero Angel | u202423711 |

---

# Registro de Versiones del Informe

| Versión | Fecha | Autor | Descripción de modificación |
| --- | --- | --- | --- |
| 1.0 | 2026-09-15 | Sulca Sanchez, Piero Angel | Estructura inicial del informe para AV1. |

---

# Project Report Collaboration Insights

Repositorio del informe: [quadrapp-project-report](https://github.com/1ASI0728-2620-9056-Quadrapp/quadrapp-project-report).

El equipo elaborará el informe colaborativamente con GitFlow y Conventional Commits. Cada integrante registrará sus aportes con su propia cuenta y otro integrante revisará sus cambios antes de integrarlos en `develop`.

Las evidencias de colaboración se actualizarán en cada entrega y serán coherentes con el Registro de Versiones del Informe.

| Entrega | Actividades y aportes de los integrantes | Evidencias de colaboración y commits |
| --- | --- | --- |
| AV1 | Por completar | Por completar |

---

# Contenido

- [Registro de Versiones del Informe](#registro-de-versiones-del-informe)
- [Project Report Collaboration Insights](#project-report-collaboration-insights)
- [Student Outcome](#student-outcome)
- [Capítulo I: Introducción](#capítulo-i-introducción)
  - [1.1. Startup Profile](#11-startup-profile)
    - [1.1.1. Descripción de la Startup](#111-descripción-de-la-startup)
    - [1.1.2. Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
  - [1.2. Solution Profile](#12-solution-profile)
    - [1.2.1. Antecedentes y problemática](#121-antecedentes-y-problemática)
    - [1.2.2. Lean UX Process](#122-lean-ux-process)
      - [1.2.2.1. Lean UX Problem Statements](#1221-lean-ux-problem-statements)
      - [1.2.2.2. Lean UX Assumptions](#1222-lean-ux-assumptions)
      - [1.2.2.3. Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4. Lean UX Canvas](#1224-lean-ux-canvas)
  - [1.3. Segmentos objetivo](#13-segmentos-objetivo)
- [Capítulo II: Requirements Elicitation & Analysis](#capítulo-ii-requirements-elicitation--analysis)
  - [2.1. Competidores](#21-competidores)
    - [2.1.1. Análisis competitivo](#211-análisis-competitivo)
    - [2.1.2. Estrategias y tácticas frente a competidores](#212-estrategias-y-tácticas-frente-a-competidores)
  - [2.2. Entrevistas](#22-entrevistas)
    - [2.2.1. Diseño de entrevistas](#221-diseño-de-entrevistas)
    - [2.2.2. Registro de entrevistas](#222-registro-de-entrevistas)
    - [2.2.3. Análisis de entrevistas](#223-análisis-de-entrevistas)
  - [2.3. Needfinding](#23-needfinding)
    - [2.3.1. User Personas](#231-user-personas)
    - [2.3.2. User Task Matrix](#232-user-task-matrix)
    - [2.3.3. Empathy Mapping](#233-empathy-mapping)
    - [2.3.4. As-is Scenario Mapping](#234-as-is-scenario-mapping)
  - [2.4. Ubiquitous Language](#24-ubiquitous-language)
- [Capítulo III: Requirements Specification](#capítulo-iii-requirements-specification)
  - [3.1. To-Be Scenario Mapping](#31-to-be-scenario-mapping)
  - [3.2. User Stories](#32-user-stories)
  - [3.3. Impact Mapping](#33-impact-mapping)
  - [3.4. Product Backlog](#34-product-backlog)
- [Capítulo IV: Strategic-Level Software Design](#capítulo-iv-strategic-level-software-design)
  - [4.1. Strategic-Level Attribute-Driven Design](#41-strategic-level-attribute-driven-design)
    - [4.1.1. Design Purpose](#411-design-purpose)
    - [4.1.2. Attribute-Driven Design Inputs](#412-attribute-driven-design-inputs)
      - [4.1.2.1. Primary Functionality (Primary User Stories)](#4121-primary-functionality-primary-user-stories)
      - [4.1.2.2. Quality Attribute Scenarios](#4122-quality-attribute-scenarios)
      - [4.1.2.3. Constraints](#4123-constraints)
    - [4.1.3. Architectural Drivers Backlog](#413-architectural-drivers-backlog)
    - [4.1.4. Architectural Design Decisions](#414-architectural-design-decisions)
    - [4.1.5. Quality Attribute Scenario Refinements](#415-quality-attribute-scenario-refinements)
  - [4.2. Strategic-Level Domain-Driven Design](#42-strategic-level-domain-driven-design)
    - [4.2.1. EventStorming](#421-eventstorming)
    - [4.2.2. Candidate Context Discovery](#422-candidate-context-discovery)
    - [4.2.3. Domain Message Flows Modeling](#423-domain-message-flows-modeling)
    - [4.2.4. Bounded Context Canvases](#424-bounded-context-canvases)
    - [4.2.5. Context Mapping](#425-context-mapping)
  - [4.3. Software Architecture](#43-software-architecture)
    - [4.3.1. Software Architecture System Landscape Diagram](#431-software-architecture-system-landscape-diagram)
    - [4.3.2. Software Architecture Context Level Diagrams](#432-software-architecture-context-level-diagrams)
    - [4.3.3. Software Architecture Container Level Diagrams](#433-software-architecture-container-level-diagrams)
    - [4.3.4. Software Architecture Deployment Diagrams](#434-software-architecture-deployment-diagrams)
- [Conclusiones](#conclusiones)
  - [Conclusiones y recomendaciones](#conclusiones-y-recomendaciones)
  - [Video About-the-Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)
  - [Videos de Exposiciones](#videos-de-exposiciones)

---

# Student Outcome

El curso contribuye al cumplimiento del Student Outcome ABET:
ABET – EAC - Student Outcome 3

Criterio: Capacidad de comunicarse efectivamente con un rango de audiencias.
En el siguiente cuadro se describe las acciones realizadas y enunciados de
conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro
del ABET – EAC - Student Outcome 3.

<table>
  <thead>
    <tr>
      <th>Criterio específico</th>
      <th>Acciones realizadas</th>
      <th>Conclusiones</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Comunica oralmente sus ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerarquicos, en el marco del desarrollo de un proyecto en ingeniería.</td>
      <td>
        <p>
          <strong>Becerra Tejeda, Alessandra Nicole</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Bejarano Martinez, Alvaro Leandro</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Melgarejo Gomez, Marcia Victoria</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Nanfuñay Liza, Pedro Jesus</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Sulca Sanchez, Piero Angel</strong><br>
          AV1: Por completar.
        </p>
      </td>
      <td>Por completar.</td>
    </tr>
    <tr>
      <td>Comunica en forma escrita ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerarquicos, en el marco del desarrollo de un proyecto en ingeniería.</td>
      <td>
        <p>
          <strong>Becerra Tejeda, Alessandra Nicole</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Bejarano Martinez, Alvaro Leandro</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Melgarejo Gomez, Marcia Victoria</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Nanfuñay Liza, Pedro Jesus</strong><br>
          AV1: Por completar.
        </p>
        <p>
          <strong>Sulca Sanchez, Piero Angel</strong><br>
          AV1: Por completar.
        </p>
      </td>
      <td>Por completar.</td>
    </tr>
  </tbody>
</table>

---

# Capítulo I: Introducción

## 1.1. Startup Profile

### 1.1.1. Descripción de la Startup

Integra Labs es nuestra startup de desarrollo de soluciones digitales. Su producto para este proyecto es Quadrapp.

*Pendiente de completar la descripción del modelo de negocio y la propuesta de valor.*

### 1.1.2. Perfiles de integrantes del equipo

<table>
  <thead>
    <tr>
      <th>Foto</th>
      <th>Nombre completo</th>
      <th>Código</th>
      <th>Carrera</th>
      <th>Habilidades técnicas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Foto por completar</td>
      <td>Becerra Tejeda, Alessandra Nicole</td>
      <td>Por completar</td>
      <td>Ingeniería de Software</td>
      <td>Descripción por completar.</td>
    </tr>
    <tr>
      <td>Foto por completar</td>
      <td>Bejarano Martinez, Alvaro Leandro</td>
      <td>Por completar</td>
      <td>Ingeniería de Software</td>
      <td>Descripción por completar.</td>
    </tr>
    <tr>
      <td>Foto por completar</td>
      <td>Melgarejo Gomez, Marcia Victoria</td>
      <td>Por completar</td>
      <td>Ingeniería de Software</td>
      <td>Descripción por completar.</td>
    </tr>
    <tr>
      <td>Foto por completar</td>
      <td>Nanfuñay Liza, Pedro Jesus</td>
      <td>Por completar</td>
      <td>Ingeniería de Software</td>
      <td>Descripción por completar.</td>
    </tr>
    <tr>
      <td><img src="assets/capitulo-01/piero-sulca.jpg" alt="Sulca Sanchez, Piero Angel" width="160"></td>
      <td>Sulca Sanchez, Piero Angel</td>
      <td>u202423711</td>
      <td>Ingeniería de Software</td>
      <td>Curso la carrera de Ingeniería de Software y tengo experiencia en desarrollo web trabajando con equipos pequeños. Me apasiona el Front End, sobre todo cuando hay espacio para el diseño creativo: interfaces 3D, animaciones, productos que se ven y se sienten distintos. En el equipo puedo aportar en levantamiento de requerimientos, diseño de interfaces, desarrollo web con React y TypeScript, diseño de bases de datos. En el equipo aporto organización y colaboración.</td>
    </tr>
  </tbody>
</table>

## 1.2. Solution Profile

### 1.2.1. Antecedentes y problemática

*Pendiente de elaboración.*

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements

*Pendiente de elaboración.*

#### 1.2.2.2. Lean UX Assumptions

*Pendiente de elaboración.*

#### 1.2.2.3. Lean UX Hypothesis Statements

*Pendiente de elaboración.*

#### 1.2.2.4. Lean UX Canvas

*Pendiente de elaboración.*

## 1.3. Segmentos objetivo

*Pendiente de elaboración.*

---

# Capítulo II: Requirements Elicitation & Analysis

## 2.1. Competidores

### 2.1.1. Análisis competitivo

<table>
  <tr>
    <th colspan="6">Competitive Analysis Landscape</th>
  </tr>
  <tr>
    <th colspan="2">¿Por qué llevar a cabo este análisis?</th>
    <td colspan="4">
      Identificar cómo Quadrapp puede diferenciarse de las soluciones actuales de estacionamiento mediante la predicción de disponibilidad futura y su especialización en comunidades educativas, considerando las tecnologías, servicios y modelos de negocio utilizados por competidores locales e internacionales.
    </td>
  </tr>
  <tr>
    <th></th>
    <th></th>
    <th>
      Quadrapp<br>
      <img src="assets/capitulo-02/Quadrapp.png" alt="Quadrapp" width="100">
    </th>
    <th>
      Apparka<br>
      <img src="assets/capitulo-02/Apparka.jpg" alt="Apparka" width="100">
    </th>
    <th>
      ParkHelp<br>
      <img src="assets/capitulo-02/Parkhelp.png" alt="ParkHelp" width="100">
    </th>
    <th>
      ParkMobile<br>
      <img src="assets/capitulo-02/Parkmobile.png" alt="ParkMobile" width="100">
    </th>
  </tr>
  <tr>
    <th rowspan="2">Perfil</th>
    <th>Overview</th>
    <td>
      Plataforma inteligente orientada a estacionamientos universitarios que combina sensado IoT, información de ocupación, datos históricos y tiempo estimado de llegada para predecir la probabilidad de encontrar un espacio y brindar recomendaciones al conductor antes de llegar al campus.
    </td>
    <td>
      Plataforma peruana de estacionamientos y movilidad que permite localizar estacionamientos, consultar disponibilidad y utilizar diferentes servicios digitales asociados a su operación.
    </td>
    <td>
      Solución tecnológica orientada a la gestión y guiado inteligente de estacionamientos mediante sensores, cámaras, herramientas de monitoreo y análisis de ocupación.
    </td>
    <td>
      Plataforma digital de estacionamientos que ofrece servicios para conductores, operadores y universidades, facilitando la localización y gestión de espacios de estacionamiento.
    </td>
  </tr>
  <tr>
    <th>Ventaja competitiva<br>¿Qué valor ofrece a los clientes?</th>
    <td>
      Predice la disponibilidad futura según el tiempo estimado de llegada, combinando información de ocupación IoT en tiempo real, datos históricos, patrones de demanda y horarios académicos. Además, genera recomendaciones que ayudan al conductor a decidir hacia qué estacionamiento dirigirse.
    </td>
    <td>
      Cuenta con presencia en el mercado peruano y experiencia en la digitalización y gestión tecnológica de estacionamientos.
    </td>
    <td>
      Integra distintas tecnologías de hardware y software para detectar la ocupación de espacios, guiar conductores y analizar el comportamiento de los estacionamientos.
    </td>
    <td>
      Cuenta con experiencia en soluciones digitales de estacionamiento y dispone de propuestas orientadas a universidades y otros entornos de alta movilidad.
    </td>
  </tr>
  <tr>
    <th rowspan="2">Perfil de Marketing</th>
    <th>Mercado objetivo</th>
    <td>
      Universidades y centros educativos con estacionamientos propios. Sus usuarios finales son estudiantes, docentes y personal administrativo que se desplazan en vehículo hacia el campus.
    </td>
    <td>
      Conductores urbanos y organizaciones que requieren soluciones tecnológicas para la gestión de estacionamientos en Perú.
    </td>
    <td>
      Universidades, centros educativos, operadores de estacionamientos y organizaciones que buscan mejorar el monitoreo y aprovechamiento de sus espacios.
    </td>
    <td>
      Universidades, ciudades, operadores de estacionamientos, estudiantes, trabajadores y visitantes.
    </td>
  </tr>
  <tr>
    <th>Estrategias de Marketing</th>
    <td>
      Alianzas B2B con universidades, implementación de pilotos dentro de campus y demostraciones dirigidas a las áreas responsables de infraestructura, movilidad y gestión de estacionamientos.
    </td>
    <td>
      Promoción de su plataforma para conductores y organizaciones, junto con soluciones empresariales relacionadas con la gestión de estacionamientos.
    </td>
    <td>
      Estrategia principalmente B2B, ofreciendo soluciones tecnológicas adaptadas a las necesidades y características de cada instalación.
    </td>
    <td>
      Acuerdos con universidades, ciudades y operadores para incorporar sus soluciones digitales dentro de distintos entornos de estacionamiento.
    </td>
  </tr>
  <tr>
    <th rowspan="3">Perfil de Producto</th>
    <th>Productos &amp; Servicios</th>
    <td>
      Predicción de disponibilidad futura, monitoreo de ocupación en tiempo real mediante IoT, análisis histórico de demanda, recomendaciones de estacionamiento, notificaciones, aplicación móvil para conductores y dashboard web para administradores.
    </td>
    <td>
      Localización de estacionamientos, consulta de disponibilidad y herramientas digitales orientadas a conductores y operadores.
    </td>
    <td>
      Sensores de estacionamiento, sistemas de detección de ocupación, guiado inteligente, dashboards, estadísticas y herramientas de monitoreo y análisis.
    </td>
    <td>
      Localización de estacionamientos, herramientas digitales para conductores y soluciones de administración destinadas a operadores y universidades.
    </td>
  </tr>
  <tr>
    <th>Precios &amp; Costos</th>
    <td>
      Modelo propuesto de suscripción o licenciamiento institucional para universidades, considerando los costos asociados a infraestructura IoT, almacenamiento, procesamiento de datos y funcionamiento de la plataforma.
    </td>
    <td>
      Los costos dependen de los servicios y soluciones tecnológicas contratadas por cada organización o estacionamiento.
    </td>
    <td>
      Los costos dependen del hardware, cantidad de espacios, infraestructura y servicios requeridos para cada instalación, por lo que se determinan según cada proyecto.
    </td>
    <td>
      El modelo comercial depende de las características del servicio implementado y de los acuerdos establecidos con cada operador o institución.
    </td>
  </tr>
  <tr>
    <th>Canales de distribución<br>(Web y/o Móvil)</th>
    <td>
      Aplicación móvil para conductores y aplicación web con dashboard para administradores.
    </td>
    <td>
      Aplicación móvil y plataforma web.
    </td>
    <td>
      Plataforma web, infraestructura física e integraciones con sistemas instalados en los estacionamientos.
    </td>
    <td>
      Aplicación móvil y servicios web integrados con operadores y universidades.
    </td>
  </tr>
  <tr>
    <th rowspan="5">Análisis SWOT</th>
    <td colspan="5">
      Se identifican las fortalezas, debilidades, oportunidades y amenazas de Quadrapp y de sus principales competidores, considerando especialmente las capacidades relacionadas con monitoreo, disponibilidad, analítica y gestión inteligente de estacionamientos.
    </td>
  </tr>
  <tr>
    <th>Fortalezas</th>
    <td>
      Especialización en estacionamientos universitarios, predicción de disponibilidad futura, integración de información IoT en tiempo real, análisis histórico, consideración del contexto académico y generación de recomendaciones para los conductores.
    </td>
    <td>
      Presencia consolidada en Perú, experiencia operativa y conocimiento del mercado local de estacionamientos.
    </td>
    <td>
      Amplia variedad de tecnologías para estacionamientos, experiencia en soluciones universitarias e integración de sensores, monitoreo y analítica.
    </td>
    <td>
      Experiencia en soluciones para estacionamientos universitarios y presencia en distintos tipos de organizaciones y operadores.
    </td>
  </tr>
  <tr>
    <th>Debilidades</th>
    <td>
      Producto nuevo que requiere suficiente información histórica para mejorar sus predicciones. La instalación y mantenimiento de sensores IoT implica una inversión inicial y la calidad de las estimaciones depende de la confiabilidad de los datos recolectados.
    </td>
    <td>
      Su propuesta se encuentra principalmente orientada a la operación y disponibilidad actual del estacionamiento, sin especialización en predicción futura según el tiempo estimado de llegada al campus.
    </td>
    <td>
      Su propuesta depende considerablemente de infraestructura tecnológica instalada y se orienta principalmente al monitoreo y guiado, más que a una predicción personalizada según el momento de llegada del conductor.
    </td>
    <td>
      Su propuesta es amplia y está orientada a diferentes mercados, por lo que puede tener menor especialización en patrones académicos y comportamiento específico de comunidades universitarias.
    </td>
  </tr>
  <tr>
    <th>Oportunidades</th>
    <td>
      Creciente digitalización de campus, aprovechamiento de datos históricos y académicos para mejorar las predicciones y posibilidad de expansión futura hacia otros espacios con patrones recurrentes de movilidad.
    </td>
    <td>
      Expandir su experiencia e infraestructura hacia universidades y otros sectores con necesidades específicas de movilidad.
    </td>
    <td>
      Incorporar capacidades predictivas avanzadas utilizando la información generada por sus sensores y sistemas de monitoreo.
    </td>
    <td>
      Aprovechar los datos generados por sus usuarios para incorporar herramientas avanzadas de análisis y planificación de capacidad.
    </td>
  </tr>
  <tr>
    <th>Amenazas</th>
    <td>
      Competidores establecidos podrían incorporar funcionalidades predictivas; las instituciones podrían mostrar resistencia frente al costo de infraestructura; la falta de datos históricos o una baja precisión inicial podría afectar la confianza en las estimaciones.
    </td>
    <td>
      Aparición de soluciones especializadas que utilicen predicción, información histórica y análisis contextual como factores diferenciadores.
    </td>
    <td>
      Aparición de soluciones con menor dependencia de infraestructura física o modelos de implementación más económicos.
    </td>
    <td>
      Competidores especializados en sectores específicos pueden ofrecer experiencias más adaptadas a las necesidades particulares de cada institución.
    </td>
  </tr>
</table>

### 2.1.2. Estrategias y tácticas frente a competidores

A partir del análisis competitivo realizado, se identificaron oportunidades para posicionar Quadrapp sin competir directamente mediante características que ya se encuentran presentes en otras soluciones de estacionamiento. La estrategia principal será concentrarse en la predicción de disponibilidad futura y el análisis del comportamiento de los estacionamientos universitarios, aprovechando información propia del contexto académico.

**Frente a Apparka:**
Quadrapp no buscará diferenciarse únicamente mediante la visualización de estacionamientos disponibles o la gestión tradicional de espacios. La estrategia será enfocarse en la predicción de disponibilidad futura, permitiendo que los conductores conozcan la probabilidad de encontrar un espacio al momento estimado de llegada al campus.
Para ello, Quadrapp combinará información actual de ocupación con datos históricos, patrones de demanda y horarios académicos, ofreciendo una experiencia especializada en comunidades educativas.

**Frente a ParkHelp:**
Frente a ParkHelp, Quadrapp buscará complementar el monitoreo mediante sensores IoT con una capa de analítica histórica y predicción que transforme los datos de ocupación en información útil para los conductores.
La diferenciación no estará únicamente en detectar qué espacios están disponibles, sino en utilizar esa información para anticipar cómo podría evolucionar la ocupación en los siguientes minutos y generar recomendaciones según el momento estimado de llegada.

**Frente a ParkMobile:**
Frente a ParkMobile, Quadrapp priorizará una experiencia especializada en el contexto universitario. La solución utilizará información relacionada con horarios académicos, horas pico, comportamiento histórico y patrones recurrentes de demanda para generar estimaciones adaptadas a cada campus.
Este enfoque permitirá que tanto conductores como administradores obtengan información relacionada específicamente con el comportamiento de su comunidad educativa.

**Tácticas principales:**
- Implementar pilotos controlados en universidades antes de realizar despliegues de mayor escala.
- Recopilar información histórica desde las primeras etapas para mejorar progresivamente la capacidad de identificar patrones de demanda.
- Medir continuamente la precisión de las predicciones y compararlas con la disponibilidad realmente observada.
- Validar periódicamente la información generada por los sensores IoT comparándola con la ocupación real de los espacios.
- Analizar la relación entre fecha, hora, horarios académicos, horas pico y ocupación histórica para mejorar los modelos de predicción.
- Mostrar a los administradores mediante un dashboard información relacionada con ocupación actual, comportamiento histórico, períodos de mayor demanda y predicciones.
- Utilizar notificaciones únicamente cuando existan cambios relevantes que puedan modificar la decisión del conductor, evitando generar alertas innecesarias.
- Establecer alianzas directas con universidades para obtener datos, ejecutar pilotos y validar la solución en situaciones reales.
- Utilizar los resultados de los pilotos como evidencia de la reducción del tiempo de búsqueda y de la utilidad de las predicciones.
- Mejorar progresivamente los modelos de predicción conforme se disponga de una mayor cantidad de datos históricos por campus.

## 2.2. Entrevistas

### 2.2.1. Diseño de entrevistas

*Pendiente de elaboración.*

### 2.2.2. Registro de entrevistas

*Pendiente de elaboración.*

### 2.2.3. Análisis de entrevistas

*Pendiente de elaboración.*

## 2.3. Needfinding

### 2.3.1. User Personas

*Pendiente de elaboración.*

### 2.3.2. User Task Matrix

*Pendiente de elaboración.*

### 2.3.3. Empathy Mapping

*Pendiente de elaboración.*

### 2.3.4. As-is Scenario Mapping

*Pendiente de elaboración.*

## 2.4. Ubiquitous Language

*Pendiente de elaboración.*

---

# Capítulo III: Requirements Specification

## 3.1. To-Be Scenario Mapping

*Pendiente de elaboración.*

## 3.2. User Stories

*Pendiente de elaboración.*

## 3.3. Impact Mapping

*Pendiente de elaboración.*

## 3.4. Product Backlog

*Pendiente de elaboración.*

---

# Capítulo IV: Strategic-Level Software Design

## 4.1. Strategic-Level Attribute-Driven Design

### 4.1.1. Design Purpose

*Pendiente de elaboración.*

### 4.1.2. Attribute-Driven Design Inputs

#### 4.1.2.1. Primary Functionality (Primary User Stories)

*Pendiente de elaboración.*

#### 4.1.2.2. Quality Attribute Scenarios

*Pendiente de elaboración.*

#### 4.1.2.3. Constraints

*Pendiente de elaboración.*

### 4.1.3. Architectural Drivers Backlog

*Pendiente de elaboración.*

### 4.1.4. Architectural Design Decisions

*Pendiente de elaboración.*

### 4.1.5. Quality Attribute Scenario Refinements

*Pendiente de elaboración.*

## 4.2. Strategic-Level Domain-Driven Design

### 4.2.1. EventStorming

*Pendiente de elaboración.*

### 4.2.2. Candidate Context Discovery

*Pendiente de elaboración.*

### 4.2.3. Domain Message Flows Modeling

*Pendiente de elaboración.*

### 4.2.4. Bounded Context Canvases

*Pendiente de elaboración.*

### 4.2.5. Context Mapping

*Pendiente de elaboración.*

## 4.3. Software Architecture

### 4.3.1. Software Architecture System Landscape Diagram

*Pendiente de elaboración.*

### 4.3.2. Software Architecture Context Level Diagrams

*Pendiente de elaboración.*

### 4.3.3. Software Architecture Container Level Diagrams

*Pendiente de elaboración.*

### 4.3.4. Software Architecture Deployment Diagrams

*Pendiente de elaboración.*

---

# Conclusiones

## Conclusiones y recomendaciones

*Pendiente de elaboración.*

## Video About-the-Team

*Pendiente de elaboración.*

---

# Bibliografía

*Pendiente de elaboración.*

---

# Anexos

## Videos de Exposiciones

| Entrega | Enlace al video |
| --- | --- |
| AV1 | Por completar |
