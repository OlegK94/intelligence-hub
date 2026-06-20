---
title: Make
type: concept
tags: [tool, automation, no-code, middleware, integration, doktorlib, tech-stack]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: No-code-Automatisierungsplattform (ehemals Integromat), die als Middleware in der DoktorLib-Pipeline eingesetzt wird — löst bei Tally-Formulareinreichungen aus und leitet Daten an Salesforce und Notion weiter
---

# Make

## Übersicht

**Make** (ehemals Integromat) ist eine No-code-Automatisierungs- und Integrationsplattform. In der [[DoktorLib Automation Pipeline]] fungiert Make als **Automatisierungs-Middleware** — die verbindende Schicht zwischen [[Tally]]-Formulareinreichungen und den nachgelagerten Datenspeichern ([[Salesforce]] und [[Notion]]).

## Rolle in der DoktorLib-Pipeline

```
[TALLY] Formulareinreichung
    ↓ (Auslöser)
[MAKE] Szenario
    ↓              ↓
[SALESFORCE]   [NOTION DB]
```

### Auslöser
- Tally-Formulareinreichung (sowohl Intake Form als auch IT Audit Form)

### Aktionen
1. **Aktion 1:** Salesforce — neuen Lead/Opportunity anlegen + Felder mit Tally-Daten befüllen
2. **Aktion 2:** Notion — neue Datenbankseite anlegen + Felder synchronisieren
3. **Fehlerbehandlung:** Benachrichtigungssystem bei Fehlern

## Warum Make

- Native Tally-Integrationsunterstützung
- Robuster Salesforce-Connector
- Notion-Integration verfügbar
- Visueller Szenario-Builder für Nicht-Entwickler
- Fehlerbehandlung und Wiederholungslogik

## Entwicklungsstand

Phase 2 der Pipeline — zum Zeitpunkt des Quelldokuments (2026-05-08) noch nicht umgesetzt.

## Offene Aufgaben

- [ ] Auslöser: Tally-Formulareinreichung
- [ ] Aktion 1: Salesforce Lead/Opportunity-Erstellung
- [ ] Aktion 2: Notion-Datenbankseite erstellen
- [ ] Fehlerbehandlung: Einrichtung der Fehlerbenachrichtigung

## Verwandte Seiten

- [[DoktorLib Automation Pipeline]] — Pipeline-Kontext
- [[DoktorLib Automation Pipeline Source Detail]] — vollständige Quelle
- [[Tally]] — vorgelagerter Auslöser
- [[Salesforce]] — nachgelagertes Aktionsziel
- [[Notion]] — nachgelagertes Aktionsziel
- [[DoktorLib]] — Organisationskontext