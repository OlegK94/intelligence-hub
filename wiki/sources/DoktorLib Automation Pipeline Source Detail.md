---
title: DoktorLib Automation Pipeline Quelldokument Detail
type: source
tags: [doktorlib, automation, tech, aktiv, tally, make, salesforce, notion, dust, pipeline, onboarding, lead-management]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-05-08
updated: 2026-06-15
summary: Vollständiges Quelldokument für die DoktorLib Automation Pipeline — End-to-End-Automatisierung des eingehenden Lead Discovery & Onboarding für Arztpraxen mit Tally, Make, Salesforce, Notion und Dust; ersetzt den manuellen Excel-KEB
---

# DoktorLib Automation Pipeline — Quelldokument Detail

## Überblick

Dieses Quelldokument (Status: In Bau, erstellt 2026-05-08) erfasst die vollständige Architektur und den Bauplan für [[DoktorLib]]s interne Automation Pipeline, mit dem Ziel einer maximalen Automatisierung des **Discovery & Onboarding Flows** für eingehende Leads (Arztpraxen).

> Für die Entitätszusammenfassung und den strategischen Kontext siehe [[DoktorLib Automation Pipeline]].

## Ziel

- **Maximale Automatisierung** des Discovery & Onboarding Flows für eingehende Leads
- **Minimale manuelle Dateneingabe**
- **Salesforce** als langfristiges Daten-Backbone

## Ist-Zustand (Aktuelle Probleme)

| Problem | Beschreibung |
|---|---|
| Späte Datenerfassung | Praxis-Stammdaten werden zu spät erfasst — erst während des Demo-Calls |
| Unstrukturierte Discovery-Notizen | Freitext in Salesforce → nicht skalierbar |
| Manueller KEB | Kundenerfassungsbogen = manuell ausgefülltes Excel → fehleranfällig |
| Keine einheitliche Datenquelle | Deployment-Team erhält Excel-Datei → fragmentierte Übergabe |

## Ziel-Architektur

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

### Flow-Zusammenfassung

1. **Vor dem Demo:** Tally Intake Form erfasst Praxis-Stammdaten vor jedem Gespräch
2. **Make Automation:** Überträgt Tally-Formulardaten in Salesforce und Notion
3. **Demo-Call:** Reduziert auf Validierung + manuelle Eingabe von Discovery Notes in SF
4. **IT-Audit:** Separates Tally-Formular für den IT-Partner, Daten fließen über Make zurück in SF + Notion
5. **Nach Vertragsunterzeichnung:** Dust Agent liest alle Salesforce-Daten → generiert KEB automatisch
6. **Deployment-Übergabe:** Notion-Link ersetzt Excel vollständig

## Stack

| Tool | Rolle | Hinweise |
|---|---|---|
| [[Tally]] | Formular-Builder (Intake + Audit) | DSGVO-konform, EU-Hosting Belgien ✅ |
| [[Make]] | Automation / Middleware | Trigger-basiertes Daten-Routing |
| [[Salesforce]] | Langfristiges Daten-Backbone | Primäre Datenquelle |
| [[Notion]] | Projektplanungs-Datenbank | Sekundär / Deployment-Ansicht |
| [[Dust Agent]] | KI-KEB-Generator | Liest SF-Daten → generiert KEB |

## Build-Phasen

### Phase 1 — Tally Intake Form
- [ ] Felder definieren: Praxistyp, Fachrichtung, aktuelle Software, Labore, IT-Infrastruktur, Gerätelandschaft
- [ ] DSGVO-konforme Formularbeschriftung (Tally, EU-Hosting Belgien ✅)
- [ ] Automatische Weiterleitung / Bestätigungsmail

**Zu erfassende Schlüsselfelder:** Praxistyp, Fachrichtung, aktuelle Software, Labore, IT-Infrastruktur, Gerätelandschaft

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

### Phase 4 — Deployment-Übergabe
- [ ] Notion-Template für Deployment-Ansicht bauen
- [ ] Link-Übergabe statt Excel

## Entscheidungen

| Entscheidung | Begründung |
|---|---|
| **Salesforce = Langfristiges Daten-Backbone** | Nicht nur Notion — SF als primäres System of Record |
| **Tally = DSGVO-konform** | Geeignet für Praxisstruktur-Daten; keine Patientendaten betroffen |
| **Dust = interne KI-Plattform** | Für die KEB-Generierung aus strukturierten SF-Daten |
| **Excel-KEB = abgelöst** | Vollständig ersetzt, nicht optimiert |

## Nächster Schritt (gemäß Quelldokument)

**Offene Entscheidung:** Zuerst die Tally-Formularstruktur aufbauen ODER zuerst den Dust Agent Prompt schreiben?

→ **Empfehlung im Quelldokument:** Tally zuerst — der Input definiert den Output. Ohne Feldstruktur kann kein sinnvoller Dust Prompt geschrieben werden.

## Bezug zur bestehenden Entitätsseite

Die bestehende Entitätsseite [[DoktorLib Automation Pipeline]] (erstellt 2026-06-13) enthielt nur begrenzte Details — sie erwähnte lediglich „Tally Form oder Dust Agent" als in Betracht gezogene Technologieoptionen, ohne die vollständige Architektur. Dieses Quelldokument zeigt:

- Der Stack ist **keine** Wahl zwischen Tally und Dust — **beide werden verwendet**, in unterschiedlichen Phasen
- **Make** und **Salesforce** sind ebenfalls zentrale Komponenten (zuvor nicht erfasst)
- **Notion** dient als sekundäre Projektmanagement-Ebene
- Die Pipeline ersetzt ein konkretes Artefakt: den **Excel-KEB (Kundenerfassungsbogen)**
- Der IT-Partner hat ein **separates Tally-Audit-Formular** (zweites Formular, nicht nur eines)

> ⚠️ **Teilweiser Widerspruch zur bestehenden Entität:** Die bestehende Entitätsseite [[DoktorLib Automation Pipeline]] beschrieb Tally und Dust als „in Betracht gezogene Technologieoptionen" und implizierte eine Wahl zwischen beiden. Das Quelldokument zeigt, dass sie **komplementäre Werkzeuge in verschiedenen Phasen** einer einzigen Pipeline sind. Entitätsseite wurde entsprechend aktualisiert.

## Verwandte Seiten

- [[DoktorLib Automation Pipeline]] — Entitätsseite (aktualisiert)
- [[DoktorLib]] — Unternehmenskontext
- [[Oleg Personal Context]] — Projektverantwortlicher
- [[MOC Strategie und Business]] — als aktives Projekt gelistet
- [[MOC Tech und Setup]] — technischer Stack-Kontext
- [[Tally]] — Formular-Builder-Tool
- [[Make]] — Automation-Middleware
- [[Salesforce]] — Daten-Backbone
- [[Notion]] — Projektplanungs-Ebene
- [[Dust Agent]] — KI-KEB-Generator
- [[Kundenerfassungsbogen]] — das zu automatisierende Artefakt