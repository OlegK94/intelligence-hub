---
title: Make
type: concept
tags: [tool, automation, no-code, middleware, integration, doktorlib, tech-stack]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: No-code automation platform (formerly Integromat) used as middleware in the DoktorLib pipeline — triggers on Tally form submissions and routes data to Salesforce and Notion
---

# Make

## Overview

**Make** (formerly Integromat) is a no-code automation and integration platform. In the [[DoktorLib Automation Pipeline]], Make serves as the **automation middleware** — the connective layer between [[Tally]] form submissions and the downstream data stores ([[Salesforce]] and [[Notion]]).

## Role in the DoktorLib Pipeline

```
[TALLY] Form Submission
    ↓ (trigger)
[MAKE] Scenario
    ↓              ↓
[SALESFORCE]   [NOTION DB]
```

### Trigger
- Tally Form Submission (both Intake Form and IT Audit Form)

### Actions
1. **Aktion 1:** Salesforce — create new Lead/Opportunity + populate fields from Tally data
2. **Aktion 2:** Notion — create new DB page + synchronize fields
3. **Error Handling:** Notification system on failure

## Why Make

- Native Tally integration support
- Robust Salesforce connector
- Notion integration available
- Visual scenario builder for non-developers
- Error handling and retry logic

## Build Status

Phase 2 of the pipeline — not yet built as of source document (2026-05-08).

## Open Build Items

- [ ] Trigger: Tally Form Submission
- [ ] Aktion 1: Salesforce Lead/Opportunity creation
- [ ] Aktion 2: Notion DB page creation
- [ ] Error Handling: failure notification setup

## Related Pages

- [[DoktorLib Automation Pipeline]] — pipeline context
- [[DoktorLib Automation Pipeline Source Detail]] — full source
- [[Tally]] — upstream trigger source
- [[Salesforce]] — downstream action target
- [[Notion]] — downstream action target
- [[DoktorLib]] — organization context
