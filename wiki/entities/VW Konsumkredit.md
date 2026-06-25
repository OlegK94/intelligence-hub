---
title: VW Konsumkredit
type: entity
tags: [kredit, schulden, finanzen, vw-bank, konsumkredit, ausgaben, sondertilgung, check24]
sources: ["raw/Privat/Finanzen/Ausgaben/VW Konsumkredit.md"]
created: 2026-06-12
updated: 2026-06-12
summary: VW Bank Konsumkredit — 50.000 € Darlehen, 84 Monate Laufzeit (Nov 2021–Nov 2028), Rate 681,57 €/Monat, Restschuld 18.858 € per Jun 2026; kein Autokredit; Sondertilgung aus Q-Bonus prüfen
---

# VW Konsumkredit

## Overview

Der **VW Bank Konsumkredit** ist ein allgemeiner Konsumkredit (kein Autokredit) bei der [[VW Bank GmbH]], vermittelt über CHECK24. Er zählt zu den laufenden Verbindlichkeiten von [[Oleg Personal Context|Oleg]] und erscheint in der [[Fixkosten Übersicht]] als monatliche Belastung.

> ⚠️ Kein Autokredit — allgemeiner Konsumkredit.

## Konditionen

| Parameter | Wert |
|---|---|
| **Darlehensbetrag** | 50.000 € |
| **Laufzeit** | 84 Monate |
| **Beginn** | November 2021 |
| **Ende** | November 2028 |
| **Rate** | 681,57 €/Monat |
| **Restschuld (Jun 2026)** | **18.858 €** |
| **Vermittlung** | CHECK24 |
| **Gläubiger** | VW Bank GmbH |
| **IBAN Gläubiger** | DE39270200000096123711 |
| **Abbuchung** | 16. des Monats |

## Restlaufzeit (Stand Jun 2026)

- **Monate verbleibend:** ~28 (bis Nov 2028)
- **Verbleibende Zahllast:** ~28 × 681,57 € = **~19.084 €** (nominal)
- **Restschuld:** 18.858 € → impliziert noch ~226 € Zinsen über Restlaufzeit

> ⚠️ **Assumption [A]:** Die genaue Zinsstruktur (Effektivzins, verbleibende Zinslast) ist aus der Quelle nicht ersichtlich. Der Effektivzins wurde bei Abschluss November 2021 vereinbart — in einer Niedrigzinsphase. Der tatsächliche Zinsaufwand der Restlaufzeit muss aus dem Kreditvertrag entnommen werden.

## Sondertilgung — Entscheidungsanalyse

### Hintergrund

Als offene Aufgabe ist dokumentiert, den **Q-Bonus (8.250 € netto)** als mögliche Teilrückzahlung zu prüfen.

### Entscheidungskriterien

| Faktor | Analyse |
|---|---|
| **Sondertilgungsklausel** | Muss im Vertrag geprüft werden — nicht alle Konsumkredite erlauben vorzeitige Rückzahlung ohne Vorfälligkeitsentschädigung |
| **Zinsersparnis** | Abhängig vom Effektivzins des Kredits vs. Alternativrendite (Tagesgeld 1%) |
| **Tagesgeld-Vergleich** | Bei Kreditkosten > 1% p.a. Effektivzins → Sondertilgung ist besser als Tagesgeld |
| **Liquiditätspuffer** | Q-Bonus als Vollrückzahlung würde Liquidität reduzieren — Teilrückzahlung sinnvoller |

### Empfohlene Vorgehensweise

- [ ] Kreditvertrag auf Sondertilgungsklausel prüfen
- [ ] Effektivzins mit Tagesgeld (1%) vergleichen
- [ ] Entscheidung: Q-Bonus (8.250 €) als Sondertilgung oder Tagesgeld/Investition?
- [ ] **Deadline Prüfung:** 2026-09-01

> **Kontext:** Der [[Q-Bonus Doctolib]] beträgt 8.250 € netto. Bei einer Restschuld von 18.858 € würde eine Sondertilgung von 8.250 € die Restschuld auf ~10.608 € reduzieren — mit entsprechend gekürzter Restlaufzeit oder reduzierter Monatsrate (je nach Vertragsbedingungen).

## Einordnung in Gesamtfinanzen

| Kontext | Wert |
|---|---|
| Monatliche Rate in [[Fixkosten Übersicht]] | 681,57 €/Mo |
| Anteil an Fixkosten gesamt | Einer der größten Einzelposten |
| Restschuld vs. Liquide Mittel | Restschuld 18.858 € >> Consorsbank Saldo 971,67 € |
| Tilgungsende | November 2028 |

## Related Pages

- [[VW Konsumkredit Source Detail]] — Quelldokument
- [[Fixkosten Übersicht]] — Monatsrate in Fixkostenplanung
- [[MOC Finanzen]] — übergeordneter Finanz-MOC
- [[Q-Bonus Doctolib]] — mögliche Sondertilgungsquelle
- [[Consorsbank Girokonto 0250120493]] — Hauptkonto (Abbuchungsquelle unklar)
- [[Schulden Übersicht]] — Gesamtschuldenkontext
- [[Oleg Personal Context]] — Kreditnehmer
