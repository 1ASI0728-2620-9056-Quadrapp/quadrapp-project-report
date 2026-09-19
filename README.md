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

*Pendiente de elaboración.*

## 3.3. Impact Mapping

*Pendiente de elaboración.*

## 3.4. Product Backlog

*Pendiente de elaboración.*

---

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
