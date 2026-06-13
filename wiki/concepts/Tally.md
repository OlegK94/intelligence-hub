---
title: Tally
type: concept
tags: [tool, form-builder, no-code, automation, dsgvo, doktorlib, tech-stack]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: No-code form builder used in the DoktorLib Automation Pipeline for DSGVO-compliant data collection from Arztpraxen; EU-hosted in Belgium
---

# Tally

## Overview

**Tally** is a no-code form builder used in the [[DoktorLib Automation Pipeline]] as the primary data collection layer for inbound leads (Arztpraxen). It serves two distinct form functions in the pipeline:

1. **Intake Form** — collects practice base data from the lead *before* the Demo Call
2. **IT Audit Form** — a separate form completed by the IT partner post-demo

## Why Tally Was Chosen

- **DSGVO-konform:** Compliant with GDPR regulations
- **EU-Hosting:** Servers located in Belgium → satisfies EU data residency requirements
- **No patient data risk:** Only captures Praxisstruktur data (practice structure, not patient records)
- **No-code:** Enables form building without developer involvement

## Role in Pipeline

```
[TALLY Intake Form] → [MAKE] → Salesforce + Notion
[TALLY IT Audit Form] → [MAKE] → Salesforce + Notion
```

Tally acts as the **input layer**; [[Make]] routes the data downstream.

## Integration Points

| Downstream Tool | How Connected |
|---|---|
| [[Make]] | Trigger: Form submission fires Make scenario |
| [[Salesforce]] | Via Make: creates/updates Lead or Opportunity |
| [[Notion]] | Via Make: creates new DB page |

## Fields Planned for Intake Form

(as of source document — not yet finalized)
- Praxistyp (practice type)
- Fachrichtung (medical specialty)
- Aktuelle Software (current software)
- Labore (labs)
- IT-Infrastruktur
- Gerätelandschaft (device landscape)

## Related Pages

- [[DoktorLib Automation Pipeline]] — primary use context
- [[DoktorLib Automation Pipeline Source Detail]] — full source
- [[Make]] — automation middleware triggered by Tally
- [[Salesforce]] — downstream data target
- [[Notion]] — downstream project layer
- [[DoktorLib]] — organization using Tally
