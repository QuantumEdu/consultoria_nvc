# SKILL: Bottleneck Detector

## 📋 METADATA
- **Skill ID**: `SKILL-006`
- **Category**: `Process Modeling`
- **Used By**: Process Intelligence Agent
- **Version**: `1.0.0`

---

## 🎯 PURPOSE
Identificar cuellos de botella en procesos mediante análisis de tiempos, capacidad y acumulación de trabajo (WIP).

---

## 📊 BOTTLENECK INDICATORS

### **Primary Signals**
```
1. HIGH WAIT TIME
   → Work queues up before this step
   → Example: "Approval takes 2 days"

2. HIGH WIP (Work In Progress)
   → Many items stuck at this stage
   → Example: "50 orders waiting for review"

3. UTILIZATION > 90%
   → Resource is saturated
   → Example: "One person handling all requests"

4. SLOW THROUGHPUT
   → Process is slowest step
   → Example: "Manual entry takes 30 min vs. 5 min others"

5. COMPLAINTS CLUSTER
   → Users frequently mention this step
   → Example: "Always waiting for Finance approval"
```

---

## 🔍 DETECTION METHODOLOGY

### **Step 1: Collect Cycle Times**
```yaml
For each process step:
  step_name: "Approval"
  processing_time: "15 min" (active work)
  wait_time: "2 days" (idle time)
  total_cycle_time: "2 days 15 min"
  
Red Flag: Wait time >> Processing time
```

### **Step 2: Measure WIP**
```yaml
For each process step:
  step_name: "Quality Review"
  items_in_queue: 35
  daily_throughput: 10
  
Calculation:
  Queue time = 35 items / 10 per day = 3.5 days backlog
  
Red Flag: Queue time > 1 day
```

### **Step 3: Calculate Utilization**
```yaml
Resource utilization:
  available_capacity: "8 hrs/day"
  actual_work: "7.5 hrs/day"
  utilization: 93.75%
  
Red Flag: > 90% utilization (saturated)
Red Flag: > 100% (impossible, overtime or queuing)
```

### **Step 4: Compare Step Times**
```yaml
Process steps:
  Step 1: 5 min
  Step 2: 10 min
  Step 3: 45 min ← BOTTLENECK
  Step 4: 5 min
  Step 5: 15 min
  
Bottleneck = Longest processing time
```

---

## 🎯 BOTTLENECK CLASSIFICATION

### **Type 1: Capacity Constraint**
```
Description: Not enough people/resources
Symptoms:
  - Queue keeps growing
  - Utilization > 90%
  - Overtime required

Example:
  "One approver for 50 requests/day"
  "Capacity: 30 requests/day"
  "Result: 20 requests backlog daily"

Solutions:
  - Add capacity (hire, delegate)
  - Reduce incoming demand
  - Increase efficiency of this step
```

### **Type 2: Process Inefficiency**
```
Description: Step takes too long
Symptoms:
  - Long processing time
  - Manual/complex work
  - Many handoffs

Example:
  "Manual data entry: 30 min per order"
  "40 orders/day = 20 hrs work (too much)"

Solutions:
  - Automate
  - Simplify
  - Provide better tools
```

### **Type 3: Dependency Bottleneck**
```
Description: Waiting for external input
Symptoms:
  - Long wait times
  - Not under team's control
  - Unpredictable timing

Example:
  "Waiting for customer to send documents"
  "Average: 3 days"

Solutions:
  - Front-load information gathering
  - Set clear deadlines
  - Automate reminders
  - Work in parallel where possible
```

### **Type 4: Policy Constraint**
```
Description: Artificial limit (policy, approval)
Symptoms:
  - Work waits unnecessarily
  - No capacity issue
  - "Because policy says so"

Example:
  "All purchases > $100 need VP approval"
  "VP reviews once per week"
  "Result: 1 week delay"

Solutions:
  - Increase approval threshold
  - Delegate authority
  - Pre-approve common items
```

---

## 📊 ANALYSIS TEMPLATE

```markdown
# BOTTLENECK ANALYSIS

## PROCESS: [Name]
## ANALYZED: [Date]

---

## CYCLE TIME BREAKDOWN

| Step | Processing | Wait | Total | % of Total |
|------|-----------|------|-------|-----------|
| Step 1 | 5 min | 0 | 5 min | 2% |
| Step 2 | 10 min | 0 | 10 min | 4% |
| **Step 3** | **45 min** | **2 days** | **2d 45m** | **92%** 🔥 |
| Step 4 | 5 min | 0 | 5 min | 2% |

**Total Cycle Time**: 2 days 1 hour
**Bottleneck**: Step 3 (92% of total time)

---

## WIP ANALYSIS

| Step | Current WIP | Capacity/Day | Queue Days |
|------|------------|-------------|-----------|
| Step 1 | 5 | 30 | 0.2 |
| Step 2 | 8 | 25 | 0.3 |
| **Step 3** | **40** | **15** | **2.7** 🔥 |
| Step 4 | 3 | 50 | 0.1 |

**Bottleneck**: Step 3 (2.7 days backlog)

---

## UTILIZATION ANALYSIS

| Resource | Available | Used | Utilization |
|----------|-----------|------|-------------|
| Person A | 8 hrs | 6 hrs | 75% |
| **Person B** | **8 hrs** | **7.8 hrs** | **97.5%** 🔥 |
| System X | 24 hrs | 12 hrs | 50% |

**Bottleneck**: Person B (saturated)

---

## ROOT CAUSE
[Why is this step the bottleneck?]

Example:
- Manual approval process (no delegation)
- One person responsible
- No clear SLA
- 40 requests/day but capacity for 15

---

## IMPACT

**Quantified Impact**:
- Queue time: 2.7 days average
- Affecting: 40 orders currently
- Cost: $X lost revenue per day delayed
- Customer satisfaction: 30% complaints about delays

---

## RECOMMENDATIONS

### Quick Wins (< 1 week)
1. [Immediate action]
   Impact: [Expected improvement]

### Medium Term (1-4 weeks)
2. [Moderate change]
   Impact: [Expected improvement]

### Strategic (> 1 month)
3. [Significant change]
   Impact: [Expected improvement]
```

---

## 🎯 WORKED EXAMPLE

### **Manufacturing: Material Bottleneck**

```markdown
## PROCESS: Order Fulfillment

### CYCLE TIME BREAKDOWN
| Step | Processing | Wait | Total |
|------|-----------|------|-------|
| Receive Order | 5 min | 0 | 5 min |
| Check Inventory | 10 min | 0 | 10 min |
| **Pick Materials** | **20 min** | **4 hrs** | **4h 20m** 🔥 |
| Assemble | 45 min | 0 | 45 min |
| Package | 10 min | 0 | 10 min |

**Total**: 5 hours 30 min
**Bottleneck**: Pick Materials (78% of cycle time)

### ROOT CAUSE
- One warehouse worker
- Manual picking (no system)
- Inventory locations not optimized
- Handles 30 orders/day but capacity for 20

### RECOMMENDATIONS
1. **Quick Win**: Organize warehouse by frequency
   - Impact: -30% picking time
   
2. **Medium**: Hire second picker OR implement batch picking
   - Impact: 2x throughput
   
3. **Strategic**: Implement WMS (Warehouse Management System)
   - Impact: Automated picking routes, -50% time
```

---

## 💡 THEORY OF CONSTRAINTS

```
Principle: System throughput is limited by its slowest step

Steps to Address:
1. IDENTIFY the constraint (bottleneck)
2. EXPLOIT the constraint (optimize current capacity)
3. SUBORDINATE everything else to the constraint
4. ELEVATE the constraint (add capacity)
5. REPEAT (find next constraint)

Example:
Step 1: Bottleneck is "Approval" (2 days)
Step 2: Exploit - Approver works on this first thing daily
Step 3: Subordinate - All prep work done before approval needed
Step 4: Elevate - Delegate some approvals OR hire second approver
Step 5: Once approval fixed, find next bottleneck
```

---

## 📊 VISUALIZATION: HEAT MAP

```
Process Flow with Heat Map:

Start → [Step 1] → [Step 2] → [🔥🔥🔥 Step 3 🔥🔥🔥] → [Step 4] → End
         5 min      10 min         2 days              5 min

Legend:
🔥🔥🔥 = Critical bottleneck (> 50% of cycle time)
🔥🔥   = Significant delay (20-50%)
🔥     = Minor delay (10-20%)
✅     = Efficient (< 10%)
```

---

## 📤 OUTPUT FORMAT

```json
{
  "bottleneck_analysis": {
    "process_id": "PROC-001",
    "analyzed_at": "2025-01-19",
    "bottlenecks": [
      {
        "step_id": "S3",
        "step_name": "Approval Process",
        "severity": "critical",
        "type": "capacity_constraint",
        "metrics": {
          "processing_time": "15 min",
          "wait_time": "2 days",
          "wip": 40,
          "utilization": "95%",
          "percent_of_total_time": "92%"
        },
        "root_cause": "Single approver with no delegation",
        "impact": {
          "queue_days": 2.7,
          "orders_affected": 40,
          "revenue_at_risk": "$50,000"
        },
        "recommendations": [
          {
            "priority": "high",
            "action": "Delegate approval authority for orders < $5K",
            "expected_impact": "Reduce queue by 60%",
            "effort": "low",
            "timeline": "1 week"
          }
        ]
      }
    ],
    "summary": {
      "total_cycle_time": "2 days 1 hour",
      "critical_path": "Approval step",
      "improvement_potential": "75% cycle time reduction"
    }
  }
}
```

---

## ✅ DETECTION CHECKLIST

- [ ] Cycle times measured for all steps
- [ ] WIP counted at each stage
- [ ] Resource utilization calculated
- [ ] Bottleneck identified (slowest step)
- [ ] Bottleneck type classified
- [ ] Root cause understood
- [ ] Impact quantified
- [ ] Recommendations prioritized

---

## 🔗 INTEGRATION

**Input from**:
- BPMN process map
- Time study data
- Observation notes
- Process logs

**Output to**:
- `as_is_process.json` → bottlenecks field
- Redesign Agent → Focus areas for improvement
- Heat maps and visualizations

---

**END OF SKILL: Bottleneck Detector**
