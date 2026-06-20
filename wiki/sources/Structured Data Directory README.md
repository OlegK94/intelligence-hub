---
title: Strukturiertes Datenverzeichnis README
type: source
tags: [data, dataview, csv, infrastructure, vault-structure, cli]
sources: ["raw/data/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: README für das Verzeichnis raw/data/ — Platzhalter mit Anweisungen zur Ablage von CSV-Exporten (Cashflow, Gesundheitsmetriken, Trainingsprotokolle) für Dataview und CLI-Tools; verbietet ausdrücklich Geheimnisse oder Zugangsdaten
---

# Strukturiertes Datenverzeichnis — README

## Überblick

Diese Quellseite erfasst das README für das Verzeichnis `raw/data/` in [[Oleg Personal Context|Olegs]] Vault. Das Verzeichnis ist als strukturierter Datenspeicher für maschinenlesbare Exporte vorgesehen, die von [[Dataview]]-Abfragen und CLI-Tools verwendet werden.

## Zweck

Das Verzeichnis `raw/data/` ist dazu gedacht, **CSV-Exporte** aus drei Bereichen zu speichern:

| Bereich | Beispiele |
|---|---|
| **Cashflow** | Monatliche Einnahmen-/Ausgaben-Exporte, Budget vs. Ist |
| **Gesundheitsmetriken** | Biomarkerwerte, Körperscanner-Messungen, HRV, Gewichtsverlauf |
| **Trainingsprotokolle** | Workout-Logs, Hyrox-Trainingsdaten, Zone 2-Aufzeichnungen |

## Einschränkungen

- **Keine Geheimnisse oder Zugangsdaten** — durch das README ausdrücklich verboten
- Die Daten hier sind strukturiert/maschinenlesbar (CSV), keine Prosanotizen
- Zur Verwendung durch Tools vorgesehen, nicht zum manuellen Durchsuchen

## Bezug zu Wiki-Konzepten

Die hier gespeicherten Daten würden einfließen in:

- **[[Biomarker Testing]]** / **[[Blutbild Panel]]** — vierteljährliche Blutpanelergebnisse als CSV
- **[[3D Body Scan]]** / **[[3D Body Scan Scaneca Mai 2026]]** — Körperzusammensetzungsmetriken über die Zeit
- **[[BMR and TDEE]]** — Kalorientracking-Exporte
- **[[Hyrox 10-Week Training]]** — Trainingsprotokoll-Daten
- **[[Fixkosten Übersicht]]** — Cashflow- / Fixkosten-Exporte
- **[[MOC Finanzen]]** — Finanzdaten-Exporte

## Dataview-Integration

[[Dataview]] ist ein Obsidian-Plugin, das SQL-ähnliche Abfragen über Vault-Inhalte ermöglicht, einschließlich CSV-Dateien in diesem Verzeichnis. Dies ermöglicht dynamische Dashboards für Gesundheitsmetriken, Finanzübersichten und Trainingsfortschritte, ohne Daten manuell in Notizen duplizieren zu müssen.

## Aktueller Stand

Zum Zeitpunkt der Erstellung des READMEs enthält das Verzeichnis **keine Datendateien** — nur dieses erklärende README. Die Befüllung mit Daten ist eine zukünftige Maßnahme, sobald CSV-Exporte erzeugt werden aus:
- Wahoo/Garmin-Trainingsexporten
- Blutlabor-Ergebnissen
- Bank-/Finom-Kontoexporten
- Nachfolgedaten aus Körperscans

## Keine Widersprüche

Dieses README widerspricht keinen bestehenden Wiki-Inhalten. Es stellt ausschließlich Infrastrukturkontext bereit.

## Verwandte Seiten

- [[Blutbild Panel]] — Gesundheitsmetriken, die hier gespeichert werden sollen
- [[3D Body Scan Scaneca Mai 2026]] — Körperzusammensetzungsdaten
- [[BMR and TDEE]] — Kontext zum Stoffwechsel-Tracking
- [[Fixkosten Übersicht]] — Cashflow-Datenquelle
- [[MOC Finanzen]] — Finanzdaten-Kontext
- [[MOC Performance und Leben]] — Kontext für Gesundheits-/Trainingsdaten
- [[Oleg Personal Context]] — Vault-Inhaber