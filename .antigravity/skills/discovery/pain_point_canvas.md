# SKILL: Pain Point Canvas

## 📋 METADATA
- **Skill ID**: `SKILL-004`
- **Category**: `Discovery`
- **Used By**: Discovery Orchestrator, Process Intelligence
- **Version**: `1.0.0`

---

## 🎯 PURPOSE
Estructurar, visualizar y cuantificar los pain points identificados durante discovery para priorizar qué resolver primero.

---

## 📥 INPUT
```json
{
  "engagement_id": "string",
  "pain_points": [
    {
      "description": "string",
      "source": "string (who reported it)",
      "frequency": "string",
      "impact_estimate": "string"
    }
  ]
}
```

---

## 📤 OUTPUT
```json
{
  "canvas_id": "PAIN-YYYYMMDD-XXXXXX",
  "pain_points": [
    {
      "id": "PP-001",
      "description": "string",
      "category": "time|money|quality|control|risk|people",
      "frequency_score": 1-5,
      "impact_score": 1-5,
      "priority_score": 1-25,
      "affected_roles": ["string"],
      "quantified_impact": {
        "time_lost": "string",
        "money_lost": "string",
        "other": "string"
      },
      "workarounds": ["string"],
      "root_cause": "string (if known)"
    }
  ],
  "prioritization_matrix": "visualization"
}
```

---

## 🗺️ PAIN POINT CANVAS STRUCTURE

```
┌────────────────────────────────────────────────────────┐
│ PAIN POINT CANVAS                                      │
├────────────────────────────────────────────────────────┤
│                                                         │
│  WHO SUFFERS IT?                                       │
│  └─ [Roles affected]                                   │
│                                                         │
│  WHAT IS THE PAIN?                                     │
│  └─ [Clear description]                                │
│                                                         │
│  WHEN DOES IT OCCUR?                                   │
│  └─ [Frequency, triggers]                              │
│                                                         │
│  WHAT'S THE IMPACT?                                    │
│  ├─ Time: [X hours/week]                               │
│  ├─ Money: [$X/month]                                  │
│  ├─ Quality: [Error rate, rework]                      │
│  └─ Other: [Customer satisfaction, etc]                │
│                                                         │
│  CURRENT WORKAROUNDS?                                  │
│  └─ [How they deal with it now]                        │
│                                                         │
│  ROOT CAUSE (if known)?                                │
│  └─ [Why it happens]                                   │
│                                                         │
└────────────────────────────────────────────────────────┘
```

---

## 📊 PAIN POINT CATEGORIES

### **1. TIME WASTE**
```
Description: Process takes too long
Examples:
- "Searching for information takes 20 min"
- "Waiting for approval takes 2 days"
- "Manual data entry takes 3 hours/day"

Impact Metric: Hours/week lost
```

### **2. MONEY LOSS**
```
Description: Process costs money unnecessarily
Examples:
- "Errors cost $5K/month in rework"
- "Overtime due to inefficiency: $10K/month"
- "Lost sales due to slow response: $20K/month"

Impact Metric: $/month lost
```

### **3. QUALITY ISSUES**
```
Description: Errors, defects, inconsistency
Examples:
- "15% error rate in invoices"
- "Rework required 30% of the time"
- "Inconsistent customer experience"

Impact Metric: % error rate, rework %
```

### **4. CONTROL LOSS**
```
Description: Lack of visibility, inability to manage
Examples:
- "Don't know real-time inventory"
- "Can't track order status"
- "No visibility into pipeline"

Impact Metric: Decisions delayed, risks not identified
```

### **5. RISK EXPOSURE**
```
Description: Compliance, security, liability risks
Examples:
- "Manual process prone to compliance violations"
- "Data not backed up properly"
- "No audit trail"

Impact Metric: Risk severity × probability
```

### **6. PEOPLE IMPACT**
```
Description: Frustration, burnout, turnover
Examples:
- "Staff frustrated, considering leaving"
- "Burnout from repetitive work"
- "Conflict due to unclear process"

Impact Metric: Turnover rate, satisfaction scores
```

---

## 📏 SCORING SYSTEM

### **Frequency Score** (1-5)
```
5 = Multiple times per day
4 = Daily
3 = Weekly
2 = Monthly
1 = Occasionally / Rarely

Example:
"Searching for documents" → Daily → Score: 4
"Server crash" → Monthly → Score: 2
```

### **Impact Score** (1-5)
```
5 = Critical (business-threatening)
4 = High (significant cost/delay)
3 = Medium (noticeable impact)
2 = Low (minor inconvenience)
1 = Minimal (barely noticeable)

Example:
"Cannot process orders" → Critical → Score: 5
"Report takes longer" → Medium → Score: 3
```

### **Priority Score** (Frequency × Impact)
```
Priority = Frequency × Impact
Range: 1-25

25 = Daily + Critical (ADDRESS IMMEDIATELY)
20 = Daily + High (HIGH PRIORITY)
16 = Daily + Medium / Weekly + Critical
12 = Weekly + High / Daily + Low
9 = Weekly + Medium
6 = Weekly + Low / Monthly + Medium
4 = Monthly + Low
1 = Rare + Minimal (LOW PRIORITY)

Prioritization:
20-25 = CRITICAL (must fix in MVP)
12-19 = HIGH (should fix in MVP)
6-11 = MEDIUM (post-MVP)
1-5 = LOW (backlog)
```

---

## 🎯 WORKED EXAMPLES

### **Example 1: Clínica - Multiple Pain Points**

```yaml
Pain Point 1:
  id: PP-001
  description: "Recepcionista pasa 20 min/día buscando información de pacientes en múltiples archivos Excel"
  category: time_waste
  affected_roles: ["Recepcionista", "Enfermera"]
  frequency: 5 (Multiple times daily - ~10 searches/day)
  impact: 3 (Medium - delays but not critical)
  priority_score: 15 (HIGH)
  quantified_impact:
    time_lost: "20 min × 10 searches × 20 días/mes = 67 horas/mes"
    cost: "67 hrs × $10/hr = $670/mes"
  workarounds: "Llama al contador, busca en 3 archivos diferentes"
  root_cause: "Información dispersa en múltiples Excel sin centralizar"

Pain Point 2:
  id: PP-002
  description: "Citas duplicadas 10% del tiempo causan conflictos con pacientes"
  category: quality
  affected_roles: ["Recepcionista", "Médico", "Paciente"]
  frequency: 4 (Daily - 3 de 30 citas/día)
  impact: 4 (High - enfado del paciente, pérdida de tiempo)
  priority_score: 16 (HIGH)
  quantified_impact:
    time_lost: "30 min/día resolviendo conflictos = 10 hrs/mes"
    money_lost: "Potencial pérdida de paciente: ~$500/mes"
    quality: "Satisfacción del paciente afectada"
  workarounds: "Doble check manual, llamar paciente para re-agendar"
  root_cause: "Dos sistemas (calendario físico + Excel) no sincronizados"

Pain Point 3:
  id: PP-003
  description: "Contador pasa 15 horas/semana conciliando datos para facturación"
  category: time_waste + money_loss
  affected_roles: ["Contador"]
  frequency: 5 (Daily)
  impact: 4 (High - costo significativo)
  priority_score: 20 (CRITICAL)
  quantified_impact:
    time_lost: "15 hrs/semana = 60 hrs/mes"
    cost: "60 hrs × $20/hr = $1,200/mes"
  workarounds: "Horas extras, usar múltiples hojas de cálculo"
  root_cause: "Datos manuales en Excel propensos a error"

Pain Point 4:
  id: PP-004
  description: "Director no tiene visibilidad de rentabilidad por paciente/servicio"
  category: control_loss
  affected_roles: ["Director"]
  frequency: 2 (Monthly cuando necesita analizar)
  impact: 4 (High - decisiones sin datos)
  priority_score: 8 (MEDIUM)
  quantified_impact:
    opportunity_cost: "Servicios no rentables continúan ofreciéndose"
  workarounds: "Análisis manual ocasional (toma 1 día completo)"
  root_cause: "Sin sistema que agregue datos de ingresos/costos"
```

**Prioritization**:
1. PP-003 (20) - Contador tiempo → MVP MUST
2. PP-002 (16) - Citas duplicadas → MVP MUST
3. PP-001 (15) - Búsqueda info → MVP SHOULD
4. PP-004 (8) - Dashboard rentabilidad → POST-MVP

---

### **Example 2: Manufactura - Production Delays**

```yaml
Pain Point 1:
  id: PP-001
  description: "30% órdenes retrasadas > 2 días esperando materiales"
  category: time_waste + money_loss
  frequency: 5 (Daily)
  impact: 5 (Critical - afecta delivery)
  priority_score: 25 (CRITICAL)
  quantified_impact:
    time_lost: "50 hrs/mes production time lost"
    money_lost: "Late penalties: $15K/mes"
  root_cause: "Inventario no refleja disponibilidad real"

Pain Point 2:
  id: PP-002
  description: "Operadores deben caminar a oficina para registrar movimientos (10 min cada vez)"
  category: time_waste
  frequency: 5 (Daily - 20 movimientos/día)
  impact: 2 (Low per incident, pero frequent)
  priority_score: 10 (MEDIUM)
  quantified_impact:
    time_lost: "10 min × 20 × 20 días = 67 hrs/mes"
  root_cause: "Sistema no accesible desde planta"
```

---

## 🎨 VISUALIZATION: PRIORITY MATRIX

```
High Impact (5)
    │
    │  [PP-003]           [PP-001]
    │  Contador           Materiales
    │  (20)               (25)
    │
    │              [PP-002]
    │              Citas Dup
    │              (16)
    │
    │      [PP-001]
    │      Búsqueda
    │      (15)
    │
    │                       [PP-004]
    │                       Dashboard
    │                       (8)
────┼────────────────────────────────────────→ High Frequency (5)
    │
Low Impact (1)
```

---

## 📋 PAIN POINT TEMPLATE

```markdown
# PAIN POINT: [ID]

## DESCRIPTION
[What is the pain point in one clear sentence]

## WHO SUFFERS
- **Primary**: [Role who feels it most]
- **Secondary**: [Other affected roles]
- **Frequency per person**: [How often each person experiences it]

## WHEN IT OCCURS
- **Trigger**: [What causes it]
- **Frequency**: [ ] Multiple/day  [ ] Daily  [ ] Weekly  [ ] Monthly  [ ] Rare
- **Pattern**: [Any pattern? Time of day, month-end, etc]

## IMPACT
### Time
- **Per incident**: [X minutes/hours]
- **Total per period**: [X hours/week or month]

### Money
- **Direct cost**: [$X/month]
- **Indirect cost**: [$X opportunity cost, etc]

### Quality
- **Error rate**: [%]
- **Rework required**: [% or hours]

### Other
- **Customer impact**: [If applicable]
- **Employee satisfaction**: [If applicable]
- **Risk**: [If applicable]

## SCORING
- **Frequency Score**: [1-5] - [Rationale]
- **Impact Score**: [1-5] - [Rationale]
- **Priority Score**: [Frequency × Impact]

## CURRENT WORKAROUNDS
1. [Workaround 1]
2. [Workaround 2]

**Effectiveness**: [How well do workarounds help?]
**Cost of workarounds**: [Time/money spent on workarounds]

## ROOT CAUSE
**Known root cause**: [If identified from 5 Whys, etc]
**Assumptions**: [If root cause is assumed]

## EVIDENCE
- [ ] Observed directly
- [ ] Reported by multiple sources
- [ ] Backed by data/metrics
- [ ] Single source report
- [ ] Assumed

## RECOMMENDED ACTION
**Priority**: [ ] CRITICAL  [ ] HIGH  [ ] MEDIUM  [ ] LOW
**Timing**: [ ] MVP Must Have  [ ] MVP Should Have  [ ] Post-MVP  [ ] Backlog
**Effort to fix**: [ ] Low  [ ] Medium  [ ] High
**Fix approach**: [Brief description of how to address]
```

---

## 💡 BEST PRACTICES

### **1. Quantify Everything**
```
❌ "Takes a lot of time"
✅ "20 minutes per occurrence, 10x/day = 3.3 hrs/day"

❌ "Costs money"
✅ "$5K/month in error corrections"
```

### **2. Get Multiple Perspectives**
```
Pain point reported by 1 person → Validate
Pain point reported by 3+ people → Likely real

Different roles may experience same issue differently:
- Manager: "We're losing money"
- User: "It's frustrating and slow"
Both valid, both important
```

### **3. Prioritize Ruthlessly**
```
You can't fix everything in MVP

Focus on:
- High frequency + High impact (Priority 20-25)
- Must-fix to deliver core value

Defer:
- Low frequency or low impact
- Nice-to-haves
```

### **4. Link to Root Causes**
```
Pain Point → Root Cause → Solution

Multiple pain points may have same root:
PP-001: Búsqueda lenta  ─┐
PP-002: Datos duplicados ├─→ Root: Información dispersa
PP-003: Errores frecuentes─┘      → Solution: Centralizar datos
```

---

## 📊 OUTPUT FORMAT

```json
{
  "pain_point_canvas": {
    "engagement_id": "ENG-20250119-001",
    "analyzed_at": "2025-01-19",
    "pain_points": [
      {
        "id": "PP-001",
        "description": "...",
        "category": "time_waste",
        "affected_roles": ["Role1", "Role2"],
        "frequency": {
          "score": 4,
          "description": "Daily"
        },
        "impact": {
          "score": 3,
          "description": "Medium"
        },
        "priority_score": 12,
        "quantified_impact": {
          "time_lost": "20 hrs/month",
          "money_lost": "$500/month",
          "quality_impact": "10% error rate"
        },
        "workarounds": ["...", "..."],
        "root_cause": "...",
        "evidence_type": "observed",
        "recommendation": {
          "priority": "HIGH",
          "timing": "MVP Should Have",
          "effort": "Medium"
        }
      }
    ],
    "summary": {
      "total_pain_points": 12,
      "critical": 2,
      "high": 4,
      "medium": 4,
      "low": 2,
      "total_time_impact": "150 hrs/month",
      "total_money_impact": "$8,500/month"
    }
  }
}
```

---

**END OF SKILL: Pain Point Canvas**
