TAGS: [automation, workflow, integration, make, zapier, tools, doktorlib]
SOURCES: ["raw/raw/_archiv/Work/DoktorLib Automation Pipeline.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: Make (ehemals Zapier) — Workflow-Automation-Plattform; verwendet in DoktorLib Automation Pipeline (Phase 2 und 3) für Trigger-Action-Szenarien; verbindet Tally Form Submission mit Salesforce & Notion

---

# Make

## Überblick

**Make** (ehemals Zapier) ist eine **Workflow-Automation-Plattform**, die in der [[DoktorLib Automation Pipeline]] die zentrale Rolle als **Integrations-Hub** spielt.

## Rollen in DoktorLib

### Phase 2: Initial Automation
- **Trigger:** Tally Form Submission (Intake Form)
- **Aktion 1:** Salesforce
  - Lead oder Opportunity erstellen
  - Felder aus Tally-Form mappen
- **Aktion 2:** Notion
  - DB-Seite erstellen
  - Felder synchronisieren
- **Error Handling:** Slack / Email Notification

### Phase 3: Audit-Automation (erweitert)
- **Trigger:** Tally Form Submission (Audit-Formular)
- **Aktion:** Salesforce + Notion aktualisieren mit Audit-Daten

## Szenarien-Architektur

```
Scenario 1: Intake Form Automation
├─ Trigger: Tally Webhook (Form Submission)
├─ Step 2: Map Tally Fields
├─ Step 3: Create Salesforce Lead
├─ Step 4: Create Notion Database Page
└─ Step 5: Error Handler (Slack Notify)

Scenario 2: Audit Form Automation
├─ Trigger: Tally Webhook (Audit Form Submission)
├─ Step 2: Map Audit Fields
├─ Step 3: Update Salesforce Opportunity
├─ Step 4: Update Notion DB Page
└─ Step 5: Error Handler (Slack Notify)
```

## Abhängigkeiten

- [[Tally]] — Trigger-Quelle (Form Submissions)
- [[Salesforce]] — Ziel-System 1
- [[Notion]] — Ziel-System 2

---

*Entität erstellt: 2026-06-17*
