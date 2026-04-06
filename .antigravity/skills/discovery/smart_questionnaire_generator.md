# SKILL: Smart Questionnaire Generator

## 📋 METADATA
- **Skill ID**: `SKILL-001`
- **Category**: `Discovery`
- **Used By**: Intake Agent, Discovery Orchestrator
- **Version**: `1.0.0`

---

## 🎯 PURPOSE

Generar cuestionarios inteligentes y contextuales para discovery, adaptados al dominio del problema y al perfil del entrevistado.

---

## 📥 INPUT

```json
{
  "domain": "process_digitalization|conflict_resolution|risk_assessment|operational_improvement",
  "interviewee_role": "executive|manager|operational_user|technical|customer",
  "engagement_phase": "intake|discovery|validation",
  "context": {
    "industry": "string (optional)",
    "problem_hint": "string (optional)"
  }
}
```

---

## 📤 OUTPUT

```json
{
  "questionnaire_id": "QUEST-YYYYMMDD-XXXXXX",
  "questions": [
    {
      "id": "Q1",
      "section": "Context",
      "question": "¿Cómo se llama su organización y a qué se dedica?",
      "type": "open_ended",
      "follow_up_triggers": ["if mentions specific industry → ask industry-specific questions"],
      "rationale": "Establece contexto básico"
    }
  ]
}
```

---

## 🔧 QUESTION TEMPLATES

### **INTAKE PHASE - Executive**

```yaml
Section: Organization Context
Q1:
  question: "¿Cómo se llama su organización y a qué se dedica?"
  type: open_ended
  
Q2:
  question: "¿Cuántas personas trabajan en la organización?"
  type: numeric
  follow_up: "if > 50 → ¿Cuántas ubicaciones tienen?"

Q3:
  question: "¿Qué los motivó a buscar ayuda en este momento?"
  type: open_ended
  critical: true
  
Section: Problem Context
Q4:
  question: "En sus propias palabras, ¿cuál es el desafío que enfrentan?"
  type: open_ended
  critical: true
  
Q5:
  question: "¿Cómo les está afectando este desafío actualmente?"
  type: open_ended
  follow_up: "Ask for quantification: tiempo, dinero, clientes"

Q6:
  question: "¿Han intentado resolver esto antes? ¿Qué funcionó y qué no?"
  type: open_ended
```

---

### **DISCOVERY PHASE - Operational User**

```yaml
Section: Daily Work
Q1:
  question: "¿Cuál es su rol y qué hace en un día típico?"
  type: open_ended
  
Q2:
  question: "Descríbame paso a paso cómo hace [proceso específico]"
  type: process_flow
  note: "Take detailed notes of each step"

Section: Pain Points
Q3:
  question: "¿Qué es lo más frustrante de este proceso?"
  type: open_ended
  critical: true
  
Q4:
  question: "¿Dónde pierde más tiempo en su trabajo diario?"
  type: open_ended
  follow_up: "¿Cuánto tiempo aproximadamente? (horas/día)"
  
Q5:
  question: "¿Con qué frecuencia ocurren errores en este proceso?"
  type: frequency
  options: ["Diario", "Semanal", "Mensual", "Raro"]
  follow_up: "if Diario|Semanal → ¿Qué tipo de errores?"

Section: Workarounds
Q6:
  question: "¿Qué trucos o atajos usa para hacer su trabajo más fácil?"
  type: open_ended
  note: "Workarounds reveal broken processes"
  
Q7:
  question: "Si pudiera cambiar UNA cosa de su proceso, ¿qué sería?"
  type: open_ended
  critical: true
```

---

### **DISCOVERY PHASE - Manager**

```yaml
Section: Management Perspective
Q1:
  question: "¿Qué métricas usa para medir el desempeño de este proceso?"
  type: open_ended
  follow_up: "¿Cuáles son los valores actuales?"
  
Q2:
  question: "¿Cuánto tiempo/dinero cuesta actualmente este proceso?"
  type: quantitative
  
Q3:
  question: "¿Qué tan urgente es resolver esto en una escala de 1-10?"
  type: scale
  follow_up: "if > 7 → ¿Qué pasa si no se resuelve en X meses?"

Section: Team & Resources
Q4:
  question: "¿Quién está más afectado por este problema en el día a día?"
  type: stakeholder_mapping
  
Q5:
  question: "¿Tiene presupuesto asignado para resolver esto?"
  type: yes_no
  follow_up_yes: "¿En qué rango estamos hablando?"
  follow_up_no: "¿Hay proceso para conseguirlo?"
  
Q6:
  question: "¿Su equipo tiene capacidad para participar en un proyecto de mejora?"
  type: yes_no
  follow_up: "¿Cuánto tiempo pueden dedicar?"
```

---

### **DOMAIN-SPECIFIC: Process Digitalization**

```yaml
Current State:
Q1:
  question: "¿Cómo registran la información actualmente?"
  type: multiple_choice
  options: ["Papel", "Excel", "Sistema específico", "Varios métodos"]
  follow_up: "Para cada método, preguntar detalles"
  
Q2:
  question: "¿Cuántas veces tienen que ingresar la misma información?"
  type: numeric
  note: "Re-entry is waste"
  
Q3:
  question: "¿Qué información necesitan que no tienen fácilmente disponible?"
  type: open_ended

Integration:
Q4:
  question: "¿Qué otros sistemas o herramientas usan en su trabajo?"
  type: list
  follow_up: "¿Cómo se comunican entre ellos?"
  
Q5:
  question: "¿Hay información que copian de un sistema a otro manualmente?"
  type: yes_no
  follow_up: "¿Con qué frecuencia y cuánto tiempo toma?"
```

---

### **DOMAIN-SPECIFIC: Conflict Resolution**

```yaml
Conflict Nature:
Q1:
  question: "¿Cómo describiría la naturaleza del conflicto?"
  type: open_ended
  
Q2:
  question: "¿Cuándo empezaron a notarlo?"
  type: timeline
  follow_up: "¿Qué evento lo desencadenó?"
  
Q3:
  question: "¿Qué equipos o personas están involucrados?"
  type: stakeholder_mapping

Impact:
Q4:
  question: "¿Cómo afecta este conflicto al trabajo diario?"
  type: open_ended
  
Q5:
  question: "¿Han perdido empleados por esta situación?"
  type: yes_no
  follow_up: "¿Cuántos en los últimos 6 meses?"

Root Causes:
Q6:
  question: "En su opinión, ¿cuál es la raíz del conflicto?"
  type: open_ended
  
Q7:
  question: "¿Hay ambigüedad sobre quién es responsable de qué?"
  type: yes_no
  follow_up: "¿Puede dar ejemplos?"
```

---

### **DOMAIN-SPECIFIC: Risk Assessment**

```yaml
Risk Context:
Q1:
  question: "¿Qué tipo de riesgo les preocupa?"
  type: multiple_choice
  options: ["Compliance/Regulatorio", "Financiero", "Operacional", "Reputacional", "Seguridad"]
  
Q2:
  question: "¿Hay una regulación o auditoría que motivó esta evaluación?"
  type: yes_no
  follow_up: "¿Cuál y cuándo es el deadline?"
  
Q3:
  question: "¿Han tenido incidentes relacionados con este riesgo?"
  type: yes_no
  follow_up: "¿Cuándo y qué pasó?"

Current Controls:
Q4:
  question: "¿Qué controles tienen actualmente para mitigar este riesgo?"
  type: list
  
Q5:
  question: "¿Cómo saben si esos controles están funcionando?"
  type: open_ended
  
Q6:
  question: "¿Qué tan confiados están en su posición actual (1-10)?"
  type: scale
  follow_up: "if < 7 → ¿Qué les falta?"
```

---

## 🔄 DYNAMIC FOLLOW-UP LOGIC

### **Trigger Patterns**

```python
# Example logic for dynamic follow-ups

if answer_contains("Excel"):
    follow_up("¿Cuántos archivos de Excel diferentes usan?")
    follow_up("¿Quién tiene acceso a estos archivos?")
    follow_up("¿Qué pasa si alguien edita el archivo al mismo tiempo?")

if answer_contains("manual"):
    follow_up("¿Cuánto tiempo toma hacer esto manualmente?")
    follow_up("¿Con qué frecuencia tienen que hacerlo?")
    follow_up("¿Qué errores ocurren cuando se hace manual?")

if answer_contains("urgente|crítico|YA"):
    follow_up("¿Qué pasa específicamente si no se resuelve?")
    follow_up("¿Hay una fecha límite concreta?")
    follow_up("¿Qué tan dispuestos están a invertir para resolverlo?")

if role == "operational_user" and mentions("frustración|enojado|cansado"):
    follow_up("¿Sus colegas sienten lo mismo?")
    follow_up("¿Han comentado esto con su jefe?")
    follow_up("¿Estarían dispuestos a probar una nueva forma de hacerlo?")
```

---

## 📊 QUESTION SELECTION ALGORITHM

```
INPUT: Domain, Role, Phase
OUTPUT: Tailored questionnaire

STEP 1: Select base template
  - Phase determines question depth
  - Role determines perspective
  
STEP 2: Add domain-specific questions
  - If process_digitalization → Add tech/system questions
  - If conflict_resolution → Add interpersonal questions
  - If risk_assessment → Add compliance questions
  
STEP 3: Prioritize by criticality
  - CRITICAL questions always included
  - OPTIONAL questions if time allows
  
STEP 4: Order questions
  - Start broad (context)
  - Go specific (details)
  - End actionable ("What would you change?")
  
STEP 5: Generate follow-up rules
  - Define triggers for each question
  - Prepare conditional paths
```

---

## 💡 BEST PRACTICES

### **Question Design Principles**

1. **Open-ended over closed**: "¿Cómo hace X?" > "¿Hace X?"
2. **Specific over vague**: "¿Cuántas horas/semana?" > "¿Mucho tiempo?"
3. **Neutral over leading**: "¿Qué opina de X?" > "¿No cree que X es malo?"
4. **One concept per question**: Avoid compound questions
5. **Quantify when possible**: Ask for numbers, not feelings

### **Interview Flow**

```
1. START: Easy, contextual questions (warm up)
2. MIDDLE: Critical, potentially uncomfortable questions
3. END: Forward-looking, positive questions (leave on good note)

Example flow:
├─ "Tell me about your role" (easy)
├─ "What frustrates you most?" (critical)
└─ "If you could change one thing..." (positive)
```

### **Red Flags to Listen For**

```
Phrase → Action
"Siempre hemos hecho así" → Probe for resistance to change
"No tengo tiempo" → Assess capacity constraints
"Mi jefe no entiende" → Identify sponsor weakness
"Cada quien hace diferente" → Process standardization gap
"Excel se rompe constantemente" → Data quality issues
```

---

## 🎯 OUTPUT FORMATS

### **Standard Output**

```json
{
  "questionnaire_id": "QUEST-20250119-001",
  "generated_at": "2025-01-19T10:00:00Z",
  "target": {
    "domain": "process_digitalization",
    "role": "operational_user",
    "phase": "discovery"
  },
  "estimated_duration": "45 minutes",
  "questions": [
    {
      "id": "Q1",
      "section": "Context",
      "question": "¿Cuál es su rol y qué hace en un día típico?",
      "type": "open_ended",
      "critical": false,
      "estimated_time": "5 min",
      "follow_up_rules": []
    },
    {
      "id": "Q2",
      "section": "Pain Points",
      "question": "¿Qué es lo más frustrante de este proceso?",
      "type": "open_ended",
      "critical": true,
      "estimated_time": "10 min",
      "follow_up_rules": [
        {
          "trigger": "mentions 'tiempo'",
          "follow_up": "¿Cuántas horas/día pierde aproximadamente?"
        }
      ]
    }
  ],
  "interviewer_notes": [
    "Listen for workarounds - they reveal broken processes",
    "Quantify everything - ask 'how much' and 'how often'",
    "Validate emotions - frustration indicates pain points"
  ]
}
```

---

## 🔗 INTEGRATION

**Used by**:
- Intake Agent → Generate intake questionnaire
- Discovery Orchestrator → Generate interview guides

**Inputs from**:
- `engagement_profile.json` → Domain, industry
- Agent parameters → Role, phase

**Outputs to**:
- Interview guide document
- `discovery_log.json` → Captured responses

---

## 📝 USAGE EXAMPLE

```python
# Pseudo-code
questionnaire = generate_questionnaire(
    domain="process_digitalization",
    interviewee_role="operational_user",
    phase="discovery",
    context={
        "industry": "healthcare",
        "problem_hint": "manual appointment scheduling"
    }
)

# Result:
# - 12 core questions
# - 8 follow-up rules
# - Estimated 45 min interview
# - Healthcare-specific language
# - Focus on process flow and pain points
```

---

## ✅ VALIDATION

**Quality Checks**:
- [ ] Questions are open-ended (avoid yes/no)
- [ ] Questions quantify impact (time, money, frequency)
- [ ] Critical questions are included
- [ ] Flow is logical (general → specific)
- [ ] Domain-specific context included
- [ ] Follow-up rules are clear

---

**END OF SKILL: Smart Questionnaire Generator**
