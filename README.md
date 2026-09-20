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
| Sulca Sanchez, Piero Angel | Por completar |

---

# Registro de Versiones del Informe

| Versión | Fecha | Autor | Descripción de modificación |
| --- | --- | --- | --- |

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
      <td>Foto por completar</td>
      <td>Sulca Sanchez, Piero Angel</td>
      <td>Por completar</td>
      <td>Ingeniería de Software</td>
      <td>Descripción por completar.</td>
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

**Parking Sensing:**

![ParkingSensing_Canvases](./assets/capitulo-04/ParkingSensing_Canvases.png)

**Occupancy:**

![Occupancy_Canvases](./assets/capitulo-04/Occupancy_Canvases.png)

**Prediction & Advisory:**

![Prediction&Advisory_Canvases](./assets/capitulo-04/Prediction&Advisory_Canvases.png)

**Parking Configuration:**

![ParkingConfiguration_Canvases](./assets/capitulo-04/ParkingConfiguration_Canvases.png)

**Notifications:**

![Notifications_Canvases](./assets/capitulo-04/Notifications_Canvases.png)

**Analytics:**

![Analytics_Canvases](./assets/capitulo-04/Analytics_Canvases.png)

**IAM:**

![IAM_Canvases](./assets/capitulo-04/IAM_Canvases.png)

### 4.2.5. Context Mapping

En esta sección se desarrollan distintas alternativas de Context Mapping para representar las relaciones entre los bounded contexts definidos para Quadrapp. El objetivo es evaluar cómo deben comunicarse entre sí, qué nivel de dependencia es adecuado y qué patrones de relación permiten mantener una arquitectura modular y alineada con las responsabilidades de cada contexto.

Para este análisis se consideran los bounded contexts Parking Sensing, Occupancy, Prediction & Advisory, Parking Configuration, Notifications, Analytics e IAM, junto con patrones de Domain-Driven Design como Customer/Supplier, Conformist, Shared Kernel y Anti-Corruption Layer.

**Opción 1 – Contextos independientes con relaciones directas:**
Se mantienen los siete bounded contexts completamente separados y se establecen relaciones directas entre aquellos que necesitan intercambiar información. La mayor parte de las dependencias utilizan el patrón Customer/Supplier, donde un contexto proporciona información que otro requiere para ejecutar sus responsabilidades.

Parking Configuration proporciona la estructura del estacionamiento a Parking Sensing y Occupancy. Luego, Parking Sensing transmite los eventos obtenidos de sensores a Occupancy, que determina la disponibilidad actual de los espacios.

A partir de dicha información, Occupancy proporciona el estado actual a Prediction & Advisory y registra los eventos correspondientes en Analytics. Analytics procesa la información histórica y entrega patrones de demanda a Prediction & Advisory. Finalmente, las recomendaciones y alertas generadas por este último contexto son enviadas a Notifications.

Por otro lado, IAM funciona como una capacidad transversal de identidad y autorización, por lo que los contextos que requieren información del usuario adoptan su modelo mediante una relación Conformist.

Ventajas:
- Mantiene responsabilidades claramente separadas.
- Facilita la comprensión de las dependencias.
- Permite que cada bounded context evolucione de forma independiente.
- Evita compartir directamente modelos internos.

Desventajas:
- Existe una mayor cantidad de relaciones entre contextos.
- Los cambios en contratos de integración pueden afectar a sus consumidores.
- Puede generarse lógica repetida para transformar información entre modelos.

![ContextMapping_Option1](./assets/capitulo-04/ContextMapping_Option1.png)

**Opción 2 – Uso de Shared Kernel entre contextos relacionados:**
Se mantiene los siete bounded contexts, pero propone compartir ciertos conceptos entre aquellos que trabajan con información estrechamente relacionada. 

En este caso, Parking Sensing y Occupancy compartirían un Shared Kernel asociado a la representación de eventos y espacios del estacionamiento. De manera similar, Occupancy y Analytics compartirían conceptos relacionados con los eventos de ocupación y su representación histórica.

El resto de relaciones mantendría principalmente el patrón Customer/Supplier. Parking Configuration continuaría proporcionando la estructura del estacionamiento, mientras que Occupancy y Analytics suministrarían información actual e histórica respectivamente a Prediction & Advisory. Este último enviaría los resultados relevantes a Notifications.
IAM continuaría operando como contexto genérico y los demás contextos se adaptarían a su modelo mediante relaciones Conformist.

Ventajas:
- Reduce la duplicación de conceptos entre contextos relacionados.
- Disminuye la necesidad de transformar información.
- Simplifica algunas comunicaciones internas.
- Puede facilitar la implementación inicial.

Desventajas:
- Incrementa el acoplamiento entre bounded contexts.
- Los cambios en un modelo compartido pueden afectar a varios contextos.
- Reduce la independencia de evolución de los módulos.
- Puede difuminar los límites del dominio si se comparte demasiada información.
Aunque esta alternativa simplifica ciertas integraciones, el uso excesivo de Shared Kernel puede hacer que los bounded contexts pierdan parte de la autonomía que se busca mediante Domain-Driven Design.

![ContextMapping_Option2](./assets/capitulo-04/ContextMapping_Option2.png)

**Opción 3 – Contextos independientes con protección de modelos:**
Se mantiene los bounded contexts independientes, pero introduce mecanismos para proteger los modelos internos cuando existen diferencias importantes entre ellos.

La principal decisión es utilizar una Anti-Corruption Layer entre Parking Sensing y Occupancy. Parking Sensing trabaja con elementos técnicos como sensores, telemetría, señales y eventos de dispositivos, mientras que Occupancy trabaja con conceptos del negocio como ocupación, disponibilidad y estado de los espacios.

La Anti-Corruption Layer se encarga de transformar los eventos técnicos provenientes del sensado en información comprensible para el dominio de Occupancy. De esta manera, Occupancy no necesita conocer los detalles de implementación de los sensores y puede evolucionar independientemente de la tecnología utilizada para capturar los datos.
Parking Configuration mantiene relaciones Customer/Supplier con Parking Sensing, Occupancy y Analytics, proporcionando información sobre campus, estacionamientos, zonas y espacios.

Entre Occupancy y Analytics se propone un Shared Kernel limitado, debido a que ambos contextos necesitan una representación consistente de determinados datos históricos de ocupación. Su alcance debe mantenerse reducido para evitar generar una dependencia excesiva.

Occupancy proporciona información actual de disponibilidad a Prediction & Advisory, mientras que Analytics aporta patrones históricos y tendencias de demanda. De esta manera, Prediction & Advisory puede combinar información actual e histórica para generar las predicciones de disponibilidad y recomendaciones al conductor.

Posteriormente, Prediction & Advisory se comunica con Notifications mediante una relación Customer/Supplier para solicitar el envío de alertas o recomendaciones relevantes.
Finalmente, IAM se mantiene como contexto genérico. Los contextos que requieren identidad, autenticación o autorización utilizan su modelo mediante una relación Conformist, evitando replicar responsabilidades relacionadas con seguridad.

Ventajas:
- Mantiene una clara separación de responsabilidades.
- Protege el modelo de Occupancy de detalles técnicos del IoT.
- Permite modificar sensores o mecanismos de captura sin afectar directamente al dominio.
- Mantiene Prediction & Advisory independiente de la infraestructura de sensado.
- Facilita la escalabilidad y evolución de cada contexto.

Desventajas:
- Requiere implementar una capa adicional de traducción.
- Aumenta ligeramente la complejidad de integración.
- El Shared Kernel entre Occupancy y Analytics requiere coordinación entre ambos contextos.
- Implica un mayor esfuerzo inicial de diseño.

![ContextMapping_Option3](./assets/capitulo-04/ContextMapping_Option3.png)

**Elección:**
Hemos seleccionado la opción 3 debido a que proporciona el mejor equilibrio entre separación de responsabilidades, independencia de los bounded contexts y control de las dependencias.

La relación mediante Anti-Corruption Layer entre Parking Sensing y Occupancy es especialmente importante, ya que evita que conceptos técnicos como telemetría, sensores o dispositivos Edge formen parte directamente del modelo de ocupación. Esto permite que la tecnología de sensado pueda evolucionar sin alterar las reglas de negocio asociadas a la disponibilidad de los estacionamientos.

Asimismo, el uso limitado de Shared Kernel entre Occupancy y Analytics permite mantener consistencia sobre los datos históricos de ocupación que ambos contextos necesitan, sin compartir modelos innecesarios con el resto de la solución.

Por otro lado, Prediction & Advisory se mantiene como el Core Domain de Quadrapp, ya que concentra el principal diferencial de la solución: estimar la probabilidad de encontrar un espacio disponible al momento de llegada y generar recomendaciones para el conductor a partir de información actual e histórica.

En conjunto, esta alternativa permite que cada bounded context mantenga un propósito específico y pueda evolucionar de manera independiente, mientras las relaciones entre ellos permanecen claramente definidas y controladas.

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
