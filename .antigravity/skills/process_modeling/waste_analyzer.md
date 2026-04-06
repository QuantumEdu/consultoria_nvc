# SKILL: Waste Analyzer (Lean 8 Mudas)

## 📋 METADATA
- **Skill ID**: `SKILL-007`
- **Category**: `Process Modeling`
- **Used By**: Process Intelligence, Redesign Agent
- **Version**: `1.0.0`
- **Origin**: Toyota Production System (Lean)

---

## 🎯 PURPOSE
Identificar y clasificar desperdicios (waste) en procesos usando los 8 tipos de Muda de Lean Manufacturing.

---

## 🗑️ THE 8 WASTES (DOWNTIME)

### **1. DEFECTS** (Errores)
```
Description: Trabajo que requiere corrección
Indicators:
  - Tasa de error > 5%
  - Rework frecuente
  - Quejas de calidad
  - Validaciones múltiples

Examples:
  ✗ "15% de facturas tienen errores"
  ✗ "Datos ingresados mal, hay que corregir"
  ✗ "Órdenes canceladas por información incorrecta"

Questions to Ask:
  - ¿Con qué frecuencia hay errores?
  - ¿Cuánto tiempo toma corregirlos?
  - ¿Por qué ocurren los errores?

Impact: Time + Cost of rework
```

### **2. OVERPRODUCTION** (Sobreproducción)
```
Description: Hacer más de lo necesario
Indicators:
  - Reportes que nadie lee
  - Features no usadas
  - Información no solicitada
  - Stock excesivo

Examples:
  ✗ "Generamos 10 reportes, solo usan 2"
  ✗ "Producimos 100 cuando solo necesitan 50"
  ✗ "Capturamos 50 campos, solo usan 10"

Questions to Ask:
  - ¿Quién usa este output?
  - ¿Con qué frecuencia se usa?
  - ¿Qué pasaría si no lo hiciéramos?

Impact: Wasted effort + Storage
```

### **3. WAITING** (Esperas)
```
Description: Tiempo sin actividad productiva
Indicators:
  - "Esperando aprobación"
  - "Esperando información"
  - "Esperando que X esté disponible"
  - Wait time >> Process time

Examples:
  ✗ "Orden espera 2 días por aprobación"
  ✗ "Usuario espera 1 hr por respuesta"
  ✗ "Proceso pausado esperando cliente"

Questions to Ask:
  - ¿Qué está esperando?
  - ¿Por qué tiene que esperar?
  - ¿Se puede hacer en paralelo?

Impact: Lead time increase
```

### **4. NON-UTILIZED TALENT** (Talento no utilizado)
```
Description: Personas con habilidades no aprovechadas
Indicators:
  - Profesional haciendo trabajo manual
  - Capacidad subutilizada
  - Creatividad no aprovechada
  - Skills desperdiciados

Examples:
  ✗ "Ingeniero pasa 4 hrs/día en data entry"
  ✗ "Gerente aprueba compras de $10"
  ✗ "Experto hace tareas administrativas"

Questions to Ask:
  - ¿Esta tarea requiere este nivel de skill?
  - ¿Podría delegarse a alguien más junior?
  - ¿Qué valor agregado no están generando?

Impact: Opportunity cost
```

### **5. TRANSPORTATION** (Transporte)
```
Description: Mover cosas innecesariamente
Indicators:
  - Movimiento físico excesivo
  - Transferencia de archivos
  - Copiar/pegar entre sistemas
  - Handoffs innecesarios

Examples:
  ✗ "Documento viaja 5 oficinas para firmas"
  ✗ "Datos copiados de Excel a sistema"
  ✗ "Producto movido 3 veces en bodega"

Questions to Ask:
  - ¿Por qué se mueve de A a B?
  - ¿Se puede eliminar el movimiento?
  - ¿Se puede digitalizar?

Impact: Time + Risk of loss
```

### **6. INVENTORY** (Inventario / WIP)
```
Description: Exceso de trabajo en progreso
Indicators:
  - Backlog grande
  - Órdenes en espera
  - Documentos pendientes
  - Multitasking excesivo

Examples:
  ✗ "50 órdenes en proceso, solo terminamos 5/día"
  ✗ "Inbox con 200 emails sin leer"
  ✗ "Proyectos iniciados pero no terminados"

Questions to Ask:
  - ¿Cuánto WIP tenemos?
  - ¿Por qué no fluye más rápido?
  - ¿Se puede limitar WIP?

Impact: Cash flow + Carrying cost
```

### **7. MOTION** (Movimiento)
```
Description: Movimiento humano innecesario
Indicators:
  - Caminar para buscar algo
  - Búsqueda de información
  - Cambiar entre aplicaciones
  - Alcanzar herramientas

Examples:
  ✗ "Buscar documento en 5 carpetas"
  ✗ "Caminar a oficina para preguntar"
  ✗ "Abrir 10 ventanas para una tarea"

Questions to Ask:
  - ¿Cuánto tiempo se pierde buscando?
  - ¿Se puede centralizar información?
  - ¿Se puede organizar mejor?

Impact: Time waste + Frustration
```

### **8. EXTRA PROCESSING** (Sobreprocesamiento)
```
Description: Más trabajo del necesario
Indicators:
  - Validaciones redundantes
  - Aprobaciones múltiples
  - Formularios excesivos
  - "Por si acaso"

Examples:
  ✗ "Triple aprobación para $100"
  ✗ "Llenar 3 formularios con misma info"
  ✗ "Validar datos ya validados"

Questions to Ask:
  - ¿Realmente agrega valor?
  - ¿Qué pasa si no lo hacemos?
  - ¿Por qué existe este paso?

Impact: Time + Bureaucracy
```

---

## 🔍 ANALYSIS METHODOLOGY

### **Step 1: Map Process**
```
Use BPMN or flowchart
Identify each step clearly
```

### **Step 2: Classify Each Step**
```
For each activity:
☑️ Value-Add: Cliente paga por esto
☐ Non-Value-Add but Necessary: Regulatorio, control
☐ Pure Waste: No agrega valor, eliminar

Example:
"Preparar comida" → Value-add
"Inspección de calidad" → Non-value but necessary
"Mover ingredientes 3 veces" → Pure waste
```

### **Step 3: Tag Waste Types**
```
For each non-value-add step:
Classify into 1+ waste types (D-O-W-N-T-I-M-E)

Example:
"Esperar aprobación" → WAITING
"Corregir errores" → DEFECTS
"Llenar 3 formas con misma info" → EXTRA PROCESSING
```

### **Step 4: Quantify Impact**
```
For each waste:
- Time lost: X hrs/week
- Money lost: $X/month
- Frequency: X times/day

Total waste by type:
DEFECTS: 10 hrs/week
WAITING: 30 hrs/week ← Biggest waste
MOTION: 5 hrs/week
```

### **Step 5: Prioritize**
```
Focus on:
1. Highest time/cost waste
2. Easiest to eliminate
3. Most frequent occurrence

Typically: WAITING and EXTRA PROCESSING are biggest
```

---

## 📊 ANALYSIS TEMPLATE

```markdown
# WASTE ANALYSIS (LEAN 8 MUDAS)

## PROCESS: [Name]
## DATE: [YYYY-MM-DD]

---

## VALUE STREAM BREAKDOWN

**Total Process Time**: 8 hours
**Value-Add Time**: 2 hours (25%)
**Non-Value-Add Time**: 6 hours (75%)

---

## WASTE BY TYPE

### 1. DEFECTS (D)
**Total Impact**: 8 hrs/week

| Activity | Frequency | Time/Instance | Total Time |
|----------|-----------|---------------|------------|
| Corregir facturas | 15/semana | 20 min | 5 hrs |
| Rehacerfiles | 10/semana | 30 min | 5 hrs |

**Root Causes**:
- Datos ingresados manualmente
- Sin validación en tiempo real

---

### 2. OVERPRODUCTION (O)
**Total Impact**: 4 hrs/week

| Activity | Frequency | Time | Why Waste? |
|----------|-----------|------|------------|
| Reporte X | 1/semana | 2 hrs | Nadie lo lee |
| Dashboard Y | 1/semana | 2 hrs | Info ya en otro reporte |

---

### 3. WAITING (W)
**Total Impact**: 30 hrs/week ← BIGGEST WASTE

| Activity | Frequency | Wait Time | Total |
|----------|-----------|-----------|-------|
| Esperar aprobación | 20/semana | 1 día | 160 hrs |
| Esperar info cliente | 10/semana | 2 días | 160 hrs |

---

[Continue for all 8 types...]

---

## SUMMARY

| Waste Type | Total Time/Week | % of Total | Priority |
|------------|----------------|-----------|----------|
| **WAITING** | **30 hrs** | **43%** | 🔥 CRITICAL |
| DEFECTS | 8 hrs | 11% | HIGH |
| EXTRA PROCESSING | 6 hrs | 9% | HIGH |
| MOTION | 5 hrs | 7% | MEDIUM |
| OVERPRODUCTION | 4 hrs | 6% | MEDIUM |
| TRANSPORTATION | 3 hrs | 4% | LOW |
| NON-UTILIZED TALENT | 10 hrs | 14% | MEDIUM |
| INVENTORY | 4 hrs | 6% | LOW |
| **TOTAL WASTE** | **70 hrs/week** | **100%** | |

---

## RECOMMENDATIONS

### Priority 1: Eliminate WAITING (43% of waste)
**Action**: Implement parallel approvals + delegation
**Impact**: -25 hrs/week
**Effort**: Medium

### Priority 2: Reduce DEFECTS (11%)
**Action**: Add data validation + templates
**Impact**: -6 hrs/week
**Effort**: Low

### Priority 3: Eliminate EXTRA PROCESSING (9%)
**Action**: Remove redundant validations
**Impact**: -5 hrs/week
**Effort**: Low
```

---

## 🎯 WORKED EXAMPLE

```markdown
## PROCESS: Order Entry

### STEP-BY-STEP WASTE ANALYSIS

| Step | Type | Waste? | Waste Type | Time |
|------|------|--------|-----------|------|
| Receive order call | VA | No | - | 5 min |
| Search customer in 3 systems | NVA | Yes | MOTION | 10 min |
| Wait for system to load | NVA | Yes | WAITING | 3 min |
| Enter data manually | NVA | Necessary | - | 15 min |
| Validate data (1st time) | NVA | Necessary | - | 2 min |
| Send to supervisor for approval | NVA | Yes | EXTRA PROC | 1 min |
| Wait for approval | NVA | Yes | WAITING | 2 hrs |
| Correct errors if any (30% time) | NVA | Yes | DEFECTS | 10 min |
| Re-enter in accounting system | NVA | Yes | TRANSPORTATION | 5 min |
| Validate again (redundant) | NVA | Yes | EXTRA PROC | 2 min |
| Send confirmation | VA | No | - | 2 min |

**Analysis**:
- VA time: 7 min (15% of 55 min process time)
- NVA necessary: 17 min (37%)
- Pure waste: 31 min (48%)

**Top Wastes**:
1. WAITING: 2 hrs (approval)
2. MOTION: 10 min (searching)
3. DEFECTS: 10 min × 30% = 3 min average
4. EXTRA PROCESSING: 3 min (redundant validation)
5. TRANSPORTATION: 5 min (re-entry)
```

---

## 💡 ELIMINATION STRATEGIES

### **For DEFECTS**
```
✓ Add validation rules
✓ Create templates
✓ Automate data entry
✓ Error-proofing (poka-yoke)
```

### **For WAITING**
```
✓ Eliminate approvals where possible
✓ Delegate authority
✓ Set SLAs
✓ Work in parallel
```

### **For MOTION**
```
✓ Centralize information
✓ Single source of truth
✓ Better organization
✓ Search functionality
```

### **For EXTRA PROCESSING**
```
✓ Challenge: "Why do we do this?"
✓ Eliminate redundant steps
✓ Consolidate validations
✓ Reduce bureaucracy
```

---

## 📤 OUTPUT FORMAT

```json
{
  "waste_analysis": {
    "process_id": "PROC-001",
    "total_cycle_time": "8 hours",
    "value_add_time": "2 hours (25%)",
    "waste_time": "6 hours (75%)",
    "waste_by_type": {
      "defects": {"hours_per_week": 8, "percent": 11, "priority": "high"},
      "overproduction": {"hours_per_week": 4, "percent": 6, "priority": "medium"},
      "waiting": {"hours_per_week": 30, "percent": 43, "priority": "critical"},
      "non_utilized_talent": {"hours_per_week": 10, "percent": 14, "priority": "medium"},
      "transportation": {"hours_per_week": 3, "percent": 4, "priority": "low"},
      "inventory": {"hours_per_week": 4, "percent": 6, "priority": "low"},
      "motion": {"hours_per_week": 5, "percent": 7, "priority": "medium"},
      "extra_processing": {"hours_per_week": 6, "percent": 9, "priority": "high"}
    },
    "recommendations": [
      {
        "waste_type": "waiting",
        "action": "Implement parallel approvals",
        "impact": "-25 hrs/week",
        "effort": "medium"
      }
    ]
  }
}
```

---

## ✅ ANALYSIS CHECKLIST

- [ ] Process mapped step-by-step
- [ ] Each step classified (VA / NVA-necessary / Waste)
- [ ] Waste tagged with D-O-W-N-T-I-M-E category
- [ ] Time quantified per waste type
- [ ] Total waste calculated
- [ ] Prioritized by impact
- [ ] Recommendations documented

---

**END OF SKILL: Waste Analyzer**
