---
title: Dust Agent
type: concept
tags: [tool, AI, LLM, automation, doktorlib, keb, knowledge-management, tech-stack]
sources: ["raw/01-Strategie-Business/DoktorLib Automation Pipeline.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Interne KI-Plattform (Dust.tt), die in der DoktorLib-Pipeline als KEB-Generator eingesetzt wird — liest Salesforce-Daten und generiert automatisch den Kundenerfassungsbogen
---

# Dust Agent

## Übersicht

**Dust** (dust.tt) ist eine interne KI-Plattform zum Aufbau von KI-Agenten, die mit Unternehmensdaten verbunden sind. In der [[DoktorLib Automation Pipeline]] fungiert ein Dust Agent als **KEB-Generator** (Phase 3): Er liest alle Salesforce-Daten eines bestimmten Kunden und generiert automatisch den [[Kundenerfassungsbogen]] (KEB) — als Ersatz für den manuellen Excel-basierten Prozess.

## Rolle in der DoktorLib-Pipeline

### Position in der Pipeline

```
Vertragsunterzeichnung (Contract Signed)
    ↓ (trigger)
[DUST AGENT]
    ← reads: [SALESFORCE] (all customer data)
    → outputs: KEB (standard format)
    ↓
Deployment erhält Notion-Link (kein Excel)
```

### Funktionsweise

1. **Input:** Liest alle strukturierten Salesforce-Daten des unterzeichnenden Kunden (befüllt aus Tally-Intake + IT-Audit + manuellen Discovery-Notizen)
2. **Verarbeitung:** LLM-basierte Generierung mithilfe eines individuellen Prompts (noch zu erstellen)
3. **Output:** KEB im Standardformat — ersetzt das manuell ausgefüllte Excel

## Warum Dust (im Vergleich zu anderen KI-Tools)

- Als **interne KI-Plattform** bei DoktorLib vorgesehen
- Ausgelegt für die Verbindung von KI-Agenten mit unternehmensinternen Datenquellen
- Kann so konfiguriert werden, dass Salesforce als Datenquelle eingebunden wird
- Ermöglicht strukturierte Ausgabegenerierung aus strukturierten Daten

## Aufbaustatus (Offene Punkte)

- [ ] Dust Agent Prompt schreiben (write the prompt)
- [ ] Input: Salesforce-Datenstruktur für den Agenten definieren
- [ ] Output: KEB-Feldstruktur definieren („noch zu definieren" — not yet defined)
- [ ] Trigger: Vertragsunterzeichnung (manuell ODER automatisch via SF Stage-Change)

## Wichtiger Hinweis zur Reihenfolge

Das Quelldokument empfiehlt ausdrücklich:
> **Zuerst Tally, dann Dust Prompt** — ohne Kenntnis der Tally-Feldstruktur (Input) kann kein sinnvoller Dust Prompt geschrieben werden. Der Input bestimmt den Output.

Dies ist die Begründung dafür, dass Phase 1 (Tally) der Phase 3 (Dust Agent) in der Aufbaureihenfolge vorausgeht.

## Bezug zur bestehenden Wiki

Die Entitätsseite der [[DoktorLib Automation Pipeline]] beschrieb Dust zuvor als eine von zwei Tool-Optionen (neben Tally). Diese Quelle stellt klar, dass Dust ein **separates Tool einer späteren Phase** ist — keine Alternative zu Tally.

## Verwandte Seiten

- [[DoktorLib Automation Pipeline]] — Pipeline-Kontext
- [[DoktorLib Automation Pipeline Source Detail]] — vollständige Quelle
- [[Salesforce]] — Datenquelle, aus der Dust liest
- [[Kundenerfassungsbogen]] — Artefakt, das Dust generiert
- [[Tally]] — vorgelagerte Datenerfassung (definiert den Input von Dust)
- [[DoktorLib]] — Organisationskontext
- [[Claude Projects Setup|Claude Projects Setup]] — Vergleich: ein weiteres KI-Tool in Olegs Stack