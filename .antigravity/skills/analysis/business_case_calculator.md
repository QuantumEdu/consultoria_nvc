# SKILL: Business Case Calculator

## 📋 METADATA
- **Skill ID**: `SKILL-009`
- **Category**: `Analysis` (CRITICAL)
- **Used By**: Discovery Orchestrator, Solution Architect, Roadmap Agent
- **Version**: `1.0.0`

---

## 🎯 PURPOSE

Calcular el **business case económico** (ROI, payback period, NPV) para justificar inversión en el proyecto, permitiendo decisiones basadas en valor económico real.

**KEY PRINCIPLE**: "Si no puedes medirlo en dinero, es difícil que aprueben el presupuesto."

---

## 💰 ECONOMIC VALUATION FRAMEWORK

### **When to Calculate Business Case**

```
TRIGGER POINTS:

1. AFTER DISCOVERY (Phase 2)
   → Cuantificar el costo del problema actual
   → "Cuánto están perdiendo HOY"

2. AFTER TO-BE DESIGN (Phase 5)
   → Cuantificar el ahorro/ganancia esperado
   → "Cuánto van a ahorrar/ganar"

3. AFTER ARCHITECTURE (Phase 6)
   → Calcular inversión necesaria
   → ROI completo: Inversión vs. Retorno

4. BEFORE GO/NO-GO DECISION
   → Validar que el ROI justifica la inversión
   → Decision gate económico
```

---

## 📊 BUSINESS CASE COMPONENTS

### **1. CURRENT STATE COST (Costo del Problema Actual)**

```yaml
CATEGORIES:

A. Direct Labor Costs (Tiempo perdido)
   Formula: Horas perdidas × Costo por hora × Frecuencia
   
   Example:
   - Recepcionista busca info: 20 min/búsqueda
   - Frecuencia: 10 búsquedas/día × 20 días/mes = 200 búsquedas
   - Tiempo total: 200 × 20 min = 67 hrs/mes
   - Costo: 67 hrs × $10/hr = $670/mes
   - ANUAL: $670 × 12 = $8,040/año

B. Error/Rework Costs (Costo de errores)
   Formula: Errores × Costo por error × Frecuencia
   
   Example:
   - Tasa error facturas: 15%
   - Órdenes/mes: 100
   - Errores/mes: 15
   - Costo corregir: $50/error (tiempo + overhead)
   - TOTAL: 15 × $50 = $750/mes
   - ANUAL: $9,000/año

C. Opportunity Costs (Oportunidades perdidas)
   Formula: Ventas perdidas o ingresos no generados
   
   Example:
   - Retrasos causan cancelaciones: 5%
   - Valor promedio orden: $500
   - Órdenes/mes: 100
   - Pérdida: 5 órdenes × $500 = $2,500/mes
   - ANUAL: $30,000/año

D. Overtime / Extra Capacity Costs
   Formula: Horas extras × Tarifa extra
   
   Example:
   - Contador trabaja 10 hrs extras/semana por proceso manual
   - Costo: 40 hrs/mes × $30/hr (1.5× normal)
   - TOTAL: $1,200/mes
   - ANUAL: $14,400/año

E. Customer Satisfaction Impact (Hard to quantify but important)
   Proxy metrics:
   - Churn rate increase: X% → $Y lost revenue
   - NPS decrease: X points → estimate impact
   - Complaints → time spent + reputation damage

F. Risk Exposure (Compliance, Security)
   Formula: Probability × Potential fine/loss
   
   Example:
   - Riesgo compliance: 10% probability
   - Multa potencial: $50,000
   - Expected cost: $5,000/año
```

**TOTAL CURRENT STATE COST FORMULA**:
```
Annual Cost of Problem = 
  Labor Waste + 
  Error Costs + 
  Opportunity Loss + 
  Overtime + 
  Risk Exposure

Example Total: $66,440/año
```

---

### **2. FUTURE STATE SAVINGS (Ahorro/Ganancia Esperada)**

```yaml
POST-IMPROVEMENT SAVINGS:

A. Time Savings → Cost Savings
   Example:
   - Proceso actual: 2.5 hrs/orden
   - Proceso futuro: 1 hr/orden
   - Ahorro: 1.5 hrs/orden
   - Órdenes/mes: 100
   - Total ahorro: 150 hrs/mes × $15/hr = $2,250/mes
   - ANUAL: $27,000/año

B. Error Reduction → Cost Savings
   Example:
   - Error rate actual: 15%
   - Error rate futuro: 5%
   - Reducción: 10 errores/mes
   - Ahorro: 10 × $50 = $500/mes
   - ANUAL: $6,000/año

C. Opportunity Capture → Revenue Increase
   Example:
   - Cancelaciones actuales: 5%
   - Cancelaciones futuras: 1%
   - Órdenes recuperadas: 4/mes
   - Valor: 4 × $500 = $2,000/mes
   - ANUAL: $24,000/año

D. Capacity Increase (sin contratar)
   Example:
   - Capacidad actual: 100 órdenes/mes
   - Capacidad futura: 150 órdenes/mes (mismo staff)
   - Ingresos adicionales: 50 × $500 × Margen 30%
   - Ganancia: $7,500/mes
   - ANUAL: $90,000/año

E. Risk Mitigation
   Example:
   - Riesgo compliance reduce de 10% a 1%
   - Ahorro expected: $4,500/año
```

**TOTAL ANNUAL BENEFIT FORMULA**:
```
Annual Benefit = 
  Time Savings + 
  Error Reduction + 
  Opportunity Capture + 
  Capacity Increase + 
  Risk Mitigation

Example Total: $151,500/año
```

---

### **3. INVESTMENT REQUIRED (Costo del Proyecto)**

```yaml
ONE-TIME COSTS:

A. Development/Implementation
   - Software development: $X
   - System setup: $X
   - Data migration: $X
   - Training: $X
   Total: $35,000

B. Hardware/Infrastructure (if needed)
   - Servers/cloud setup: $X
   - Licenses (one-time): $X
   Total: $2,000

C. Change Management
   - Training materials: $X
   - Workshops: $X
   Total: $3,000

TOTAL ONE-TIME: $40,000

---

RECURRING COSTS (Annual):

A. Software/Licenses
   - SaaS subscriptions: $X/mes × 12
   - Tool licenses: $X/año
   Total: $3,600/año

B. Maintenance/Support
   - Bug fixes/updates: 20% of dev cost
   - Support hours: $X/año
   Total: $7,000/año

C. Hosting/Infrastructure
   - Cloud hosting: $X/mes × 12
   Total: $2,400/año

TOTAL RECURRING: $13,000/año
```

---

## 📈 ROI CALCULATIONS

### **Key Metrics**

#### **1. Simple ROI**
```
ROI = (Total Benefit - Total Cost) / Total Cost × 100%

Example:
Year 1:
  Benefit: $151,500
  Cost: $40,000 (one-time) + $13,000 (recurring) = $53,000
  ROI = ($151,500 - $53,000) / $53,000 × 100%
  ROI = 186% (Year 1)

Year 2:
  Benefit: $151,500
  Cost: $13,000 (recurring only)
  ROI = ($151,500 - $13,000) / $13,000 × 100%
  ROI = 1,065% (Year 2)
```

#### **2. Payback Period**
```
Payback Period = Total Investment / Annual Net Benefit

Example:
  Investment: $40,000
  Annual Net Benefit: $151,500 - $13,000 = $138,500
  Payback = $40,000 / $138,500 = 0.29 años
  Payback = 3.5 meses ✅ (Excelente)

Thresholds:
  ✅ < 6 meses: Excelente
  ✅ 6-12 meses: Bueno
  ⚠️ 12-24 meses: Aceptable (depende)
  ❌ > 24 meses: Difícil justificar
```

#### **3. NPV (Net Present Value)**
```
NPV = Σ (Benefit_year / (1+r)^year) - Investment

Where:
  r = discount rate (typically 8-12%)
  year = 1, 2, 3, 4, 5

Example (r=10%, 5-year horizon):
  Year 0: -$40,000 (investment)
  Year 1: +$138,500 / 1.10 = +$125,909
  Year 2: +$138,500 / 1.21 = +$114,463
  Year 3: +$138,500 / 1.33 = +$104,135
  Year 4: +$138,500 / 1.46 = +$94,863
  Year 5: +$138,500 / 1.61 = +$86,242

  NPV = -$40,000 + $525,612 = $485,612
  
  ✅ NPV > 0: Proyecto rentable
```

#### **4. IRR (Internal Rate of Return)**
```
IRR = Discount rate where NPV = 0

Example: IRR = 345% (muy alto, proyecto muy rentable)

Interpretation:
  IRR > 30%: Excelente inversión
  IRR 15-30%: Buena inversión
  IRR 8-15%: Aceptable
  IRR < 8%: No recomendable
```

---

## 🎯 BUSINESS CASE TEMPLATE

```markdown
# BUSINESS CASE: [Project Name]

**Prepared by**: [Name]
**Date**: [YYYY-MM-DD]
**Decision Required**: [Go/No-Go for $X investment]

---

## EXECUTIVE SUMMARY

**Problem**: [One sentence problem]
**Solution**: [One sentence solution]
**Investment**: $40,000 (one-time) + $13,000/año (recurring)
**Return**: $138,500/año net benefit
**Payback**: 3.5 meses
**ROI Year 1**: 186%

**Recommendation**: ✅ PROCEED - Strong business case

---

## 1. CURRENT STATE COST (What We're Losing Today)

### Time Waste
| Activity | Time Lost | Cost/Hr | Frequency | Annual Cost |
|----------|-----------|---------|-----------|-------------|
| Manual data entry | 20 hrs/week | $15 | 50 weeks | $15,000 |
| Searching for info | 10 hrs/week | $15 | 50 weeks | $7,500 |
| Rework/corrections | 8 hrs/week | $20 | 50 weeks | $8,000 |
| **Subtotal** | | | | **$30,500** |

### Error Costs
- Error rate: 15% of 1,200 orders/year
- Errors: 180/year
- Cost per error: $50 (correction time + customer service)
- **Total**: $9,000/year

### Opportunity Loss
- Delayed orders lead to 5% cancellation
- Lost orders: 60/year × $500 = $30,000/year
- **Total**: $30,000/year

### Overtime
- 10 hrs/week extra time @ $30/hr
- **Total**: $15,000/year

### Risk Exposure
- Compliance risk: 10% × $50K fine
- **Expected cost**: $5,000/year

**TOTAL CURRENT STATE COST: $89,500/year**

---

## 2. FUTURE STATE BENEFIT (What We'll Save/Gain)

### Time Savings
- Automation saves 30 hrs/week
- Cost savings: 30 × $15 × 50 = $22,500/year

### Error Reduction
- Error rate drops to 5% (10% improvement)
- Savings: 120 errors × $50 = $6,000/year

### Opportunity Recovery
- Cancellation rate drops to 1%
- Recovered orders: 48/year × $500 = $24,000/year

### Capacity Increase
- Handle 50% more volume (same staff)
- Additional margin: 600 orders × $500 × 30% = $90,000/year

### Risk Mitigation
- Compliance risk drops to 1%
- Savings: $4,500/year

**TOTAL ANNUAL BENEFIT: $147,000/year**

---

## 3. INVESTMENT REQUIRED

### One-Time Costs
| Item | Cost |
|------|------|
| Software development | $28,000 |
| System setup | $2,000 |
| Training | $3,000 |
| Data migration | $4,000 |
| Contingency (15%) | $5,550 |
| **Total One-Time** | **$42,550** |

### Recurring Annual Costs
| Item | Cost |
|------|------|
| Software licenses | $3,600 |
| Hosting | $2,400 |
| Maintenance (20% dev) | $5,600 |
| Support | $2,000 |
| **Total Recurring** | **$13,600/year** |

---

## 4. FINANCIAL ANALYSIS

### ROI Calculation
```
Year 1:
  Benefit: $147,000
  Cost: $42,550 + $13,600 = $56,150
  Net: $90,850
  ROI: 162%

Year 2:
  Benefit: $147,000
  Cost: $13,600
  Net: $133,400
  ROI: 981%

3-Year Cumulative:
  Benefit: $441,000
  Cost: $83,350
  Net: $357,650
  ROI: 429%
```

### Payback Period
```
Payback = $42,550 / ($147,000 - $13,600)
Payback = 3.8 months ✅
```

### NPV (10% discount, 5 years)
```
NPV = $485,612 ✅
IRR = 345% ✅
```

---

## 5. RISK ANALYSIS

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Adoption resistance | Medium | High | Strong change management plan |
| Technical complexity | Low | Medium | Phased implementation |
| Budget overrun | Medium | Medium | 15% contingency + fixed scope |
| Timeline delay | Medium | Low | Agile approach with MVP |

**Overall Risk**: MEDIUM (Manageable)

---

## 6. ALTERNATIVES CONSIDERED

### Option 1: Do Nothing
- Cost: $0
- Benefit: $0
- **Problem persists, losing $89,500/year**

### Option 2: Hire More Staff
- Cost: $50,000/year (one FTE)
- Benefit: Partial relief (~$30,000 savings)
- **Net: -$20,000/year (negative ROI)**

### Option 3: Implement System (RECOMMENDED)
- Cost: $42,550 + $13,600/year
- Benefit: $147,000/year
- **Net: +$90,850 Year 1 ✅**

---

## 7. DECISION CRITERIA

| Criterion | Threshold | Actual | Status |
|-----------|-----------|--------|--------|
| ROI Year 1 | > 50% | 162% | ✅ Pass |
| Payback Period | < 12 months | 3.8 months | ✅ Pass |
| NPV (5 year) | > $0 | $485,612 | ✅ Pass |
| Risk Level | Low-Medium | Medium | ✅ Pass |
| Budget Available | > Investment | $50,000 | ✅ Pass |

**DECISION: ✅ GO - All criteria met**

---

## 8. IMPLEMENTATION PHASING (Risk Mitigation)

### Phase 1: Quick Wins (Weeks 1-4)
- Investment: $5,000
- Benefit: $15,000/year
- Payback: 4 months
- **Builds confidence before larger investment**

### Phase 2: Core System (Weeks 5-12)
- Investment: $25,000
- Benefit: $80,000/year
- **Main value delivery**

### Phase 3: Advanced Features (Weeks 13-16)
- Investment: $12,550
- Benefit: $52,000/year
- **Full benefit realization**

**Risk Mitigation**: Can stop after Phase 1 if business case doesn't materialize

---

## 9. SUCCESS METRICS

| Metric | Baseline | Target (6 mo) | Target (12 mo) |
|--------|----------|---------------|----------------|
| Time per order | 2.5 hrs | 1.5 hrs | 1 hr |
| Error rate | 15% | 8% | 5% |
| Orders/month | 100 | 120 | 150 |
| Customer satisfaction | 70% | 80% | 85% |
| Staff overtime hrs | 40/month | 20/month | 10/month |

---

## 10. RECOMMENDATION

**✅ APPROVE PROJECT**

**Rationale**:
1. Strong ROI (162% Year 1, 981% Year 2)
2. Fast payback (3.8 months)
3. High NPV ($485K over 5 years)
4. Manageable risk with mitigation plan
5. Aligns with strategic goals
6. Competitive necessity

**Next Steps**:
1. Secure budget approval: $42,550
2. Assign project sponsor
3. Begin Phase 1 (Quick Wins)
4. Monitor metrics monthly

**Approval Required From**:
- [ ] CFO (budget)
- [ ] Operations Director (process owner)
- [ ] IT Director (technical feasibility)
```

---

## 📊 SENSITIVITY ANALYSIS

```markdown
## What if our assumptions are wrong?

### Scenario 1: Conservative (70% of expected benefit)
- Annual Benefit: $102,900 (vs. $147,000)
- Year 1 Net: $46,750
- Payback: 5.4 months
- ROI: 83%
- **Decision: Still GOOD**

### Scenario 2: Optimistic (130% of expected benefit)
- Annual Benefit: $191,100
- Year 1 Net: $134,950
- Payback: 2.9 months
- ROI: 240%
- **Decision: Excellent**

### Scenario 3: Cost Overrun (+30%)
- Investment: $55,315
- Payback: 5.0 months
- ROI: 125%
- **Decision: Still acceptable**

### Break-Even Analysis
**Minimum benefit needed**: $56,150 (Year 1 cost)
**Buffer**: Actual benefit is 262% of break-even
**Conclusion**: Large margin of safety ✅
```

---

## 💡 USAGE IN AGENT WORKFLOW

### **Discovery Phase (Agent 02)**
```
Output: Current State Cost
- Quantify pain points in $$
- "You're losing $89,500/year"
- Creates urgency
```

### **TO-BE Phase (Agent 06)**
```
Output: Expected Savings
- Quantify improvements in $$
- "You'll save $147,000/year"
- Validates solution value
```

### **Architecture Phase (Agent 07)**
```
Input: Investment needed
- Calculate project cost
- "Investment: $42,550"
```

### **Roadmap Phase (Agent 08)**
```
Output: Complete Business Case
- ROI, Payback, NPV
- Go/No-Go recommendation
- Decision support for approval
```

---

## 📤 OUTPUT FORMAT

```json
{
  "business_case": {
    "engagement_id": "ENG-001",
    "prepared_at": "2025-01-19",
    "current_state_cost": {
      "time_waste": 30500,
      "error_costs": 9000,
      "opportunity_loss": 30000,
      "overtime": 15000,
      "risk_exposure": 5000,
      "total_annual": 89500
    },
    "future_state_benefit": {
      "time_savings": 22500,
      "error_reduction": 6000,
      "opportunity_recovery": 24000,
      "capacity_increase": 90000,
      "risk_mitigation": 4500,
      "total_annual": 147000
    },
    "investment": {
      "one_time": 42550,
      "recurring_annual": 13600
    },
    "financial_metrics": {
      "roi_year1": "162%",
      "payback_months": 3.8,
      "npv_5year": 485612,
      "irr": "345%"
    },
    "recommendation": "GO",
    "confidence": "high"
  }
}
```

---

## ✅ VALIDATION CHECKLIST

- [ ] Current costs quantified with evidence
- [ ] Benefits are realistic (not wishful thinking)
- [ ] All investment costs included (no hidden costs)
- [ ] Payback period < 18 months
- [ ] ROI > 50% year 1
- [ ] NPV > 0
- [ ] Sensitivity analysis done
- [ ] Risk mitigation addressed
- [ ] Stakeholders agree with numbers

---

**END OF SKILL: Business Case Calculator**
