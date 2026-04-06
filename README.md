# NVC — Proyecto de Consultoría Organizacional
## Índice General del Proyecto (Scaffolding)

---

| Campo              | Detalle                                          |
|--------------------|--------------------------------------------------|
| **Cliente**        | NVC — Nutrición, Vacunas y Consultoría           |
| **Director General** | Ignacio (apellido pendiente)                   |
| **Consultor**      | Externo                                          |
| **Inicio**         | Febrero 2026                                     |
| **Última actualización** | 5 de abril de 2026                       |
| **Objetivo**       | Profesionalizar operación y escalar a 10 sucursales |

---

## CONVENCIÓN DE VERSIONING

Todos los documentos siguen la notación: `nombre_vN_AAAAMMDD.md`

- `v1` = primera versión, `v2` = segunda versión, etc.
- `AAAAMMDD` = fecha de creación o última modificación
- Cada documento contiene además una tabla interna de **historial de versiones**
- Los borradores se marcan con `[BORRADOR]` hasta ser validados con el DG

---

## MAPA COMPLETO DEL PROYECTO

### 📁 Raíz del proyecto

| Archivo / Carpeta | Tipo | Descripción |
|-------------------|------|-------------|
| `README.md` | Índice | **Este archivo.** Mapa general del proyecto, convenciones y navegación |
| `neogcio.md` | Insumo | Descripción inicial del negocio (primer brief del cliente antes del diagnóstico) |
| `documentos/` | Carpeta | Documentos de propuesta inicial generados antes del diagnóstico formal |
| `.antigravity/` | Sistema | Motor agéntico multi-agente de consultoría (ver sección dedicada abajo) |

---

### 📁 `documentos/` — Propuesta inicial (pre-diagnóstico)

> Documentos generados antes del Diagnóstico 01. Son la base de la propuesta comercial y el punto de partida del plan.

| Archivo | Descripción |
|---------|-------------|
| `basico.docx` | Propuesta básica inicial: actividades prioritarias 0–4 meses, cronograma de 16 semanas y organigrama sugerido |
| `Aquí va el PLAN TÁCTICO OPERATIVO DETALLADO.docx` | Plan semana a semana (12 semanas): diagnóstico, estructura, procedimientos, indicadores, marketing y modelo replicable |
| `CRONOGRAMA MAESTRO.docx` | Cronograma maestro en 3 fases: Control y Estructura, Sistematizar, Marketing y Expansión. Incluye organigrama propuesto y dashboard gerencial |
| `MANUAL DE OPERACIONES NVC.docx` | Manual de operaciones v1 base: procedimientos de caja, inventario, atención a clientes, facturación, políticas y checklist de apertura de sucursal |
| `Propuesta Basica Inicial previa al diagnostico completo.pdf` | Versión PDF de la propuesta comercial entregada al cliente antes del diagnóstico formal |

---

### 📁 `1602026_avance/` — Notas de campo

| Archivo | Descripción |
|---------|-------------|
| `entrevistageneral1.md` | Notas crudas de la primera entrevista con el DG (16/02/2026). Contiene: personal por sucursal, sistemas, procesos, dolores operativos, flota, tecnología. **Base del Diagnóstico 01** |
| `entrevista_vianey_rossy_20260405.md` | Notas de entrevista directa con Lic. Vianey y su auxiliar Rossy (05/04/2026). Funciones reales de ambas. **Base de actualización v1.1 de manuales** |

---

### 📁 `02_diagnostico/` — Diagnósticos formales

> Documentos de diagnóstico redactados en formato de consultoría profesional.

| Archivo | Versión | Estado | Descripción |
|---------|---------|--------|-------------|
| `diagnostico01_20260216.md` | v1.0 | Borrador — validar con DG | Primer diagnóstico formal. Entrevista redactada profesionalmente con: descripción de la empresa, personal (14 personas en 3 sucursales), sistemas, procesos, hallazgos críticos y fortalezas |
| `pendientes01_20260216.md` | v1.0 | Listo | 40+ preguntas organizadas en 7 secciones (legal, RRHH, operaciones, sistemas, financiero, comercial, estrategia) para el Diagnóstico 02 |

---

### 📁 `03_plan_estrategico/` — Plan de consultoría

| Archivo | Versión | Estado | Descripción |
|---------|---------|--------|-------------|
| `plan_estrategico_v2_20260219.md` | v2.0 | Borrador — validar con DG | Plan actualizado post-diagnóstico. Incluye: marco estratégico, misión/visión propuestas, 4 fases (Fundamentos, Estructura, Sistemas, Marketing/Expansión), cronograma maestro 12 semanas, KPIs, opciones de POS, dashboard gerencial, riesgos y modelo replicable de apertura de sucursal |

---

### 📁 `04_estructura_organizacional/` — Estructura formal

| Archivo | Versión | Estado | Descripción |
|---------|---------|--------|-------------|
| `estructura_organizacional_v1_20260219.md` | v1.1 | Borrador — validar con DG | Organigrama formal actual y objetivo (a 12 meses). **v1.1:** Rossy reclasificada de "Cajera" a "Auxiliar Administrativo". Pendientes: sucursales 4 y 5, cajero/a Apatzingán, datos legales |

---

### 📁 `05_manual_de_funciones/` — Funciones por puesto

| Archivo | Versión | Estado | Descripción |
|---------|---------|--------|-------------|
| `manual_funciones_v1_20260219.md` | v1.1 | Borrador — validar con DG | Manual de funciones de 11 puestos (Aux. Administrativo agregado en v1.1). **v1.1:** Funciones de Vianey ampliadas, Rossy reclasificada de "Cajera" a "Auxiliar Administrativo", puesto de Cajero/a genérico agregado. **Pendiente v1.2:** política de uniforme y gafete |

---

### 📁 `06_manual_de_organizacion/` — Manual institucional

| Archivo | Versión | Estado | Descripción |
|---------|---------|--------|-------------|
| `manual_organizacion_v1_20260219.md` | v1.1 | Borrador — validar con DG | **v1.1:** Atribuciones del área administrativa ampliadas con funciones confirmadas de Vianey (mermas, conciliación bancaria mensual, trámites bancarios, responsable de personal, políticas). **Pendiente v1.2:** política de uniforme y gafete a detalle |

---

### 📁 `07_purina_investigacion/` — Investigación de proveedor

| Archivo | Descripción |
|---------|-------------|
| `purina_prospectivo_20260219.md` | Resumen prospectivo de Purina para NVC. Cubre: **Purina Animal Nutrition** (Agribrands/Cargill): misión, presencia en México (8 plantas), portafolio acuícola (Nutripec, AquaMax), mercado acuícola Michoacán ($2B USD, Michoacán 2do lugar nacional), relación con distribuidores. **Nestlé Purina PetCare**: inversión $220M USD 2024, estrategia de marca, redes sociales, 4 campañas ejemplo (Felix en OXXO, Juntos es Mejor, Jóvenes Veterinarios, Robbie Williams). Termina con plan de marketing de 5 ejes adaptado para NVC |
| `investigacion_purina_mexico_20260219.md` | Investigación detallada completa con fuentes verificadas |

---

### 📁 `08_resumen_ejecutivo/` — Entregables para el DG

| Archivo | Descripción |
|---------|-------------|
| `resumen01_20260219.md` | **Primer resumen ejecutivo para el Director General.** Contiene: mapa de todos los documentos generados, hallazgos críticos del Diagnóstico 01, resumen del plan estratégico por fases, estado de manuales, hallazgos de Purina, próximos pasos (Diagnóstico 02, análisis de inventarios/ventas históricos), cronograma próximas 4 semanas, compromisos pendientes del DG |

---

### 📁 `09_sistemas_tecnologia/` — Análisis de sistemas y software

| Archivo | Versión | Descripción |
|---------|---------|-------------|
| `mybussines.md` | v2.0 | Análisis técnico completo de MyBusiness POS. **v2.0:** Versión 2017 confirmada para NVC. Sección 15 con hallazgos de uso real: arquitectura BD local, traspasos manuales, tres flujos de dinero, cobranza sin certeza, gastos en Excel, AnyDesk, BVisual. Evaluación vs. v24 y comparativa con alternativas |

---

### 📁 `10_presentations/` — Presentación general del proyecto

| Archivo | Módulo | Diapositivas | Descripción |
|---------|--------|-------------|-------------|
| `00_indice_maestro.md` | Índice | — | Mapa de módulos, flujo recomendado, instrucciones PowerPoint |
| `01_empresa_diagnostico.md` | La Empresa y el Diagnóstico | 12 | Quiénes somos, metodología, equipo, hallazgos, Purina |
| `02_organizacion_personas.md` | Organización y Personas | 10 | Organigrama, funciones Vianey + Rossy, planta de personal |
| `03_plan_estrategico.md` | Plan Estratégico | 10 | 4 fases, KPIs, modelo replicable, cronograma |
| `04_sistemas_tecnologia.md` | Sistemas y Tecnología | 10 | MyBusiness 2017, 3 flujos de dinero, hoja de ruta |
| `05_hallazgos_acciones.md` | Hallazgos y Próximos Pasos | 8 | Top 12 hallazgos, 4 riesgos críticos, acciones inmediatas |
| `logo_nvc.jpg` | Logo | — | Logo oficial NVC |

---



> Motor de consultoría multi-agente de 4 capas. **No es específico de NVC** — es el framework metodológico del consultor que se aplica a este y otros proyectos.

### ¿Qué es?

Sistema de **Problem Discovery & Solution Design Autopilot**: garantiza que nunca se proponga tecnología antes de entender el problema real. Principio rector: *"Primero resuelves el problema. Luego profesionalizas. Después sistematizas. Al final gobernar."*

### Arquitectura (4 capas)

```
LAYER 4 — WORKFLOWS (Orquestación)
LAYER 3 — AGENTS (8 agentes especializados)
LAYER 2 — SKILLS & TOOLS (14+ herramientas ejecutables)
LAYER 1 — FOUNDATION (Reglas + Memoria + Economía)
```

### 📄 Archivos del sistema

#### Fundación (LAYER 1)

| Archivo | Descripción |
|---------|-------------|
| `.agrules` | Reglas éticas y metodológicas del sistema (NON-NEGOTIABLE). Define el pipeline de 8 fases, quality gates, anti-patterns prohibidos, criterios de complejidad y madurez organizacional |
| `ECONOMIC_INTEGRATION.md` | Guía de valoración económica. Cómo cuantificar: costo del estado actual, beneficios esperados, inversión y business case completo (ROI, Payback, NPV, IRR) |
| `README.md` | Documentación del sistema: propósito, arquitectura, pipeline, dominios soportados, quick start |

#### Memoria / Esquemas JSON (LAYER 1)

| Archivo | Descripción |
|---------|-------------|
| `memory/engagement_profile.json` | Perfil activo del engagement actual (datos del cliente NVC) |
| `memory/engagement_profile.schema.json` | Esquema de datos del perfil de engagement |
| `memory/problem_statement.json` | Declaración del problema documentada |
| `memory/problem_statement.schema.json` | Esquema de datos del problem statement |
| `memory/decision_log.schema.json` | Esquema para el log de decisiones del consultor |

#### Agentes especializados (LAYER 3)

| Archivo | Agente | Función |
|---------|--------|---------|
| `agents/01_intake_domain_classifier.md` | Intake & Domain Classifier | Recibe el primer contacto del cliente, clasifica el dominio (digitalización, mejora operativa, resolución conflictos, riesgo) y genera el engagement_profile inicial |
| `agents/02_discovery_orchestrator.md` | Discovery Orchestrator ⭐ | Conduce entrevistas, análisis de causa raíz, mapeo de stakeholders y **cuantificación económica del estado actual** ($X/año en pérdidas) |
| `agents/03_depth_maturity_assessor.md` | Depth & Maturity Assessor | Evalúa complejidad (técnica, organizacional, impacto del cambio, calidad de datos) y madurez. Recomienda track: Quick / Standard / Deep Dive |
| `agents/04_methodology_advisor.md` | Methodology Advisor | Selecciona y adapta los frameworks metodológicos por fase: Design Thinking, BPMN, Lean, MoSCoW, TOGAF, Agile |
| `agents/05_process_intelligence.md` | Process Intelligence | Mapea el proceso AS-IS en BPMN, detecta cuellos de botella y analiza desperdicios (Lean 8 Mudas) |
| `agents/06_redesign_optimization.md` | Redesign & Optimization ⭐ | Diseña el proceso TO-BE aplicando Lean (Eliminar → Simplificar → Automatizar) y cuantifica los **beneficios económicos esperados** |
| `agents/07_solution_architect.md` | Solution Architect ⭐ | Define el MVP (MoSCoW), diseña la arquitectura de solución, selecciona tecnología (Low-code / SaaS / Custom) y cuantifica la **inversión requerida** |
| `agents/08_implementation_roadmap.md` | Implementation Roadmap ⭐ | Genera el roadmap de implementación, plan de gestión del cambio, mitigación de riesgos y el **business case completo (ROI, Payback, NPV)** |

#### Skills / Herramientas (LAYER 2)

**Discovery:**

| Archivo | Skill | Función |
|---------|-------|---------|
| `skills/discovery/smart_questionnaire_generator.md` | Smart Questionnaire | Genera cuestionarios de entrevista personalizados por dominio y perfil de stakeholder |
| `skills/discovery/5_whys_engine.md` | 5 Whys Engine | Motor de análisis de causa raíz. Hace mínimo 3 niveles de "¿Por qué?" para separar síntoma de causa real |
| `skills/discovery/stakeholder_mapper.md` | Stakeholder Mapper | Mapea y prioriza a los actores clave del problema: quiénes sufren, quiénes deciden, quiénes bloquean |
| `skills/discovery/pain_point_canvas.md` | Pain Point Canvas | Canvas visual para mapear dolores operativos: por rol, por proceso, por impacto |

**Process Modeling:**

| Archivo | Skill | Función |
|---------|-------|---------|
| `skills/process_modeling/bpmn_assistant.md` | BPMN Assistant | Asiste en la construcción de diagramas de proceso AS-IS y TO-BE en notación BPMN 2.0 |
| `skills/process_modeling/bottleneck_detector.md` | Bottleneck Detector | Identifica y prioriza los cuellos de botella del proceso actual con scoring de impacto |
| `skills/process_modeling/waste_analyzer.md` | Waste Analyzer | Analiza desperdicios bajo los 8 tipos de muda de Lean (sobreproducción, espera, transporte, sobreprocesamiento, inventario, movimiento, defectos, talento) |

**Analysis:**

| Archivo | Skill | Función |
|---------|-------|---------|
| `skills/analysis/moscow_prioritizer.md` | MoSCoW Prioritizer | Prioriza funcionalidades del MVP en: Must Have, Should Have, Could Have, Won't Have |
| `skills/analysis/business_case_calculator.md` | Business Case Calculator ⭐ | **Herramienta más crítica del sistema.** Calcula: costo del estado actual, beneficios esperados, inversión, ROI, Payback, NPV, IRR. Usado en 3 fases del pipeline |

#### Workflows (LAYER 4)

| Archivo | Workflow | Cuándo usar |
|---------|----------|------------|
| `workflows/01_core_workflow.md` | Core Workflow | Pipeline universal de 8 fases para cualquier tipo de problema |
| `workflows/02_process_digitalization.md` | Process Digitalization | Cuando el cliente quiere digitalizar un proceso manual (caso más común) |
| `workflows/03_operational_improvement.md` | Operational Improvement | Cuando el proceso es lento/ineficiente y puede no necesitar tecnología |

#### Ejemplos

| Archivo | Descripción |
|---------|-------------|
| `examples/01_clinica_dental_complete.md` | Caso completo end-to-end: clínica dental. Incluye discovery, AS-IS, TO-BE, arquitectura y business case (ROI 447%, Payback 2.2 meses) |
| `examples/engagement_profile.json` | Ejemplo de perfil de engagement completo |
| `examples/problem_statement.json` | Ejemplo de problem statement documentado |

---

## CÓMO NAVEGAR EL PROYECTO

```
¿Qué buscas?                          → Ve a...
─────────────────────────────────────────────────────────────
Entender el negocio NVC               → neogcio.md
Análisis de MyBusiness POS           → 09_sistemas_tecnologia/mybussines.md
Notas crudas de entrevista            → 1602026_avance/entrevistageneral1.md
Diagnóstico formal (profesional)      → 02_diagnostico/diagnostico01_20260216.md
Preguntas para siguiente entrevista   → 02_diagnostico/pendientes01_20260216.md
Plan de trabajo y tiempos             → 03_plan_estrategico/plan_estrategico_v2_20260219.md
Quién reporta a quién / organigrama   → 04_estructura_organizacional/estructura_organizacional_v1_20260219.md
Qué hace cada puesto / KPIs           → 05_manual_de_funciones/manual_funciones_v1_20260219.md
Políticas, sistemas, calendario       → 06_manual_de_organizacion/manual_organizacion_v1_20260219.md
Investigación sobre Purina            → 07_purina_investigacion/purina_prospectivo_20260219.md
Resumen para el Director General      → 08_resumen_ejecutivo/resumen01_20260219.md
Propuesta inicial al cliente          → documentos/
Motor metodológico del consultor      → .antigravity/README.md
Reglas del sistema agéntico           → .antigravity/.agrules
Calcular ROI / business case          → .antigravity/skills/analysis/business_case_calculator.md
```

---

## ESTADO ACTUAL DEL PROYECTO

| Fase | Estado | Próximo paso |
|------|--------|-------------|
| Diagnóstico 01 | ✅ Completado | Validar con DG |
| Diagnóstico 02 | ⏳ Pendiente | Agendar entrevista |
| Plan Estratégico v2 | ✅ Borrador | Validar con DG |
| Estructura Organizacional v1.1 | ✅ Actualizado | Rossy reclasificada; confirmar cajero/a Apatzingán |
| Manual de Funciones v1.1 | ✅ Actualizado | Funciones Vianey ampliadas, Rossy como Aux. Admin |
| Manual de Organización v1.1 | ✅ Actualizado | Atribuciones área admin. ampliadas |
| Investigación Purina | ✅ Completado | Presentar al DG |
| Análisis MyBusiness | ✅ Completado v2.0 | Hallazgos de uso real integrados |
| Presentación general (5 módulos) | ✅ Completado | En `10_presentations/` |
| Diagnóstico 02 | ⏳ Pendiente | Agendar entrevista |
| Dashboard Gerencial v1 | ⏳ Pendiente | Semana 3 |
| Análisis inventarios/ventas | ⏳ Pendiente | Descargar MyBusiness |
| Política uniforme + gafete | ⏳ Pendiente | Definir con DG → v1.2 manuales |
| Misión / Visión / Valores | ⏳ Pendiente validación | Sesión con DG |
| Cajero/a Apatzingán | ⏳ Pendiente | Confirmar qué persona opera la caja |

---

*Proyecto NVC | Consultoría Organizacional | Iniciado Feb 2026 | Última actualización: Abril 2026*
