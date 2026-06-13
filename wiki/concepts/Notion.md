---
title: Notion
type: concept
tags: [tool, project-management, database, doktorlib, tech-stack, automation]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Project planning and collaboration tool used as secondary data layer in the DoktorLib pipeline — receives synchronized data from Make and provides deployment-facing view replacing Excel handover
---

# Notion

## Overview

**Notion** is a flexible all-in-one workspace tool used for notes, databases, wikis, and project management. In the [[DoktorLib Automation Pipeline]], Notion serves as the **secondary data layer** and **deployment-facing view** — complementing [[Salesforce]] (the primary backbone) with a more accessible interface for the deployment team.

## Role in the DoktorLib Pipeline

### Pipeline Position

```
[TALLY] → [MAKE] → [NOTION DB] (synchronized alongside Salesforce)
                        ↓
              Deployment team accesses Notion-Link
              (replaces Excel handover)
```

### Specific Uses

| Phase | Notion Role |
|---|---|
| Phase 2 (Make Automation) | Receives Tally intake data — new DB page created per customer |
| IT Audit (Make) | IT audit data synchronized to existing Notion page |
| Phase 4 (Deployment Handover) | Deployment-specific Notion template built; link shared instead of Excel |

## Design Decision: Notion as Secondary, Salesforce as Primary

The source document explicitly positions Notion as **Projektplanung** (project planning) while [[Salesforce]] is the **Daten-Backbone** (data backbone). This means:
- Notion is the *human-readable, deployment-facing* layer
- Salesforce is the *system-of-record, integration-facing* layer
- Data flows from Tally → Make → **both** systems in parallel

## Deployment Handover Benefit

The key outcome of using Notion for deployment:
- **Before:** Deployment team receives Excel file (no single source of truth, version control issues)
- **After:** Deployment team receives a **Notion link** (always current, connected to live data)

## Build Status (Open Items)

- [ ] Notion-Template für Deployment-Ansicht bauen (build deployment view template)
- [ ] Link-Übergabe definieren (define link handover process)

## Related Pages

- [[DoktorLib Automation Pipeline]] — pipeline context
- [[DoktorLib Automation Pipeline Source Detail]] — full source
- [[Make]] — automation layer writing to Notion
- [[Salesforce]] — primary data backbone (Notion is secondary)
- [[Tally]] — upstream input source
- [[DoktorLib]] — organization context
