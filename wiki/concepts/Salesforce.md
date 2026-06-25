---
title: Salesforce
type: concept
tags: [tool, crm, data-backbone, saas, doktorlib, tech-stack, automation]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: CRM-Plattform, die als langfristiges Daten-Backbone der DoktorLib Automation Pipeline ausgewählt wurde — primäres System of Record für alle Lead- und Kundendaten
---

# Salesforce

## Überblick

**Salesforce** ist eine führende Enterprise-CRM-Plattform (Customer Relationship Management). In der [[DoktorLib Automation Pipeline]] wurde sie als **langfristiges Daten-Backbone** designiert — das primäre System of Record für alle Lead-, Opportunity- und Kundendaten.

## Rolle in der DoktorLib Pipeline

### Architekturentscheidung

> **Salesforce = Langfristiges Daten-Backbone** (nicht nur Notion)

Dies ist eine explizite Architekturentscheidung, die in der Quelle dokumentiert ist. Salesforce wird gegenüber Notion als primärer Datenspeicher gewählt, weil:
- Skalierbarkeit bei wachsendem Lead-Volumen
- Strukturierte feldbasierte Daten (vs. Notions flexibler, aber weniger strukturierter DB)
- Integration mit [[Dust Agent]] für die KEB-Generierung
- CRM-native Workflows (Opportunity-Stufen, Lead-Routing)

### Position im Datenfluss

```
[TALLY] → [MAKE] → [SALESFORCE] ← [DUST AGENT reads]
                        ↓
                 [NOTION] (sekundär)
```

### Konkrete Einsatzbereiche

| Phase | Salesforce-Rolle |
|---|---|
| Phase 2 (Make Automation) | Empfängt Tally-Intake-Daten via Make — Lead/Opportunity wird angelegt und Felder werden befüllt |
| Demo Call | Discovery Notes werden manuell vom Sales-Rep eingetragen |
| IT-Audit (Make) | Empfängt IT-Audit-Daten aus dem zweiten Tally-Formular |
| Phase 3 (Dust Agent) | Alle SF-Daten werden vom Dust Agent ausgelesen, um das KEB zu generieren |

## Aktueller Zustand (Problem)

Vor der Pipeline wurde Salesforce genutzt für:
- Discovery Notes als Freitext (nicht skalierbar)
- Unvollständige Dateneingabe (spät — erst beim Demo Call)

Die Pipeline verwandelt Salesforce in ein **vollständiges, strukturiertes, frühzeitig befülltes** Datensystem.

## Auslöser für den Dust Agent

- **Stage-Change-Trigger:** Wenn sich die SF-Opportunity-Stufe auf „Vertragsunterzeichnung" ändert, kann dies optional den Dust Agent automatisch auslösen
- Manueller Auslöser ist ebenfalls möglich

## Verwandte Seiten

- [[DoktorLib Automation Pipeline]] — Pipeline-Kontext
- [[DoktorLib Automation Pipeline Source Detail|DoktorLib Automation Pipeline Quellendetail]] — vollständige Quelle
- [[Make]] — Automatisierungsschicht, die in Salesforce schreibt
- [[Tally]] — Eingabequelle
- [[Dust Agent]] — liest Salesforce-Daten für die KEB-Generierung
- [[Notion]] — sekundäre Schicht neben Salesforce
- [[DoktorLib]] — Organisationskontext