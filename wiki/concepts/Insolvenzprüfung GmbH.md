---
title: "Insolvenzprüfung GmbH"
type: concept
tags: [insolvenz, gmbh, ug, §17-inso, §19-inso, §15a-inso, zahlungsunfähigkeit, überschuldung, antragspflicht, geschäftsführer, haftung, wagglz, ok-capital]
sources: ["raw/raw/Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md"]
created: 2026-06-20
updated: 2026-06-20
summary: Konzeptseite zur Insolvenzprüfung für GmbH/UG-Geschäftsführer nach deutschem Insolvenzrecht — §17 InsO (Zahlungsunfähigkeit), §19 InsO (Überschuldung mit Fortführungsprognose), §15a InsO (21-Tage-Antragspflicht); persönliche Haftungsrisiken; Anfechtung von Zahlungen nach Insolvenzreife; direkt relevant für Wagglz GmbH und OK Capital UG
---

# Insolvenzprüfung GmbH

## Überblick

Die **Insolvenzprüfung** für Kapitalgesellschaften (GmbH, UG) ist ein gesetzlich definierter Prüfungsprozess, den der **Geschäftsführer** laufend durchführen muss. Bei Vorliegen der gesetzlichen Tatbestände besteht eine **Insolvenzantragspflicht**. Diese Konzeptseite beschreibt die relevanten gesetzlichen Grundlagen, direkt angewandt auf die Situation von [[Oleg Personal Context|Oleg]] als GF der [[Wagglz GmbH]] und Inhaber der [[OK Capital UG]].

> Zur vollständigen Analyse-Methodik und dem Claude-Prompt, der diese Prüfung enthält, siehe [[Master Prompt Gesamtfinanzanalyse]] und [[Gesamtfinanzanalyse Methodik]].

---

## Die drei Insolvenztatbestände

### 1. Zahlungsunfähigkeit — § 17 InsO

**Definition:** Die Gesellschaft ist nicht in der Lage, ihre fälligen Zahlungspflichten zu erfüllen.

**Prüfschema:**
```
Fällige Verbindlichkeiten > Verfügbare Liquidität (inkl. kurzfristig verfügbare Mittel)?
→ JA + Lücke > 10% + nicht schließbar innerhalb 3 Wochen = ZAHLUNGSUNFÄHIG
```

**Relevante Indikatoren für Wagglz GmbH / OK Capital UG:**
- Kontostand der Gesellschaft (aus Kontoauszügen Geschäftskonto)
- Offene Verbindlichkeiten gegenüber Lieferanten, Finanzamt (KSt, GewSt, USt)
- Fällige Jahresabschluss-Erstellungskosten (5.000 € aktuell)
- Laufende Fixkosten vs. Einnahmen

**Abgrenzung: Zahlungsunwilligkeit ≠ Zahlungsunfähigkeit**
- Wenn Mittel vorhanden, aber Zahlung verweigert wird → keine InsO-Tatbestand
- Wenn Mittel objektiv fehlen → § 17 InsO erfüllt

---

### 2. Überschuldung — § 19 InsO

**Definition:** Vermögen der Gesellschaft deckt bestehende Verbindlichkeiten nicht mehr (negatives Eigenkapital) **UND** Fortführungsprognose ist negativ.

**Zweistufige Prüfung:**

**Stufe 1 — Ist das bilanzielle Eigenkapital negativ?**
```
Aktiva (Buchwerte / Verkehrswerte) < Passiva (Verbindlichkeiten)
→ Eigenkapital negativ = Überschuldungsverdacht
```

**Stufe 2 — Fortführungsprognose**
```
Kann die Gesellschaft in den nächsten 12 Monaten fortgeführt werden?
→ Positive Prognose: Überschuldung begründet KEINE Antragspflicht
→ Negative Prognose: Antragspflicht besteht
```

> **Praxishinweis:** Die **Fortführungsprognose** ist entscheidend. Viele Start-ups haben negatives Eigenkapital, aber solange eine realistische positive Fortführungsprognose besteht (neue Finanzierungsrunde, konkrete Aufträge, Gesellschafterdarlehen mit Rangrücktritt), entsteht keine Antragspflicht. Für [[Wagglz GmbH]] hängt dies maßgeblich davon ab, ob Olegs laufende Gesellschafterdarlehen (~357 €/Mo) als Rangrücktritt ausgestaltet sind.

**Gesellschafterdarlehen und Rangrücktritt:**
- Ohne Rangrücktritt: Darlehen ist eine reguläre Verbindlichkeit → erhöht die Passiva → verschlechtert die Überschuldungsbilanz
- Mit Rangrücktritt: Darlehen wird wie Eigenkapital behandelt → reduziert effektive Verbindlichkeiten → verbessert die Überschuldungsbilanz
- Der [[Master Prompt Gesamtfinanzanalyse]] fragt explizit, ob Rangrücktritte in den Darlehensverträgen vorhanden sind

---

### 3. Drohende Zahlungsunfähigkeit — § 18 InsO

**Definition:** Die Gesellschaft wird voraussichtlich nicht in der Lage sein, ihre bestehenden Zahlungspflichten im Zeitpunkt der Fälligkeit zu erfüllen.

**Wichtig:** Drohende Zahlungsunfähigkeit begründet **kein Recht** auf Insolvenzantrag für den Gläubiger und **keine Pflicht** für den GF — aber sie gibt dem Schuldner ein freiwilliges Antragsrecht, um ggf. ein Insolvenzverfahren in geordneterer Lage zu eröffnen.

---

## § 15a InsO — Antragspflicht und Fristen

### Die 21-Tage-Frist

Wenn Zahlungsunfähigkeit **oder** Überschuldung mit negativer Fortführungsprognose vorliegt:

```
Erkennen des Tatbestands → SPÄTESTENS 3 WOCHEN → Insolvenzantrag stellen
```

**Wer muss den Antrag stellen?**
- Jedes Mitglied des Vertretungsorgans → **jeder Geschäftsführer** persönlich
- Für [[Wagglz GmbH]]: Oleg Kober als alleiniger GF
- Für [[OK Capital UG]]: Oleg Kober als Inhaber/GF

### Konsequenzen bei Verletzung

| Konsequenz | Rechtsgrundlage |
|---|---|
| **Strafverfolgung** (Freiheitsstrafe bis 3 Jahre oder Geldstrafe) | § 15a Abs. 4 InsO |
| **Zivilrechtliche Schadensersatzpflicht** gegenüber Gläubigern | § 823 Abs. 2 BGB i.V.m. § 15a InsO |
| **Anfechtung** von Zahlungen, die nach Insolvenzreife geleistet wurden | §§ 129 ff. InsO |
| **§ 64 GmbHG (alt) / § 15b InsO (neu)** — Erstattungspflicht für Zahlungen nach Insolvenzreife | § 15b InsO |

---

## Anfechtungsrisiko — Zahlungen nach Insolvenzreife

Ein besonders kritisches Risiko: Wenn **nach** Eintritt der Zahlungsunfähigkeit oder Überschuldung noch Zahlungen aus dem Gesellschaftsvermögen geleistet wurden (z.B. an Gesellschafter, Lieferanten, Steuerberater), können diese in der späteren Insolvenz **angefochten** werden.

**Relevante Frage für die Analyse:**
> „Wurden in den letzten 3 Jahren Zahlungen nach Insolvenzreife geleistet?" — [[Master Prompt Gesamtfinanzanalyse]], Schritt 1d

Dies betrifft auch die laufenden Gesellschafterdarlehen (~357 €/Mo), die Oleg aus seinem Privatvermögen in die Gesellschaft(en) fließen lässt — diese könnten in der Insolvenz zurückgefordert werden.

---

## Ampel-Schema für die Analyse

| Farbe | Tatbestand | Handlungsbedarf |
|---|---|---|
| 🟢 **GRÜN** | Zahlungsfähig + Eigenkapital positiv (oder EK negativ, aber Fortführungsprognose positiv) | Keine akute Insolvenzgefahr |
| 🟡 **GELB** | Zahlungsfähig, aber EK negativ UND Fortführungsprognose unklar | Insolvenzberater einschalten |
| 🔴 **ROT** | Zahlungsunfähig (§ 17) ODER überschuldet mit negativer Prognose (§ 19) | 21-Tage-Frist läuft — **sofort handeln** |

---

## Praktische Heuristiken für Wagglz GmbH / OK Capital UG

Auf Basis der im [[Master Prompt Gesamtfinanzanalyse]] genannten Eckdaten lassen sich folgende Vorab-Einschätzungen ableiten (ohne Dokumenteneinsicht):

| Indikator | Signal |
|---|---|
| Keine erkennbaren Umsätze / Rückflüsse | 🔴 Risikosignal — kein Cashflow aus Geschäftsbetrieb |
| Laufende Gesellschafterdarlehen ~357 €/Mo | 🟡 Ambivalent — hält Gesellschaft am Leben, aber erhöht Verbindlichkeiten (ohne Rangrücktritt) |
| Jahresabschlüsse nicht erstellt/fällig | 🔴 Risikosignal — fehlende Abschlüsse erschweren Überschuldungsprüfung |
| Ursprüngliches Kapital aus privatem Kredit | 🔴 Risikosignal — privates Haftungsrisiko |

> ⚠️ **Wichtiger Hinweis:** Diese Vorab-Einschätzung basiert ausschließlich auf den im Prompt genannten Eckdaten. Die tatsächliche Insolvenzlage kann nur durch Einsicht in Bilanzen, Kontoauszüge und BWA festgestellt werden.

---

## Verwandte Seiten

- [[Master Prompt Gesamtfinanzanalyse]] — vollständiger Analyse-Prompt (Quelldokument)
- [[Gesamtfinanzanalyse Methodik]] — übergeordnetes 4-Rollen-Framework
- [[Wagglz GmbH]] — primäre analysierte Gesellschaft
- [[OK Capital UG]] — zweite analysierte Gesellschaft
- [[Oleg Personal Context]] — GF in der Haftungspflicht
- [[MOC Finanzen]] — übergeordnete Finanz-MOC
- [[SP STB]] — Steuerberater; in der Analyse beteiligt
