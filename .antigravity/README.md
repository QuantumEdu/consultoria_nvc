# Problem Discovery & Solution Design Autopilot

## 🎯 PROPÓSITO

Sistema agéntico multi-agente para **consultores y facilitadores** que resuelve problemas ANTES de proponer tecnología.

**Principio fundamental**: "Los clientes expresan síntomas, no causas raíz. Nuestra misión es encontrar el problema real, cuantificarlo económicamente, y diseñar la solución óptima que el cliente puede ejecutar."

---

## 💡 ¿QUÉ RESUELVE?

### **Problema que resuelve el sistema**:

❌ **Antes (sin el sistema)**:
```
Cliente: "Queremos un sistema para X"
Consultor: "Les va a costar $40K y toma 3 meses"
Cliente: "Mmm... déjame pensarlo"
→ No hay urgencia, no hay claridad, no hay aprobación
```

✅ **Después (con el sistema)**:
```
Cliente: "Queremos un sistema para X"

Sistema ejecuta discovery → Encuentra:
- Problema real: Proceso caótico cuesta $34K/año
- Solución óptima: Low-code, $9.5K inversión
- Business case: Ahorra $52K/año, ROI 447%, Payback 2.2 meses

Consultor: "Están perdiendo $34K/año. Solución cuesta $9.5K, 
            recuperan en 2 meses. ¿Aprobamos?"
Cliente: "¡Por supuesto! ¿Cuándo empezamos?"
→ Urgencia clara, justificación económica, aprobación inmediata
```

---

## 🏗️ ARQUITECTURA DEL SISTEMA

### **4 Capas**

```
┌────────────────────────────────────────────────────────┐
│ LAYER 4: WORKFLOWS (Orquestación)                     │
│ ├─ Core Workflow (universal)                          │
│ ├─ Process Digitalization                             │
│ ├─ Operational Improvement                            │
│ ├─ Conflict Resolution                                │
│ └─ Risk Assessment                                     │
├────────────────────────────────────────────────────────┤
│ LAYER 3: AGENTS (Especializados)                      │
│ ├─ 01: Intake & Domain Classifier                     │
│ ├─ 02: Discovery Orchestrator ⭐                      │
│ ├─ 03: Depth & Maturity Assessor                      │
│ ├─ 04: Methodology Advisor                            │
│ ├─ 05: Process Intelligence                           │
│ ├─ 06: Redesign & Optimization                        │
│ ├─ 07: Solution Architect                             │
│ └─ 08: Implementation Roadmap ⭐                      │
├────────────────────────────────────────────────────────┤
│ LAYER 2: SKILLS & TOOLS (Ejecutables)                 │
│ ├─ Discovery: Questionnaires, 5 Whys, Stakeholders    │
│ ├─ Process: BPMN, Bottlenecks, Waste Analyzer         │
│ ├─ Analysis: MoSCoW, Business Case Calculator ⭐      │
│ └─ Generators: Playbooks, Roadmaps, Templates         │
├────────────────────────────────────────────────────────┤
│ LAYER 1: FOUNDATION (Base)                            │
│ ├─ .agrules (Reglas éticas + Pipeline)                │
│ ├─ Memory Schemas (JSON structures)                   │
│ └─ Economic Integration Guide ⭐                      │
└────────────────────────────────────────────────────────┘

⭐ = Componentes críticos con valoración económica
```

---

## 📈 VALORACIÓN ECONÓMICA INTEGRADA

### **3 Puntos de Cuantificación Obligatorios**

```
Phase 2: DISCOVERY
├─ Cuantificar: CURRENT STATE COST
├─ Pregunta: "¿Cuánto cuesta el problema HOY?"
├─ Categorías:
│  • Time waste ($X/año)
│  • Error costs ($X/año)
│  • Opportunity loss ($X/año)
│  • Overtime ($X/año)
│  • Risk exposure ($X/año)
└─ Output: "Están perdiendo $34,224/año"

Phase 5: TO-BE DESIGN
├─ Cuantificar: EXPECTED BENEFITS
├─ Pregunta: "¿Cuánto van a ahorrar/ganar?"
├─ Categorías:
│  • Time savings ($X/año)
│  • Error reduction ($X/año)
│  • Capacity increase ($X/año)
│  • Opportunity capture ($X/año)
└─ Output: "Van a ahorrar $52,320/año"

Phase 7: ROADMAP
├─ Cuantificar: COMPLETE BUSINESS CASE
├─ Calcular:
│  • ROI Year 1: (Benefit - Cost) / Cost
│  • Payback Period: Investment / Annual Benefit
│  • NPV (5 years, 10% discount)
│  • IRR (Internal Rate of Return)
├─ Decision Gate: GO/NO-GO
└─ Output: "ROI 447%, Payback 2.2 meses → STRONG GO"
```

### **Decision Gates Económicos**

```
Gate 1 (After Discovery):
✅ Current state cost > $20K/año → Continue
❌ < $20K/año → Consider low-code or decline

Gate 2 (After TO-BE):
✅ Expected benefit > 2× Problem cost → Continue
❌ < 2× → Replantear TO-BE

Gate 3 (After Architecture):
✅ Investment < 1× Annual benefit → Continue
❌ > 1× (Payback > 1 year) → Adjust scope

Gate 4 (Final GO/NO-GO):
✅ ROI > 50% + Payback < 18 mo + NPV > 0 → GO
⚠️ 3/4 criteria → CONDITIONAL GO
❌ < 3/4 criteria → NO-GO
```

---

## 🔄 PIPELINE UNIVERSAL (8 Fases)

```
FASE 0: INTAKE (1-2 días)
├─ Classify domain
├─ Identify stakeholders
├─ Capture constraints (budget, timeline)
└─ Output: engagement_profile.json

FASE 1: DISCOVERY ⭐ (1-2 semanas)
├─ Stakeholder interviews (3+ perfiles)
├─ Root cause analysis (5 Whys, Fishbone)
├─ ECONOMIC QUANTIFICATION (current state cost)
└─ Output: problem_statement.json + $X/año cost

FASE 2: DEPTH ASSESSMENT (2-3 días)
├─ Complexity scoring (4 dimensions)
├─ Maturity assessment (4 dimensions)
├─ Track recommendation (Quick/Standard/Deep)
└─ Output: GO/NO-GO decision

FASE 3: METHODOLOGY (1-2 días)
├─ Select frameworks by phase
├─ Create methodology playbook
└─ Output: Tailored approach

FASE 4: AS-IS MODELING (1-3 semanas)
├─ Map current process (BPMN)
├─ Identify bottlenecks
├─ Analyze waste (Lean 8 Mudas)
└─ Output: as_is_process.json

FASE 5: TO-BE DESIGN ⭐ (1-3 semanas)
├─ Apply Lean: ELIMINATE → SIMPLIFY → AUTOMATE
├─ ECONOMIC QUANTIFICATION (expected benefits)
├─ User validation
└─ Output: to_be_process.json + $X/año savings

FASE 6: ARCHITECTURE (1-2 semanas)
├─ Define MVP (MoSCoW)
├─ Design solution
├─ Select technology
├─ ECONOMIC QUANTIFICATION (investment cost)
└─ Output: solution_architecture.json + $X investment

FASE 7: ROADMAP ⭐ (1 semana)
├─ Define phases & sprints
├─ Change management plan
├─ Risk mitigation
├─ COMPLETE BUSINESS CASE (ROI, Payback, NPV)
└─ Output: implementation_roadmap.json

✅ READY FOR EXECUTION
```

**Duration Total**:
- Quick Track: 2-4 semanas
- Standard Track: 6-10 semanas
- Deep Dive: 12-20 semanas

---

## 🎯 DOMINIOS SOPORTADOS

### **1. Process Digitalization** (Más común)
```
Trigger: "Queremos un sistema para [proceso manual]"
Focus: Manual/Excel → Sistema digital
Examples: Appointment scheduling, Inventory, Order processing
Solution Mix: 70% tech + 20% process + 10% training
Track: Standard (6-10 weeks, $15K-$50K)
```

### **2. Operational Improvement**
```
Trigger: "Nuestro proceso es lento/ineficiente"
Focus: Process optimization (may not need tech)
Examples: Manufacturing efficiency, Service delivery
Solution Mix: 60% process + 30% training + 10% simple tech
Track: Quick-to-Standard (4-8 weeks, $5K-$30K)
```

### **3. Conflict Resolution**
```
Trigger: "Tenemos conflictos entre equipos/personas"
Focus: Organizational issues, role clarity
Examples: Department conflicts, unclear responsibilities
Solution Mix: 80% organizational + 20% process
Track: Standard (6-12 weeks, $10K-$40K)
```

### **4. Risk Assessment**
```
Trigger: "Necesitamos evaluar/mitigar riesgos"
Focus: Compliance, security, operational risks
Examples: Regulatory compliance, cybersecurity assessment
Solution Mix: 70% analysis + 30% controls/process
Track: Standard-to-Deep (8-16 weeks, $20K-$100K)
```

---

## 📊 RESULTADOS TÍPICOS

### **ROI por Dominio**

| Domain | Investment Range | ROI Year 1 | Payback | Success Rate |
|--------|-----------------|-----------|---------|--------------|
| **Process Digitalization** | $5K-$50K | 200-800% | 2-8 mo | 85% |
| **Operational Improvement** | $5K-$30K | 500-2000% | 1-3 mo | 70% |
| **Conflict Resolution** | $10K-$40K | 150-400% | 6-12 mo | 65% |
| **Risk Assessment** | $20K-$100K | 100-300% | 8-18 mo | 75% |

### **Factores de Éxito**

**Alta probabilidad éxito** (>80%):
✅ Executive sponsor comprometido
✅ Problema cuantificado claramente
✅ Usuarios involucrados en diseño
✅ Budget alineado a ROI
✅ Capacidad técnica adecuada

**Baja probabilidad éxito** (<50%):
❌ Solución pre-determinada sin discovery
❌ Sponsor débil o ausente
❌ Resistencia al cambio no addressada
❌ Over-engineering (solución muy compleja)
❌ Budget insuficiente para necesidad real

---

## 🛠️ CÓMO USAR EL SISTEMA

### **Paso 1: Inicio de Engagement**

```bash
# 1. Crear engagement profile
# Input: Email/contacto inicial del cliente

Agent 01: Intake & Domain Classifier
→ Genera questionnaire
→ Clasifica dominio
→ Output: engagement_profile.json
```

### **Paso 2: Discovery**

```bash
# 2. Profundizar en problema
# Input: engagement_profile.json

Agent 02: Discovery Orchestrator
→ Entrevistas (usar Smart Questionnaire Generator)
→ Root cause (usar 5 Whys Engine)
→ Pain points (usar Pain Point Canvas)
→ ⭐ ECONOMIC QUANTIFICATION ⭐
   (usar Business Case Calculator)
→ Output: problem_statement.json + $X/año cost
```

### **Paso 3: Depth Assessment**

```bash
# 3. Evaluar complejidad y capacidad
# Input: problem_statement.json

Agent 03: Depth & Maturity Assessor
→ Score complexity (4 dimensions)
→ Score maturity (4 dimensions)
→ Recommend track
→ GO/NO-GO decision
→ Output: depth_assessment en engagement_profile.json
```

### **Paso 4: AS-IS & TO-BE**

```bash
# 4. Modelar proceso actual y futuro
# Input: problem_statement.json

Agent 05: Process Intelligence
→ Map AS-IS (usar BPMN Assistant)
→ Identify bottlenecks (usar Bottleneck Detector)
→ Analyze waste (usar Waste Analyzer)
→ Output: as_is_process.json

Agent 06: Redesign & Optimization
→ Apply Lean (Eliminate → Simplify → Automate)
→ Design TO-BE
→ ⭐ ECONOMIC QUANTIFICATION ⭐ (expected benefits)
→ User validation
→ Output: to_be_process.json + $X/año savings
```

### **Paso 5: Architecture**

```bash
# 5. Diseñar solución
# Input: to_be_process.json

Agent 07: Solution Architect
→ Define MVP (usar MoSCoW Prioritizer)
→ Design architecture
→ Select technology (Low-code/SaaS/Custom)
→ ⭐ ECONOMIC QUANTIFICATION ⭐ (investment)
→ Output: solution_architecture.json + $X cost
```

### **Paso 6: Roadmap & Business Case**

```bash
# 6. Plan implementation + Complete business case
# Input: All previous artifacts

Agent 08: Implementation Roadmap
→ Define phases
→ Change management plan
→ Risk mitigation
→ ⭐ COMPLETE BUSINESS CASE ⭐
   • ROI = (Benefit - Cost) / Cost
   • Payback = Investment / Annual Benefit
   • NPV, IRR
   • Decision: GO/NO-GO
→ Output: implementation_roadmap.json

→ Present to client for approval
```

---

## 📁 ESTRUCTURA DE ARCHIVOS

```
problem-discovery-autopilot/
├── .agrules                          # Reglas éticas + Pipeline
├── ECONOMIC_INTEGRATION.md           # Guía valoración económica ⭐
├── README.md                          # Este archivo
│
├── memory/                            # Esquemas de datos
│   ├── engagement_profile.schema.json
│   ├── problem_statement.schema.json
│   └── decision_log.schema.json
│
├── agents/                            # 8 Agentes especializados
│   ├── 01_intake_classifier.md
│   ├── 02_discovery_orchestrator.md   # Con economic quantification
│   ├── 03_depth_assessor.md
│   ├── 04_methodology_advisor.md
│   ├── 05_process_intelligence.md
│   ├── 06_redesign_optimization.md    # Con economic quantification
│   ├── 07_solution_architect.md        # Con economic quantification
│   └── 08_implementation_roadmap.md    # Complete business case ⭐
│
├── skills/                            # 15+ Herramientas
│   ├── discovery/
│   │   ├── smart_questionnaire_generator.md
│   │   ├── 5_whys_engine.md
│   │   ├── stakeholder_mapper.md
│   │   └── pain_point_canvas.md
│   ├── process_modeling/
│   │   ├── bpmn_assistant.md
│   │   ├── bottleneck_detector.md
│   │   └── waste_analyzer.md
│   └── analysis/
│       ├── moscow_prioritizer.md
│       └── business_case_calculator.md  ⭐ CRITICAL
│
├── workflows/                         # 5 Workflows
│   ├── 01_core_workflow.md            # Universal pipeline
│   ├── 02_process_digitalization.md   # Más común
│   └── 03_operational_improvement.md
│
└── examples/                          # Casos completos
    └── 01_clinica_dental_complete.md  # End-to-end con ROI
```

---

## 💰 BUSINESS CASE CALCULATOR (SKILL-009)

### **Componente MÁS CRÍTICO del sistema**

**Ubicación**: `skills/analysis/business_case_calculator.md`

**Usado en 3 fases**:
1. **Discovery** (Phase 2): Current state cost
2. **TO-BE** (Phase 5): Expected benefits
3. **Roadmap** (Phase 7): Complete business case

**Cálculos que hace**:

```yaml
CURRENT STATE COST:
├─ Time waste: Horas perdidas × Costo/hora
├─ Error costs: Errores × Costo corrección
├─ Opportunity loss: Ventas perdidas × Margen
├─ Overtime: Horas extras × Tarifa
└─ Risk exposure: Probabilidad × Impacto
→ TOTAL: $X/año

EXPECTED BENEFITS:
├─ Time savings: Horas saved × Costo/hora
├─ Error reduction: Errores evitados × Costo
├─ Capacity increase: Volumen adicional × Margen
└─ Opportunity capture: Ventas recuperadas × Margen
→ TOTAL: $X/año

INVESTMENT:
├─ One-time: Development + Setup + Training
└─ Recurring: Licenses + Hosting + Maintenance
→ TOTAL: $X

FINANCIAL METRICS:
├─ ROI Year 1 = (Benefit - Cost) / Cost × 100%
├─ Payback = Investment / (Annual Benefit - Annual Cost)
├─ NPV = Σ(Benefit/(1+r)^t) - Investment
└─ IRR = Discount rate where NPV = 0

DECISION:
IF ROI > 50% AND Payback < 18mo AND NPV > 0:
  → GO ✅
ELSE:
  → Review or NO-GO ❌
```

**Ejemplo de uso** (Clínica):
```
Current State Cost: $34,224/año
Expected Benefit: $52,320/año
Investment: $9,555 (Year 1)

ROI = ($52,320 - $9,555) / $9,555 = 447%
Payback = $9,555 / $52,320 = 2.2 meses
NPV (5y, 10%) = $184,627

→ STRONG GO ✅
```

---

## 🎓 BEST PRACTICES

### **1. Siempre Cuantificar**
```
❌ "Pierden mucho tiempo"
✅ "Pierden 200 hrs/mes = $2,000/mes = $24,000/año"

Principio: Si no puedes ponerle precio, difícil aprobar presupuesto
```

### **2. Be Conservative**
```
❌ "Podrían ahorrar $500K/año"
✅ "Estimamos $130K/año conservadoramente, 
    potencialmente hasta $180K"

Principio: Mejor subestimar que sobreestimar
```

### **3. Validate with Users**
```
❌ Diseñar en sala de juntas
✅ Co-diseñar con usuarios (TO-BE workshop)

Principio: "Nada sobre nosotros sin nosotros"
```

### **4. Simple First**
```
❌ "Necesitamos IA/blockchain/microservices"
✅ "Airtable + Zapier resuelve el 90%"

Principio: Solución más simple que funciona
```

### **5. Economics Drive Decisions**
```
Checkpoint económico en cada fase:
- Discovery: ¿Problema cuesta suficiente?
- TO-BE: ¿Mejora es significativa?
- Architecture: ¿Costo es razonable?
- Roadmap: ¿ROI justifica inversión?

Principio: Decision gates cuantitativos, no subjetivos
```

---

## 🚀 QUICK START

### **Caso nuevo - 10 pasos**:

```
1. Recibir contacto cliente
   → Crear engagement_profile.json

2. Ejecutar Intake (Agent 01)
   → Classify domain
   → Identify stakeholders

3. Ejecutar Discovery (Agent 02) ⭐
   → Interviews (3+ perfiles)
   → 5 Whys root cause
   → ⭐ Quantify current state cost ($X/año)

4. Ejecutar Depth Assessment (Agent 03)
   → Score complexity & maturity
   → Recommend track
   → GO/NO-GO?

5. Select Methodologies (Agent 04)
   → Generate playbook

6. Map AS-IS (Agent 05)
   → BPMN + Bottlenecks + Waste

7. Design TO-BE (Agent 06) ⭐
   → Apply Lean
   → ⭐ Quantify expected benefits ($X/año)
   → User validation

8. Design Solution (Agent 07) ⭐
   → MVP (MoSCoW)
   → Architecture
   → ⭐ Quantify investment ($X)

9. Create Roadmap (Agent 08) ⭐
   → Phases
   → Change management
   → ⭐ Complete business case (ROI, Payback, NPV)

10. Present & Approve
    → Executive presentation
    → Budget approval
    → Start implementation
```

---

## 📞 SOPORTE

**Documentación**:
- `.agrules`: Reglas del sistema
- `ECONOMIC_INTEGRATION.md`: Guía valoración económica
- `agents/*.md`: Documentación de cada agente
- `skills/*.md`: Documentación de cada herramienta
- `workflows/*.md`: Pipelines especializados
- `examples/*.md`: Casos completos

**Troubleshooting**:
- Ver `examples/01_clinica_dental_complete.md` para caso completo
- Cada agent.md tiene sección de ejemplos
- Business Case Calculator tiene templates completos

---

## 📈 MÉTRICAS DE ÉXITO DEL SISTEMA

**Engagement Success**:
- Problem validated: > 90%
- GO decision confidence: > 85%
- Business case solid: > 80%

**Economic Accuracy**:
- ROI projections within ±30% of actual: > 75%
- Payback projections within ±30% of actual: > 80%

**Client Satisfaction**:
- Would recommend: > 90%
- Felt problem was understood: > 95%
- Valued economic quantification: > 90%

---

**Versión**: 1.0.0  
**Última actualización**: 2025-01-20  
**Autor**: Problem Discovery Autopilot System

---

**END OF README**
