---
title: Gesellschafterdarlehen
type: concept
tags: [steuer, finanzen, gmbh, ug, darlehen, gesellschafter, eigenkapitalersatz, verdeckte-einlage, insolvenz, rangruecktritt]
sources: ["raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md"]
created: 2026-06-10
updated: 2026-06-10
summary: Gesellschafterdarlehen (shareholder loans) — legal and tax concept for loans from shareholders to their GmbH/UG; relevant for Oleg's ~357 €/mo transfers from personal account to Wagglz GmbH and OK Capital UG; covers Rangrücktritt, eigenkapitalersetzend, verdeckte Einlage risk
---

# Gesellschafterdarlehen

## Overview

Ein **Gesellschafterdarlehen** ist ein Darlehen, das ein Gesellschafter (Anteilseigner) an seine Gesellschaft (GmbH, UG) vergibt — anstelle einer Eigenkapitalerhöhung. Es ist ein häufiges Finanzierungsinstrument für kleine GmbHs, bringt aber steuerliche und insolvenzrechtliche Besonderheiten mit sich.

## Relevanz für Oleg

[[Oleg Personal Context|Oleg]] transferiert monatlich **~357 €** von seinem Privatkonto an seine Unternehmensstrukturen ([[Wagglz GmbH]], [[OK Capital UG]]). Der Prompt kategorisiert dies als "laufende Gesellschafterdarlehen Privat → Unternehmen."

## Arten und Abgrenzung

### Echtes Darlehen
- Rückzahlungsanspruch des Gesellschafters gegenüber der Gesellschaft
- Fremdkapital in der Bilanz
- Verzinsung möglich (marktüblicher Zinssatz erforderlich)
- Rückzahlbar bei Liquidität

### Verdeckte Einlage (steuerlich problematisch)
- Wenn ein Gesellschafter der Gesellschaft Mittel zuführt **ohne** angemessene Gegenleistung
- Steuerrechtlich: Erhöhung der Anschaffungskosten der Beteiligung
- Risiko: Wenn die Darlehen nicht marktüblich verzinst und dokumentiert sind

### Eigenkapitalersetzend (insolvenzrechtlich relevant)
- Wenn Gesellschafterdarlehen in der **Krise** der Gesellschaft gegeben werden
- Seit MoMiG 2008 (§ 39 Abs. 1 Nr. 5 InsO): Gesellschafterdarlehen sind im Insolvenzfall **immer nachrangig** gegenüber anderen Gläubigern
- Kein expliziter "Eigenkapitalersatz" mehr notwendig — automatische Nachrangigkeit

## Insolvenzrechtliche Konsequenzen (§ 39 InsO)

```
Insolvenzfall:
Erste Befriedigung:  Bevorrechtete Gläubiger (§ 54 InsO)
Danach:              Gewöhnliche Insolvenzgläubiger (§ 38 InsO)
Zuletzt:             Nachrangige Gläubiger — inkl. ALLE Gesellschafterdarlehen (§ 39 InsO)
```

**Praktisch:** Im Insolvenzfall ist die Rückzahlung von Gesellschafterdarlehen sehr unwahrscheinlich.

### Anfechtungsrisiko (§ 135 InsO)
- Rückzahlungen von Gesellschafterdarlehen innerhalb von **10 Jahren** vor Insolvenzantrag sind **anfechtbar**
- Der Insolvenzverwalter kann diese Zahlungen zurückfordern
- Dies gilt auch für Zinszahlungen auf Gesellschafterdarlehen

## Rangrücktritt

Ein **Rangrücktritt** ist eine vertragliche Vereinbarung, bei der der Gesellschafter erklärt, seine Darlehensforderung hinter alle anderen Gläubiger zurückzustellen (auch hinter einfache Insolvenzgläubiger). 

### Bedeutung für Überschuldungsprüfung (§ 19 InsO)
- Gesellschafterdarlehen **mit** qualifiziertem Rangrücktritt → werden **nicht** als Verbindlichkeit in der Überschuldungsbilanz gewertet
- Gesellschafterdarlehen **ohne** Rangrücktritt → sind Verbindlichkeiten → können zur Überschuldung beitragen

> ⚠️ **Für Oleg kritisch:** Sind die laufenden Transfers (~357 €/Mo) formal als Darlehen dokumentiert? Gibt es Rangrücktrittsvereinbarungen? Dies ist eine der Kernanforderungen in der Dokumenten-Checkliste des Prompts.

## Steuerliche Aspekte

### Verzinsung
- Gesellschafterdarlehen müssen marktüblich verzinst sein, sonst:
  - Verdeckte Gewinnausschüttung (vGA) an den Gesellschafter (wenn zu hoch)
  - Verdeckte Einlage (wenn unverzinst oder zu niedrig verzinst)

### Verlustverrechnung
- Wenn die Darlehen **ausfallen** (Gesellschaft kann nicht zurückzahlen), ist dies für Oleg privat:
  - Bei GmbH-Beteiligung: Verlust aus §17 EStG (Veräußerungsverlust)
  - Darlehensverlust: Nach BFH-Rechtsprechung eingeschränkt absetzbar
  - **Nicht** einfach gegen laufendes Einkommen verrechenbar

## Optimierungsoptionen (zu prüfen mit Steuerberater)

1. **Formalisierung:** Darlehensvertrag mit Zinssatz + Rückzahlungsplan abschließen
2. **Rangrücktritt:** Qualifizierter Rangrücktritt zur Verbesserung der Überschuldungsbilanz
3. **Umwandlung:** Darlehen in Eigenkapital umwandeln (Kapitalerhöhung)
4. **Abschreibung:** Darlehensverlust steuerlich geltend machen (eingeschränkt)

## Related Pages

- [[Wagglz GmbH]] — Darlehensempfängerin
- [[OK Capital UG]] — Darlehensempfängerin
- [[Oleg Personal Context]] — Darlehensgeber
- [[Oleg Financial Situation]] — Finanzkontext
- [[Insolvenzprüfung]] — insolvenzrechtlicher Kontext
- [[Master Prompt Gesamtfinanzanalyse]] — Analyse-Prompt Source
