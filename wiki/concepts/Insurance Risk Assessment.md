---
title: "Insurance Risk Assessment"
type: concept
tags: [versicherung, risiko, entscheidungsfindung, gesundheitsprüfung, prämien-kalkulation, risikoleben]
sources: []
created: 2026-06-18
updated: 2026-06-18
summary: Framework zur Evaluierung von Versicherungs-Wechsel-Risiken — Schwerpunkt auf Gesundheitsprüfungen, Age Underwriting, Prämien-Eskalation vs. Rabatt-Gewinn. Anwendungsfall: Risikolebensversicherung bei Allianz-Konsolidierung (entschieden: Bestandsschutz).
---

# Insurance Risk Assessment

## Überblick

Insurance Risk Assessment ist die quantitative Evaluierung von Kosten und Risiken bei einem Versicherungs-Wechsel. Die zentralen Fragen:

1. **Wird eine neue Prämie höher sein als die bestehende?** (Age Underwriting, Gesundheitsprüfung)
2. **Übersteigt das Erhöhungsrisiko den Rabatt-Gewinn?**
3. **Gibt es Alternative: Bestandsschutz vs. Wechsel?**

## Kernkonzepte

### Age Underwriting

Versicherer kalkulieren Risikolebensversicherung nach **Eintrittsalter**. Das Prinzip:
- Prämie bei **Alter 35 (aktuell):** €40/Monat (beispielhaft)
- Prämie bei **Alter 36 (neuer Anbieter):** €42/Monat (Alter +1 Jahr, Mortalitäts-Erhöhung)
- **Perpetuale Bindung:** Die €42/Monat-Prämie bleibt für die gesamte Laufzeit; nicht rückzuändern

**Implikation:** Ein einjähriger Wechsel-Verzug kostet permanent zusätzliche €24/Jahr (oder mehr bei größeren Alterssprüngen).

### Gesundheitsprüfung (Underwriting)

Bei Neuabschluss werden umfassendere Gesundheitsfragen gestellt:
- **Bestehende Police:** Wurde bei jüngerer Gesundheit abgeschlossen; Deckung "frozen" auch wenn Gesundheit verschlechtert
- **Neue Police:** Vollständige medizinische Historie prüfbar; Risiken können zu **höhere Prämien oder Ablehnungen** führen

**Szenario:** Versicherter mit neuer Diagnose (z.B. erhöhter Blutdruck) nach dem Abschluss:
- Bestehende Police: Keine Erhöhung (locked-in)
- Neue Police: +20–50% Risikoaufschlag oder sogar Ablehnung

### Prämien-Eskalationsrisiko

Die Kombination aus Age Underwriting + Gesundheitsprüfung führt zu **prämienerhöhungsrisiko**:

**Pessimistisches Szenario:**
```
Aktuelle Risikoleben-Prämie:           €40/Monat
Neuer Anbieter (Alter +1):             €42/Monat
Gesundheitsaufschlag (neu erkannt):    +€15/Monat
Gesamte neue Prämie:                   €57/Monat

Erhöhung:                              €17/Monat = €204/Jahr
Rabatt bei Allianz 20%:                ~€8/Monat = €96/Jahr

Netto-Verlust durch Wechsel:           €108/Jahr
```

## Entscheidungs-Framework

### Schnell-Entscheidung: Sollte ich wechseln?

**JA, wenn:**
- ✅ Neue Prämie ist eindeutig günstiger (market research bestätigt)
- ✅ Rabatt ≥ 15% und Eintrittsalter niedrig (<40 Jahre)
- ✅ Gesundheitsstatus stabil / gute Prognose

**NEIN, wenn:**
- ❌ Gesundheitsprüfung-Risiko signifikant
- ❌ Eintrittsalter schon erhöht (>50 Jahre)
- ❌ Rabatt <15% und Prämien-Erhöhungs-Wahrscheinlichkeit >30%
- ❌ Bestandspolice bereits lange gehalten (Zinseszins-Effekt; locked-in prämie)

### Quantitatives Modell

**Break-even-Analyse:**

```
Rabatt pro Monat = Aktuelle Prämie × Rabatt %
Erwartete Prämien-Erhöhung = Aktuelle Prämie × (Age-Factor + Health-Risk-Factor)

Jahres-Nettogewinn = (Rabatt × 12 Monate) − (Erhöhungsrisiko × Erhöhungs-Wahrscheinlichkeit)

Wenn Jahres-Nettogewinn < 0 → Bestandsschutz vorziehen
```

**Beispiel (Risikoleben):**
```
Aktuelle Prämie:              €40/Monat = €480/Jahr
Rabatt 20%:                   €96/Jahr
Age-Factor (Alter +1):        +€24/Jahr
Health-Risk (geschätzt 40%):  +€60/Jahr × 40% = €24/Jahr erwartet
Erhöhungs-Risiko gesamt:      €48/Jahr

Netto = €96 − €48 = €48/Jahr Gewinn → Marginal, nicht überzeugend
Varianz: Wenn Health-Risk > 50% → Netto negativ → Nicht wechseln
```

---

## Anwendungsfall: Risikolebensversicherung (Allianz-Konsolidierung)

### Bewertung
| Faktor | Befund | Gewichtung |
|---|---|---|
| **Aktuelle Prämie** | unbekannt (€30–50/Monat geschätzt) | Basis |
| **Rabatt-Gewinn** | €6–10/Monat (20% auf €30–50) | +€120/Jahr |
| **Age Underwriting Risiko** | €20–30/Monat zusätzlich | −€240–360/Jahr |
| **Gesundheitsprüfung Risiko** | Mittel (Diagnosen prüfbar) | −€10–30/Monat |
| **Netto Jahres-Gewinn** | €120 − €240−360 − €120−360 | **NEGATIV** |

### Entscheidung: ❌ NICHT WECHSELN
- **Begründung:** Prämien-Erhöhungs-Risiko überwiegt Rabatt-Gewinn deutlich
- **Alternative:** Bestandspolice behalten; Rabatt bei anderen 3 Policen (Haftpflicht, Hausrat, Rechtsschutz) realisieren
- **Konsequenz:** 4 statt 5 Policen bei Allianz — aber still eine attraktive Konsolidierung

---

## Mitigationsstrategien

| Risiko | Mitigation |
|---|---|
| **Gesundheitsprüfungs-Risiko hoch** | Vor Wechsel: aktuelles Gesundheitsattest einholen; ggf. Arzt konsultieren |
| **Unsicherer neuer Prämienpreis** | Angebots-Gültigkeit prüfen (typisch 4–6 Wochen); garantierte Kalkulationen verlangen |
| **Übergangsversicherung** | Alte & neue Police zeitlich überlappen; Doppel-Prämie für Monat akzeptabel zur Lückenvermeidung |
| **Versichertenkommunikation** | Mit Makler sprechen, nicht direktem Anbieter-Support; Makler können verhandeln |

---

## Verknüpfungen

- **[[Insurance Consolidation Strategy]]** — Rahmen für Konsolidierungs-Entscheidungen
- **[[Allianz Insurance Consolidation]]** — Praktische Anwendung (Risikoleben-Entscheidung)
- **[[Risikolebensversicherung]]** — Versicherungsprodukt-Konzept
- **[[Age Underwriting]]** — Prämien-Kalkulationsprinzip
- **[[Bestandsschutz]]** — Alternative zur Konsolidierung

---

*Konzept erstellt: 2026-06-18*
*Fallbeispiel: Risikolebensversicherung, 20% Rabatt reicht nicht gegen Erhöhungsrisiko*
