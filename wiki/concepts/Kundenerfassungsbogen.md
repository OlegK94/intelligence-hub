---
title: Kundenerfassungsbogen
type: concept
tags: [doktorlib, document, onboarding, deployment, keb, automation, process]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Der KEB — DoktorLibs Kundenerfassungsdokument, das beim Deployment verwendet wird; aktuell ein manuell ausgefülltes Excel, das durch den KI-generierten Output der Dust-Agent-Pipeline ersetzt wird
---

# Kundenerfassungsbogen (KEB)

## Überblick

Der **Kundenerfassungsbogen** (KEB) ist das formale Dokument von [[DoktorLib]], das alle wesentlichen Kundendaten erfasst, die für das Deployment ihrer Praxissoftware in einer Arztpraxis erforderlich sind. Er ist das zentrale Übergabe-Artefakt vom Vertrieb an das Deployment-Team.

## Aktueller Stand (Problem)

- **Format:** Manuell ausgefüllte Excel-Tabelle
- **Prozess:** Vertriebsmitarbeiter trägt Daten aus verschiedenen Touchpoints ein (Demo-Call, Discovery-Notizen, IT-Audit)
- **Probleme:**
  - Fehleranfällig (manuelle Eingabe)
  - Keine einheitliche Datenquelle
  - Deployment-Team arbeitet mit einer statischen Datei (keine Live-Updates)
  - Keine Verbindung zu Salesforce und Notion

## Zielzustand (Zukunft)

Mit der [[DoktorLib Automation Pipeline]]:

```
Vertragsunterzeichnung (trigger)
    ↓
[DUST AGENT] reads all Salesforce data
    ↓
KEB generated automatically in standard format
    ↓
Deployment accesses via Notion link (no Excel)
```

- **Format:** Automatisch generiert vom [[Dust Agent]] auf Basis von [[Salesforce]]-Daten
- **Zugriff:** Das Deployment-Team erhält einen [[Notion]]-Link
- **Datenquelle:** Einzelner, aktueller, vernetzter Datensatz

## KEB-Feldstruktur

Stand Quelldokument (2026-05-08): **noch zu definieren**. Die Felddefinition ist eine Voraussetzung für den Dust-Agent-Prompt — er kann nicht geschrieben werden, ohne zu wissen, was der KEB enthalten muss.

Erwartete Feldkategorien basierend auf Tally-Eingabefeldern:
- Praxistyp
- Fachrichtung
- Aktuelle Software
- Labore
- IT-Infrastruktur
- Gerätelandschaft
- Discovery Notes (aus dem Demo-Call)
- IT-Audit-Daten (vom IT-Partner)

## Strategische Bedeutung

Der KEB ist das **Artefakt, das definiert, welche Daten entlang der gesamten Pipeline erfasst werden müssen**. Seine Feldstruktur legt fest:
- Was das Tally-Intake-Formular abfragen muss
- Was das IT-Audit-Tally-Formular erfassen muss
- Was der Dust-Agent-Prompt generieren muss

Deshalb empfiehlt die Quelle, **zuerst die Tally-Felder zu definieren** — die Ausgabestruktur des KEBs sollte die Eingabestruktur bestimmen.

## Verwandte Seiten

- [[DoktorLib Automation Pipeline]] — Pipeline, die den manuellen KEB ersetzt
- [[DoktorLib Automation Pipeline Source Detail]] — vollständige Quelle
- [[Dust Agent]] — Tool, das den KEB automatisch generiert
- [[Salesforce]] — Datenquelle für die KEB-Generierung
- [[Notion]] — Bereitstellungsmedium (Link ersetzt Excel)
- [[Tally]] — Datenerfassung als Grundlage des KEBs
- [[DoktorLib]] — Organisationskontext