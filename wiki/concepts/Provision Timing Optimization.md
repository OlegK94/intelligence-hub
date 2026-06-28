TAGS: [personal-finance, cash-flow, provisioning, income-timing, doctolib, quarterly]
SOURCES: ["raw/Finanzdaten/Privat/CLAUDE.md"]
CREATED: 2026-06-21
UPDATED: 2026-06-21
SUMMARY: Olegs Provision wird quartalsweise mit 1-Monat-Lag ausgezahlt (Jan/Apr/Jul/Okt); 4 Zahlungen à ~€4.611 netto = ~€18.444/Jahr; in Nicht-Provisions-Monaten tritt Defizit auf; Optimierungsziel ist Provision-Puffer-Verwaltung zur Finanzierung der strukturalen Neun-Monats-Defizitphasen

---

# Provision Timing Optimization

## Überblick

Olegs [[Doctolib GmbH]] Provision unterliegt einem **quartalsweisen Rhythmus mit 1-Monat-Verzögerung**, was ein strukturelles Cashflow-Managementproblem schafft. Diese Seite adressiert die Timing-Mechanik und optimale Puffer-Verwaltung.

## Provisionsstruktur

| Parameter | Wert |
|---|---|
| **Jährliche Provision brutto** | €32.000 |
| **Netto pro Zahlung** | ~€4.611 |
| **Zahlungsrhythmus** | Quartalsweise |
| **Zahlungsmonate** | Januar, April, Juli, Oktober |
| **Lag nach Quartalsende** | 1 Monat (z.B. Q1 endet 31.03, bezahlt 30.04) |

## Jahreskalender — Provision vs. Fixkosten

```
MONAT       PROVISION    FIXKOSTEN    SALDO
Jan         +€4.611      −€2.676      +€1.935
Feb            —         −€2.676      −€2.676
Mrz            —         −€2.676      −€2.676
────────────────────────────────────────────
Apr         +€4.611      −€2.676      +€1.935
Mai            —         −€2.676      −€2.676
Jun            —         −€2.676      −€2.676
────────────────────────────────────────────
Jul         +€4.611      −€2.676      +€1.935
Aug            —         −€2.676      −€2.676
Sep            —         −€2.676      −€2.676
────────────────────────────────────────────
Okt         +€4.611      −€2.676      +€1.935
Nov            —         −€2.676      −€2.676
Dez            —         −€2.676      −€2.676
────────────────────────────────────────────
JAHRESSALDO (ohne Variable):  −€7.970
```

> ⚠️ **Muster:** 4 positive Monate (+€1.935 netto Surplus) + 8 negative Monate (−€2.676 netto Deficit).

## Das Defizitproblem

Selbst wenn Oleg die gesamte Provision **aus den Jan/Apr/Jul/Okt-Zahlungen** speichert:

```
Vier Provisionsüber-Schüsse:  4 × €1.935 = €7.740/Jahr
Acht Defizitmonate:           8 × €2.676 = €21.408/Jahr
────────────────────────────────────────────
NETTO (ohne Variable):        −€13.668/Jahr
```

**Erkenntnis:** Selbst perfekte Provisionsthrift reicht nicht aus, um die **Basis-Fixkosten** zu decken. Das Strukturdefizit wird durch **variable Ausgaben** (Lebensmittel, Restaurants, Spontankäufe ~€13.000–15.000/Jahr) verschärft.

## Optimierungsstrategie: Der 3-Monats-Puffer

Um das Defizitproblem zu lösen, benötigt Oleg einen **aufgebauten Provision-Puffer** von mindestens **3 Monatskosten (~€8.000)**, um Defizitmonate zu überbrücken:

### Phase 1: Puffer-Aufbau (Monat 1–4)
- Jan: Provision €4.611 → speichern €3.000 (nicht für Februarverlust ausgeben)
- Feb–Mar: Überbrückung aus gespartem Puffer
- Apr: Provision €4.611 → speichern €3.000
- → Nach 4 Monaten: Puffer ~€6.000

### Phase 2: Steady-State (Monat 5+)
- Jul: Provision €4.611 → speichern €3.000
- Okt: Provision €4.611 → speichern €3.000
- Feb, Mai, Aug, Nov: Aus Puffer abheben €2.676
- → Puffer bleibt stabil auf ~€6.000–8.000

## Realistische Implementierung

**Problem:** Aus dem Quelldokument geht hervor, dass Oleg die Provision **nicht spart**, sondern **konsumiert**. Das bedeutet:

1. **Fehlendes Puffer-Tracking:** Oleg weiß wahrscheinlich nicht, dass er einen Puffer aufbauen sollte
2. **Psychologische Anker:** Große Zahlungen (€4.611) werden als "verfügbares Einkommen" wahrgenommen, nicht als "Puffer-Gelegenheit"
3. **Mangelnde Disziplin:** Spontankäufe >€200 (Suit Supply, etc.) korrelieren zeitlich mit Provisionsempfang

### Empfohlene Maßnahmen

| Maßnahme | Effekt |
|---|---|
| **Automatische Überweisung:** 50% der Provision auf separates Sparkonto (Tag 1 nach Eingang) | Verhindert mentale Verfügbarkeit |
| **Visuelles Tracking:** Puffer-Status in Excel/Dashboard | Feedback-Verstärkung |
| **Zielsetzen:** "Puffer von €8.000 innerhalb von 6 Monaten" | Konkrete Metrik |
| **Monatliche Review:** Sollte der Puffer fallen, Konsum-Reduktion aktivieren | Frühe Warnung |

## Alternativer Ansatz: Gewalt-Strukturelle Lösung

Falls Oleg die Provision-Puffer-Disziplin **nicht aufbringen kann**, ist die strukturelle Lösung:

**Wagglz-Abbau oder Exit.**

```
Wagglz lfd. Kosten:        €357/Monat = €4.284/Jahr
Wagglz Jahresabschluss:    €5.000 (2025)
─────────────────────────────────────
Vermiedene Kosten (Jahr 1): €9.284
Vermiedene Kosten (ab Jahr 2): €4.284/Jahr (keine Abschluss mehr)
```

Durch Wagglz-Exit könnte Oleg den **gesamten strukturalen Deficit eliminieren** — ohne Disziplin, ohne Sparkonto, rein durch Kostenreduktion.

---

## Verwandte Seiten

- [[Oleg Personal Context — Financial Deep Dive]] — Vollständige Finanzanalyse
- [[Wagglz GmbH]] — Struktur-Verursacher der Belastung
- [[MOC Finanzen]] — Finanzplanung MOC
- [[Fixkosten Übersicht]] — monatliche Kostenerfassung
- [[Oleg Personal Context]] — Basis-Profilseite
