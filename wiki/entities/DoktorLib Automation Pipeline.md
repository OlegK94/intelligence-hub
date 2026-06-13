---
title: DoktorLib Automation Pipeline
type: entity
tags: [automation, saas, workflow, doktorlib, project, tally, make, salesforce, notion, dust-agent, aktiv, onboarding, lead-management]
sources: ["raw/00-MOC/🏠 Home.md", "raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-13
updated: 2026-06-15
summary: Active automation project at DoktorLib — end-to-end pipeline (Tally → Make → Salesforce/Notion → Dust Agent) to automate inbound lead Discovery & Onboarding for Arztpraxen, replacing manual Excel KEB; Priority 2 as of June 2026
---

# DoktorLib Automation Pipeline

## Overview

The DoktorLib Automation Pipeline is an active work project ([[Oleg Personal Context|Oleg]]'s Priority 2 as of June 2026) to automate the end-to-end **Discovery & Onboarding flow** for inbound leads (Arztpraxen / medical practices) at [[DoktorLib]]. The pipeline uses a combination of no-code and AI tools to eliminate manual data entry and replace the existing Excel-based KEB (Kundenerfassungsbogen / customer registration form).

> For full architecture, build phases, and source detail, see [[DoktorLib Automation Pipeline Source Detail]].

## Project Status

- **Status:** 🟡 In Bau (In Development)
- **Priority:** 2 of 6 active priorities
- **Next Step:** Build Tally Intake Form first (input defines the Dust Agent output)
- **Source Created:** 2026-05-08

## The Problem Being Solved

| Problem | Detail |
|---|---|
| Late data capture | Practice base data only collected during Demo Call — too late |
| Unstructured discovery notes | Free-text in Salesforce → not scalable |
| Manual KEB | Excel-based customer registration form → error-prone, fragmented |
| No single source of truth | Deployment receives Excel → no connected handover |

## Technology Stack

| Tool | Role |
|---|---|
| [[Tally]] | Form builder — Intake Form (pre-demo) + IT Audit Form |
| [[Make]] | Automation middleware — routes data from Tally to SF and Notion |
| [[Salesforce]] | Long-term data backbone — primary system of record |
| [[Notion]] | Project planning DB — secondary layer for deployment view |
| [[Dust Agent]] | AI agent — reads Salesforce data, generates KEB automatically |

> ⚠️ **Correction from earlier version:** The original entity page described Tally and Dust as alternative options. The source document (see [[DoktorLib Automation Pipeline Source Detail]]) clarifies that **both are used** in complementary phases — Tally for data collection (Phase 1), Dust for KEB generation (Phase 3).

## Target Flow

```
Inbound Lead
    ↓
[TALLY] Intake Form (vor Demo)
    ↓
[MAKE] → [SALESFORCE] + [NOTION DB]
    ↓
Demo-Call (Validierung only)
    ↓
IT-Partner → [TALLY] Audit Form
    ↓
[MAKE] → Salesforce + Notion
    ↓
Vertragsunterzeichnung
    ↓
[DUST AGENT] → KEB automatisch generiert
    ↓
Deployment erhält Notion-Link (kein Excel)
```

## Build Phases

1. **Phase 1 — Tally Intake Form:** Define fields (Praxistyp, Fachrichtung, Software, Labore, IT-Infrastruktur, Gerätelandschaft), DSGVO-compliant setup
2. **Phase 2 — Make Automation:** Trigger on Tally submission → create SF Lead/Opportunity + Notion DB page, with error handling
3. **Phase 3 — Dust Agent (KEB-Generator):** Prompt design, SF data input structure, KEB output format, trigger on contract signature
4. **Phase 4 — Deployment Handover:** Notion template for deployment view, link-based handover replaces Excel

## Key Decisions Made

- **Salesforce = Long-Term Data Backbone** (not just Notion)
- **Tally = DSGVO-konform** for Praxisstruktur-Daten (EU-Hosting Belgien ✅; no patient data)
- **Dust = internal AI platform** for KEB generation
- **Excel KEB = replaced entirely** (not optimized)

## Context

This project sits within [[Oleg Personal Context|Oleg]]'s broader work at [[DoktorLib]] in B2B SaaS sales targeting medical practices. The automation directly impacts the Sales → Deployment handover process and reduces manual overhead at every stage.

The [[Tally]] DSGVO note is significant: collecting Praxisstruktur data (practice structure, not patient data) under GDPR is permissible with proper form labeling. EU hosting in Belgium satisfies data residency requirements.

## Related Pages

- [[DoktorLib Automation Pipeline Source Detail]] — full source document with architecture
- [[DoktorLib]] — parent company
- [[Oleg Personal Context]] — project owner
- [[MOC Strategie und Business]] — strategic MOC
- [[MOC Tech und Setup]] — technical stack context
- [[Tally]] — form builder tool concept
- [[Make]] — automation middleware concept
- [[Salesforce]] — CRM backbone concept
- [[Notion]] — project planning layer
- [[Dust Agent]] — AI KEB generator
- [[Kundenerfassungsbogen]] — artifact being automated
