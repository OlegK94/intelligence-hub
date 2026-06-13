---
title: Insolvenzprüfung
type: concept
tags: [insolvenz, recht, gmbh, ug, geschaeftsfuehrer, haftung, insolvenzantragspflicht, paragraf17, paragraf19, inso, germany]
sources: ["raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md"]
created: 2026-06-10
updated: 2026-06-10
summary: German insolvency law concepts relevant to GmbH/UG management — §17 InsO (Zahlungsunfähigkeit), §19 InsO (Überschuldung), 21-day filing obligation, and personal liability risks for Geschäftsführer
---

# Insolvenzprüfung — Deutsches Insolvenzrecht

## Overview

Die Insolvenzprüfung ist für [[Oleg Personal Context|Oleg Kober]] als Geschäftsführer der [[Wagglz GmbH]] und der [[OK Capital UG]] eine rechtliche Pflicht. Dieses Konzept-Dokument erläutert die relevanten deutschen Insolvenztatbestände.

## Die zwei Insolvenztatbestände

### § 17 InsO — Zahlungsunfähigkeit

**Definition:** Eine Gesellschaft ist zahlungsunfähig, wenn sie nicht in der Lage ist, fällige Zahlungsverpflichtungen zu erfüllen.

**Schwellenwert (Rechtsprechung):**
- Dauerhaft (>3 Wochen) unfähig
- Liquiditätslücke >10% der Gesamtverbindlichkeiten

**Prüfung:**
```
Liquide Mittel (Bankguthaben + kurzfristig liquidierbare Assets)
────────────────────────────────────────────────────────────────
Fällige Verbindlichkeiten (innerhalb 3 Wochen)

Ratio < 90% → Zahlungsunfähigkeit anzunehmen
```

**Besonderheit:** Zahlungsstockung (temporäre Liquiditätslücke <3 Wochen) ist kein Insolvenztatbestand.

### § 19 InsO — Überschuldung

**Definition:** Eine Gesellschaft ist überschuldet, wenn ihr Vermögen die Verbindlichkeiten nicht mehr deckt UND die Fortführungsprognose negativ ist.

**Zweistufige Prüfung:**
1. **Stufe 1 — Bilanzielle Überschuldung:** Eigenkapital negativ?
2. **Stufe 2 — Fortführungsprognose:** Ist der Fortbestand des Unternehmens überwiegend wahrscheinlich?

```
Wenn EK < 0 UND Fortführungsprognose negativ → Überschuldung (§ 19 InsO)
Wenn EK < 0 ABER Fortführungsprognose positiv → (noch) kein Insolvenztatbestand
```

**Wichtig:** Gesellschafterdarlehen mit **Rangrücktritt** (eigenkapitalähnlich) werden bei der Überschuldungsprüfung nicht als Verbindlichkeit gewertet — dies ist steuerlich und insolvenzrechtlich bedeutsam.

## Insolvenzantragspflicht

### Frist
- **21-Tage-Frist** ab Eintritt der Insolvenzreife (Zahlungsunfähigkeit ODER Überschuldung)
- Seit COVID-Reformen (SanInsFoG 2021): Bei Überschuldung 6 Wochen, bei Zahlungsunfähigkeit 3 Wochen

### Pflicht des Geschäftsführers
- Ohne schuldhaftes Zögern Insolvenzantrag beim zuständigen Amtsgericht stellen
- Verstoß: **Persönliche Haftung** des Geschäftsführers
- Mögliche Strafbarkeit (§ 15a InsO)

### Zuständiges Gericht
- Berlin: Amtsgericht Charlottenburg (Insolvenzabteilung)

## Geschäftsführer-Haftung

### Insolvenzreife-Haftung (§ 15b InsO)
Zahlungen nach Eintritt der Insolvenzreife müssen vom Geschäftsführer **persönlich erstattet** werden — auch wenn die Zahlungen im normalen Geschäftsbetrieb erfolgten.

### Anfechtungsrisiko
- Zahlungen an **Gesellschafter** (z.B. Gesellschafterdarlehen-Rückzahlungen) in den letzten **10 Jahren** vor Insolvenz können angefochten werden (§ 135 InsO)
- Zahlungen an **Dritte** in den letzten **3 Monaten** vor Insolvenz: anfechtbar (§ 130 InsO)

### Persönliche Durchgriffshaftung
- Normalerweise schützt die GmbH/UG-Struktur vor persönlicher Haftung
- Ausnahmen: Insolvenzverschleppung, sittenwidrige Schädigung, formlose Mischung Privat/Gesellschaft

## Relevanz für Oleg

| Gesellschaft | Risikofaktor | Status |
|---|---|---|
| [[Wagglz GmbH]] | Keine erkennbaren Einnahmen, VW-Kredit-Finanzierung | 🟡 Zu prüfen |
| [[OK Capital UG]] | Dormant, aber laufende Pflichten | 🟡 Zu prüfen |

### Besonderes Risiko: VW-Bank-Kredit-Fluss
Der Kapitalzufluss in die Wagglz GmbH über den persönlichen VW-Bank-Kredit könnte bei späterer Insolvenz der GmbH steuerlich und insolvenzrechtlich geprüft werden:
- **War es ein Gesellschafterdarlehen?** → Eigenkapitalersatz-Regeln (§ 39 InsO)
- **War es eine verdeckte Einlage?** → Steuerliche Konsequenzen
- **Anfechtbarkeit?** → Bei Insolvenz innerhalb von 10 Jahren

## Handlungsoptionen bei Insolvenzreife

| Option | Beschreibung | Empfohlen wenn |
|---|---|---|
| **Sanierung** | Restrukturierung, Kapitalerhöhung | Fortführungsprognose positiv |
| **Eigenverwaltung** | Schuldner bleibt Verwalter (§ 270 InsO) | Frühzeitige Einleitung |
| **Regelinsolvenz** | Externer Insolvenzverwalter | Standard |
| **Liquidation** | Geordnete Abwicklung vor Insolvenzreife | Falls noch liquide |

## Related Pages

- [[Wagglz GmbH]] — primäre Gesellschaft
- [[OK Capital UG]] — zweite Gesellschaft
- [[Oleg Personal Context]] — Geschäftsführer
- [[Oleg Financial Situation]] — Finanzsituation
- [[Gesellschafterdarlehen]] — Finanzierungsinstrument mit Insolvenzrelevanz
- [[Master Prompt Gesamtfinanzanalyse]] — Analyse-Prompt
