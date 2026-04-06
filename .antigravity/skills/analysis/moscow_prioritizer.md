# SKILL: MoSCoW Prioritizer

## 📋 METADATA
- **Skill ID**: `SKILL-008`
- **Category**: `Analysis`
- **Used By**: Solution Architect Agent
- **Version**: `1.0.0`

---

## 🎯 PURPOSE
Priorizar features y requerimientos usando la metodología MoSCoW (Must, Should, Could, Won't) para definir MVP efectivo.

---

## 📊 MoSCoW CATEGORIES

### **MUST HAVE** (Crítico - MVP Blocker)
```
Definition: Sin esto, la solución NO funciona
Criteria:
  ✓ Requerido por ley/regulación
  ✓ Resuelve el pain point #1
  ✓ Core functionality sin la cual no tiene sentido
  ✓ ROI negativo sin esto

Questions:
  - "¿Qué pasa si no lo incluimos en v1?"
  - If answer is "La solución no sirve" → MUST

Target: < 30% del total de features

Examples:
  ✓ Login/autenticación (si hay datos sensibles)
  ✓ Crear orden (en sistema de órdenes)
  ✓ Búsqueda básica (en sistema de búsqueda)
  ✓ Pago (en e-commerce)
```

### **SHOULD HAVE** (Importante - Muy Deseable)
```
Definition: Importante pero la solución funciona sin esto
Criteria:
  ✓ Mejora significativa de experiencia
  ✓ Alta demanda de usuarios
  ✓ Impacto positivo en adopción
  ✓ Puede agregarse en v1.1 sin problema

Questions:
  - "¿Usuarios se frustrarán si no está?"
  - "¿Compite con alternativas sin esto?"

Target: 20-30% del total

Examples:
  ◉ Notificaciones automáticas
  ◉ Reportes básicos
  ◉ Filtros avanzados
  ◉ Export a Excel
```

### **COULD HAVE** (Nice to Have - Deseable)
```
Definition: Agrega valor pero no crítico
Criteria:
  ✓ Mejora incremental
  ✓ Pocos usuarios lo necesitan
  ✓ Puede esperar sin problema
  ✓ "Lujo" más que necesidad

Questions:
  - "¿Cuántos usuarios lo usarían realmente?"
  - "¿Vale la pena el esfuerzo?"

Target: 20-30% del total

Examples:
  ○ Dashboard sofisticado
  ○ Personalización avanzada
  ○ Integraciones secundarias
  ○ Features de conveniencia
```

### **WON'T HAVE** (Fuera de Scope - No Ahora)
```
Definition: Explícitamente fuera del alcance actual
Criteria:
  ✓ No agrega valor a MVP
  ✓ Complejidad no justificada
  ✓ Puede agregarse mucho después
  ✓ "Nice idea pero no ahora"

Questions:
  - "¿Es esto realmente necesario?"
  - "¿Podemos vivir sin esto por 6 meses?"

Target: 20-40% del total (features in backlog)

Examples:
  ✗ IA/ML avanzado (en v1)
  ✗ Mobile app (si web es suficiente)
  ✗ Integraciones no críticas
  ✗ Features "por si acaso"
```

---

## 🔄 PRIORITIZATION PROCESS

### **Step 1: List All Features**
```
Brainstorm completo:
- Requerimientos del cliente
- Ideas del equipo
- Best practices de industria
- Competitive features

Resultado: Lista de 30-50 features potenciales
```

### **Step 2: Apply Initial Filter**
```
Para cada feature, preguntar:
1. "¿Resuelve el pain point principal?"
2. "¿Es técnicamente factible en MVP timeline?"
3. "¿Costo/esfuerzo es razonable?"

Si alguna respuesta es "No" → Likely WON'T HAVE
```

### **Step 3: Categorize (First Pass)**
```
Para cada feature que pasó filtro:

MUST if:
  - Blocker absoluto
  - Regulatorio
  - Core del core

SHOULD if:
  - Importante pero no blocker
  - Alta demanda de usuarios
  - Diferenciador competitivo

COULD if:
  - Nice to have
  - Bajo impacto
  - Pocas personas lo necesitan

WON'T if:
  - Fuera de scope MVP
  - Demasiado complejo para v1
  - No justifica el esfuerzo
```

### **Step 4: Validate with Stakeholders**
```
Review con:
- Product Owner / Cliente
- End Users (muestra)
- Technical Lead

Ajustar basado en feedback
```

### **Step 5: Check MVP Size**
```
Count:
- MUST: ¿Cuántos features?
- Total effort: ¿Cuántas semanas?

Red Flags:
⚠️ MUST > 10 features → Probablemente demasiado
⚠️ MVP > 3 meses → Replantear scope

Ideal MVP:
✓ 5-8 MUST features
✓ 6-10 weeks development
✓ Demuestra valor core
```

---

## 📋 PRIORITIZATION TEMPLATE

```markdown
# MoSCoW PRIORITIZATION

## PROJECT: [Name]
## DATE: [YYYY-MM-DD]
## PARTICIPANTS: [Names]

---

## MUST HAVE (Critical for MVP)

| Feature | User Story | Effort | Rationale |
|---------|-----------|--------|-----------|
| User Login | As a user, I want to login | 3 days | Security requirement |
| Create Order | As a user, I want to create order | 5 days | Core functionality |
| View Order Status | As a user, I want to see my orders | 2 days | Minimum viable |

**Total MUST effort**: 10 days (2 weeks)
**Validation**: Cliente confirmó que sin estos 3, sistema no sirve

---

## SHOULD HAVE (High Priority)

| Feature | User Story | Effort | Rationale |
|---------|-----------|--------|-----------|
| Email notifications | As a user, I want email alerts | 2 days | Improves UX significantly |
| Basic reporting | As a manager, I want reports | 3 days | High demand from users |
| Search orders | As a user, I want to search | 2 days | Frequently requested |

**Total SHOULD effort**: 7 days (1.5 weeks)
**Note**: Si hay tiempo en MVP, agregar; sino, va en v1.1

---

## COULD HAVE (Nice to Have)

| Feature | User Story | Effort | Why COULD? |
|---------|-----------|--------|------------|
| Advanced filters | As a user, I want complex filters | 3 days | Incremental value |
| Export to PDF | As a user, I want PDF export | 2 days | Workaround: manual export OK |
| Dashboard | As a manager, I want dashboard | 5 days | Reports cubren por ahora |

**Total COULD effort**: 10 days (2 weeks)
**Plan**: Backlog para v1.2

---

## WON'T HAVE (Out of Scope for Now)

| Feature | User Story | Why WON'T? |
|---------|-----------|------------|
| Mobile app | As a user, I want mobile | Responsive web es suficiente para MVP |
| AI recommendations | As a user, I want AI suggestions | Demasiado complejo, no core value |
| Multi-language | As a user, I want multiple languages | Solo necesitan English/Spanish ahora |
| Integration with SystemX | As a admin, I want integration | SystemX no es crítico, puede ser manual |

**Plan**: Evaluar en 6 meses post-launch

---

## MVP SCOPE SUMMARY

**MVP = MUST HAVE**
- Features: 3
- Effort: 10 days (2 weeks)
- Delivery: 3 semanas (con testing + buffer)

**Extended MVP = MUST + SHOULD** (if time allows)
- Features: 6 total
- Effort: 17 days (~3.5 weeks)
- Delivery: 5-6 semanas

**Full Backlog**:
- MUST: 3 (30%)
- SHOULD: 3 (30%)
- COULD: 3 (30%)
- WON'T: 4 (40%)
- Total features considered: 13

---

## DECISION LOG

**Why these MUST?**
- Login: Seguridad básica requerida
- Create Order: Es el core del sistema
- View Status: Usuarios necesitan visibilidad

**Why X is SHOULD not MUST?**
- Email notif: Sistema funciona sin esto, usuarios pueden check manual
- Reporting: Pueden extraer datos manualmente en v1

**Why Y is WON'T?**
- Mobile app: Costo alto, responsive web es suficiente
- AI: Complejidad no justificada para MVP
```

---

## 🎯 WORKED EXAMPLES

### **Example 1: Appointment Scheduling System**

```markdown
## MUST HAVE (MVP Blockers)
1. ✓ Registrar paciente (5 pts)
2. ✓ Agendar cita (8 pts)
3. ✓ Ver calendario disponibilidad (5 pts)
4. ✓ Cancelar cita (3 pts)

Total: 21 story points (~3 weeks)

## SHOULD HAVE
5. ◉ Enviar recordatorio automático (5 pts)
6. ◉ Historial de citas (3 pts)
7. ◉ Búsqueda de paciente (3 pts)

Total: 11 pts (~1.5 weeks)

## COULD HAVE
8. ○ Dashboard de métricas (8 pts)
9. ○ Integración con WhatsApp (5 pts)
10. ○ Notas del médico (5 pts)

## WON'T HAVE
11. ✗ Expediente médico completo (EMR)
12. ✗ Facturación electrónica
13. ✗ Teleconsulta

**MVP Decision**: Solo MUST (3 semanas)
**Rationale**: Cliente necesita rapidez, SHOULD puede ir en v1.1
```

---

### **Example 2: Inventory Management**

```markdown
## MUST (No funciona sin esto)
1. ✓ Registrar producto
2. ✓ Entrada de inventario
3. ✓ Salida de inventario
4. ✓ Consultar stock actual

## SHOULD (Muy importante)
5. ◉ Alertas de stock bajo
6. ◉ Historial de movimientos
7. ◉ Búsqueda avanzada

## COULD (Deseable)
8. ○ Reportes de rotación
9. ○ Códigos de barra
10. ○ Múltiples bodegas

## WON'T (v2.0+)
11. ✗ Integración con ERP
12. ✗ Forecast de demanda (IA)
13. ✗ Optimización de reorden
```

---

## 💡 BEST PRACTICES

### **1. Be Ruthless with MUST**
```
❌ BAD: 15 MUST features
✅ GOOD: 5-8 MUST features

Principle: Si no duele dejarlo fuera, no es MUST
```

### **2. Use Kano Model to Validate**
```
Ask users:
"Si [feature] NO está, ¿qué tan insatisfecho estarías?"
  - Muy insatisfecho → MUST
  - Algo insatisfecho → SHOULD
  - No me importa → COULD/WON'T
```

### **3. Consider Technical Dependencies**
```
Feature X depends on Feature Y
→ Both must be MUST or both SHOULD
→ Can't have X as MUST and Y as COULD
```

### **4. Validate with "So What?" Test**
```
For cada MUST feature:
"So what if we don't include this?"
  - "System is useless" → Valid MUST
  - "Users will be unhappy" → Maybe SHOULD
  - "Would be nice" → Not MUST
```

### **5. Timeboxing Rule**
```
MVP development should be:
- Quick/Experimental: 2-4 weeks
- Standard: 6-10 weeks
- Complex: 10-16 weeks

If MUST features exceed timeline → Re-prioritize
```

---

## 📊 OUTPUT FORMAT

```json
{
  "moscow_prioritization": {
    "project_id": "PROJ-001",
    "prioritized_at": "2025-01-19",
    "must_have": [
      {
        "feature_id": "F001",
        "name": "User Login",
        "user_story": "As a user, I want to login securely",
        "effort_points": 3,
        "rationale": "Security requirement",
        "dependencies": []
      }
    ],
    "should_have": [...],
    "could_have": [...],
    "wont_have": [...],
    "summary": {
      "total_features": 20,
      "must_count": 5,
      "should_count": 6,
      "could_count": 5,
      "wont_count": 4,
      "mvp_effort": "3 weeks",
      "extended_mvp_effort": "5 weeks"
    },
    "mvp_definition": {
      "scope": "MUST only",
      "features": 5,
      "estimated_delivery": "3-4 weeks",
      "validated_by": ["Product Owner", "Tech Lead"]
    }
  }
}
```

---

## ✅ PRIORITIZATION CHECKLIST

- [ ] All features listed
- [ ] Each feature has user story
- [ ] Effort estimated for each
- [ ] MUST < 30% of total features
- [ ] MVP timeline < 12 weeks
- [ ] Dependencies identified
- [ ] Validated with stakeholders
- [ ] Technical feasibility confirmed
- [ ] Budget alignment checked

---

**END OF SKILL: MoSCoW Prioritizer**
