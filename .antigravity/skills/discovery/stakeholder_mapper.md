# SKILL: Stakeholder Mapper

## 📋 METADATA
- **Skill ID**: `SKILL-003`
- **Category**: `Discovery`
- **Used By**: Intake Agent, Discovery Orchestrator, Roadmap Agent
- **Version**: `1.0.0`

---

## 🎯 PURPOSE
Identificar, clasificar y mapear stakeholders según su poder, interés, e impacto en el proyecto.

---

## 📥 INPUT
```json
{
  "engagement_id": "string",
  "stakeholders": [
    {
      "name": "string",
      "role": "string",
      "department": "string (optional)"
    }
  ]
}
```

---

## 📤 OUTPUT
```json
{
  "stakeholder_map": [
    {
      "name": "string",
      "role": "string",
      "power": "high|medium|low",
      "interest": "high|medium|low",
      "impact": "high|medium|low",
      "category": "key_player|keep_satisfied|keep_informed|minimal_effort",
      "engagement_strategy": "string"
    }
  ],
  "power_interest_matrix": "visualization_url"
}
```

---

## 🗺️ POWER/INTEREST MATRIX

```
High Interest
    │
    │  MANAGE CLOSELY        │  KEEP SATISFIED
    │  (High Power,          │  (High Power,
    │   High Interest)       │   Low Interest)
    │  - Key decision makers │  - Executives
────┼──────────────────────┼───────────────────→ High Power
    │  KEEP INFORMED        │  MONITOR
    │  (Low Power,          │  (Low Power,
    │   High Interest)      │   Low Interest)
    │  - End users          │  - Peripheral roles
    │
Low Interest
```

---

## 📊 STAKEHOLDER CATEGORIES

### **1. KEY PLAYERS** (High Power, High Interest)
**Characteristics**: Decision makers who care about the project
**Examples**: Project Sponsor, Department Head affected
**Engagement Strategy**:
- Involve in all major decisions
- Weekly/bi-weekly updates
- Get their buy-in early
- Address concerns immediately

---

### **2. KEEP SATISFIED** (High Power, Low Interest)
**Characteristics**: Have authority but not directly involved
**Examples**: C-level not directly affected, Budget approver
**Engagement Strategy**:
- Monthly high-level updates
- Focus on business outcomes
- Don't overwhelm with details
- Escalate only critical issues

---

### **3. KEEP INFORMED** (Low Power, High Interest)
**Characteristics**: Affected by project but no decision authority
**Examples**: End users, Operational staff
**Engagement Strategy**:
- Regular communication
- Involve in design/testing
- Training and support
- Create champions from this group

---

### **4. MONITOR** (Low Power, Low Interest)
**Characteristics**: Minimally affected or involved
**Examples**: Adjacent departments, Support roles
**Engagement Strategy**:
- Occasional updates
- FYI communications
- No active management needed

---

## 🎯 ASSESSMENT CRITERIA

### **Power Assessment** (1-10 scale)
```
10 = CEO, Final decision maker
8-9 = C-level, Budget owner
6-7 = Director, Department head
4-5 = Manager, Process owner
2-3 = Team lead, Influencer
1 = Individual contributor

Conversion:
9-10 = High
5-8 = Medium
1-4 = Low
```

### **Interest Assessment** (1-10 scale)
```
10 = Will lose job if fails / Primary beneficiary
8-9 = Directly affected daily
6-7 = Indirectly affected
4-5 = Aware but not impacted
2-3 = Peripheral awareness
1 = Unaware

Conversion:
8-10 = High
4-7 = Medium
1-3 = Low
```

### **Impact Assessment** (Separate dimension)
```
How much will change affect them:
High = Major change to daily work
Medium = Moderate change
Low = Minimal change
```

---

## 🎭 STAKEHOLDER ROLES

### **Common Roles**

| Role | Typical Power | Typical Interest | Priority |
|------|---------------|------------------|----------|
| **Executive Sponsor** | High | High | Critical |
| **Project Champion** | Medium | High | Critical |
| **Budget Owner** | High | Medium | Critical |
| **Process Owner** | Medium | High | High |
| **End Users** | Low | High | High |
| **IT Lead** | Medium | Medium | High |
| **Department Head** | High | Medium | Medium |
| **Support Staff** | Low | Medium | Medium |
| **Adjacent Teams** | Low | Low | Low |

---

## 📋 STAKEHOLDER ANALYSIS TEMPLATE

```markdown
# STAKEHOLDER ANALYSIS

## STAKEHOLDER: [Name]

**Role**: [Title/Position]
**Department**: [Department]
**Contact**: [Email/Phone]

### ASSESSMENT
- **Power**: [High/Medium/Low] - [Rationale]
- **Interest**: [High/Medium/Low] - [Rationale]
- **Impact**: [High/Medium/Low] - [How affected]

**Category**: [Key Player / Keep Satisfied / Keep Informed / Monitor]

### ENGAGEMENT STRATEGY
**Frequency**: [Daily/Weekly/Monthly/As needed]
**Channel**: [Meeting/Email/Slack/etc]
**Content**: [What to communicate]
**Concerns**: [Known concerns or objections]

### INFLUENCE
**Can influence**: [Who they can influence]
**Influenced by**: [Who influences them]
**Attitude**: [Supporter/Neutral/Resistor]

### ACTIONS
- [ ] Initial meeting scheduled
- [ ] Role clarified (RACI)
- [ ] Communication plan defined
- [ ] Concerns addressed
```

---

## 🎯 WORKED EXAMPLE

### **Clínica Appointment System**

```yaml
Stakeholder 1:
  name: "Dr. Rodriguez (Director)"
  role: "Executive Sponsor"
  power: High (10/10) - Final decision, budget owner
  interest: High (9/10) - System affects clinic efficiency
  impact: Medium - Uses system occasionally
  category: KEY PLAYER - Manage Closely
  strategy:
    - Weekly 15-min check-ins
    - Involved in major decisions
    - Monthly ROI reports
  concerns: "Cost, disruption to operations"
  attitude: Supporter

Stakeholder 2:
  name: "María (Recepcionista)"
  role: "Primary End User"
  power: Low (3/10) - No decision authority
  interest: High (10/10) - Uses system all day
  impact: High - Entire workflow changes
  category: KEEP INFORMED
  strategy:
    - Involve in design workshops
    - Extensive training
    - Daily support during rollout
    - Make her a champion
  concerns: "Learning new system, job security"
  attitude: Initially resistant, can become champion

Stakeholder 3:
  name: "Jorge (Contador)"
  role: "Finance/Billing user"
  power: Medium (6/10) - Controls billing process
  interest: Medium (6/10) - Needs billing data
  impact: Medium - Partial workflow change
  category: KEEP INFORMED
  strategy:
    - Include in integration design
    - Training on financial reports
    - Weekly updates
  concerns: "Data accuracy, integration with accounting"
  attitude: Neutral

Stakeholder 4:
  name: "IT Support (External)"
  role: "Technical Support"
  power: Low (2/10) - No decision power
  interest: Low (3/10) - Just another system
  impact: Low - Minimal involvement
  category: MONITOR
  strategy:
    - FYI communications
    - Provide technical docs
  concerns: None
  attitude: Neutral
```

---

## 🔗 RACI INTEGRATION

Stakeholder Mapping feeds into RACI Matrix:

| Activity | Dr. Rodriguez | María | Jorge | IT |
|----------|---------------|-------|-------|-----|
| Requirements | A | C | C | I |
| Design | A | R | C | I |
| Testing | I | R | C | I |
| Training | C | R | C | I |
| Go-Live Decision | R/A | I | I | I |

```
R = Responsible (does the work)
A = Accountable (final say)
C = Consulted (input needed)
I = Informed (kept updated)
```

---

## 💡 BEST PRACTICES

### **1. Update Regularly**
```
Stakeholder dynamics change:
- Power shifts (promotions, departures)
- Interest changes (priorities shift)
- New stakeholders emerge

Review stakeholder map:
- At project start
- Monthly during project
- When major changes occur
```

### **2. Identify Champions Early**
```
Look for:
- High interest stakeholders
- Respected by peers
- Good communicators
- Early adopters

Invest in them:
- Early access to system
- Involve in design
- Empower to influence others
```

### **3. Address Resistors Proactively**
```
Don't ignore resistance:
- Understand their concerns
- Involve them early
- Find WIIFM (What's In It For Me)
- Convert or neutralize
```

### **4. Don't Over-Engage Low Priority**
```
Spending too much time on:
- Low power, low interest stakeholders
- Takes time from key players

Be efficient:
- FYI emails
- Self-service info
- Group updates
```

---

## 🚨 RED FLAGS

```
⚠️ WARNING SIGNS:

1. No Executive Sponsor identified
   → Project likely to fail

2. Key users not engaged
   → Adoption risk

3. Budget owner is "Low Interest"
   → Funding risk

4. IT not involved (but tech project)
   → Implementation risk

5. All stakeholders in same quadrant
   → Assessment likely incorrect
```

---

## 📊 OUTPUT FORMAT

```json
{
  "stakeholder_analysis": {
    "engagement_id": "ENG-20250119-001",
    "analyzed_at": "2025-01-19",
    "stakeholders": [
      {
        "id": "STK-001",
        "name": "Dr. Rodriguez",
        "role": "Director / Executive Sponsor",
        "department": "Management",
        "power": {
          "score": 10,
          "level": "high",
          "rationale": "Final decision maker, budget owner"
        },
        "interest": {
          "score": 9,
          "level": "high",
          "rationale": "Directly responsible for clinic efficiency"
        },
        "impact": {
          "score": 6,
          "level": "medium",
          "rationale": "Uses system occasionally"
        },
        "category": "key_player",
        "engagement_strategy": {
          "frequency": "weekly",
          "channel": "meeting",
          "content": "Progress, decisions, ROI metrics",
          "priority": "critical"
        },
        "concerns": ["Cost", "Operational disruption"],
        "attitude": "supporter"
      }
    ],
    "summary": {
      "total_stakeholders": 8,
      "key_players": 2,
      "keep_satisfied": 1,
      "keep_informed": 4,
      "monitor": 1,
      "supporters": 3,
      "neutral": 4,
      "resistors": 1
    }
  }
}
```

---

**END OF SKILL: Stakeholder Mapper**
