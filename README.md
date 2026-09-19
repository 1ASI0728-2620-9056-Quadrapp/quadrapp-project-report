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

*Pendiente de elaboración.*

### 2.1.2. Estrategias y tácticas frente a competidores

*Pendiente de elaboración.*

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

El As-is Scenario Mapping permite visualizar cómo viven actualmente los usuarios el proceso de estacionar dentro de un campus universitario, antes de la introducción de Quadrapp. Para cada segmento objetivo se elaboró un mapa a partir de su User Persona, con las filas **Phases**, **Doing**, **Thinking** y **Feeling**.

El proceso seguido por el equipo fue el siguiente:

1. **Preparación:** se revisaron los User Personas, las entrevistas y el Empathy Mapping para definir el alcance de cada mapa y el escenario a analizar: "llegar al campus, estacionar y salir del estacionamiento".
2. **Lluvia de ideas individual:** cada integrante escribió por separado, en notas adhesivas, lo que el usuario hace, piensa y siente durante el proceso.
3. **Revisión e identificación de fases:** se agruparon las notas por afinidad y se definieron las fases como columnas del mapa.
4. **Nombrado de fases:** se asignó un nombre descriptivo a cada fase, orientado a la actividad del usuario.
5. **Etiquetado de áreas:** se identificaron las áreas positivas, las áreas negativas (puntos de dolor) y las *blank areas*, es decir, aquellas sobre las que el equipo necesita aprender más.


#### Conductores de la comunidad educativa

![As-is Scenario Mapping – Conductores de la comunidad educativa](./assets/capitulo-02/as-is-conductores.jpg)

**Áreas positivas:** el conductor cuenta con un estacionamiento gratuito dentro o cerca del campus, y la validación con credencial le da una sensación de seguridad.

**Áreas negativas (puntos de dolor):**
- Incertidumbre total antes de salir: solo dispone de información informal, no de datos.
- Tiempo perdido y desplazamientos innecesarios buscando espacio.
- Colas en el ingreso y la salida por la validación manual de credenciales.
- Congestión en los puntos de acceso durante las horas pico.

**Blank areas:**
- ¿Cuánto tiempo real dedican al día a buscar estacionamiento?
- ¿Cómo deciden actualmente a qué zona o estacionamiento dirigirse?
- ¿Qué alternativas usan cuando no encuentran espacio?

#### Administradores de estacionamientos universitarios

![As-is Scenario Mapping – Administradores de estacionamientos universitarios](./assets/capitulo-02/as-is-administradores.jpg)

**Áreas positivas:** cuenta con personal de vigilancia presente en el campus y con un control de acceso basado en la credencial institucional ya establecido.

**Áreas negativas (puntos de dolor):**
- Información de ocupación desactualizada o basada en recorridos manuales.
- Registros manuales propensos a error y difíciles de consolidar.
- Gestión reactiva de las horas de alta demanda.
- Ausencia de datos históricos organizados para analizar patrones.

**Blank areas:**
- ¿Cuántas personas intervienen hoy en el control de accesos y cuánto tiempo les toma?
- ¿Con qué herramientas registran actualmente la ocupación y los movimientos de vehículos?
- ¿Qué indicadores le piden a la administración las áreas de dirección?



## 2.4. Ubiquitous Language

En esta sección se define el Ubiquitous Language del dominio del proyecto, con el objetivo de establecer un lenguaje común entre todos los miembros del equipo y los stakeholders. Este glosario incluye términos clave del dominio de la gestión de estacionamientos en universidades y centros educativos, evitando ambigüedades y facilitando la comunicación durante el desarrollo de la solución.

| Term | Definition |
| --- | --- |
| Campus (Campus) | Espacio físico de la universidad o centro educativo donde se desarrollan las actividades académicas y donde se ubican los estacionamientos. |
| Educational Community (Comunidad Educativa) | Conjunto de estudiantes, docentes y personal administrativo que se trasladan regularmente al campus. |
| Driver (Conductor) | Miembro de la comunidad educativa que llega al campus en un vehículo y utiliza el estacionamiento. |
| Parking Administrator (Administrador de Estacionamiento) | Persona responsable de supervisar la ocupación, el acceso y la operación diaria de los estacionamientos de la institución. |
| Parking Lot (Estacionamiento) | Área destinada al aparcamiento de vehículos dentro o junto al campus, administrada por la institución. |
| Parking Zone (Zona de Estacionamiento) | Sección delimitada de un estacionamiento (nivel, sector o bloque) que agrupa un conjunto de espacios. |
| Parking Space (Espacio de Estacionamiento) | Lugar individual y delimitado donde puede estacionarse un vehículo. |
| Vehicle (Vehículo) | Automóvil u otro medio de transporte motorizado que ingresa al estacionamiento y está asociado a un conductor. |
| License Plate (Placa) | Identificador único de un vehículo, utilizado para asociarlo con su conductor y validar su acceso. |
| Authorized Vehicle (Vehículo Autorizado) | Vehículo registrado cuyo conductor tiene permiso para ingresar y utilizar el estacionamiento. |
| Occupancy (Ocupación) | Cantidad de espacios de estacionamiento ocupados en un momento determinado. |
| Availability (Disponibilidad) | Cantidad de espacios de estacionamiento libres en un momento determinado. |
| Availability Prediction (Predicción de Disponibilidad) | Estimación de cuántos espacios estarán libres en un momento futuro, basada en información actual e histórica. |
| Availability Probability (Probabilidad de Disponibilidad) | Nivel de posibilidad, expresado como porcentaje, de que el conductor encuentre un espacio libre al momento de su llegada. No constituye una garantía. |
| Estimated Time of Arrival (Tiempo Estimado de Llegada) | Momento en que se calcula que el conductor llegará al estacionamiento, según su ubicación y desplazamiento. |
| Historical Occupancy (Ocupación Histórica) | Registro de la ocupación del estacionamiento en fechas y horas pasadas, utilizado para identificar comportamientos recurrentes. |
| Academic Schedule (Horario Académico) | Calendario de clases y actividades de la institución que influye en los momentos de llegada y salida de los conductores. |
| Peak Hours (Horas Pico) | Períodos de mayor demanda de estacionamiento, generalmente al inicio y al término de las clases. |
| Demand Pattern (Patrón de Demanda) | Comportamiento recurrente en la cantidad de vehículos que buscan estacionar según el día, la hora o el calendario académico. |
| Congestion (Congestión) | Acumulación de vehículos dentro o alrededor del campus que dificulta la circulación, la búsqueda de espacio o el acceso. |
| Parking Search Time (Tiempo de Búsqueda de Estacionamiento) | Tiempo que un conductor invierte desde su llegada al campus hasta encontrar un espacio donde estacionar. |
| Reservation (Reserva) | Asignación anticipada de un espacio de estacionamiento a un conductor para un período determinado. |
| Entry (Ingreso) | Momento en que un vehículo autorizado accede al estacionamiento. |
| Exit (Salida) | Momento en que un vehículo abandona el estacionamiento y finaliza su estadía. |
| Parking Stay (Estadía) | Período comprendido entre el ingreso y la salida de un vehículo del estacionamiento. |
| Access Control (Control de Acceso) | Proceso mediante el cual se verifica que un vehículo o conductor pueda ingresar o salir del estacionamiento. |
| Access QR Code (Código QR de Acceso) | Código que el conductor presenta como alternativa de identificación cuando la placa no puede ser reconocida. |
| Access Exception (Excepción de Acceso) | Situación en la que el reconocimiento de la placa falla o el vehículo no puede validarse, requiriendo un mecanismo alternativo. |
| Parking Fee (Tarifa de Estacionamiento) | Monto que el conductor debe pagar por el uso del estacionamiento o por una reserva. |
| Payment (Pago) | Acción mediante la cual el conductor abona la tarifa correspondiente a su estadía o reserva. |
| Institutional License (Licencia Institucional) | Acuerdo mediante el cual una universidad o centro educativo contrata el uso de la solución para sus estacionamientos. |

<div style="break-after: page;"></div>

# Capítulo III: Requirements Specification

## 3.1. To-Be Scenario Mapping

El To-Be Scenario Mapping representa cómo se espera que los usuarios vivan el proceso de estacionar en el campus una vez que Quadrapp esté en funcionamiento. Para cada segmento objetivo se elaboró un mapa a partir de su User Persona, con las filas **Phases**, **Doing**, **Thinking** y **Feeling**.

El proceso seguido por el equipo fue el siguiente:

1. **Preparación:** se retomaron los As-is Scenario Mapping, los puntos de dolor identificados y las funcionalidades priorizadas de Quadrapp.
2. **Lluvia de ideas individual:** cada integrante propuso cómo cambiaría lo que el usuario hace, piensa y siente con la solución implementada.
3. **Revisión e identificación de fases:** se agruparon las ideas y se definieron las fases como columnas, buscando que fueran comparables con las del As-is.
4. **Nombrado de fases:** se asignó un nombre a cada fase, orientado a la experiencia mejorada del usuario.
5. **Comparación con el As-is:** se contrastó cada mapa con su versión As-is para identificar los cambios que Quadrapp aporta en cada fase.

Al igual que en el As-is, se mantiene que el estacionamiento es gratuito para la comunidad educativa y que la credencial de la UPC es obligatoria para ingresar.

#### Conductores de la comunidad educativa

![To-Be Scenario Mapping – Conductores de la comunidad educativa](assets/capitulo-03/to-be-conductores.jpg)

#### Administradores de estacionamientos universitarios

![To-Be Scenario Mapping – Administradores de estacionamientos universitarios](./assets/capitulo-03/to-be-administradores.jpg)

## 3.2. User Stories

**Epics:**

| Epic ID | Título                                        | Descripción                                                                                                                                                                            | User Stories Asociadas                   |
| ------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| EP01    | Acceso e identidad                            | Permitir que estudiantes, docentes y administradores accedan al sistema mediante autenticación institucional y gestionen su sesión de forma segura.                                    | US01, US02, US03                         |
| EP02    | Disponibilidad de estacionamientos            | Permitir consultar el estado actual de los estacionamientos universitarios, incluyendo espacios disponibles, ocupados y estados desconocidos por zona.                                 | US04, US05, US06, US07, US08             |
| EP03    | Predicción y asesoría de llegada              | Proporcionar predicciones de disponibilidad futura y asesoría de llegada considerando el tiempo estimado de llegada del usuario al estacionamiento.                                    | US09, US10, US11, US12, US13, US14, US15 |
| EP04    | Gestión e infraestructura de estacionamientos | Gestionar la configuración de estacionamientos, zonas, espacios y accesos vehiculares, además de la integración y monitoreo de los sensores IoT utilizados para detectar la ocupación. | US16, US17, US18, US19, US20, US21       |
| EP05    | Analítica y notificaciones                    | Permitir consultar información histórica de ocupación y periodos de mayor demanda, así como gestionar alertas y preferencias de notificación para los usuarios.                        | US22, US23, US24, US25                   |


**User Stories:**

<table> <thead> <tr> <th>Epic / US ID</th> <th>Título</th> <th>Descripción</th> <th>Criterios de Aceptación (Escenarios)</th> <th>Relacionado</th> </tr> </thead> <tbody>

<tr>
  <td><strong>US01</strong></td>
  <td>Inicio de sesión institucional</td>
  <td>Como estudiante, docente o personal administrativo, quiero iniciar sesión con mi cuenta institucional para acceder a las funcionalidades de QuadRapp según mi rol.</td>
  <td>
    <strong>Escenario 1: Inicio de sesión exitoso.</strong><br>
    Dado que el usuario posee una cuenta institucional válida,<br>
    cuando ingresa a QuadRapp e inicia sesión,<br>
    entonces el sistema permite su acceso a la aplicación.<br><br>
    <strong>Escenario 2: Credenciales inválidas.</strong><br>
    Dado que el usuario proporciona credenciales incorrectas,<br>
    cuando intenta iniciar sesión,<br>
    entonces el sistema muestra un mensaje indicando que las credenciales no son válidas.<br><br>
    <strong>Escenario 3: Sesión activa.</strong><br>
    Dado que el usuario ya tiene una sesión válida,<br>
    cuando vuelve a abrir la aplicación,<br>
    entonces el sistema mantiene su acceso sin solicitar nuevamente sus credenciales.
  </td>
  <td>EP01</td>
</tr>

<tr>
  <td><strong>US02</strong></td>
  <td>Cerrar sesión</td>
  <td>Como usuario, quiero cerrar mi sesión para evitar que otra persona pueda acceder a mi cuenta desde el dispositivo.</td>
  <td>
    <strong>Escenario 1: Cierre exitoso.</strong><br>
    Dado que el usuario tiene una sesión activa,<br>
    cuando selecciona la opción "Cerrar sesión",<br>
    entonces el sistema finaliza su sesión.<br><br>
    <strong>Escenario 2: Acceso posterior al cierre.</strong><br>
    Dado que el usuario cerró su sesión,<br>
    cuando intenta acceder a una funcionalidad protegida,<br>
    entonces el sistema solicita nuevamente la autenticación.<br><br>
    <strong>Escenario 3: Confirmación.</strong><br>
    Dado que el usuario selecciona "Cerrar sesión",<br>
    cuando confirma la acción,<br>
    entonces el sistema lo redirige a la pantalla de inicio de sesión.
  </td>
  <td>EP01</td>
</tr>

<tr>
  <td><strong>US03</strong></td>
  <td>Gestionar sesión expirada</td>
  <td>Como usuario, quiero que el sistema controle la expiración de mi sesión para mantener protegido mi acceso a QuadRapp.</td>
  <td>
    <strong>Escenario 1: Sesión expirada.</strong><br>
    Dado que la sesión del usuario ha expirado,<br>
    cuando intenta acceder a una funcionalidad protegida,<br>
    entonces el sistema solicita una nueva autenticación.<br><br>
    <strong>Escenario 2: Expiración durante el uso.</strong><br>
    Dado que el usuario está utilizando la aplicación,<br>
    cuando su sesión expira,<br>
    entonces el sistema muestra un mensaje indicando que debe iniciar sesión nuevamente.<br><br>
    <strong>Escenario 3: Nueva autenticación.</strong><br>
    Dado que la sesión anterior expiró,<br>
    cuando el usuario se autentica nuevamente de forma correcta,<br>
    entonces puede continuar utilizando QuadRapp.
  </td>
  <td>EP01</td>
</tr>

<tr>
  <td><strong>US04</strong></td>
  <td>Consultar estacionamientos universitarios</td>
  <td>Como usuario, quiero visualizar los estacionamientos disponibles dentro de mi universidad para identificar las áreas donde puedo estacionar.</td>
  <td>
    <strong>Escenario 1: Estacionamientos disponibles.</strong><br>
    Dado que existen estacionamientos configurados,<br>
    cuando el usuario ingresa a la sección de estacionamientos,<br>
    entonces el sistema muestra los estacionamientos disponibles.<br><br>
    <strong>Escenario 2: Estacionamiento fuera de servicio.</strong><br>
    Dado que un estacionamiento se encuentra fuera de servicio,<br>
    cuando el usuario consulta los estacionamientos,<br>
    entonces el sistema indica que dicho estacionamiento no se encuentra disponible.<br><br>
    <strong>Escenario 3: Sin estacionamientos configurados.</strong><br>
    Dado que no existen estacionamientos registrados,<br>
    cuando el usuario accede a la sección,<br>
    entonces el sistema muestra un mensaje informativo.
  </td>
  <td>EP02</td>
</tr>

<tr>
  <td><strong>US05</strong></td>
  <td>Consultar disponibilidad actual</td>
  <td>Como usuario, quiero conocer la disponibilidad actual de los espacios de estacionamiento para decidir dónde estacionar.</td>
  <td>
    <strong>Escenario 1: Espacios disponibles.</strong><br>
    Dado que existen datos actualizados de los sensores,<br>
    cuando el usuario consulta un estacionamiento,<br>
    entonces el sistema muestra los espacios libres y ocupados.<br><br>
    <strong>Escenario 2: Espacio ocupado.</strong><br>
    Dado que un sensor determina que un espacio está ocupado,<br>
    cuando se actualiza la información de disponibilidad,<br>
    entonces el espacio se muestra como ocupado.<br><br>
    <strong>Escenario 3: Espacio libre.</strong><br>
    Dado que un sensor determina que un espacio está libre,<br>
    cuando se actualiza la información,<br>
    entonces el espacio se muestra como disponible.
  </td>
  <td>EP02</td>
</tr>

<tr>
  <td><strong>US06</strong></td>
  <td>Consultar disponibilidad por zona</td>
  <td>Como usuario, quiero visualizar la disponibilidad agrupada por zonas para identificar rápidamente dónde existe mayor disponibilidad.</td>
  <td>
    <strong>Escenario 1: Consulta por zona.</strong><br>
    Dado que un estacionamiento posee varias zonas,<br>
    cuando el usuario consulta su disponibilidad,<br>
    entonces el sistema muestra el estado de cada zona.<br><br>
    <strong>Escenario 2: Zona con espacios disponibles.</strong><br>
    Dado que una zona contiene espacios libres y ocupados,<br>
    cuando el usuario consulta la zona,<br>
    entonces el sistema muestra su disponibilidad correspondiente.<br><br>
    <strong>Escenario 3: Zona sin información.</strong><br>
    Dado que una zona no posee información actualizada,<br>
    cuando el usuario consulta su estado,<br>
    entonces el sistema indica que la información no está disponible.
  </td>
  <td>EP02</td>
</tr>

<tr>
  <td><strong>US07</strong></td>
  <td>Actualizar disponibilidad</td>
  <td>Como usuario, quiero recibir actualizaciones de la ocupación de los estacionamientos para consultar información cercana al estado real.</td>
  <td>
    <strong>Escenario 1: Cambio a ocupado.</strong><br>
    Dado que un sensor detecta que un espacio cambia de libre a ocupado,<br>
    cuando el evento es procesado,<br>
    entonces el sistema actualiza el estado del espacio.<br><br>
    <strong>Escenario 2: Cambio a libre.</strong><br>
    Dado que un sensor detecta que un espacio cambia de ocupado a libre,<br>
    cuando el evento es procesado,<br>
    entonces el sistema refleja el nuevo estado.<br><br>
    <strong>Escenario 3: Sin nuevos eventos.</strong><br>
    Dado que no existen nuevos eventos de los sensores,<br>
    cuando el usuario consulta la disponibilidad,<br>
    entonces el sistema conserva el último estado válido registrado.
  </td>
  <td>EP02</td>
</tr>

<tr>
  <td><strong>US08</strong></td>
  <td>Gestionar estado desconocido</td>
  <td>Como usuario, quiero identificar cuándo un espacio no tiene información confiable para evitar interpretar un dato desactualizado como disponibilidad real.</td>
  <td>
    <strong>Escenario 1: Sensor sin comunicación.</strong><br>
    Dado que un sensor deja de enviar información durante el periodo configurado,<br>
    cuando se supera el tiempo establecido,<br>
    entonces el espacio pasa al estado <strong>UNKNOWN</strong>.<br><br>
    <strong>Escenario 2: Espacio desconocido.</strong><br>
    Dado que un espacio se encuentra en estado UNKNOWN,<br>
    cuando el usuario consulta la disponibilidad,<br>
    entonces el sistema no lo muestra como libre ni ocupado con certeza.<br><br>
    <strong>Escenario 3: Recuperación del sensor.</strong><br>
    Dado que un sensor vuelve a enviar información válida,<br>
    cuando el sistema recibe el nuevo evento,<br>
    entonces actualiza nuevamente el estado del espacio.
  </td>
  <td>EP02</td>
</tr>

<tr>
  <td><strong>US09</strong></td>
  <td>Consultar predicción de disponibilidad</td>
  <td>Como usuario, quiero consultar la disponibilidad futura de los estacionamientos para anticipar si encontraré un espacio al llegar al campus.</td>
  <td>
    <strong>Escenario 1: Predicción disponible.</strong><br>
    Dado que existen datos históricos suficientes,<br>
    cuando el usuario consulta una predicción,<br>
    entonces el sistema muestra la disponibilidad estimada.<br><br>
    <strong>Escenario 2: Identificación del horizonte.</strong><br>
    Dado que existe una predicción disponible,<br>
    cuando el usuario la consulta,<br>
    entonces el sistema indica el periodo futuro al que corresponde.<br><br>
    <strong>Escenario 3: Predicción no disponible.</strong><br>
    Dado que no existe una predicción disponible,<br>
    cuando el usuario realiza la consulta,<br>
    entonces el sistema muestra un mensaje informativo.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>US10</strong></td>
  <td>Consultar diferentes horizontes de predicción</td>
  <td>Como usuario, quiero consultar predicciones a 15, 30, 45 y 60 minutos para conocer cómo podría variar la disponibilidad antes de mi llegada.</td>
  <td>
    <strong>Escenario 1: Todos los horizontes disponibles.</strong><br>
    Dado que existen predicciones válidas,<br>
    cuando el usuario consulta la información futura,<br>
    entonces visualiza las predicciones de 15, 30, 45 y 60 minutos.<br><br>
    <strong>Escenario 2: Información parcial.</strong><br>
    Dado que solamente existen predicciones para algunos horizontes,<br>
    cuando el usuario realiza la consulta,<br>
    entonces el sistema muestra los datos disponibles e indica los faltantes.<br><br>
    <strong>Escenario 3: Predicción vencida.</strong><br>
    Dado que una predicción ya no corresponde al periodo vigente,<br>
    cuando el usuario consulta la información,<br>
    entonces el sistema evita mostrarla como predicción actual.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>US11</strong></td>
  <td>Visualizar nivel de saturación</td>
  <td>Como usuario, quiero visualizar el nivel de saturación esperado del estacionamiento para comprender rápidamente su disponibilidad futura.</td>
  <td>
    <strong>Escenario 1: Baja saturación.</strong><br>
    Dado que la predicción indica una ocupación baja,<br>
    cuando el sistema genera el resultado,<br>
    entonces muestra la categoría <strong>LOW</strong>.<br><br>
    <strong>Escenario 2: Saturación limitada.</strong><br>
    Dado que la predicción indica una ocupación cercana al límite,<br>
    cuando el sistema genera el resultado,<br>
    entonces muestra la categoría <strong>LIMITED</strong>.<br><br>
    <strong>Escenario 3: Alta saturación.</strong><br>
    Dado que la predicción indica una ocupación alta,<br>
    cuando el sistema genera el resultado,<br>
    entonces muestra la categoría <strong>HIGH</strong>.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>US12</strong></td>
  <td>Gestionar predicciones con datos insuficientes</td>
  <td>Como usuario, quiero recibir información clara cuando no existan suficientes datos para generar una predicción confiable.</td>
  <td>
    <strong>Escenario 1: Datos históricos insuficientes.</strong><br>
    Dado que el sistema no posee suficientes datos históricos,<br>
    cuando el usuario solicita una predicción,<br>
    entonces el sistema informa que la predicción no está disponible.<br><br>
    <strong>Escenario 2: Datos inconsistentes.</strong><br>
    Dado que los datos históricos presentan inconsistencias,<br>
    cuando el sistema intenta generar una predicción,<br>
    entonces evita mostrar una predicción no confiable.<br><br>
    <strong>Escenario 3: Datos suficientes.</strong><br>
    Dado que posteriormente existen suficientes datos válidos,<br>
    cuando se ejecuta nuevamente la predicción,<br>
    entonces el sistema puede generar el resultado.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>US13</strong></td>
  <td>Obtener asesoría de llegada</td>
  <td>Como usuario, quiero recibir una asesoría basada en la disponibilidad prevista y mi tiempo estimado de llegada para conocer las condiciones esperadas al llegar.</td>
  <td>
    <strong>Escenario 1: ETA válido.</strong><br>
    Dado que el usuario proporciona un tiempo estimado de llegada válido,<br>
    cuando solicita la asesoría,<br>
    entonces el sistema consulta la predicción correspondiente.<br><br>
    <strong>Escenario 2: Predicción disponible.</strong><br>
    Dado que existe una predicción para el momento estimado de llegada,<br>
    cuando se genera la asesoría,<br>
    entonces el sistema muestra la categoría de disponibilidad esperada.<br><br>
    <strong>Escenario 3: Sin información suficiente.</strong><br>
    Dado que no existe información suficiente para generar la asesoría,<br>
    cuando el usuario realiza la consulta,<br>
    entonces el sistema informa que no está disponible.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>US14</strong></td>
  <td>Actualizar asesoría según ETA</td>
  <td>Como usuario, quiero que la asesoría se actualice cuando cambie mi tiempo estimado de llegada para consultar información acorde a mi llegada prevista.</td>
  <td>
    <strong>Escenario 1: Cambio de ETA.</strong><br>
    Dado que cambia el tiempo estimado de llegada,<br>
    cuando el usuario solicita una actualización,<br>
    entonces el sistema recalcula la asesoría.<br><br>
    <strong>Escenario 2: Nuevo horizonte.</strong><br>
    Dado que el nuevo ETA corresponde a otro horizonte de predicción,<br>
    cuando se actualiza la asesoría,<br>
    entonces el sistema utiliza la predicción correspondiente.<br><br>
    <strong>Escenario 3: Nuevo ETA sin predicción.</strong><br>
    Dado que no existe una predicción para el nuevo ETA,<br>
    cuando el usuario solicita la actualización,<br>
    entonces el sistema informa que no existe información disponible.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>US15</strong></td>
  <td>Mostrar categoría de disponibilidad esperada</td>
  <td>Como usuario, quiero visualizar una categoría simple de disponibilidad esperada para interpretar rápidamente las condiciones del estacionamiento al momento de mi llegada.</td>
  <td>
    <strong>Escenario 1: Disponibilidad favorable.</strong><br>
    Dado que la disponibilidad esperada es favorable,<br>
    cuando se genera la asesoría,<br>
    entonces el sistema muestra la categoría <strong>LOW</strong>.<br><br>
    <strong>Escenario 2: Disponibilidad limitada.</strong><br>
    Dado que la disponibilidad esperada es limitada,<br>
    cuando se genera la asesoría,<br>
    entonces el sistema muestra la categoría <strong>LIMITED</strong>.<br><br>
    <strong>Escenario 3: Alta ocupación esperada.</strong><br>
    Dado que la disponibilidad esperada es desfavorable,<br>
    cuando se genera la asesoría,<br>
    entonces el sistema muestra la categoría <strong>HIGH</strong>.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>US16</strong></td>
  <td>Registrar estacionamiento universitario</td>
  <td>Como administrador de estacionamientos, quiero registrar los estacionamientos de la universidad para que puedan ser utilizados por QuadRapp.</td>
  <td>
    <strong>Escenario 1: Registro exitoso.</strong><br>
    Dado que el administrador proporciona los datos obligatorios,<br>
    cuando registra un estacionamiento,<br>
    entonces el sistema crea el estacionamiento correctamente.<br><br>
    <strong>Escenario 2: Datos incompletos.</strong><br>
    Dado que faltan datos obligatorios,<br>
    cuando el administrador intenta registrar el estacionamiento,<br>
    entonces el sistema solicita completar la información requerida.<br><br>
    <strong>Escenario 3: Registro duplicado.</strong><br>
    Dado que el estacionamiento ya existe,<br>
    cuando el administrador intenta registrarlo nuevamente,<br>
    entonces el sistema impide la duplicación.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>US17</strong></td>
  <td>Configurar zonas y espacios</td>
  <td>Como administrador de estacionamientos, quiero configurar las zonas y espacios de cada estacionamiento para representar su distribución física en QuadRapp.</td>
  <td>
    <strong>Escenario 1: Crear zona.</strong><br>
    Dado que el administrador selecciona un estacionamiento,<br>
    cuando crea una nueva zona,<br>
    entonces la zona queda asociada al estacionamiento correspondiente.<br><br>
    <strong>Escenario 2: Registrar espacio.</strong><br>
    Dado que existe una zona configurada,<br>
    cuando el administrador registra un espacio,<br>
    entonces el espacio queda asociado a dicha zona.<br><br>
    <strong>Escenario 3: Espacio duplicado.</strong><br>
    Dado que un espacio ya existe dentro de una zona,<br>
    cuando el administrador intenta registrarlo nuevamente,<br>
    entonces el sistema impide la duplicación.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>US18</strong></td>
  <td>Asociar sensor a espacio</td>
  <td>Como administrador de estacionamientos, quiero asociar cada sensor físico con su espacio correspondiente para identificar correctamente la ocupación.</td>
  <td>
    <strong>Escenario 1: Asociación exitosa.</strong><br>
    Dado que existe un sensor registrado y un espacio configurado,<br>
    cuando el administrador los asocia,<br>
    entonces el sistema guarda la relación.<br><br>
    <strong>Escenario 2: Sensor ya asociado.</strong><br>
    Dado que el sensor ya se encuentra asociado a otro espacio,<br>
    cuando el administrador intenta asociarlo nuevamente,<br>
    entonces el sistema impide la asociación duplicada.<br><br>
    <strong>Escenario 3: Desactivación.</strong><br>
    Dado que un sensor deja de estar operativo,<br>
    cuando el administrador lo desactiva,<br>
    entonces el sistema conserva su relación histórica con el espacio.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>US19</strong></td>
  <td>Configurar accesos vehiculares</td>
  <td>Como administrador de estacionamientos, quiero configurar los accesos de entrada y salida para registrar los movimientos de vehículos dentro del estacionamiento.</td>
  <td>
    <strong>Escenario 1: Registrar acceso.</strong><br>
    Dado que el administrador configura un nuevo acceso,<br>
    cuando proporciona sus datos,<br>
    entonces el acceso queda asociado al estacionamiento correspondiente.<br><br>
    <strong>Escenario 2: Acceso de entrada.</strong><br>
    Dado que un acceso está configurado como entrada,<br>
    cuando recibe un evento de movimiento vehicular,<br>
    entonces el sistema registra el evento como ingreso.<br><br>
    <strong>Escenario 3: Acceso de salida.</strong><br>
    Dado que un acceso está configurado como salida,<br>
    cuando recibe un evento de movimiento vehicular,<br>
    entonces el sistema registra el evento como salida.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>US20</strong></td>
  <td>Monitorear salud de sensores</td>
  <td>Como administrador de estacionamientos, quiero conocer el estado de los sensores para identificar dispositivos que presentan problemas de comunicación o funcionamiento.</td>
  <td>
    <strong>Escenario 1: Sensor operativo.</strong><br>
    Dado que un sensor reporta periódicamente su estado,<br>
    cuando el sistema recibe su reporte,<br>
    entonces registra la última comunicación del dispositivo.<br><br>
    <strong>Escenario 2: Sensor sin comunicación.</strong><br>
    Dado que un sensor deja de enviar información durante el tiempo establecido,<br>
    cuando se supera dicho periodo,<br>
    entonces el sistema identifica el dispositivo como no disponible.<br><br>
    <strong>Escenario 3: Recuperación.</strong><br>
    Dado que un sensor vuelve a comunicarse,<br>
    cuando el sistema recibe un nuevo reporte,<br>
    entonces actualiza nuevamente su estado.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>US21</strong></td>
  <td>Reconciliar eventos de entrada y salida</td>
  <td>Como sistema de ocupación, quiero contrastar los eventos de entrada y salida con los estados reportados por los sensores de espacios para detectar inconsistencias.</td>
  <td>
    <strong>Escenario 1: Registro de entrada.</strong><br>
    Dado que un acceso registra el ingreso de un vehículo,<br>
    cuando el evento es procesado,<br>
    entonces el sistema incorpora el movimiento al contexto de ocupación.<br><br>
    <strong>Escenario 2: Inconsistencia detectada.</strong><br>
    Dado que los eventos de entrada y salida presentan diferencias respecto a los estados de los espacios,<br>
    cuando el sistema realiza la validación,<br>
    entonces identifica la inconsistencia.<br><br>
    <strong>Escenario 3: Resolución.</strong><br>
    Dado que posteriormente se reciben nuevos eventos válidos,<br>
    cuando el sistema puede resolver la inconsistencia,<br>
    entonces actualiza el estado de ocupación correspondiente.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>US22</strong></td>
  <td>Consultar historial de ocupación</td>
  <td>Como administrador de estacionamientos, quiero consultar el historial de ocupación para analizar el comportamiento de los estacionamientos universitarios.</td>
  <td>
    <strong>Escenario 1: Consulta histórica.</strong><br>
    Dado que existen registros históricos,<br>
    cuando el administrador selecciona un periodo,<br>
    entonces el sistema muestra la información correspondiente.<br><br>
    <strong>Escenario 2: Filtrado por zona.</strong><br>
    Dado que existen registros de diferentes zonas,<br>
    cuando el administrador selecciona una zona,<br>
    entonces el sistema muestra la información correspondiente a dicha zona.<br><br>
    <strong>Escenario 3: Sin registros.</strong><br>
    Dado que no existen datos para el periodo seleccionado,<br>
    cuando el administrador realiza la consulta,<br>
    entonces el sistema muestra un mensaje indicando que no existen registros.
  </td>
  <td>EP05</td>
</tr>

<tr>
  <td><strong>US23</strong></td>
  <td>Identificar horas de mayor ocupación</td>
  <td>Como administrador de estacionamientos, quiero identificar los periodos con mayor ocupación para conocer los horarios de mayor demanda.</td>
  <td>
    <strong>Escenario 1: Identificación de horas pico.</strong><br>
    Dado que existen suficientes datos históricos,<br>
    cuando el administrador consulta la analítica,<br>
    entonces el sistema muestra los periodos de mayor ocupación.<br><br>
    <strong>Escenario 2: Comparación temporal.</strong><br>
    Dado que existen datos de diferentes días y horarios,<br>
    cuando el administrador consulta la información,<br>
    entonces puede identificar variaciones en los niveles de ocupación.<br><br>
    <strong>Escenario 3: Datos insuficientes.</strong><br>
    Dado que no existen suficientes datos históricos,<br>
    cuando el administrador consulta el análisis,<br>
    entonces el sistema informa que no existe información suficiente.
  </td>
  <td>EP05</td>
</tr>

<tr>
  <td><strong>US24</strong></td>
  <td>Recibir alertas de baja disponibilidad</td>
  <td>Como usuario, quiero recibir una alerta cuando la disponibilidad prevista del estacionamiento sea limitada o alta para anticipar posibles dificultades al estacionar.</td>
  <td>
    <strong>Escenario 1: Alerta generada.</strong><br>
    Dado que el usuario tiene habilitadas las notificaciones,<br>
    cuando la disponibilidad prevista alcanza el nivel configurado,<br>
    entonces el sistema genera una alerta.<br><br>
    <strong>Escenario 2: Notificaciones deshabilitadas.</strong><br>
    Dado que el usuario deshabilitó las notificaciones,<br>
    cuando se alcanza una condición de baja disponibilidad,<br>
    entonces el sistema no envía una notificación push.<br><br>
    <strong>Escenario 3: Evitar alertas repetitivas.</strong><br>
    Dado que ya se envió una alerta para una condición determinada,<br>
    cuando la misma condición continúa activa,<br>
    entonces el sistema evita generar alertas repetitivas innecesarias.
  </td>
  <td>EP05</td>
</tr>

<tr>
  <td><strong>US25</strong></td>
  <td>Gestionar preferencias de notificaciones</td>
  <td>Como usuario, quiero configurar mis preferencias de notificaciones para decidir qué alertas deseo recibir.</td>
  <td>
    <strong>Escenario 1: Activar notificaciones.</strong><br>
    Dado que el usuario accede a sus preferencias,<br>
    cuando habilita las notificaciones,<br>
    entonces el sistema guarda la configuración y permite recibir las alertas correspondientes.<br><br>
    <strong>Escenario 2: Desactivar notificaciones.</strong><br>
    Dado que el usuario deshabilita las notificaciones,<br>
    cuando se genera una alerta posterior,<br>
    entonces el sistema no envía la notificación push.<br><br>
    <strong>Escenario 3: Modificar preferencias.</strong><br>
    Dado que el usuario cambia sus preferencias,<br>
    cuando guarda la configuración,<br>
    entonces los nuevos valores se aplican a las siguientes notificaciones.
  </td>
  <td>EP05</td>
</tr>
</tbody> </table>


**Technical Stories:**

<table>
  <thead>
    <tr>
      <th>Epic / User Story ID</th>
      <th>Título</th>
      <th>Descripción</th>
      <th>Criterios de Aceptación</th>
      <th>Relacionado con (Epic ID)</th>
    </tr>
  </thead>
  <tbody>

<tr>
  <td><strong>TS01</strong></td>
  <td>Configuración de autenticación y gestión de sesiones</td>
  <td>Como desarrollador, quiero configurar el mecanismo de autenticación y gestión de sesiones de QuadRapp, para garantizar que los usuarios puedan acceder al sistema de forma segura y que las sesiones puedan validarse y finalizarse correctamente.</td>
  <td>
    <strong>Escenario 1: Autenticación exitosa.</strong><br>
    Dado que un usuario proporciona credenciales válidas,<br>
    cuando el proveedor de identidad valida las credenciales,<br>
    entonces el sistema permite el acceso a QuadRapp y establece una sesión válida.<br><br>
    <strong>Escenario 2: Credenciales no válidas.</strong><br>
    Dado que un usuario proporciona credenciales incorrectas,<br>
    cuando el proveedor de identidad procesa la autenticación,<br>
    entonces el acceso es rechazado y no se crea una sesión válida.<br><br>
    <strong>Escenario 3: Sesión expirada.</strong><br>
    Dado que la sesión del usuario ha expirado,<br>
    cuando intenta acceder a una funcionalidad protegida,<br>
    entonces el sistema solicita una nueva autenticación sin permitir el acceso a los recursos protegidos.
  </td>
  <td>EP01</td>
</tr>

<tr>
  <td><strong>TS02</strong></td>
  <td>Configuración del API Gateway y BFF para la aplicación móvil</td>
  <td>Como desarrollador, quiero configurar un punto de entrada para la aplicación móvil, para centralizar el acceso a los servicios de QuadRapp y facilitar la composición de información proveniente de diferentes contextos.</td>
  <td>
    <strong>Escenario 1: Enrutamiento de solicitudes.</strong><br>
    Dado que la aplicación móvil envía una solicitud válida,<br>
    cuando el gateway identifica el recurso solicitado,<br>
    entonces enruta la solicitud al servicio correspondiente.<br><br>
    <strong>Escenario 2: Composición de información.</strong><br>
    Dado que la aplicación solicita información de un estacionamiento,<br>
    cuando el BFF procesa la solicitud,<br>
    entonces puede combinar la configuración del estacionamiento, el estado actual y la asesoría disponible en una respuesta para la aplicación móvil.<br><br>
    <strong>Escenario 3: Servicio no disponible.</strong><br>
    Dado que uno de los servicios solicitados no está disponible,<br>
    cuando el gateway procesa la solicitud,<br>
    entonces retorna una respuesta controlada sin exponer errores internos de los servicios.
  </td>
  <td>EP01, EP02, EP03</td>
</tr>

<tr>
  <td><strong>TS03</strong></td>
  <td>Configuración de persistencia y aislamiento de datos por contexto</td>
  <td>Como desarrollador, quiero configurar la persistencia de datos de los principales contextos de QuadRapp, para mantener separados los datos de configuración, ocupación, predicción y analítica según sus responsabilidades.</td>
  <td>
    <strong>Escenario 1: Persistencia de configuración.</strong><br>
    Dado que un administrador registra la configuración de un estacionamiento,<br>
    cuando el servicio procesa la información,<br>
    entonces los datos del estacionamiento, zonas y espacios se almacenan correctamente.<br><br>
    <strong>Escenario 2: Persistencia de ocupación.</strong><br>
    Dado que se recibe un evento válido de cambio de estado de un espacio,<br>
    cuando el contexto de ocupación procesa el evento,<br>
    entonces actualiza el estado correspondiente y registra la información necesaria para su trazabilidad.<br><br>
    <strong>Escenario 3: Separación de responsabilidades.</strong><br>
    Dado que un contexto necesita consultar información de otro contexto,<br>
    cuando se realiza la integración,<br>
    entonces utiliza sus interfaces o eventos definidos sin acceder directamente a la persistencia interna del otro contexto.
  </td>
  <td>EP02, EP03, EP04, EP05</td>
</tr>

<tr>
  <td><strong>TS04</strong></td>
  <td>Implementación de ingesta de eventos IoT mediante gateway</td>
  <td>Como desarrollador, quiero implementar la recepción de eventos provenientes de los sensores mediante un gateway IoT, para integrar las lecturas de los dispositivos físicos con los servicios de QuadRapp sin exponer directamente los sensores a Internet.</td>
  <td>
    <strong>Escenario 1: Recepción de evento de espacio.</strong><br>
    Dado que un sensor detecta un cambio de estado en un espacio,<br>
    cuando el gateway recibe y publica el evento,<br>
    entonces el sistema registra un evento SpaceStateDetected con sensorId, estado, lectura, timestamp y eventId.<br><br>
    <strong>Escenario 2: Recepción de evento de entrada o salida.</strong><br>
    Dado que un sensor de acceso detecta el movimiento de un vehículo,<br>
    cuando el gateway procesa el evento,<br>
    entonces publica un evento VehicleMovementDetected indicando el acceso, dirección, timestamp y eventId.<br><br>
    <strong>Escenario 3: Pérdida temporal de conectividad.</strong><br>
    Dado que el gateway pierde temporalmente la conexión con el backend,<br>
    cuando continúa recibiendo eventos de los sensores,<br>
    entonces almacena temporalmente los eventos y los publica cuando se restablece la conectividad.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>TS05</strong></td>
  <td>Configuración de comunicación MQTT para eventos IoT</td>
  <td>Como desarrollador, quiero configurar MQTT para la comunicación entre el gateway y los servicios de QuadRapp, para transmitir eventos IoT de manera confiable y desacoplada.</td>
  <td>
    <strong>Escenario 1: Publicación de evento.</strong><br>
    Dado que el gateway recibe un evento válido de un dispositivo,<br>
    cuando publica el evento mediante MQTT,<br>
    entonces el mensaje llega al tópico correspondiente utilizando QoS 1.<br><br>
    <strong>Escenario 2: Reintento de entrega.</strong><br>
    Dado que un mensaje no puede ser confirmado inicialmente,<br>
    cuando MQTT procesa la entrega,<br>
    entonces realiza el mecanismo de retransmisión correspondiente para alcanzar la entrega al consumidor.<br><br>
    <strong>Escenario 3: Evento inválido.</strong><br>
    Dado que llega un mensaje que no cumple con el esquema definido,<br>
    cuando el consumidor valida el mensaje,<br>
    entonces rechaza el evento y evita actualizar el estado de ocupación con información inválida.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>TS06</strong></td>
  <td>Implementación de procesamiento e idempotencia de eventos de ocupación</td>
  <td>Como desarrollador, quiero implementar el procesamiento controlado de eventos de sensores, para evitar duplicidades, inconsistencias y cambios incorrectos en el estado de los espacios de estacionamiento.</td>
  <td>
    <strong>Escenario 1: Procesamiento de evento válido.</strong><br>
    Dado que se recibe un evento SpaceStateDetected válido,<br>
    cuando el contexto de ocupación procesa el evento,<br>
    entonces actualiza el estado del espacio asociado y registra la fecha de actualización.<br><br>
    <strong>Escenario 2: Evento duplicado.</strong><br>
    Dado que se recibe nuevamente un evento con un eventId ya procesado,<br>
    cuando el sistema valida la idempotencia,<br>
    entonces ignora el evento duplicado sin modificar nuevamente el estado del espacio.<br><br>
    <strong>Escenario 3: Lectura inconsistente.</strong><br>
    Dado que se recibe un evento fuera de orden o incompatible con el estado registrado,<br>
    cuando el sistema procesa el evento,<br>
    entonces aplica las reglas de ordenamiento y validación definidas antes de actualizar la ocupación.
  </td>
  <td>EP02, EP04</td>
</tr>

<tr>
  <td><strong>TS07</strong></td>
  <td>Implementación del modelo de predicción de ocupación</td>
  <td>Como desarrollador, quiero implementar el componente de predicción de disponibilidad utilizando datos históricos de ocupación y flujo vehicular, para generar pronósticos de disponibilidad futura de los estacionamientos.</td>
  <td>
    <strong>Escenario 1: Generación de predicción.</strong><br>
    Dado que existen datos históricos suficientes de ocupación,<br>
    cuando el modelo ejecuta una predicción,<br>
    entonces genera pronósticos de disponibilidad para los horizontes de 15, 30, 45 y 60 minutos.<br><br>
    <strong>Escenario 2: Inclusión de contexto temporal.</strong><br>
    Dado que el modelo procesa información histórica,<br>
    cuando genera una predicción,<br>
    entonces considera las variables temporales disponibles, como patrones de ocupación y calendario académico.<br><br>
    <strong>Escenario 3: Datos insuficientes.</strong><br>
    Dado que no existe suficiente información histórica para generar una predicción confiable,<br>
    cuando el sistema intenta ejecutar el modelo,<br>
    entonces informa que la predicción no está disponible o tiene datos insuficientes, sin generar un resultado no sustentado.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>TS08</strong></td>
  <td>Implementación del servicio de asesoría de llegada</td>
  <td>Como desarrollador, quiero implementar un servicio que combine la predicción de ocupación con el tiempo estimado de llegada del usuario, para generar una categoría de disponibilidad esperada al momento de llegada.</td>
  <td>
    <strong>Escenario 1: Cálculo de asesoría.</strong><br>
    Dado que existe una predicción válida y el dispositivo proporciona un ETA en minutos,<br>
    cuando el servicio procesa ambos datos,<br>
    entonces determina la categoría de disponibilidad esperada para el momento estimado de llegada.<br><br>
    <strong>Escenario 2: Cambio del ETA.</strong><br>
    Dado que el ETA del usuario cambia,<br>
    cuando se solicita una nueva asesoría,<br>
    entonces el sistema recalcula la categoría utilizando el nuevo tiempo estimado de llegada.<br><br>
    <strong>Escenario 3: Predicción no disponible.</strong><br>
    Dado que no existe una predicción válida para el momento de llegada,<br>
    cuando se solicita la asesoría,<br>
    entonces el sistema informa que no puede generar una asesoría basada en predicción.
  </td>
  <td>EP03</td>
</tr>

<tr>
  <td><strong>TS09</strong></td>
  <td>Configuración de actualización en tiempo casi real de disponibilidad</td>
  <td>Como desarrollador, quiero implementar mecanismos de actualización periódica y comunicación en tiempo casi real, para que la aplicación pueda mostrar información reciente sobre la ocupación de los estacionamientos.</td>
  <td>
    <strong>Escenario 1: Actualización periódica.</strong><br>
    Dado que el usuario consulta un estacionamiento,<br>
    cuando transcurre el intervalo de actualización configurado,<br>
    entonces la aplicación solicita el estado más reciente disponible.<br><br>
    <strong>Escenario 2: Actualización durante la permanencia.</strong><br>
    Dado que el usuario se encuentra utilizando la aplicación dentro del estacionamiento,<br>
    cuando se produce un cambio de disponibilidad,<br>
    entonces el sistema puede actualizar la información mostrada mediante el mecanismo de comunicación configurado.<br><br>
    <strong>Escenario 3: Información desactualizada.</strong><br>
    Dado que no se recibe una actualización durante un periodo determinado,<br>
    cuando la aplicación muestra el estado almacenado,<br>
    entonces indica la antigüedad de la información para evitar presentarla como completamente actualizada.
  </td>
  <td>EP02, EP03</td>
</tr>

<tr>
  <td><strong>TS10</strong></td>
  <td>Implementación del monitoreo de salud de dispositivos IoT</td>
  <td>Como desarrollador, quiero implementar el registro y monitoreo del estado de salud de los sensores y gateways, para detectar dispositivos con problemas de conectividad, batería o comunicación.</td>
  <td>
    <strong>Escenario 1: Reporte de salud recibido.</strong><br>
    Dado que un dispositivo envía un reporte de salud,<br>
    cuando el sistema procesa el DeviceHealthReported,<br>
    entonces registra el dispositivo, nivel de batería, señal, última conexión y timestamp.<br><br>
    <strong>Escenario 2: Dispositivo sin comunicación.</strong><br>
    Dado que un dispositivo no reporta actividad durante el periodo establecido,<br>
    cuando el sistema ejecuta la verificación de salud,<br>
    entonces identifica el dispositivo como potencialmente desconectado.<br><br>
    <strong>Escenario 3: Recuperación del dispositivo.</strong><br>
    Dado que un dispositivo previamente identificado con problemas vuelve a reportar información válida,<br>
    cuando el sistema recibe el nuevo reporte,<br>
    entonces actualiza su estado y registra la última comunicación disponible.
  </td>
  <td>EP04</td>
</tr>

<tr>
  <td><strong>TS11</strong></td>
  <td>Implementación de procesamiento histórico para analítica de ocupación</td>
  <td>Como desarrollador, quiero implementar un modelo de consulta histórica de ocupación y flujo vehicular, para proporcionar información agregada que permita analizar el comportamiento de los estacionamientos.</td>
  <td>
    <strong>Escenario 1: Consulta histórica.</strong><br>
    Dado que existen registros históricos de ocupación,<br>
    cuando el administrador solicita información de un periodo determinado,<br>
    entonces el sistema retorna los datos históricos correspondientes al estacionamiento o zona seleccionada.<br><br>
    <strong>Escenario 2: Identificación de periodos de mayor ocupación.</strong><br>
    Dado que existen registros históricos suficientes,<br>
    cuando se ejecuta el procesamiento analítico,<br>
    entonces identifica los periodos con mayor nivel de ocupación según los datos registrados.<br><br>
    <strong>Escenario 3: Sin información suficiente.</strong><br>
    Dado que el periodo consultado no contiene datos suficientes,<br>
    cuando se solicita el análisis,<br>
    entonces el sistema informa que no existen datos suficientes para generar el resultado.
  </td>
  <td>EP05</td>
</tr>

<tr>
  <td><strong>TS12</strong></td>
  <td>Implementación del sistema de notificaciones y preferencias</td>
  <td>Como desarrollador, quiero implementar el envío de notificaciones y la gestión de preferencias de notificación de QuadRapp, para comunicar a los usuarios eventos relevantes relacionados con la disponibilidad de los estacionamientos.</td>
  <td>
    <strong>Escenario 1: Configuración de preferencias.</strong><br>
    Dado que un usuario configura sus preferencias de notificación,<br>
    cuando el sistema procesa la configuración,<br>
    entonces almacena correctamente las preferencias asociadas al usuario.<br><br>
    <strong>Escenario 2: Envío de alerta de baja disponibilidad.</strong><br>
    Dado que se cumple la condición definida para generar una alerta de baja disponibilidad,<br>
    cuando el servicio de notificaciones procesa el evento,<br>
    entonces envía la notificación al usuario que tiene habilitado este tipo de alerta.<br><br>
    <strong>Escenario 3: Notificaciones desactivadas.</strong><br>
    Dado que un usuario ha desactivado las alertas de baja disponibilidad,<br>
    cuando se produce el evento correspondiente,<br>
    entonces el sistema no envía dicha notificación al usuario.
  </td>
  <td>EP05</td>
</tr>

<tr>
  <td><strong>TS13</strong></td>
  <td>Implementación de caché y funcionamiento parcial sin conexión</td>
  <td>Como desarrollador, quiero implementar almacenamiento local de información relevante de la aplicación móvil, para que el usuario pueda consultar datos previamente obtenidos cuando exista una interrupción temporal de conectividad.</td>
  <td>
    <strong>Escenario 1: Almacenamiento de configuración.</strong><br>
    Dado que la aplicación obtiene correctamente el mapa y la configuración de un estacionamiento,<br>
    cuando recibe una nueva versión de la configuración,<br>
    entonces almacena localmente la información junto con su versión correspondiente.<br><br>
    <strong>Escenario 2: Consulta sin conexión.</strong><br>
    Dado que el dispositivo pierde temporalmente la conexión,<br>
    cuando el usuario consulta la información previamente almacenada,<br>
    entonces la aplicación muestra el último estado disponible e indica su antigüedad.<br><br>
    <strong>Escenario 3: Recuperación de conexión.</strong><br>
    Dado que la conexión vuelve a estar disponible,<br>
    cuando la aplicación detecta la conectividad,<br>
    entonces solicita información actualizada al backend y reemplaza los datos almacenados cuando corresponde.
  </td>
  <td>EP02, EP03</td>
</tr>

  </tbody>
</table>



## 3.3. Impact Mapping

*Pendiente de elaboración.*

## 3.4. Product Backlog

En esta sección, se presenta el product backlog de QuadRapp como una recopilación organizada y priorizada de historias de usuario y historias técnicas. La estimación se realizó mediante story points, utilizando la escala de Fibonacci, considerando la complejidad, esfuerzo e incertidumbre de cada elemento. Asimismo, se empleó la técnica MoSCoW para establecer la prioridad de implementación.

| Orden | User Story ID | Título                                                                 | Descripción                                                                                                                                                                                             | Epic ID                | Story Points | MoSCoW      |
| ----- | ------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------ | ----------- |
| 1     | US01          | Inicio de sesión institucional                                         | Como usuario, quiero iniciar sesión en QuadRapp para acceder de forma segura a las funcionalidades disponibles.                                                                                         | EP01                   | 3            | Must Have   |
| 2     | US02          | Cerrar sesión                                                          | Como usuario, quiero cerrar sesión para finalizar de forma segura mi acceso a QuadRapp.                                                                                                                 | EP01                   | 2            | Must Have   |
| 3     | US03          | Gestionar sesión expirada                                              | Como usuario, quiero recibir una indicación cuando mi sesión haya expirado para volver a autenticarme y continuar utilizando la aplicación.                                                             | EP01                   | 3            | Must Have   |
| 4     | US04          | Consultar estacionamientos universitarios                              | Como usuario, quiero consultar los estacionamientos disponibles de la universidad para identificar dónde puedo estacionar.                                                                              | EP02                   | 3            | Must Have   |
| 5     | US05          | Consultar disponibilidad actual                                        | Como usuario, quiero consultar la disponibilidad actual de los espacios para conocer cuántos se encuentran libres u ocupados.                                                                           | EP02                   | 5            | Must Have   |
| 6     | US06          | Consultar disponibilidad por zona                                      | Como usuario, quiero consultar la disponibilidad de cada zona del estacionamiento para identificar dónde existen espacios disponibles.                                                                  | EP02                   | 3            | Must Have   |
| 7     | US07          | Actualizar disponibilidad                                              | Como usuario, quiero visualizar información actualizada sobre la disponibilidad para tomar decisiones con datos recientes.                                                                              | EP02                   | 5            | Must Have   |
| 8     | US08          | Gestionar estado desconocido                                           | Como sistema, quiero identificar los espacios cuyo estado no pueda determinarse correctamente para evitar mostrar información potencialmente incorrecta.                                                | EP02                   | 5            | Must Have   |
| 9     | US09          | Consultar predicción de disponibilidad                                 | Como usuario, quiero consultar la predicción de disponibilidad futura para conocer las condiciones esperadas del estacionamiento.                                                                       | EP03                   | 5            | Must Have   |
| 10    | US10          | Consultar diferentes horizontes de predicción                          | Como usuario, quiero consultar predicciones para diferentes intervalos de tiempo para evaluar la disponibilidad esperada al momento de mi llegada.                                                      | EP03                   | 5            | Must Have   |
| 11    | US11          | Visualizar nivel de saturación                                         | Como usuario, quiero visualizar el nivel de saturación esperado del estacionamiento para comprender rápidamente su nivel de ocupación.                                                                  | EP03                   | 3            | Must Have   |
| 12    | US12          | Gestionar predicciones con datos insuficientes                         | Como sistema, quiero identificar cuándo no existen suficientes datos para generar una predicción confiable para evitar presentar resultados no sustentados.                                             | EP03                   | 5            | Must Have   |
| 13    | US13          | Obtener asesoría de llegada                                            | Como usuario, quiero obtener una asesoría basada en la disponibilidad prevista y mi tiempo estimado de llegada para conocer las condiciones esperadas al llegar al estacionamiento.                     | EP03                   | 8            | Must Have   |
| 14    | US14          | Actualizar asesoría según ETA                                          | Como usuario, quiero que la asesoría se actualice cuando cambie mi tiempo estimado de llegada para recibir información acorde con mi nueva hora de llegada.                                             | EP03                   | 5            | Should Have |
| 15    | US15          | Mostrar categoría de disponibilidad esperada                           | Como usuario, quiero visualizar una categoría de disponibilidad esperada para interpretar fácilmente las condiciones previstas al momento de mi llegada.                                                | EP03                   | 3            | Must Have   |
| 16    | US16          | Registrar estacionamiento universitario                                | Como administrador, quiero registrar los estacionamientos universitarios para configurar los espacios que serán gestionados por QuadRapp.                                                               | EP04                   | 5            | Must Have   |
| 17    | US17          | Configurar zonas y espacios                                            | Como administrador, quiero configurar las zonas y espacios de cada estacionamiento para representar correctamente su distribución.                                                                      | EP04                   | 8            | Must Have   |
| 18    | US18          | Asociar sensor a espacio                                               | Como administrador, quiero asociar cada sensor con un espacio de estacionamiento para relacionar las lecturas físicas con su ubicación correspondiente.                                                 | EP04                   | 5            | Must Have   |
| 19    | US19          | Configurar accesos vehiculares                                         | Como administrador, quiero configurar los accesos de entrada y salida para registrar correctamente el movimiento de vehículos.                                                                          | EP04                   | 5            | Must Have   |
| 20    | US20          | Monitorear salud de sensores                                           | Como administrador, quiero monitorear el estado de los sensores para identificar problemas de conectividad o funcionamiento.                                                                            | EP04                   | 5            | Should Have |
| 21    | US21          | Reconciliar eventos de entrada y salida                                | Como administrador, quiero contar y reconciliar los eventos de entrada y salida con el estado de los espacios para detectar posibles inconsistencias en la ocupación.                                   | EP04                   | 8            | Should Have |
| 22    | US22          | Consultar historial de ocupación                                       | Como administrador, quiero consultar el historial de ocupación de los estacionamientos para analizar su comportamiento en diferentes periodos.                                                          | EP05                   | 5            | Should Have |
| 23    | US23          | Identificar horas de mayor ocupación                                   | Como administrador, quiero identificar las horas de mayor ocupación para conocer los periodos de mayor demanda de los estacionamientos.                                                                 | EP05                   | 5            | Should Have |
| 24    | US24          | Recibir alertas de baja disponibilidad                                 | Como usuario, quiero recibir alertas cuando la disponibilidad de estacionamientos sea baja para estar informado sobre posibles dificultades para encontrar un espacio.                                  | EP05                   | 5            | Could Have  |
| 25    | US25          | Gestionar preferencias de notificaciones                               | Como usuario, quiero gestionar mis preferencias de notificación para decidir qué alertas relacionadas con la disponibilidad deseo recibir.                                                              | EP05                   | 3            | Could Have  |
| 26    | TS01          | Configuración de autenticación y gestión de sesiones                   | Como desarrollador, quiero configurar el mecanismo de autenticación y gestión de sesiones de QuadRapp para garantizar un acceso seguro y una correcta validación de las sesiones.                       | EP01                   | 5            | Must Have   |
| 27    | TS02          | Configuración del API Gateway y BFF para la aplicación móvil           | Como desarrollador, quiero configurar un punto de entrada para la aplicación móvil para centralizar el acceso a los servicios de QuadRapp y facilitar la composición de información.                    | EP01, EP02, EP03       | 8            | Must Have   |
| 28    | TS03          | Configuración de persistencia y aislamiento de datos por contexto      | Como desarrollador, quiero configurar la persistencia de datos de los principales contextos de QuadRapp para mantener separados los datos según sus responsabilidades.                                  | EP02, EP03, EP04, EP05 | 8            | Must Have   |
| 29    | TS04          | Implementación de ingesta de eventos IoT mediante gateway              | Como desarrollador, quiero implementar la recepción de eventos provenientes de los sensores mediante un gateway IoT para integrar las lecturas de los dispositivos físicos con QuadRapp.                | EP04                   | 8            | Must Have   |
| 30    | TS05          | Configuración de comunicación MQTT para eventos IoT                    | Como desarrollador, quiero configurar MQTT para la comunicación entre el gateway y los servicios de QuadRapp para transmitir eventos IoT de manera confiable y desacoplada.                             | EP04                   | 5            | Must Have   |
| 31    | TS06          | Implementación de procesamiento e idempotencia de eventos de ocupación | Como desarrollador, quiero implementar el procesamiento controlado de eventos de sensores para evitar duplicidades, inconsistencias y cambios incorrectos en el estado de los espacios.                 | EP02, EP04             | 8            | Must Have   |
| 32    | TS07          | Implementación del modelo de predicción de ocupación                   | Como desarrollador, quiero implementar el componente de predicción de disponibilidad utilizando datos históricos de ocupación y flujo vehicular para generar pronósticos de disponibilidad futura.      | EP03                   | 13           | Must Have   |
| 33    | TS08          | Implementación del servicio de asesoría de llegada                     | Como desarrollador, quiero implementar un servicio que combine la predicción de ocupación con el tiempo estimado de llegada para generar una categoría de disponibilidad esperada.                      | EP03                   | 8            | Must Have   |
| 34    | TS09          | Configuración de actualización en tiempo casi real de disponibilidad   | Como desarrollador, quiero implementar mecanismos de actualización periódica y comunicación en tiempo casi real para mostrar información reciente sobre la ocupación.                                   | EP02, EP03             | 8            | Must Have   |
| 35    | TS10          | Implementación del monitoreo de salud de dispositivos IoT              | Como desarrollador, quiero implementar el registro y monitoreo del estado de salud de sensores y gateways para detectar problemas de conectividad o comunicación.                                       | EP04                   | 5            | Should Have |
| 36    | TS11          | Implementación de procesamiento histórico para analítica de ocupación  | Como desarrollador, quiero implementar un modelo de consulta histórica de ocupación y flujo vehicular para proporcionar información agregada sobre el comportamiento de los estacionamientos.           | EP05                   | 8            | Should Have |
| 37    | TS12          | Implementación del sistema de notificaciones y preferencias            | Como desarrollador, quiero implementar el envío de notificaciones y la gestión de preferencias para comunicar a los usuarios eventos relevantes relacionados con la disponibilidad.                     | EP05                   | 5            | Could Have  |
| 38    | TS13          | Implementación de caché y funcionamiento parcial sin conexión          | Como desarrollador, quiero implementar almacenamiento local de información relevante para que el usuario pueda consultar datos previamente obtenidos durante interrupciones temporales de conectividad. | EP02, EP03             | 5            | Should Have |


**Total de Story Points: 220**


# Capítulo IV: Strategic-Level Software Design

## 4.1. Strategic-Level Attribute-Driven Design

En esta sección se presenta el proceso de Attribute-Driven Design (ADD) aplicado a Quadrapp. Se define el propósito del diseño, los inputs del proceso (funcionalidad primaria, escenarios de atributos de calidad y restricciones), el backlog de Architectural Drivers, las decisiones de diseño con su evaluación de patrones y los escenarios de atributos de calidad refinados.


### 4.1.1. Design Purpose

El propósito del diseño es definir la arquitectura de alto nivel de Quadrapp, una solución que permite a los conductores de la comunidad educativa conocer no solo la disponibilidad actual de un estacionamiento universitario, sino también la probabilidad de encontrar un espacio libre al momento de su llegada. Con esto se busca reducir la incertidumbre, el tiempo de búsqueda y la congestión dentro y alrededor del campus, que son los problemas identificados en el Capítulo I.

Para lograrlo, la arquitectura debe combinar información en tiempo real (sensores IoT y procesamiento Edge) con datos históricos, horarios académicos y tiempos estimados de llegada, para generar predicciones de disponibilidad. Al mismo tiempo, debe ofrecer a los administradores de estacionamientos universitarios un dashboard que centralice la ocupación, las reservas, los movimientos de vehículos, el comportamiento histórico y los períodos de mayor demanda, de modo que puedan pasar de una gestión reactiva a una preventiva.

El diseño también debe respetar el contexto del negocio: el estacionamiento es gratuito para la comunidad educativa y el ingreso exige la credencial institucional, por lo que Quadrapp no gestiona cobros ni reemplaza el control de acceso. Su aporte está en la información, la predicción y la gestión.

Las decisiones de esta sección orientan el diseño estratégico con Domain-Driven Design (4.2) y las vistas de arquitectura (4.3). Se priorizan los atributos de calidad que más afectan la confianza del conductor en la predicción: precisión, frescura de los datos, disponibilidad ante fallas de conectividad y desempeño en horas pico.


### 4.1.2. Attribute-Driven Design Inputs

Los inputs del proceso ADD son la funcionalidad primaria con impacto en la arquitectura, los escenarios de atributos de calidad y las restricciones no negociables impuestas por el negocio y por el curso. A continuación se detalla cada uno.


#### 4.1.2.1. Primary Functionality (Primary User Stories)

*Pendiente de elaboración.*

#### 4.1.2.2. Quality Attribute Scenarios

Se identificaron ocho escenarios de atributos de calidad en primera instancia, a partir de los Business Outcomes, las Features Assumptions y los riesgos del Lean UX (sección 1.2.2). Cubren la precisión de la predicción, la frescura de los datos de ocupación, la disponibilidad ante caídas de conexión, el desempeño en horas pico, la integración con servicios externos, la calidad de los datos de sensores, la seguridad y la capacidad de incorporar nuevas instituciones.

| ID | Atributo | Fuente | Estímulo | Artefacto | Entorno | Respuesta | Medida |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QAS-01 | Correctness (precisión de la predicción) | Conductor de la comunidad educativa | Consulta la probabilidad de encontrar espacio para su hora estimada de llegada | Servicio de predicción de disponibilidad | Operación normal, con información histórica suficiente | Calcula la probabilidad combinando ocupación actual, reservas, histórico, horario académico y tiempo estimado de llegada, y la presenta como estimación, no como garantía | Al menos 80 % de aciertos en la categoría de disponibilidad (alta, media o baja) frente a la ocupación real a la hora de llegada, medido semanalmente |
| QAS-02 | Performance (frescura de los datos) | Sensor IoT de un espacio | Cambia el estado de un espacio (libre u ocupado) | Nodo Edge y servicio de ocupación | Operación normal, con conexión a la nube | El nodo Edge valida el evento, actualiza la ocupación local y la propaga a la nube y a los clientes | Cambio visible en la app y el dashboard en 5 s o menos (percentil 95); procesamiento en Edge en 1 s o menos |
| QAS-03 | Availability (tolerancia a desconexión) | Red o proveedor de conectividad | Se pierde la conexión entre el nodo Edge y la nube | Nodo Edge | Horario académico, incluyendo hora pico | El nodo Edge sigue procesando y almacenando eventos localmente y los sincroniza al restablecerse la conexión | 100 % de eventos procesados localmente durante la caída; sincronización en 5 min o menos tras la reconexión; pérdida de eventos de 0.1 % o menos |
| QAS-04 | Performance y Scalability | Conductores de la comunidad educativa | Pico de consultas de disponibilidad al inicio o fin de clases | API de consulta de disponibilidad | Hora pico | Atiende las consultas escalando horizontalmente los servicios de lectura | Hasta 500 consultas concurrentes con tiempo de respuesta de 2 s o menos (percentil 95) y tasa de error menor a 1 % |
| QAS-05 | Interoperability y Resilience | Servicio externo de tiempos de viaje | El servicio no responde o excede el tiempo de espera | Servicio de predicción (integración externa) | Operación normal | Detecta la falla, deja de invocar al servicio temporalmente y usa un tiempo de llegada basado en promedios históricos, informando que es aproximado | 100 % de consultas respondidas, sin errores visibles al usuario, en 3 s o menos |
| QAS-06 | Reliability (calidad de los datos) | Sensor IoT | Falla o deja de enviar señal | Nodo Edge y servicio de monitoreo | Operación normal | Detecta la ausencia de señal, marca el espacio como "sin datos", reduce la confianza de la predicción y alerta al administrador | Detección en 60 s o menos; alerta en 1 min o menos; disponibilidad de datos de ocupación de 95 % o más |
| QAS-07 | Security | Usuario no autenticado o sin el rol requerido | Intenta acceder al dashboard o a las reservas de otro usuario | API Gateway y servicio de identidad | Operación normal | Rechaza la solicitud y registra el intento en auditoría | 100 % de accesos no autorizados rechazados; registro en 1 s o menos; comunicaciones cifradas con TLS |
| QAS-08 | Modifiability (multi-institución) | Equipo de Integra Labs | Incorporar una nueva universidad con sus estacionamientos, zonas y sensores | Plataforma de gestión de instituciones | Operación normal con instituciones ya activas | Registra la institución y su infraestructura mediante configuración, aislando sus datos de las demás | Alta en 1 día hábil o menos, sin cambios de código ni interrupción del servicio; aislamiento de datos del 100 % |


#### 4.1.2.3. Constraints




### 4.1.3. Architectural Drivers Backlog

*Pendiente de elaboración.*

### 4.1.4. Architectural Design Decisions

Las decisiones de diseño se tomaron en seis iteraciones, siguiendo los stages del Quality Attribute Workshop. En cada iteración se seleccionaron los drivers de mayor prioridad, se identificaron patrones y tácticas candidatas, y se evaluaron sus ventajas y desventajas frente a los escenarios de calidad y las restricciones. Cuando hubo más de tres candidatos, se consideraron los tres más relevantes. Los criterios de decisión fueron el cumplimiento de las medidas de respuesta, la alineación con DDD, el uso de tecnologías open-source y la viabilidad de implementación por el equipo.

#### Candidate Pattern Evaluation Matrix

**Iteración 1: Estilo arquitectónico** (Drivers: TS-01, TS-02, QAD-04)

| Pattern | Pro | Con |
| --- | --- | --- |
| Monolito modular | Simple de desplegar y depurar; menor costo operativo. | Escala como una sola unidad; acopla la predicción con las consultas; dificulta aislar contextos. |
| **Microservicios por Bounded Context con API Gateway** | Escala de forma independiente lectura y predicción; se alinea con los Bounded Contexts; permite tecnologías diversas. | Mayor complejidad operativa; consistencia eventual; requiere observabilidad. |
| Serverless (FaaS) | Escalado automático y pago por uso. | Los arranques en frío afectan la latencia; poco adecuado para conexiones persistentes de dispositivos; dependencia del proveedor. |

**Decisión:** microservicios por Bounded Context, expuestos mediante un API Gateway.

**Iteración 2: Ingesta de ocupación y resiliencia** (Drivers: FD-05, QAD-02, QAD-03, QAD-06, TS-06)

| Pattern | Pro | Con |
| --- | --- | --- |
| **Edge computing con Store-and-Forward (mensajería ligera local y cola persistente)** | Procesa localmente con baja latencia; sigue operando sin conexión; sincroniza sin pérdidas al reconectar. | Sincronización más compleja (orden y duplicados); requiere mantener el nodo Edge. |
| Ingesta directa a la nube (cloud-centric) | Arquitectura más simple; un único punto de procesamiento. | Depende de la conexión; mayor latencia; se pierden datos ante caídas. |
| Polling periódico desde la nube | Fácil de implementar. | Datos poco frescos; tráfico innecesario; no cumple los 5 s. |

**Decisión:** Edge computing con Store-and-Forward y monitoreo de latidos (heartbeat) de sensores para detectar fallas.

**Iteración 3: Consulta y distribución de datos** (Drivers: FD-01, QAD-02, QAD-04)

| Pattern | Pro | Con |
| --- | --- | --- |
| **CQRS con read model en caché, alimentado por eventos, y actualización push a clientes** | Consultas rápidas y escalables; datos frescos al recibir eventos. | Consistencia eventual; más componentes que mantener. |
| Consulta directa a la base de datos transaccional | Simple; siempre consistente. | La carga de lectura en hora pico degrada el desempeño. |
| Materialización batch periódica | Bajo costo de cómputo. | Datos desactualizados; no cumple la frescura de QAS-02. |

**Decisión:** CQRS con read model en caché alimentado por eventos, más notificaciones push para app y dashboard.

**Iteración 4: Predicción de disponibilidad** (Drivers: FD-02, QAD-01)

| Pattern | Pro | Con |
| --- | --- | --- |
| **Servicio de predicción desacoplado con modelo de ML supervisado** | Aprovecha múltiples variables (hora, día, horario académico, reservas, tiempo de llegada); se puede reentrenar. | Requiere datos históricos suficientes; riesgo de arranque en frío. |
| Heurística por promedios históricos por franja horaria | Simple y explicable; funciona con pocos datos. | Menos preciso ante cambios de demanda. |
| Series temporales clásicas | Buen ajuste a patrones estacionales. | Incorpora con dificultad variables externas como reservas o tiempo de llegada. |

**Decisión:** servicio de predicción desacoplado con modelo de ML, con la heurística por promedios históricos como contingencia mientras no haya datos suficientes. El modelo se reentrena periódicamente con datos nuevos.

**Iteración 5: Integración externa y seguridad** (Drivers: QAD-05, QAD-07, TS-04, TS-07)

*Integración con el servicio externo (QAD-05):*

| Pattern | Pro | Con |
| --- | --- | --- |
| **Circuit Breaker con fallback y Anti-Corruption Layer** | Evita cascadas de fallas; permite responder con un valor aproximado; aísla el modelo externo del dominio. | Requiere configurar umbrales y mantener el fallback. |
| Reintentos con backoff | Fácil de implementar. | Aumenta la latencia durante la falla; no garantiza respuesta. |
| Llamada directa sin protección | Menor esfuerzo inicial. | Una falla externa se propaga al usuario. |

*Autenticación y autorización (QAD-07):*

| Pattern | Pro | Con |
| --- | --- | --- |
| **Autenticación con tokens (OAuth 2.0 y JWT) y control por roles (RBAC) en el API Gateway** | Estándar; sin estado; centraliza la seguridad; separa roles de conductor y administrador. | Requiere gestión de expiración y renovación de tokens. |
| Sesiones de servidor con cookies | Simple para web. | Menos adecuado para app móvil y para escalar horizontalmente. |
| API keys estáticas | Muy simples. | Débiles; no identifican al usuario ni sus roles. |

**Decisión:** circuit breaker con fallback y Anti-Corruption Layer para el servicio externo; OAuth 2.0 con JWT y RBAC en el API Gateway; cifrado TLS en todas las comunicaciones.

**Iteración 6: Soporte multi-institución** (Drivers: QAD-08, TS-02)

| Pattern | Pro | Con |
| --- | --- | --- |
| **Multi-tenancy lógico (esquema compartido con identificador de institución)** | Alta de instituciones por configuración; menor costo de infraestructura. | Exige controles estrictos de aislamiento de datos. |
| Instancia dedicada por institución | Aislamiento fuerte. | Alto costo operativo; no cumple el alta en 1 día hábil. |
| Base de datos por institución | Buen aislamiento con infraestructura compartida. | Más complejidad de administración y migraciones. |

**Decisión:** multi-tenancy lógico con identificador de institución en cada dato, con pruebas de aislamiento.

**Resumen de decisiones adoptadas**

| ID | Decisión | Drivers atendidos |
| --- | --- | --- |
| DD-01 | Microservicios por Bounded Context con API Gateway | TS-01, TS-02, QAD-04 |
| DD-02 | Edge computing con Store-and-Forward y monitoreo de latidos | FD-05, QAD-02, QAD-03, QAD-06, TS-06 |
| DD-03 | CQRS con read model en caché, eventos y notificaciones push | FD-01, QAD-02, QAD-04 |
| DD-04 | Servicio de predicción con ML y contingencia heurística | FD-02, QAD-01 |
| DD-05 | Circuit Breaker con fallback y Anti-Corruption Layer para el servicio externo | QAD-05, TS-04 |
| DD-06 | OAuth 2.0 con JWT, RBAC en el API Gateway y TLS | QAD-07, TS-07 |
| DD-07 | Multi-tenancy lógico por institución | QAD-08 |


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
