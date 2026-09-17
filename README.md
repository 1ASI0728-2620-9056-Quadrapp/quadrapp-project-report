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

Hemos observado que los conductores que se trasladan a universidades y centros educativos enfrentan dificultades para encontrar estacionamiento, especialmente durante horarios de alta concurrencia como el inicio y término de clases. Aunque un estacionamiento pueda mostrar espacios disponibles en un momento determinado, esta información no garantiza que dichos espacios continúen libres cuando el conductor llegue, generando incertidumbre, pérdida de tiempo, recorridos innecesarios y congestión dentro y alrededor del campus.

Por otro lado, las universidades y administradores de estacionamientos necesitan gestionar de manera eficiente la ocupación, el ingreso y la salida de vehículos, así como aprovechar la información generada diariamente para comprender los patrones de movilidad de su comunidad. Los sistemas tradicionales suelen concentrarse en mostrar la disponibilidad actual o controlar el acceso, pero no aprovechan suficientemente los datos históricos y operativos para anticipar cómo cambiará la ocupación en los siguientes minutos.

Esta situación evidencia una brecha entre conocer cuántos espacios están disponibles actualmente y poder estimar qué probabilidad existe de encontrar uno al momento de llegar. Factores como el tiempo estimado de llegada, vehículos que se aproximan al campus, reservas existentes, registros históricos de ocupación, fecha, hora y horarios académicos pueden aportar información relevante para reducir esta incertidumbre.

Frente a esta problemática, Quadrapp busca atender inicialmente a conductores de la comunidad educativa y administradores de estacionamientos universitarios, mediante una plataforma que combine información en tiempo real con datos históricos para estimar la disponibilidad futura de espacios. Asimismo, se busca agilizar la operación del estacionamiento mediante mecanismos automatizados de ingreso, salida y cobro, contribuyendo a una experiencia más predecible para el conductor y a una gestión más eficiente para las instituciones educativas.

#### 1.2.2.2. Lean UX Assumptions

**Business Assumptions:**
1. Los conductores de la comunidad educativa necesitan conocer no solo la disponibilidad actual de estacionamientos, sino también la probabilidad de encontrar un espacio disponible al momento estimado de su llegada al campus.
2. Las necesidades de los conductores y de la instituciones serán atendidas mediante una aplicación móvil integrada con sensores IoT, datos históricos de ocupación, reservas, horarios académicos y estimaciones de tiempo de llegada, permitiendo generar predicciones sobre la disponibilidad futura de estacionamientos.
3. Nuestros clientes iniciales serán universidades y centros educativos que administran estacionamientos propios y buscan reducir la congestión, optimizar el uso de sus espacios y mejorar la experiencia de movilidad dentro del campus.
4. El principal valor que los conductores esperan de Quadrapp es contar con información que reduzca la incertidumbre sobre si encontrarán un espacio disponible cuando lleguen, permitiéndoles tomar mejores decisiones antes y durante su desplazamiento.
5. Los administradores de estacionamientos también podrán obtener valor mediante un dashboard que centralice información sobre ocupación actual, reservas, ingresos, salidas, comportamiento histórico y períodos de mayor demanda.
6. Obtendremos nuestra base inicial de clientes mediante alianzas con universidades y centros educativos, demostraciones de la solución en campus y propuestas de mejora de la gestión de estacionamientos dirigidas a las áreas responsables de infraestructura, seguridad y movilidad.
7. Generaremos ingresos principalmente mediante un modelo de suscripción o licenciamiento institucional para universidades, considerando servicios adicionales asociados a la infraestructura IoT, procesamiento Edge y automatización de accesos.
8. Nuestra principal competencia serán plataformas de estacionamiento como Apparka, sistemas tradicionales de control de acceso y soluciones de parking inteligente orientadas principalmente a mostrar disponibilidad actual, gestionar pagos o automatizar el ingreso de vehículos.
9. Nuestro mayor riesgo es que la predicción de disponibilidad no alcance un nivel de precisión suficiente para generar confianza en los conductores, debido a información incompleta, fallas en sensores o cambios inesperados en el comportamiento de ocupación del estacionamiento.
10. ¿Cuáles son las suposiciones que, si se demuestran falsas, harán que el proyecto fracase?
    - Los conductores no considerarán útil una predicción si perciben diferencias frecuentes entre la probabilidad mostrada y la disponibilidad real al momento de llegar.
    - Las universidades podrían no estar dispuestas a invertir en infraestructura IoT, cámaras y dispositivos Edge si el beneficio operativo no justifica su costo de implementación.
    - La cantidad y calidad de los datos históricos podría ser insuficiente para generar predicciones confiables durante las primeras etapas de adopción.
    - Las fallas en sensores, cámaras o conectividad podrían afectar la información utilizada para calcular la ocupación y disponibilidad futura.
    - Los usuarios podrían continuar prefiriendo métodos tradicionales de ingreso y pago si los procesos automatizados no reducen significativamente los tiempos de espera.

**Business Outcomes:**
1. Lograr que al menos una institución educativa implemente un piloto de Quadrapp durante el primer año de operación.
2. Reducir en al menos un 20 % el tiempo promedio dedicado por los conductores a buscar estacionamiento dentro del campus durante los primeros seis meses de uso.
3. Alcanzar una precisión mínima del 80 % en las estimaciones de disponibilidad futura una vez que el sistema cuente con suficiente información histórica.
4. Conseguir que al menos el 60 % de los conductores activos consulte la predicción de disponibilidad antes de ingresar al campus durante períodos de alta demanda.
5. Reducir en al menos un 25 % el tiempo promedio de ingreso y salida de vehículos mediante el reconocimiento automático de placas y los mecanismos digitales de acceso.
6. Mantener una tasa de disponibilidad de datos de ocupación superior al 95 % mediante la integración de sensores IoT y dispositivos Edge instalados en los estacionamientos.

**User Assumptions:**
1. ¿Quién es el usuario?
Conductores de la comunidad educativa (estudiantes, docentes y personal administrativo) que se trasladen regularmente al campus, y administradores de estacionamientos universitarios responsables de supervisar la ocupación y operación de dichos espacios.

2. ¿Dónde encajaría nuestro producto en la vida o trabajo del usuario?
    - Para los conductores: Antes y durante su desplazamiento hacia la universidad, utilizando la aplicación móvil para consultar disponibilidad actual, conocer la probabilidad de encontrar un espacio al momento estimado de llegada, realizar reservas y gestionar su acceso al estacionamiento.
    - Para los administradores: Durante la operación diaria del estacionamiento, utilizando un dashboard para supervisar la ocupación, revisar accesos, reservas, comportamiento histórico y períodos de mayor demanda.

3. ¿Qué problemas resuelve el producto para el usuario?
    - Incertidumbre sobre la disponibilidad de estacionamientos al momento de llegar al campus.
    - Tiempo perdido recorriendo estacionamientos sin espacios disponibles.
    - Congestión generada durante los horarios de mayor demanda.
    - Falta de información anticipada para planificar y decidir hacia qué estacionamiento dirigirse.
    - Procesos manuales o poco eficientes para controlar el ingreso y salida de vehículos.

4. ¿En qué contexto utiliza el usuario el producto?
    - Los conductores utilizarán principalmente la aplicación móvil mientras planifican o realizan su desplazamiento hacia el campus, consultando la disponibilidad actual y estimada según su tiempo aproximado de llegada.
    - Los administradores utilizarán el dashboard durante la jornada académica para supervisar el estado de los estacionamientos, revisar períodos de alta ocupación y controlar los procesos de ingreso y salida.

5. ¿Qué características son esenciales para el usuario? ¿Y por qué?
    - Predicción de disponibilidad futura: Permite conocer la probabilidad de encontrar un espacio en tiempo real mientras el conductor se encuentre desplazando a su punto de llegada.
    - Disponibilidad en tiempo real: Proporciona información actualizada sobre espacios libres y ocupados.
    - Reservas de estacionamiento: Permite asegurar un espacio cuando el usuario lo requiera, realizando el pago correspondiente.
    - Reconocimiento automático de placas: Agiliza los procesos de ingreso, salida y asociación del vehículo con el usuario.
    - Acceso mediante QR: Funciona como alternativa cuando el reconocimiento de placas no pueda realizarse correctamente.
    - Dashboard de gestión: Permite a los administradores analizar ocupación, demanda y patrones históricos del estacionamiento.

6. ¿Cómo debería verse y comportarse el producto?
    - La aplicación móvil debe mostrar de manera clara la disponibilidad actual del estacionamiento y la probabilidad estimada de encontrar un espacio al momento de llegada, evitando presentar la predicción como una garantía absoluta.
    - El aplicación web debe centralizar la ocupación actual, reservas, ingresos, salidas,información histórica y predicciones, presentando los datos de forma comprensible en un dashboard para apoyar la toma de decisiones del administrador.

**User Outcomes:**
1. Los conductores quieren reducir la incertidumbre antes de dirigirse hacia un estacionamiento, conociendo qué tan probable es encontrar un espacio cuando lleguen al campus.
2. Los usuarios esperan disminuir el tiempo perdido buscando estacionamiento y evitar desplazamientos innecesarios entre diferentes zonas o estacionamientos de la universidad.
3. Los conductores esperan que las predicciones sean suficientemente precisas para confiar en ellas al momento de decidir hacia qué estacionamiento dirigirse.
4. Los usuarios valoran procesos rápidos de ingreso y salida mediante reconocimiento de placas, manteniendo una alternativa sencilla mediante QR cuando el reconocimiento automático no funcione correctamente.
5. Los administradores de estacionamientos universitarios quieren reducir el esfuerzo operativo asociado al control de vehículos y contar con información histórica y actual que les permita anticipar períodos de alta demanda.

**Features Assumptions:**
1. **Predicción de disponibilidad futura**
    - Suposición: Si combinamos la ocupación actual obtenida mediante IoT con reservas, vehículos próximos al campus, datos históricos, fecha, hora, horarios académicos y tiempo estimado de llegada, podremos calcular una probabilidad útil de encontrar un espacio disponible cuando el conductor llegue.
    - Riesgo: Si la predicción presenta errores frecuentes debido a cambios inesperados en la demanda o datos insuficientes, los conductores podrían perder confianza en la funcionalidad.

2. **Monitoreo de ocupación mediante IoT**
    - Suposición: Los sensores IoT permitirán identificar cambios de ocupación en los espacios de estacionamiento y mantener actualizada la información utilizada por la aplicación y el sistema de predicción.
    - Riesgo: Fallas en sensores, problemas de conectividad o lecturas incorrectas podrían provocar diferencias entre la ocupación registrada por el sistema y la ocupación real.

3. **Procesamiento mediante Edge Computing**
    - Suposición: Procesar localmente eventos relacionados con sensores, cámaras, ingresos y salidas permitirá responder rápidamente ante cambios de ocupación y reducir la dependencia constante de servicios externos o de la nube.
    - Riesgo: La distribución del procesamiento entre dispositivos Edge y servicios centrales podría aumentar la complejidad de sincronización, mantenimiento y recuperación ante fallos.

4. **Reconocimiento automático de placas**
    - Suposición: Utilizar cámaras para reconocer las placas permitirá identificar automáticamente a los vehículos autorizados y agilizar los procesos de ingreso, salida y cobro del estacionamiento.
    - Riesgo: Factores como iluminación, suciedad, posición del vehículo o deterioro de la placa podrían impedir una identificación correcta y generar demoras en el acceso.

5. **Acceso alternativo mediante QR**
    - Suposición: Proporcionar un código QR permitirá que el conductor pueda ingresar o salir del estacionamiento cuando el reconocimiento automático de placas falle, evitando depender de tickets físicos.
    - Riesgo: Si el mecanismo alternativo requiere demasiados pasos o genera demoras durante horas punta, podría ocasionar colas en los puntos de acceso.

6. **Dashboard de gestión y análisis**
    - Suposición: Los administradores utilizarán un dashboard con información sobre ocupación actual, datos históricos, predicciones, reservas e ingresos para identificar patrones de demanda y mejorar la gestión de los estacionamientos.
    - Riesgo: Si la información presentada es difícil de interpretar o no permite tomar acciones concretas, los administradores podrían continuar utilizando métodos tradicionales de gestión.

#### 1.2.2.3. Lean UX Hypothesis Statements

- Creemos que los conductores reducirán el tiempo que dedican a buscar estacionamiento si pueden conocer la probabilidad de encontrar un espacio al momento de su llegada. Lo sabremos cuando al menos el 60 % consulte la predicción antes de ingresar al campus, la precisión alcance un mínimo del 80 % y el tiempo de búsqueda se reduzca en al menos un 20 %.

- Creemos que los sensores IoT permitirán mantener información confiable y actualizada sobre la ocupación de los estacionamientos. Lo confimaremos cuando la disponibilidad de los datos se mantenga por encima del 95 % durante el período piloto.

- Creemos que el procesamiento local permitirá mantener el monitoreo del estacionamiento incluso cuando existan interrupciones temporales de conexión con la nube. Lo confirmaremos cuando los eventos continúen procesándose localmente y los datos pendientes puedan sincronizarse posteriormente sin pérdidas relevantes.

- Creemos que el reconocimiento automático de placas agilizará el ingreso y salida de vehículos al reducir los procesos manuales de identificación. Lo sabremos cuando el tiempo promedio de acceso y salida disminuya al menos un 25 % respecto al proceso actual.

- Creemos que el uso de códigos QR permitirá mantener un proceso de acceso rápido cuando el reconocimiento de placas falle. Lo confirmaremos cuando la mayoría de estos casos puedan resolverse mediante QR sin utilizar tickets físicos ni requerir intervención manual.

- Creemos que los administradores podrán gestionar mejor los estacionamientos si cuentan con información centralizada sobre ocupación, reservas, historial y predicciones. Lo confirmaremos cuando utilicen el dashboard durante la operación diaria y la información les permita tomar decisiones sobre la disponibilidad y demanda de los espacios. Ahora continuemos con el Canvas.

#### 1.2.2.4. Lean UX Canvas

![LeanUXCanvas_Quadrapp](./assets/capitulo-01/LeanUXCanvas_Quadrapp.png)

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
