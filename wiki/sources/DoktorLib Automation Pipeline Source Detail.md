---
title: DoktorLib Automation Pipeline Source Detail
type: source
tags: [doktorlib, automation, tech, aktiv, tally, make, salesforce, notion, dust, pipeline, onboarding, lead-management]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-05-08
updated: 2026-06-15
summary: Full source document for the DoktorLib Automation Pipeline — end-to-end automation of inbound lead Discovery & Onboarding for Arztpraxen using Tally, Make, Salesforce, Notion, and Dust; replaces manual Excel KEB
---

# DoktorLib Automation Pipeline — Source Detail

## Overview

This source document (status: In Bau, created 2026-05-08) captures the full architecture and build plan for [[DoktorLib]]'s internal automation pipeline, targeting maximum automation of the **Discovery & Onboarding flow** for inbound leads (Arztpraxen / medical practices).

> For the entity summary and strategic context, see [[DoktorLib Automation Pipeline]].

## Goal

- **Maximale Automatisierung** of the Discovery & Onboarding flow for inbound leads
- **Minimale manuelle Dateneingabe** (minimal manual data entry)
- **Salesforce** as Long-Term Data Backbone

## Ist-Zustand (Current State — Problems)

| Problem | Description |
|---|---|
| Late data capture | Practice base data collected too late — only during Demo Call |
| Unstructured discovery notes | Free-text in Salesforce → not scalable |
| Manual KEB | Kundenerfassungsbogen (customer registration form) = manually filled Excel → error-prone |
| No single source of truth | Deployment team receives Excel file → fragmented handover |

## Ziel-Architektur (Target Architecture)

```
Inbound Lead
    ↓
[TALLY] Intake Form (vor Demo / before demo call)
    ↓
[MAKE] Automation
    ↓              ↓
[SALESFORCE]   [NOTION DB]
(Daten-Backbone)  (Projektplanung)
    ↓
Demo-Call (nur Validierung + Discovery Notes manuell in SF)
    ↓
IT-Partner → separates [TALLY] Audit-Formular
    ↓
[MAKE] schreibt Audit-Daten → Salesforce + Notion
    ↓
Vertragsunterzeichnung
    ↓
[DUST AGENT] liest alle SF-Daten → generiert KEB automatisch
    ↓
Deployment erhält Notion-Link (kein Excel mehr)
```

### Flow Summary

1. **Pre-Demo:** Tally Intake Form collects practice base data before any call
2. **Make Automation:** Pushes Tally submission data into both Salesforce and Notion
3. **Demo Call:** Reduced to validation + manual Discovery Notes entry in SF only
4. **IT Audit:** Separate Tally form for IT partner, data flows back into SF + Notion via Make
5. **Post-Signature:** Dust Agent reads all Salesforce data → auto-generates KEB
6. **Deployment Handover:** Notion link replaces Excel entirely

## Stack

| Tool | Role | Notes |
|---|---|---|
| [[Tally]] | Form builder (Intake + Audit) | DSGVO-konform, EU-Hosting Belgien ✅ |
| [[Make]] | Automation / middleware | Trigger-based data routing |
| [[Salesforce]] | Long-term data backbone | Primary record of truth |
| [[Notion]] | Project planning DB | Secondary / deployment view |
| [[Dust Agent]] | AI KEB generator | Reads SF data → generates KEB |

## Build-Phasen (Build Phases)

### Phase 1 — Tally Intake Form
- [ ] Felder definieren: Praxistyp, Fachrichtung, aktuelle Software, Labore, IT-Infrastruktur, Gerätelandschaft
- [ ] DSGVO-konforme Formularbeschriftung (Tally, EU-Hosting Belgien ✅)
- [ ] Automatische Weiterleitung / Bestätigungsmail

**Key fields to capture:** Practice type, medical specialty, current software, labs, IT infrastructure, device landscape

### Phase 2 — Make Automation
- [ ] Trigger: Tally Form Submission
- [ ] Aktion 1: Salesforce — neues Lead/Opportunity erstellen + Felder befüllen
- [ ] Aktion 2: Notion — neue DB-Seite erstellen + Felder synchronisieren
- [ ] Error Handling: Benachrichtigung bei Fehler

### Phase 3 — Dust Agent (KEB-Generator)
- [ ] Dust Agent Prompt schreiben
- [ ] Input: Salesforce-Daten (Struktur definieren)
- [ ] Output: KEB im Standard-Format (Felder: noch zu definieren)
- [ ] Trigger: Vertragsunterzeichnung (manuell oder automatisch via SF-Stage-Change)

### Phase 4 — Deployment Handover
- [ ] Notion-Template für Deployment-Ansicht bauen
- [ ] Link-Übergabe statt Excel

## Entscheidungen (Decisions Made)

| Decision | Rationale |
|---|---|
| **Salesforce = Long-Term Data Backbone** | Not just Notion — SF as primary system of record |
| **Tally = DSGVO-konform** | Suitable for Praxisstruktur-Daten (practice structure data); no patient data involved |
| **Dust = internal AI platform** | For KEB generation from structured SF data |
| **Excel KEB = abgelöst** | Replaced entirely, not optimized |

## Nächster Schritt (Next Step as of Source)

**Open decision:** Build Tally form structure first OR write Dust Agent Prompt first?

→ **Recommendation in source:** Tally first — input defines the output. Without field structure, no meaningful Dust Prompt can be written.

## Relationship to Existing Entity Page

The existing [[DoktorLib Automation Pipeline]] entity page (created 2026-06-13) had limited detail — it mentioned only "Tally Form or Dust Agent" as technology options under consideration, without the full architecture. This source document reveals:

- The stack is **not** a choice between Tally and Dust — **both are used** in different phases
- **Make** and **Salesforce** are also core components (not previously captured)
- **Notion** serves as the secondary project management layer
- The pipeline replaces a specific artifact: the **Excel KEB (Kundenerfassungsbogen)**
- The IT partner has a **separate Tally audit form** (second form, not just one)

> ⚠️ **Partial Contradiction with Existing Entity:** The existing [[DoktorLib Automation Pipeline]] entity page described Tally and Dust as "technology options under consideration," implying a choice between them. The source document shows they are **complementary tools in different phases** of a single pipeline. Entity page updated accordingly.

## Related Pages

- [[DoktorLib Automation Pipeline]] — entity page (updated)
- [[DoktorLib]] — company context
- [[Oleg Personal Context]] — project owner
- [[MOC Strategie und Business]] — listed as active project
- [[MOC Tech und Setup]] — technical stack context
- [[Tally]] — form builder tool
- [[Make]] — automation middleware
- [[Salesforce]] — data backbone
- [[Notion]] — project planning layer
- [[Dust Agent]] — AI KEB generator
- [[Kundenerfassungsbogen]] — the artifact being automated
