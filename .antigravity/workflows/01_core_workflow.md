# WORKFLOW: CORE (Universal Pipeline)

## 📋 METADATA
- **Workflow ID**: `WF-CORE-001`
- **Type**: `Universal`
- **Applies To**: All engagements
- **Version**: `1.0.0`

---

## 🎯 PURPOSE

Pipeline universal que aplica a TODOS los engagements, independiente del dominio. Define las fases obligatorias desde intake hasta roadmap de implementación.

**Key Principle**: "Problem first, solution later. Always."

---

## 🔄 WORKFLOW PHASES

```
┌────────────────────────────────────────────────────────────┐
│                    CORE WORKFLOW                           │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  Phase 0: INTAKE                                           │
│  ├─ Understand context                                     │
│  ├─ Classify domain                                        │
│  └─ Capture constraints                                    │
│     │                                                       │
│     ↓ Quality Gate: Problem clarity checkpoint            │
│     │                                                       │
│  Phase 1: DISCOVERY                                        │
│  ├─ Deep dive into problem                                 │
│  ├─ Root cause analysis                                    │
│  ├─ Stakeholder interviews                                 │
│  └─ Economic quantification (Current state cost)          │
│     │                                                       │
│     ↓ Quality Gate: Real problem validated                │
│     │                                                       │
│  Phase 2: DEPTH ASSESSMENT                                 │
│  ├─ Complexity scoring                                     │
│  ├─ Maturity assessment                                    │
│  ├─ Track recommendation (Quick/Standard/Deep)            │
│  └─ GO/NO-GO decision                                      │
│     │                                                       │
│     ↓ Quality Gate: Engagement profiling complete         │
│     │                                                       │
│  Phase 3: METHODOLOGY SELECTION                            │
│  ├─ Select frameworks by phase                             │
│  ├─ Create methodology playbook                            │
│  └─ Training plan (if needed)                             │
│     │                                                       │
│     ↓ Quality Gate: Approach validated                    │
│     │                                                       │
│  Phase 4: AS-IS MODELING (skip if greenfield)             │
│  ├─ Map current process (BPMN)                            │
│  ├─ Identify bottlenecks                                   │
│  ├─ Analyze waste (Lean)                                   │
│  └─ Quantify current metrics                              │
│     │                                                       │
│     ↓ Quality Gate: Current state documented              │
│     │                                                       │
│  Phase 5: TO-BE DESIGN                                     │
│  ├─ Redesign process (Lean principles)                    │
│  ├─ Eliminate waste                                        │
│  ├─ Define target metrics                                  │
│  ├─ Economic quantification (Expected benefits)           │
│  └─ User validation                                        │
│     │                                                       │
│     ↓ Quality Gate: Improved process validated            │
│     │                                                       │
│  Phase 6: MVP & ARCHITECTURE (skip if non-technical)      │
│  ├─ Define MVP scope (MoSCoW)                             │
│  ├─ Design architecture                                    │
│  ├─ Select technology stack                                │
│  ├─ Economic quantification (Investment cost)             │
│  └─ Build vs Buy analysis                                 │
│     │                                                       │
│     ↓ Quality Gate: Solution designed                     │
│     │                                                       │
│  Phase 7: IMPLEMENTATION ROADMAP                           │
│  ├─ Define phases & sprints                                │
│  ├─ Resource planning                                      │
│  ├─ Change management plan                                 │
│  ├─ Risk mitigation                                        │
│  ├─ COMPLETE BUSINESS CASE (ROI, Payback, NPV)           │
│  └─ Success metrics                                        │
│     │                                                       │
│     ↓ Quality Gate: Implementation plan approved          │
│     │                                                       │
│  ✅ READY FOR EXECUTION                                    │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## 📊 PHASE DETAILS

### **PHASE 0: INTAKE** (1-2 días)

**Agent**: Intake & Domain Classifier (AGT-001)

**Inputs**:
- Client initial contact
- Problem description (high-level)

**Activities**:
1. Capture organization context
2. Understand trigger event
3. Classify domain (process, conflict, risk, etc)
4. Identify stakeholders
5. Capture constraints (budget, timeline)
6. Assess urgency

**Outputs**:
- `engagement_profile.json` (initial)
- Domain classification
- Stakeholder map (preliminary)

**Quality Gate**: ✅ Can articulate problem clearly?

**Duration**: 1-2 days
**Effort**: 4-8 hours

---

### **PHASE 1: DISCOVERY** (1-2 semanas)

**Agent**: Discovery Orchestrator (AGT-002)

**Inputs**:
- `engagement_profile.json`
- Stakeholder list

**Activities**:
1. Plan discovery (who to interview)
2. Conduct stakeholder interviews (3+ profiles)
3. Process observation (Gemba walks)
4. Root cause analysis (5 Whys, Fishbone)
5. Evidence collection (quantify impact)
6. **Economic quantification (CRITICAL)**:
   - Time waste → $X/year
   - Error costs → $X/year
   - Opportunity loss → $X/year
   - Total current state cost
7. Problem statement formulation
8. Validation workshop

**Tools**:
- Smart Questionnaire Generator
- 5 Whys Engine
- Pain Point Canvas
- Business Case Calculator (current state)

**Outputs**:
- `problem_statement.json` (validated)
- Economic impact quantified
- Root causes identified
- Evidence documented

**Quality Gate**: 
- ✅ Problem validated by 3+ stakeholders?
- ✅ Current state cost quantified?
- ✅ Root causes identified?

**Duration**: 1-2 weeks (depends on stakeholder availability)
**Effort**: 20-40 hours

---

### **PHASE 2: DEPTH ASSESSMENT** (2-3 días)

**Agent**: Depth & Maturity Assessor (AGT-003)

**Inputs**:
- `problem_statement.json`
- `engagement_profile.json`

**Activities**:
1. Assess complexity (4 dimensions)
2. Assess maturity (4 dimensions)
3. Recommend track (Quick/Standard/Deep Dive)
4. Identify risks
5. Validate capacity (Can they execute?)
6. **Economic validation**: Budget vs. Problem cost
7. GO/NO-GO recommendation

**Outputs**:
- `engagement_profile.json` (updated with assessment)
- Track recommendation
- Risk register (initial)
- Capacity validation

**Quality Gate**:
- ✅ Complexity & maturity scored?
- ✅ Track selected?
- ✅ GO decision?

**Duration**: 2-3 days
**Effort**: 8-16 hours

---

### **PHASE 3: METHODOLOGY SELECTION** (1-2 días)

**Agent**: Methodology Advisor (AGT-004)

**Inputs**:
- `engagement_profile.json`
- `problem_statement.json`
- Track selected

**Activities**:
1. Analyze context (domain, complexity, maturity)
2. Select frameworks by phase:
   - Discovery: Design Thinking, 5 Whys, etc
   - AS-IS: BPMN, VSM, etc
   - TO-BE: Lean, Six Sigma, etc
   - MVP: MoSCoW, Kano, etc
   - Architecture: TOGAF, etc
   - Implementation: Agile, Kotter, etc
3. Design methodology integration
4. Tailor to client context
5. Generate playbook
6. Training plan (if needed)

**Outputs**:
- Methodology Playbook (customized)
- Tool recommendations
- Training plan

**Quality Gate**:
- ✅ Frameworks selected for each phase?
- ✅ Client understands approach?

**Duration**: 1-2 days
**Effort**: 8-12 hours

---

### **PHASE 4: AS-IS MODELING** (1-3 semanas)

**Agent**: Process Intelligence (AGT-005)

**Skip if**: Greenfield (no existing process)

**Inputs**:
- `problem_statement.json`
- Methodology playbook

**Activities**:
1. Define scope (boundaries)
2. Process discovery (observation + interviews)
3. Create BPMN diagram
4. Collect metrics (cycle time, error rate, etc)
5. Bottleneck analysis
6. Waste identification (Lean 8 Mudas)
7. Pain point mapping
8. Opportunity identification

**Tools**:
- BPMN Assistant
- Bottleneck Detector
- Waste Analyzer

**Outputs**:
- `as_is_process.json`
- BPMN diagram
- Metrics baseline
- Bottleneck analysis
- Waste categorized

**Quality Gate**:
- ✅ Process validated by users ("así lo hacemos")?
- ✅ Bottlenecks quantified?
- ✅ Metrics captured?

**Duration**: 1-3 weeks (depends on complexity)
**Effort**: 20-60 hours

---

### **PHASE 5: TO-BE DESIGN** (1-3 semanas)

**Agent**: Redesign & Optimization (AGT-006)

**Inputs**:
- `as_is_process.json` (or problem statement if greenfield)
- Methodology playbook

**Activities**:
1. Apply Lean principles:
   - ELIMINATE waste
   - SIMPLIFY complexity
   - STANDARDIZE what works
   - AUTOMATE last
2. Design TO-BE process
3. Define target metrics
4. **Economic quantification (CRITICAL)**:
   - Time savings → $X/year
   - Error reduction → $X/year
   - Capacity increase → $X/year
   - Total expected benefits
5. Impact analysis
6. User validation workshop
7. Approval

**Tools**:
- Waste Analyzer
- Business Case Calculator (future benefits)

**Outputs**:
- `to_be_process.json`
- TO-BE diagram
- Target metrics
- Expected benefits quantified
- Change impact assessment

**Quality Gate**:
- ✅ TO-BE is SIMPLER than AS-IS?
- ✅ Expected benefits quantified?
- ✅ Users validated "esto funcionaría"?

**Duration**: 1-3 weeks
**Effort**: 20-60 hours

---

### **PHASE 6: MVP & ARCHITECTURE** (1-2 semanas)

**Agent**: Solution Architect (AGT-007)

**Skip if**: Non-technical solution (process only)

**Inputs**:
- `to_be_process.json`
- `engagement_profile.json`

**Activities**:
1. Extract requirements from TO-BE
2. Prioritize features (MoSCoW)
3. Define MVP scope (20-30% of features)
4. Decide solution type:
   - Low-code/No-code
   - SaaS/Off-the-shelf
   - Custom development
   - Hybrid
5. Design architecture
6. Select technology stack
7. **Economic quantification (CRITICAL)**:
   - Development cost
   - Infrastructure cost
   - Recurring costs
   - Total investment
8. Build vs Buy analysis
9. Cost estimation

**Tools**:
- MoSCoW Prioritizer
- Business Case Calculator (investment)

**Outputs**:
- `solution_architecture.json`
- MVP scope defined
- Architecture diagram
- Technology stack
- Cost estimate

**Quality Gate**:
- ✅ MVP is truly "minimum" (< 30% features)?
- ✅ Architecture aligned to capability?
- ✅ Investment cost quantified?

**Duration**: 1-2 weeks
**Effort**: 16-40 hours

---

### **PHASE 7: IMPLEMENTATION ROADMAP** (1 semana)

**Agent**: Implementation Roadmap (AGT-008)

**Inputs**:
- `solution_architecture.json`
- `to_be_process.json`
- All previous artifacts

**Activities**:
1. Define phases (Foundation, MVP, Pilot, Launch, etc)
2. Sprint planning (for Agile components)
3. Dependencies & critical path
4. Resource planning (RACI matrix)
5. Change management plan (ADKAR)
6. Risk mitigation
7. **COMPLETE BUSINESS CASE (CRITICAL)**:
   - Current state cost (from Discovery)
   - Expected benefits (from TO-BE)
   - Investment (from Architecture)
   - ROI, Payback, NPV, IRR
   - Sensitivity analysis
   - Decision recommendation
8. Success metrics & monitoring
9. Budget & timeline finalization

**Tools**:
- Business Case Calculator (complete)
- Risk Matrix
- Roadmap Generator

**Outputs**:
- `implementation_roadmap.json`
- Complete business case
- Phase plan with timeline
- Resource allocation
- Risk register
- Change management plan
- Success metrics

**Quality Gate**:
- ✅ Business case is solid (ROI > 50%, Payback < 18 mo)?
- ✅ All risks have mitigations?
- ✅ Change management plan complete?
- ✅ Approval obtained?

**Duration**: 1 week
**Effort**: 20-30 hours

---

## 💰 ECONOMIC DECISION GATES

### **Gate 1: After Discovery**
```
Question: ¿El problema justifica inversión?

Check:
- Current state cost > $20K/year
- Problem is real (validated by 3+ sources)
- Pain is significant

If PASS → Continue to Depth Assessment
If FAIL → Replantear o decline
```

### **Gate 2: After Depth Assessment**
```
Question: ¿Cliente tiene capacidad para ejecutar?

Check:
- Maturity score > 2.0
- Budget available ≥ Expected cost
- Sponsor committed

If PASS → Continue to Methodology
If CONDITIONAL → Risk mitigation plan
If FAIL → Decline or adjust scope
```

### **Gate 3: After TO-BE**
```
Question: ¿La mejora esperada justifica continuar?

Check:
- Expected benefits > 2× Problem cost
- TO-BE is simpler than AS-IS
- Users validated feasibility

If PASS → Continue to Architecture
If FAIL → Replantear TO-BE
```

### **Gate 4: After Architecture**
```
Question: ¿El costo de solución es razonable?

Check:
- Investment < 1× Annual benefit
- Payback < 18 months (estimated)
- Technical feasibility confirmed

If PASS → Continue to Roadmap
If FAIL → Adjust architecture or scope
```

### **Gate 5: Final GO/NO-GO**
```
Question: ¿Aprobamos el proyecto?

Check:
- ✅ ROI Year 1 > 50%
- ✅ Payback < 18 months
- ✅ NPV > 0
- ✅ Risk = Acceptable
- ✅ Budget approved
- ✅ Stakeholders committed

If 5-6 checks PASS → ✅ GO
If 3-4 checks PASS → ⚠️ CONDITIONAL GO
If < 3 checks PASS → ❌ NO-GO
```

---

## 🎯 TRACK ADAPTATIONS

### **QUICK TRACK** (< 1 mes, $2K-$8K)

**Skip/Simplify**:
- AS-IS: Light documentation, no formal BPMN
- Architecture: Low-code solution, minimal design
- Roadmap: Simple plan, 1-2 phases

**Focus**:
- Discovery: Essential
- TO-BE: Quick wins only
- Business case: Simplified (Payback focus)

**Duration**: 2-4 weeks
**Deliverables**: Problem statement + Quick solution plan

---

### **STANDARD TRACK** (1-2 meses, $15K-$50K)

**Full Process**: All phases executed

**Adjustments**:
- AS-IS: Standard BPMN
- Architecture: Balanced design
- Roadmap: 3-4 phases

**Duration**: 6-10 weeks
**Deliverables**: Complete documentation + Implementation plan

---

### **DEEP DIVE TRACK** (2-4+ meses, $50K-$250K+)

**Full Process + Enhanced**:
- AS-IS: Multiple sub-processes, detailed VSM
- TO-BE: Advanced optimization, Six Sigma
- Architecture: Enterprise-grade
- Roadmap: Multi-phase with governance

**Additional**:
- Formal stakeholder engagement
- Executive workshops
- Detailed training program

**Duration**: 12-20+ weeks
**Deliverables**: Comprehensive transformation plan

---

## 📊 TYPICAL TIMELINES

| Track | Discovery | AS-IS | TO-BE | Arch | Roadmap | Total |
|-------|-----------|-------|-------|------|---------|-------|
| **Quick** | 3 days | Skip | 5 days | 2 days | 2 days | 2-3 weeks |
| **Standard** | 2 weeks | 2 weeks | 2 weeks | 1.5 weeks | 1 week | 8-10 weeks |
| **Deep Dive** | 3 weeks | 4 weeks | 4 weeks | 3 weeks | 2 weeks | 16-20 weeks |

---

## ✅ COMPLETION CRITERIA

**Engagement is complete when**:
- [ ] All phases executed (or skipped with rationale)
- [ ] All quality gates passed
- [ ] Business case approved
- [ ] Implementation roadmap signed off
- [ ] Client has all deliverables
- [ ] Knowledge transfer complete
- [ ] Next steps clear

**Deliverables Package**:
1. Problem statement (validated)
2. AS-IS process (if applicable)
3. TO-BE process (validated)
4. Solution architecture (if technical)
5. Complete business case (ROI, Payback, NPV)
6. Implementation roadmap
7. Methodology playbook
8. Risk register
9. Change management plan
10. Success metrics dashboard

---

## 🔄 ITERATION & FEEDBACK

**Continuous Improvement**:
- After each phase, review with client
- Adjust subsequent phases based on learnings
- If assumptions change, revisit business case
- Monthly retrospectives

**Red Flags that Trigger Iteration**:
- ⚠️ Problem statement changes significantly
- ⚠️ Budget constraints emerge
- ⚠️ Key stakeholder leaves
- ⚠️ Technology constraints discovered
- ⚠️ Business case weakens

---

## 📈 SUCCESS METRICS

**Engagement Success**:
- Problem validated: > 90% of engagements
- GO decision confidence: > 85% high confidence
- Business case solid: > 80% meet all criteria
- Client satisfaction: > 90% would recommend

**Implementation Success** (if tracked):
- On-time delivery: > 75%
- On-budget: > 80%
- Benefits realized: > 70% of projected
- User adoption: > 85%

---

**END OF CORE WORKFLOW**
