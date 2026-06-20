---
title: Vault-Architektur
type: concept
tags: [vault, architecture, workflow, ingest, raw, wiki, obsidian, meta]
sources: ["raw/README.md"]
created: 2026-06-15
updated: 2026-06-15
summary: Die zweischichtige Vault-Architektur trennt unveränderliche Rohquellen vom lebendigen Wiki — raw/ enthält Originalnotizen, wiki/ enthält integriertes Wissen; das Ingest-Skript verbindet beide Ebenen
---

# Vault-Architektur

## Überblick

Der Vault verwendet eine **zweischichtige Architektur**, die Roh-Quellmaterial strikt von integriertem Wiki-Wissen trennt. Dieses Muster (ähnlich dem Karpathy LLM Wiki-Ansatz) stellt sicher, dass:
1. Originalquellen unverändert erhalten bleiben
2. Wissenssynthese ausschließlich in der Wiki-Schicht stattfindet
3. Alle Wiki-Seiten auf spezifische Quelldateien zurückverfolgt werden können

## Zweischichtiges Modell

```
Schicht 1: raw/           ← Unveränderliches Quellmaterial
           ↓
       python3 tools/ingest.py
           ↓
Schicht 2: wiki/          ← Lebendige, integrierte Wissensbasis
```

### Schicht 1 — raw/
- **Unveränderlich nach dem Ingest** — Dateien werden nie bearbeitet
- Gegliedert nach Lebens-/Geschäftsbereichen (Privat, Business, _archiv)
- Enthält Originalnotizen, Exporte, Vorlagen und Dokumente
- Beinhaltet `inbox/` als Staging-Bereich für neues Material
- Siehe [[Raw Vault Structure README]] für die vollständige Verzeichnisübersicht

### Schicht 2 — wiki/
- **Lebendig und aktualisierbar** — kontinuierlich verfeinert und erweitert
- Gegliedert nach Wissenstyp:
  - `wiki/entities/` — spezifische Personen, Orte, Unternehmen, Ereignisse
  - `wiki/concepts/` — Ideen, Methoden, Frameworks
  - `wiki/sources/` — eine Quellzusammenfassungsseite pro eingepflegter Rohdatei
  - `wiki/syntheses/` — quellenübergreifende Synthese und Analyse
  - `wiki/comparisons/` — strukturierte Vergleiche
- Durchgehend verbunden über [[Obsidian]]-Wikilinks

## Ingest-Workflow

1. **Neue Inhalte** landen in `raw/inbox/`
2. **Ingest-Skript** (`python3 tools/ingest.py`) verarbeitet die Datei
3. **Quellzusammenfassungsseite** wird in `wiki/sources/` erstellt (eine pro Rohdatei)
4. **Entitäts-/Konzeptseiten** werden bei Bedarf erstellt oder aktualisiert
5. **Index wird** mit neuen Einträgen aktualisiert
6. **Rohdatei bleibt unveränderlich** — das Wiki ist der einzige Wahrheitspunkt

## Seitentyp-Hierarchie

| Typ | Zweck | Speicherort |
|---|---|---|
| `source` | Zusammenfassung einer einzelnen Rohdatei | `wiki/sources/` |
| `entity` | Bestimmte Person, Unternehmen, Ereignis usw. | `wiki/entities/` |
| `concept` | Methode, Framework, Idee | `wiki/concepts/` |
| `synthesis` | Quellenübergreifende Analyse | `wiki/syntheses/` |
| `comparison` | Strukturierter A-vs-B-Vergleich | `wiki/comparisons/` |

## Ausschlussbereich

`raw/_archiv/` ist explizit vom aktiven Ingest ausgeschlossen. Inhalte dort (primär ältere Arbeitshistorie) sollen keine Wiki-Seiten erzeugen.

## Namenskonventionen

- **Quellseiten:** Nach der Rohdatei benannt, um Rückverfolgbarkeit zu gewährleisten
- **Entitätsseiten:** Menschenlesbare Eigennamen (Personen, Unternehmen, Ereignisse)
- **Konzeptseiten:** Themenname (z. B. „BMR and TDEE", „Brick Training")
- **Kein .md-Suffix** in Wikilinks — Obsidian löst diese automatisch auf

## YAML-Frontmatter-Standard

Jede Wiki-Seite verwendet:
```yaml
---
title: Menschenlesbarer Titel
type: source|entity|concept|synthesis|comparison
tags: [tag1, tag2]
sources: ["raw/path/to/source.md"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
summary: Einzeilige Beschreibung
---
```

## Verwandte Seiten

- [[Raw Vault Structure README]] — die README-Datei, die die raw/-Struktur definiert
- [[Oleg Personal Context]] — Vault-Inhaber
- [[MOC Performance und Leben]] — Performance-MOC
- [[MOC Finanzen]] — Finanz-MOC
- [[MOC Strategie und Business]] — Business-MOC
- [[MOC Tech und Setup]] — Tech-MOC