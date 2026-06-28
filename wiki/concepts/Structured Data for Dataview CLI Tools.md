---
title: Structured Data for Dataview / CLI Tools
type: concept
tags: [structured-data, dataview, cli, csv, automation, dashboards, cashflow, health-metrics, training-logs]
sources: ["raw/raw/data/README.md"]
created: 2026-06-17
updated: 2026-06-17
summary: Placeholder framework for CSV data exports enabling Obsidian Dataview queries and command-line tool integration; intended for cashflow tracking, health metrics, training logs; schema and structure TBD; no credentials/secrets in versioned files.
---

# Structured Data für Dataview / CLI-Tools

## Überblick

Dieser Bereich ist ein **verwalteter Platzhalter** für strukturierte Datenexporte, die sich an zwei Ökosysteme richten:

1. **[[Obsidian]] Dataview Plugin** — ermöglicht SQL-ähnliche Abfragen über Markdown-YAML-Frontmatter und CSV-Dateien
2. **CLI-Tools** — Python/Bash-Scripts für automatisierte Auswertungen, Dashboards, Finanz-Tracking

## Datentypen (geplant)

| Datentyp | Format | Quelle | Verarbeitung |
|---|---|---|---|
| **Cashflow** | CSV | Finanz-Tracking (monatliche Einnahmen, Ausgaben, Bestandsveränderung) | Monatliches Roll-up, Szenario-Modellierung |
| **Health Metrics** | CSV | Performance-Protokoll (Gewicht, WHR, KFA, Blutbild, HRV) | 12-Wochen-Vergleiche, Trend-Analyse |
| **Training Logs** | CSV | Hyrox Prep, Zone 2 Sessions (Datum, Dauer, Intensität, Notizen) | Wöchentliche Aufsummierung, VO₂-Trend |
| **Business KPIs** | CSV | Performance Coffee (Orders, Revenue, CAC, Abo-Anteil, Repeat Rate) | Monatliche Dashboards, Go-Live-Tracking |

## Datenschutz & Sicherheit

⚠️ **Regel:** Keine Gehälter, Bankdaten, Passwörter oder persönliche IDs in versionierten Dateien.

Erlaubte Felder:
- ✅ Aggregate Finanzzahlen (Monatssummen, Kategorien)
- ✅ Performance-Metriken (KFA, Gewicht, Trainingsdaten)
- ✅ Business-KPIs (Orders, CAC, Margin%)
- ✅ Zeitstempel, Beschreibungen

Verbotene Felder:
- ❌ Gehälter, Provisionen (brutto)
- ❌ Bank-Account-Nummern, IBAN
- ❌ Personnennummern, Sozialversicherung
- ❌ Passwörter, API-Keys, Credentials

## Schema-Entwurf (TBD)

### Cashflow-CSV

```
datum,kategorie,betrag_eur,typ,notiz
2026-06-15,doctolib_netto,3638.82,income,Fixed salary
2026-06-15,provision_q2,4611.00,income,Quarterly commission
2026-06-01,vw_kredit,-681.57,expense,Auto loan
2026-06-01,kiefero,-176.53,expense,Orthodontics
2026-06-01,gesellschafterdarlehen,-357.00,expense,Company loan
```

### Health-Metrics-CSV

```
datum,metrik,wert,einheit,quelle,notiz
2026-05-29,kfa,20.3,%,scaneca_3d,Baseline
2026-05-29,magermasse,77.1,kg,scaneca_3d,Baseline
2026-05-29,taille,97.2,cm,scaneca_3d,Baseline
2026-05-29,whr,0.92,ratio,scaneca_3d,Baseline
```

### Training-Log-CSV

```
datum,protokoll,typ,dauer_min,intensitaet,notizen
2026-06-10,zone2,cardio,75,steady,Nasal breathing, 145 bpm avg
2026-06-11,hyrox_prep,strength,60,high,SkiErg + wall climbs
2026-06-12,zone2,cardio,90,steady,Recovery session
```

## Integration mit Werkzeugen

### Obsidian Dataview (Beispiel-Query)

```javascript
TABLE WITHOUT ID
  datum,
  kategorie,
  betrag_eur
FROM "raw/data/cashflow.csv"
WHERE tipo = "expense"
SORT betrag_eur DESC
```

### CLI-Tools (geplant)

**Python-Beispiel:**
```bash
python3 tools/cashflow_rollup.py --month 2026-06 --output dashboard.md
# Generiert monatliche Zusammenfassung nach Kategorien
```

**Bash-Beispiel:**
```bash
./tools/health_metrics_trend.sh --metric kfa --weeks 12
# Zeigt 12-Wochen-Trend KFA mit Baseline-Vergleich
```

## Governance

| Aspekt | Regel |
|---|---|
| **Update-Frequenz** | Wöchentlich (Training, Metriken); Monatlich (Cashflow, KPIs) |
| **Zuständigkeit** | Oleg (Finanzen, Gesundheit); Hai oder CMO (Business KPIs) |
| **Validierung** | Spot-checks gegen Source-of-Truth (Bank, 3D-Scan, Training-App) |
| **Versionierung** | Git-commits mit Commit-Message "data: [type] update [date]" |
| **Archivierung** | CSV-Dateien behalten historische Reihen (keine Löschung) |

## Nächste Schritte

1. **Schema finalisieren** — abstimmen mit Stakeholdern (Oleg, Hai, evtl. Data Engineer)
2. **CSV-Templates** — Vorlagen für jede Datenklasse erstellen
3. **Dataview-Queries schreiben** — Dashboard-Seiten für Cashflow, Health, Business KPIs
4. **CLI-Tools entwickeln** — Python-Scripts für Monatliche Rollups, Trend-Analyse, Alerts
5. **Automated Ingestion** — Überlegen, ob Bank-APIs, Scaneca-API, Training-App-Exports automatisiert werden können

## Verknüpfungen

- **[[00 Finanz-Übersicht]]** — Quelle für Cashflow-Daten
- **[[00 Performance-Übersicht]]** — Quelle für Health-Metrics
- **[[Hyrox Prep]]** — Quelle für Training-Logs
- **[[Unit Economics]]** — Destination für Business-KPI-Auswertungen
- **[[Progress Tracking]]** — Konzept für Measurement-Serien
- **[[Obsidian]]** — Datenbasis-Tool
