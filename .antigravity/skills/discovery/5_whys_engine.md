# SKILL: 5 Whys Engine

## 📋 METADATA
- **Skill ID**: `SKILL-002`
- **Category**: `Discovery`
- **Used By**: Discovery Orchestrator, Process Intelligence
- **Version**: `1.0.0`
- **Origin**: Toyota Production System (Lean Manufacturing)

---

## 🎯 PURPOSE

Guiar el análisis de causa raíz usando la técnica de los 5 Whys, ayudando a profundizar desde síntomas superficiales hasta causas raíz verdaderas.

---

## 📥 INPUT

```json
{
  "problem_statement": "string (the perceived problem or symptom)",
  "context": {
    "domain": "string (optional)",
    "frequency": "string (optional)",
    "impact": "string (optional)"
  }
}
```

---

## 📤 OUTPUT

```json
{
  "analysis_id": "5WHY-YYYYMMDD-XXXXXX",
  "initial_problem": "string",
  "chain": [
    {
      "level": 1,
      "why": "¿Por qué ocurre el problema inicial?",
      "answer": "string",
      "evidence": "string",
      "validation_status": "validated|assumed|uncertain"
    }
  ],
  "root_cause": "string (the final why)",
  "confidence_level": "high|medium|low",
  "actionable_fix": "string"
}
```

---

## 🔧 METHODOLOGY

### **The 5 Whys Framework**

```
Problem Statement (Surface symptom)
    ↓
Why #1? → Reason 1 (Immediate cause)
    ↓
Why #2? → Reason 2 (Deeper cause)
    ↓
Why #3? → Reason 3 (Systemic cause)
    ↓
Why #4? → Reason 4 (Organizational cause)
    ↓
Why #5? → ROOT CAUSE (Foundational issue)
```

**Key Principle**: Stop when you reach something that is:
1. **Actionable**: You can fix it
2. **Foundational**: Fixing it eliminates the problem
3. **Not "because that's how it is"**: Real reason, not acceptance

---

## 📋 TEMPLATE STRUCTURE

### **5 Whys Analysis Template**

```markdown
## PROBLEM STATEMENT
[Clear, specific description of the problem]

---

### WHY #1: Why does [problem] occur?
**Answer**: [First-level reason]
**Evidence**: [How do we know this? Observed, reported, data]
**Validated**: [Yes/No/Partially]

---

### WHY #2: Why does [reason from Why #1] occur?
**Answer**: [Second-level reason]
**Evidence**: [Supporting evidence]
**Validated**: [Yes/No/Partially]

---

### WHY #3: Why does [reason from Why #2] occur?
**Answer**: [Third-level reason]
**Evidence**: [Supporting evidence]
**Validated**: [Yes/No/Partially]

---

### WHY #4: Why does [reason from Why #3] occur?
**Answer**: [Fourth-level reason]
**Evidence**: [Supporting evidence]
**Validated**: [Yes/No/Partially]

---

### WHY #5: Why does [reason from Why #4] occur?
**Answer**: [ROOT CAUSE]
**Evidence**: [Supporting evidence]
**Validated**: [Yes/No/Partially]

---

## ROOT CAUSE IDENTIFIED
**Root Cause**: [Final answer]
**Confidence**: [High/Medium/Low]

**Validation Test**: If we fix [root cause], will [original problem] be eliminated?
→ [Yes/No/Partially - explain]

**Actionable Fix**: [What concrete action addresses the root cause]
```

---

## 🎯 WORKED EXAMPLES

### **Example 1: Clínica - Citas Duplicadas**

```markdown
## PROBLEM STATEMENT
10% de las citas se agendan duplicadas, causando conflictos

---

### WHY #1: ¿Por qué se agendan citas duplicadas?
**Answer**: La recepcionista no ve todas las citas agendadas
**Evidence**: Observación directa, recepcionista confirmó
**Validated**: Yes

---

### WHY #2: ¿Por qué no ve todas las citas agendadas?
**Answer**: Las citas están registradas en dos lugares: calendario físico + Excel
**Evidence**: Se vieron ambos sistemas en uso
**Validated**: Yes

---

### WHY #3: ¿Por qué hay dos sistemas?
**Answer**: El Excel lo empezó a usar contabilidad para facturación, el calendario físico era el original
**Evidence**: Entrevista con contador y recepcionista
**Validated**: Yes

---

### WHY #4: ¿Por qué no consolidaron en un solo sistema?
**Answer**: Nadie tenía la autoridad ni el tiempo para decidir qué sistema usar y migrar datos
**Evidence**: Director confirmó que no había proceso de decisión
**Validated**: Yes

---

### WHY #5: ¿Por qué no había autoridad/tiempo para tomar esa decisión?
**Answer**: La clínica creció rápidamente de 5 a 20 empleados sin definir procesos formales ni roles claros
**Evidence**: Director explicó crecimiento no planificado
**Validated**: Yes

---

## ROOT CAUSE IDENTIFIED
**Root Cause**: Crecimiento organizacional sin estructura formal de procesos ni roles definidos

**Validation Test**: Si definimos roles claros y procesos formales, ¿se eliminarían las citas duplicadas?
→ Yes - Con proceso formal de gestión de citas en UN sistema centralizado

**Actionable Fix**: 
1. Definir proceso formal de agenda (un solo sistema)
2. Asignar responsable de mantener integridad del calendario
3. Migrar datos históricos a sistema único
```

---

### **Example 2: Manufactura - Retrasos en Producción**

```markdown
## PROBLEM STATEMENT
30% de las órdenes de producción se retrasan más de 2 días

---

### WHY #1: ¿Por qué se retrasan las órdenes?
**Answer**: Esperan materiales que no están disponibles
**Evidence**: Log de producción muestra "waiting for materials"
**Validated**: Yes

---

### WHY #2: ¿Por qué los materiales no están disponibles?
**Answer**: El inventario no refleja lo que realmente hay en bodega
**Evidence**: Conteo físico vs. sistema difiere en 25%
**Validated**: Yes

---

### WHY #3: ¿Por qué el inventario no es preciso?
**Answer**: Las salidas de material no siempre se registran en el sistema
**Evidence**: Operadores confirmaron que "a veces olvidan registrar"
**Validated**: Yes

---

### WHY #4: ¿Por qué olvidan registrar las salidas?
**Answer**: El proceso de registro es manual y tedioso (lleva 10 min), y cuando hay prisa lo saltan
**Evidence**: Observación del proceso, entrevistas
**Validated**: Yes

---

### WHY #5: ¿Por qué el proceso es manual y tedioso?
**Answer**: El sistema de inventario no está integrado con el área de producción; tienen que caminar a oficina y escribir en computadora
**Evidence**: Sistema legacy sin terminales en planta
**Validated**: Yes

---

## ROOT CAUSE IDENTIFIED
**Root Cause**: Sistema de inventario legacy no integrado con proceso de producción, causando fricción que lleva a no registrar movimientos

**Validation Test**: Si facilitamos el registro de movimientos (ej: tablet en planta), ¿mejoraría la precisión del inventario y se reducirían retrasos?
→ Yes - Elimina la fricción que causa el no-registro

**Actionable Fix**: 
1. Implementar terminales/tablets en área de producción
2. Simplificar proceso de registro (scan QR vs. manual entry)
3. Hacer registro obligatorio antes de retirar material (control en bodega)
```

---

### **Example 3: RH - Alta Rotación de Personal**

```markdown
## PROBLEM STATEMENT
Rotación de personal es 35% anual (industry average es 15%)

---

### WHY #1: ¿Por qué la gente se va?
**Answer**: Exit interviews muestran "falta de crecimiento" como razón #1
**Evidence**: 70% de exit interviews mencionan esto
**Validated**: Yes

---

### WHY #2: ¿Por qué sienten falta de crecimiento?
**Answer**: No hay plan de carrera definido ni promociones claras
**Evidence**: No existe documento de career paths, últimas 5 promociones fueron ad-hoc
**Validated**: Yes

---

### WHY #3: ¿Por qué no hay planes de carrera?
**Answer**: RH nunca los diseñó porque "no teníamos tiempo"
**Evidence**: Director RH confirmó
**Validated**: Yes

---

### WHY #4: ¿Por qué RH no tenía tiempo?
**Answer**: Equipo de RH pasa 80% del tiempo en tareas operativas (nómina, permisos, etc)
**Evidence**: Time tracking de RH
**Validated**: Yes

---

### WHY #5: ¿Por qué RH está sobrecargado con tareas operativas?
**Answer**: Procesos de RH son manuales (Excel, papel); no hay automatización ni self-service para empleados
**Evidence**: Observación de procesos, 50+ tickets/semana de "solicitudes simples"
**Validated**: Yes

---

## ROOT CAUSE IDENTIFIED
**Root Cause**: Procesos de RH manuales consumen capacidad del equipo, dejando sin tiempo para iniciativas estratégicas como desarrollo de talento

**Validation Test**: Si automatizamos procesos operativos de RH, ¿tendrían tiempo para crear planes de carrera y reducir rotación?
→ Yes - Liberaría 50-60% del tiempo de RH para trabajo estratégico

**Actionable Fix**: 
1. Implementar self-service para empleados (solicitudes, consultas)
2. Automatizar procesos repetitivos (aprobaciones, permisos)
3. Con tiempo liberado, diseñar e implementar career paths
```

---

## 🚨 COMMON PITFALLS & HOW TO AVOID

### **Pitfall 1: Stopping Too Soon**
```
❌ BAD:
Problem: Errores en facturación
Why #1: Software tiene bugs
STOP → This is not root cause!

✅ GOOD:
Problem: Errores en facturación
Why #1: Software tiene bugs
Why #2: ¿Por qué el software tiene bugs?
   → Falta QA testing
Why #3: ¿Por qué no hay QA?
   → No está en el presupuesto
Why #4: ¿Por qué no está presupuestado?
   → Management prioriza velocidad sobre calidad
ROOT CAUSE: Cultura de "ship fast" sin control de calidad
```

### **Pitfall 2: Going in Circles**
```
❌ BAD:
Why #1: A causa B
Why #2: B causa C
Why #3: C causa A ← Loop!

FIX: Revisar si estás confundiendo síntoma con causa
```

### **Pitfall 3: Multiple Causes (Splitting)**
```
⚠️ CAUTION:
Why #1: ¿Por qué X?
Answer: Por A y B y C ← Multiple branches

FIX: Elegir la causa DOMINANTE o hacer 5 Whys por cada branch
```

### **Pitfall 4: Accepting "That's How It Is"**
```
❌ BAD:
Why #5: ¿Por qué no hay proceso?
Answer: "Porque nunca lo hemos tenido"
← NOT actionable!

✅ GOOD:
Why #5: ¿Por qué nunca lo implementaron?
Answer: "Porque no había claridad sobre quién era responsable de definirlo"
ROOT CAUSE: Falta de ownership sobre diseño de procesos
```

---

## 🎓 BEST PRACTICES

### **1. Validate Each Why**
```
For each answer, ask:
- "¿Cómo sabemos esto?"
- "¿Es observado o asumido?"
- "¿Podemos verificarlo?"

Evidence types:
✅ Observed directly
✅ Reported by multiple sources
✅ Backed by data
⚠️ Single person's opinion
❌ Pure assumption
```

### **2. Use Different Types of Why**
```
Not just "Why did X happen?"
Also:
- "Why didn't Y prevent this?"
- "Why wasn't this caught earlier?"
- "Why is this acceptable?"
```

### **3. Involve People Who Know**
```
Don't do 5 Whys in isolation
Include:
- People who experience the problem
- People who work the process
- People who have historical context
```

### **4. Test the Root Cause**
```
Final validation:
"If we fix [root cause], will [original problem] be completely eliminated?"

If answer is "No" or "Partially" → Not true root cause yet
```

### **5. Look for Systemic vs. Individual Causes**
```
❌ BAD root cause: "Juan forgot to do X"
   → This blames individual

✅ GOOD root cause: "No checklist exists to ensure X is done"
   → This addresses system
```

---

## 📊 OUTPUT QUALITY CHECKLIST

### **Good 5 Whys Analysis Has**:
- [ ] Clear problem statement (specific, measurable)
- [ ] Each "why" has evidence
- [ ] Progresses from symptom to system
- [ ] Reaches actionable root cause
- [ ] Root cause is validated (if we fix it, problem goes away)
- [ ] Root cause addresses system, not individual
- [ ] 3-5 levels deep (sometimes 3 is enough, sometimes need 6+)

### **Red Flags**:
- ⚠️ Stops at "software bug" or "human error" (too shallow)
- ⚠️ Root cause is "bad luck" or "that's how it is" (not actionable)
- ⚠️ No evidence for answers (pure speculation)
- ⚠️ Blames individual person (should be system)
- ⚠️ Circular logic (A causes B causes A)

---

## 🔗 INTEGRATION

**Used by**:
- Discovery Orchestrator → Root cause analysis
- Process Intelligence → Understanding process problems
- Redesign Agent → Validating improvement hypotheses

**Inputs from**:
- Interview notes
- Problem statement
- Observation data

**Outputs to**:
- `problem_statement.json` → root_causes field
- Root cause diagrams
- Actionable recommendations

---

## 📝 USAGE TEMPLATE

```markdown
# 5 WHYS ANALYSIS

**Date**: YYYY-MM-DD
**Analyst**: [Name]
**Participants**: [Names of people involved]

---

## PROBLEM STATEMENT
[One sentence describing the problem]
- **Frequency**: [How often it occurs]
- **Impact**: [Quantified impact]

---

## ANALYSIS

### WHY #1
**Question**: Why does [problem] occur?
**Answer**: 
**Evidence**: 
**Validated**: [ ] Yes  [ ] No  [ ] Partially

### WHY #2
**Question**: Why does [answer #1] occur?
**Answer**: 
**Evidence**: 
**Validated**: [ ] Yes  [ ] No  [ ] Partially

### WHY #3
**Question**: Why does [answer #2] occur?
**Answer**: 
**Evidence**: 
**Validated**: [ ] Yes  [ ] No  [ ] Partially

### WHY #4
**Question**: Why does [answer #3] occur?
**Answer**: 
**Evidence**: 
**Validated**: [ ] Yes  [ ] No  [ ] Partially

### WHY #5
**Question**: Why does [answer #4] occur?
**Answer**: 
**Evidence**: 
**Validated**: [ ] Yes  [ ] No  [ ] Partially

---

## ROOT CAUSE
**Identified Root Cause**: 

**Confidence Level**: [ ] High  [ ] Medium  [ ] Low

**Validation Question**: If we fix [root cause], will [original problem] be eliminated?
**Answer**: 

---

## ACTIONABLE RECOMMENDATIONS
1. [Action 1]
2. [Action 2]
3. [Action 3]

---

## NEXT STEPS
- [ ] Validate root cause with additional data
- [ ] Present findings to stakeholders
- [ ] Design solution to address root cause
```

---

**END OF SKILL: 5 Whys Engine**
