# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

This is a **documentation-driven consulting engagement**, not a software project. It has two components:

1. **NVC Client Engagement** — Organizational consulting for NVC (Nutrición, Vacunas y Consultoría), a food supplement, animal vaccine, and veterinary consultation company scaling from 1 matrix + 4 branches to 10 locations.
2. **`.antigravity/` Framework** — A reusable multi-agent methodology for problem discovery before solution design. Can be applied to future consulting engagements beyond NVC.

There are no build commands, package managers, tests, or deployments. Everything is markdown and JSON.

## Navigation

- **Start here:** `README.md` — Master index with links to all documents and current status.
- **Current NVC status:** `08_resumen_ejecutivo/resumen01_20260219.md`
- **NVC active problem definition:** `.antigravity/memory/problem_statement.json` and `engagement_profile.json`
- **Framework rules (non-negotiable):** `.antigravity/.agrules`
- **Framework overview:** `.antigravity/README.md`

## Project Conventions

**Versioning:** All deliverable documents follow `filename_vN_YYYYMMDD.md`.
Example: `plan_estrategico_v2_20260219.md` = version 2, updated 2026-02-19.
Each file contains an internal version history table.

**Directory numbering** reflects consulting phases:
- `02_diagnostico/` → Diagnosis
- `03_plan_estrategico/` → Strategic Plan
- `04_estructura_organizacional/` → Org Structure
- `05_manual_de_funciones/` → Job Descriptions
- `06_manual_de_organizacion/` → Institutional Manual
- `07_purina_investigacion/` → Supplier Research
- `08_resumen_ejecutivo/` → Executive Summary
- `09_sistemas_tecnologia/` → Systems Analysis

## .antigravity Framework Architecture

The framework is organized in 4 layers:

**Layer 1 – Foundation:** `.agrules` (rules), `memory/*.json` (engagement state), `ECONOMIC_INTEGRATION.md` (business case methodology)

**Layer 2 – Skills:** Executable tools grouped in `skills/discovery/`, `skills/process_modeling/`, `skills/analysis/`. The most critical is `skills/analysis/business_case_calculator.md` — it quantifies problem cost, savings, and full ROI/NPV/Payback at 3 pipeline gates.

**Layer 3 – Agents:** 8 sequential agents in `agents/` (01→08): Intake → Discovery → Maturity → Methodology → Process Intelligence → Redesign → Solution Architect → Roadmap.

**Layer 4 – Workflows:** `workflows/` contains orchestration templates that select which agents to activate depending on the problem type (process digitalization, operational improvement, etc.).

## Core Consulting Rules (from .agrules)

- **Never propose technology or solutions before understanding the real problem.**
- AS-IS process modeling is mandatory before any redesign.
- Economic quantification is required at 3 gates: Discovery, TO-BE Design, and Roadmap.
- Problem discovery must include ≥2 stakeholder profiles.
- Never digitalize a broken process — fix it first.
- GO decision criteria: ROI > 50% AND Payback < 18 months AND NPV > 0.

## NVC Engagement Context

**Client problem:** Extreme centralization (Director General is the single decision-maker), no process documentation, information silos across branches, legal risks (staff not registered with IMSS), and insufficient technology for multi-location scale. Estimated opportunity cost: $1.44M/year.

**Current phase:** Diagnosis (40% complete). Second interview pending to answer 40+ follow-up questions (`02_diagnostico/pendientes01_20260216.md`).

**Pending work:** Detailed AS-IS process modeling, TO-BE redesign with economic quantification, technology architecture recommendation, implementation roadmap, and change management plan.

**Memory state files** (keep updated as engagement progresses):
- `.antigravity/memory/engagement_profile.json` — complexity scores, maturity, workflow selected
- `.antigravity/memory/problem_statement.json` — validated problem, root causes, stakeholders, impact
