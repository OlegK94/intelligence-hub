---
title: Salesforce
type: concept
tags: [tool, crm, data-backbone, saas, doktorlib, tech-stack, automation]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: CRM platform selected as the Long-Term Data Backbone for the DoktorLib Automation Pipeline — primary system of record for all lead and customer data
---

# Salesforce

## Overview

**Salesforce** is a leading enterprise CRM (Customer Relationship Management) platform. In the [[DoktorLib Automation Pipeline]], it has been designated as the **Long-Term Data Backbone** — the primary system of record for all lead, opportunity, and customer data.

## Role in the DoktorLib Pipeline

### Design Decision

> **Salesforce = Long-Term Data Backbone** (not just Notion)

This is an explicit architectural decision documented in the source. Salesforce is chosen over Notion as the primary data store because:
- Scalability for growing lead volume
- Structured field-based data (vs. Notion's flexible but less structured DB)
- Integration with [[Dust Agent]] for KEB generation
- CRM-native workflows (Opportunity stages, Lead routing)

### Data Flow Position

```
[TALLY] → [MAKE] → [SALESFORCE] ← [DUST AGENT reads]
                        ↓
                 [NOTION] (secondary)
```

### Specific Uses

| Phase | Salesforce Role |
|---|---|
| Phase 2 (Make Automation) | Receives Tally intake data via Make — Lead/Opportunity created + fields populated |
| Demo Call | Discovery Notes entered manually by sales rep |
| IT Audit (Make) | Receives IT Audit data from second Tally form |
| Phase 3 (Dust Agent) | All SF data read by Dust Agent to generate KEB |

## Current State (Problem)

Pre-pipeline, Salesforce was used for:
- Discovery Notes as free-text (not scalable)
- Partial data entry (late — only at Demo Call stage)

The pipeline transforms Salesforce into a **complete, structured, early-populated** data system.

## Trigger for Dust Agent

- **Stage-Change trigger:** When SF Opportunity stage changes to "Vertragsunterzeichnung" (contract signed), this can optionally trigger the Dust Agent automatically
- Manual trigger also possible

## Related Pages

- [[DoktorLib Automation Pipeline]] — pipeline context
- [[DoktorLib Automation Pipeline Source Detail]] — full source
- [[Make]] — automation layer writing to Salesforce
- [[Tally]] — input source
- [[Dust Agent]] — reads Salesforce data for KEB generation
- [[Notion]] — secondary layer alongside Salesforce
- [[DoktorLib]] — organization context
