# SKILL: BPMN Assistant

## 📋 METADATA
- **Skill ID**: `SKILL-005`
- **Category**: `Process Modeling`
- **Used By**: Process Intelligence Agent
- **Version**: `1.0.0`

---

## 🎯 PURPOSE
Guiar el mapeo de procesos usando notación BPMN 2.0, asegurando diagramas claros y estandarizados.

---

## 📊 BPMN ELEMENTS QUICK REFERENCE

### **Core Elements**

| Element | Symbol | Usage | Example |
|---------|--------|-------|---------|
| **Start Event** | ⭕ | Trigger que inicia proceso | Cliente llama |
| **End Event** | ⊚ | Fin del proceso | Orden completada |
| **Task/Activity** | ▭ | Acción ejecutada | Registrar cliente |
| **Exclusive Gateway** | ◇ | Decisión (if/else) | ¿Aprobado? Sí/No |
| **Parallel Gateway** | ⬦ | Actividades simultáneas | Enviar + Facturar |
| **Sequence Flow** | → | Orden de ejecución | A → B |
| **Message Flow** | ⋯→ | Comunicación entre roles | Cliente → Sistema |
| **Data Object** | 📄 | Información | Orden de compra |
| **Pool/Lane** | ▭▭▭ | Roles/Sistemas | Recepcionista / Sistema |

---

## 🗺️ PROCESS MAPPING TEMPLATE

```
┌─────────────────────────────────────────────────────────┐
│ PROCESO: [Nombre del Proceso]                          │
├─────────────────────────────────────────────────────────┤
│ LANE: [Rol 1]                                          │
│   ⭕ → [Actividad 1] → [Actividad 2] → ◇              │
│                                          ├─Sí→ [Act 3] │
│                                          └─No→ [Act 4] │
├─────────────────────────────────────────────────────────┤
│ LANE: [Rol 2]                                          │
│                [Actividad 5] → [Actividad 6] → ⊚       │
└─────────────────────────────────────────────────────────┘
```

---

## 📋 MAPPING WORKFLOW

### **STEP 1: Define Scope**
```yaml
Start Event: ¿Qué inicia el proceso?
End Event: ¿Cuándo termina?
Boundaries: ¿Qué está dentro/fuera?

Example:
Start: "Cliente solicita cita"
End: "Cita confirmada y registrada"
Out of scope: Facturación posterior
```

### **STEP 2: Identify Actors**
```yaml
Roles/Lanes needed:
- Cliente
- Recepcionista
- Sistema
- Médico (si aplica)

Each role = One swim lane
```

### **STEP 3: Map Happy Path**
```
1. Start → Primera actividad
2. Actividad 1 → Actividad 2
3. Continue until End
4. No excepciones aún

Focus: El flujo normal sin errores
```

### **STEP 4: Add Gateways (Decisions)**
```
Where decisions occur:
◇ Exclusive (XOR): Solo una ruta
  Example: ¿Aprobado? → Sí o No

⬦ Parallel (AND): Ambas rutas
  Example: Enviar email Y actualizar sistema
```

### **STEP 5: Add Exceptions**
```
Common exception patterns:
- Error handling paths
- Rework loops
- Escalation paths
- Timeout scenarios

Mark with different color or annotation
```

### **STEP 6: Annotate Details**
```
For each activity:
- Duration (average)
- Frequency (per day/week)
- Tools used
- Pain points (⚠️ icon)
```

---

## 🎯 EXAMPLE: Appointment Scheduling

```
┌────────────────────────────────────────────────────────────┐
│ PROCESO: Agendamiento de Cita                             │
├────────────────────────────────────────────────────────────┤
│ CLIENTE                                                    │
│   ⭕ Llama → [Proporciona info] ⋯→                        │
│                                  ↓                         │
├────────────────────────────────────────────────────────────┤
│ RECEPCIONISTA                                             │
│              ← [Recibe llamada] → [Busca disponibilidad]  │
│              ⚠️ 10 min           → [Registra en Excel]    │
│              → [Confirma por teléfono] → ⊚                │
├────────────────────────────────────────────────────────────┤
│ SISTEMA (Excel)                                           │
│                      [Calendario físico consultado] 📄     │
└────────────────────────────────────────────────────────────┘

Legend:
⚠️ = Pain point identified
📄 = Document/Data used
⋯→ = Communication between lanes
```

---

## 💡 BEST PRACTICES

### **1. Keep It Simple**
```
✅ One page per process
✅ 5-15 activities per diagram
✅ Clear naming (Verb + Object)

❌ 50+ activities (split into sub-processes)
❌ Vague names ("Process data")
❌ Too much detail
```

### **2. Naming Convention**
```
Activities: [Verb] + [Object]
✅ "Registrar cliente"
✅ "Validar orden"
✅ "Enviar confirmación"

❌ "Registro" (incomplete)
❌ "Paso 1" (not descriptive)
```

### **3. Use Annotations**
```
Add metadata:
[Activity Name]
Duration: 5 min
Frequency: 30x/day
Tool: Excel
⚠️ Error prone
```

### **4. Highlight Pain Points**
```
Visual indicators:
⚠️ = Friction/Problem
🔥 = Bottleneck
💰 = High cost
⏱️ = Time waste
```

---

## 📤 OUTPUT FORMAT

```json
{
  "bpmn_diagram": {
    "process_id": "PROC-001",
    "process_name": "Appointment Scheduling",
    "scope": {
      "start_event": "Cliente solicita cita",
      "end_event": "Cita confirmada",
      "boundaries": "Desde llamada hasta confirmación"
    },
    "lanes": [
      {
        "lane_id": "L1",
        "actor": "Cliente",
        "activities": [...]
      },
      {
        "lane_id": "L2",
        "actor": "Recepcionista",
        "activities": [
          {
            "id": "A1",
            "name": "Recibir llamada",
            "type": "task",
            "duration": "2 min",
            "tools": ["Teléfono"],
            "pain_points": []
          },
          {
            "id": "A2",
            "name": "Buscar disponibilidad",
            "type": "task",
            "duration": "10 min",
            "tools": ["Calendario físico"],
            "pain_points": ["Búsqueda manual lenta"]
          }
        ]
      }
    ],
    "connections": [
      {"from": "START", "to": "A1"},
      {"from": "A1", "to": "A2"},
      {"from": "A2", "to": "A3"}
    ],
    "gateways": [
      {
        "id": "G1",
        "type": "exclusive",
        "question": "¿Hay disponibilidad?",
        "outcomes": ["Sí", "No"]
      }
    ]
  }
}
```

---

## 🔗 INTEGRATION

**Input from**:
- Process interviews
- Observation notes
- Existing documentation

**Output to**:
- `as_is_process.json`
- Bottleneck analysis
- TO-BE redesign

---

## ✅ QUALITY CHECKLIST

- [ ] Start and End events clearly defined
- [ ] All activities named with Verb + Object
- [ ] Lanes represent different actors
- [ ] Sequence flows show logical order
- [ ] Gateways have clear decision criteria
- [ ] Pain points marked
- [ ] Durations annotated
- [ ] Process fits on one page
- [ ] Users validate "así lo hacemos"

---

**END OF SKILL: BPMN Assistant**
