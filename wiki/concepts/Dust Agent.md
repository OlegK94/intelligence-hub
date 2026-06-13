---
title: Dust Agent
type: concept
tags: [tool, AI, LLM, automation, doktorlib, keb, knowledge-management, tech-stack]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Internal AI platform (Dust.tt) used in the DoktorLib pipeline as the KEB-Generator — reads Salesforce data and auto-generates the Kundenerfassungsbogen (customer registration document)
---

# Dust Agent

## Overview

**Dust** (dust.tt) is an internal AI platform for building AI agents connected to company data. In the [[DoktorLib Automation Pipeline]], a Dust Agent serves as the **KEB-Generator** (Phase 3): it reads all Salesforce data for a given customer and automatically generates the [[Kundenerfassungsbogen]] (KEB) — replacing the manual Excel-based process.

## Role in the DoktorLib Pipeline

### Pipeline Position

```
Vertragsunterzeichnung (Contract Signed)
    ↓ (trigger)
[DUST AGENT]
    ← reads: [SALESFORCE] (all customer data)
    → outputs: KEB (standard format)
    ↓
Deployment erhält Notion-Link (kein Excel)
```

### What It Does

1. **Input:** Reads all structured Salesforce data for the signed customer (populated from Tally intake + IT audit + manual discovery notes)
2. **Processing:** LLM-based generation using a custom prompt (to be written)
3. **Output:** KEB in standard format — replacing the manually filled Excel

## Why Dust (vs. Other AI Tools)

- Designated as **interne KI-Plattform** (internal AI platform) at DoktorLib
- Designed for connecting AI agents to company data sources
- Can be configured to read Salesforce as a data source
- Enables structured output generation from structured data

## Build Status (Open Items)

- [ ] Dust Agent Prompt schreiben (write the prompt)
- [ ] Input: Define Salesforce data structure for agent
- [ ] Output: Define KEB field structure ("noch zu definieren" — not yet defined)
- [ ] Trigger: Contract signature (manual OR automatic via SF Stage-Change)

## Key Sequencing Note

The source document explicitly recommends:
> **Tally first, Dust Prompt second** — without knowing the Tally field structure (input), a meaningful Dust Prompt cannot be written. The input defines the output.

This is the rationale for Phase 1 (Tally) preceding Phase 3 (Dust Agent) in the build sequence.

## Relationship to Existing Wiki

The [[DoktorLib Automation Pipeline]] entity page previously described Dust as one of two tool options (alongside Tally). This source clarifies Dust is a **separate, later-phase tool** — not an alternative to Tally.

## Related Pages

- [[DoktorLib Automation Pipeline]] — pipeline context
- [[DoktorLib Automation Pipeline Source Detail]] — full source
- [[Salesforce]] — data source Dust reads from
- [[Kundenerfassungsbogen]] — artifact Dust generates
- [[Tally]] — upstream data collection (defines Dust's input)
- [[DoktorLib]] — organization context
- [[Claude Projects Setup]] — comparison: another AI tool in Oleg's stack
