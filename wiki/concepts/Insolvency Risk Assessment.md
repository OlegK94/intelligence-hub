---
title: "Insolvency Risk Assessment"
type: concept
tags: [insolvency, risk, §17-insol, §19-insol, zahlungsunfähigkeit, überschuldung, 21-tage-frist, geschäftsführer-haftung, audit]
sources: ["raw/raw/Privat/Finanzen/Master Prompt – Gesamtanalyse.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Deutsches Insolvenzrecht-Rahmenwerk zur Bewertung von Zahlungsunfähigkeit (§17 InsO) und Überschuldung (§19 InsO); Antragspflicht greift innerhalb 21-Tage-Frist bei Insolvenzreife; Geschäftsführer-Haftung für Zahlungen nach dieser Frist; Framework für Wagglz GmbH + OK Capital UG Audit
---

# Insolvency Risk Assessment

## Überblick

Das **Insolvency Risk Assessment** ist ein strukturiertes Framework zur Bewertung des Insolvenzrisikos einer Gesellschaft gemäß deutschem Insolvenzordnung ([[InsO]]). Es wird in der [[Master Prompt — Gesamtfinanzanalyse]] als **Analyseschritt 1** priorisiert und richtet sich insbesondere auf:

1. [[Wagglz GmbH]] — Gesellschaft mit strukturellem Defizit, Verlustvortrag ~€150k
2. [[OK Capital UG]] — Kapitalverbrauchende Gesellschaft ohne Rückfluss

---

## Rechtliche Grundlagen

### § 17 InsO — Zahlungsunfähigkeit

Eine Gesellschaft ist **zahlungsunfähig**, wenn sie nicht in der Lage ist, ihre Verbindlichkeiten zu erfüllen, die fällig sind:

- **Fokus:** Liquiditätssituation (Cash-Realität)
- **Frage:** Kann die Gesellschaft ihre Rechnungen zahlen?
- **Beweis:** Kontoauszüge, BWA-Liquiditätsspalte, Analyse von Zahlungsverzögerungen

### § 19 InsO — Überschuldung

Eine Gesellschaft ist **überschuldet**, wenn das bilanzielle Eigenkapital negativ ist:

- **Fokus:** Bilanzielle Vermögenslage
- **Frage:** Ist die Bilanz-Passivseite größer als die Aktivseite?
- **Beweis:** Jahresabschluss, Bilanz, Eigenkapitalkonto
- **Zusatz:** Wenn überschuldet, Fortführungsprognose prüfen (Kann sich Unternehmen erholen?)

### § 21 InsO — Antragspflicht (21-Tage-Frist)

Wenn ein Geschäftsführer Zahlungsunfähigkeit oder Überschuldung feststellt, muss er:
- Innerhalb von **21 Tagen** einen Insolvenzantrag stellen, ODER
- Glaubhaft machen, dass das Unternehmen wieder solvent wird (Sanierungsprognose)

**Konsequenzen bei Verzug:**
- Persönliche Haftung des GF für Schäden an Gläubigern
- Anfechtung von Zahlungen, die nach Insolvenzreife geleistet wurden (§ 130 InsO)

---

## Assessment-Struktur

### Schritt 1: Zahlungsunfähigkeit (§17)-Prüfung

| Kriterium | Frage | Datenbasis |
|---|---|---|
| **Liquidität** | Hat die Gesellschaft genügend Barreserven? | Kontoauszüge, Tagesgeld |
| **Fällige Verbindlichkeiten** | Welche Schulden sind überfällig? | Rechnungen, Mahnaruf, BWA |
| **Cashflow-Prognose** | Kann die nächsten 12 Monate Rechnungen zahlen? | BWA, Provisionskalender, Kundenverträge |
| **Gesamtbewertung** | GRÜN: Liquid; GELB: Angespannt; ROT: Nicht zahlungsfähig | Aggregation aller Faktoren |

### Schritt 2: Überschuldung (§19)-Prüfung

| Kriterium | Frage | Datenbasis |
|---|---|---|
| **Eigenkapital** | Ist das Eigenkapital positiv oder negativ? | Jahresabschluss (Bilanz) |
| **Trend** | Wird das Eigenkapital besser oder schlechter? | Mehrjahrs-Bilanzvergleich |
| **Fortführungsprognose** | Kann sich das EK wieder positiv entwickeln? | Gewinn-/Verlustprognose 12–24 Monate |
| **Gesamtbewertung** | GRÜN: Positiv EK, stabil; GELB: Negativ EK, Sanierungshoffnung; ROT: Negativ EK, aussichtslos | Aggregation |

### Schritt 3: Antragspflicht-Prüfung (§21)

| Situation | Aktion | Deadline |
|---|---|---|
| Zahlungsunfähigkeit ODER Überschuldung UND keine Sanierungsprognose | Insolvenzantrag stellen | 21 Tage nach Feststellung |
| Zahlungsunfähigkeit ODER Überschuldung ABER glaubhafte Sanierungsprognose | Sanierungsplan vorlegen (Alternative zu Antrag) | 21 Tage |
| Keine Zahlungsunfähigkeit, Eigenkapital positiv | Keine Antragspflicht | — |

### Schritt 4: GF-Haftungsrisiko-Prüfung

| Risiko | Faktoren |
|---|---|
| **Persönliche Haftung** | Hat GF Zahlungen nach Insolvenzreife geleistet, ohne Antrag zu stellen? → persönliche Schadensersatzpflicht gegenüber Gläubigern |
| **Anfechtungsrisiko** | Welche Zahlungen wurden in den letzten 3 Jahren getätigt? Waren sie anfechtbar nach §130 InsO? |
| **Dokumentation** | Hat GF die Insolvenzreife dokumentiert? (E-Mail an Steuerberater zählt als Beweis) |

---

## Anwendung auf Wagglz GmbH + OK Capital UG

Beide Gesellschaften müssen gegen dieses Framework bewertet werden:

| Gesellschaft | §17 Status? | §19 Status? | Antragspflicht 21-Tage? | GF-Haftungsrisiko? |
|---|---|---|---|---|
| **Wagglz GmbH** | ⏳ Ausstehend (Kontoauszüge erforderlich) | ⏳ Ausstehend (Jahresabschluss erforderlich) | ? | ? |
| **OK Capital UG** | ⏳ Ausstehend (Kontoauszüge erforderlich) | ⏳ Ausstehend (Jahresabschluss erforderlich) | ? | ? |

Detaillierte Auditierung erfolgt durch den [[Master Prompt — Gesamtfinanzanalyse]].

---

## Verwandte Seiten

- [[Master Prompt — Gesamtfinanzanalyse]] — primärer Audit-Prompt, nutzt diesen Framework
- [[Wagglz GmbH]] — Gesellschaft 1, zu audieren
- [[OK Capital UG]] — Gesellschaft 2, zu audieren
- [[Rehabilitation Plan]] — Strategische Optionen nach negativem Audit
- [[Oleg Personal Context|Oleg Kober]] — Geschäftsführer (persönliche Haftung)
- [[00 Finanz-Übersicht]] — Kontextuelle Finanzlage
- [[Verlustvortrag]] — Relevanz für Überschuldungsprognose (Steuerliche Gewinne möglich?)
