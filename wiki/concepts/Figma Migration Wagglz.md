---
title: "Figma Migration Wagglz"
type: concept
tags: [wagglz, wufflz, figma, design, migration, obsidian, export, katalog]
sources: ["raw/Business/Wagglz/Design/figma-index.md"]
created: 2026-06-13
updated: 2026-06-14
summary: Konzept und Prozess der Figma-zu-Obsidian-Migration für alle Wagglz/Wufflz-Design-Dateien — 10 kanonische Dateien als Priorität; Export via figma_export.py; PNGs in raw/assets/wagglz-tier/; Ingest via ingest.py; aktuell 1/10 abgeschlossen
---

# Figma Migration Wagglz — Konzept

## Überblick

Die **Figma-zu-Obsidian-Migration** überführt alle Design-Artefakte von [[Wagglz GmbH]] / [[Wufflz]] aus Figma in das Knowledge-Base-System (Obsidian). Ziel ist eine maschinenlesbare, versionierte und verlinkbare Dokumentation aller Design-Dateien — mit PNGs, Manifesten und Wiki-Seiten pro Datei.

---

## Warum die Migration

- **Wissenserhalt:** Figma-Dateien sind nur über das Figma-Tool zugänglich; bei Beendigung des Accounts oder Rate-Limits gehen Designs verloren
- **Verlinkbarkeit:** Obsidian-Wikilinks ermöglichen Querverweise zwischen Design-Artefakten und Business-Kontext (Pitchdecks ↔ Investoren-Kontext, Wireframes ↔ Feature-Planung)
- **Offline-Verfügbarkeit:** PNGs lokal gespeichert; unabhängig von Figma-Verfügbarkeit
- **KI-Ingest:** Manifeste und PNGs können als Kontext für KI-Assistenz verwendet werden

---

## Technische Architektur

```
Figma API
    ↓
tools/figma_export.py   (Export-Skript)
    ↓
raw/assets/wagglz-tier/{file_key}/   (PNGs + Manifest)
    ↓
tools/ingest.py         (Wiki-Ingest)
    ↓
wiki/sources/           (Manifest-Wiki-Seiten)
```

### Wichtige Dateien

| Datei | Zweck |
|-------|-------|
| `tools/figma_export.py` | Export-Tool: Frames als PNGs via Figma REST-API |
| `tools/ingest.py` | Ingest-Tool: Manifest → Wiki-Seite |
| `figma-catalog.json` | Maschinenlesbarer Katalog aller Figma-Dateien |
| `raw/Business/Wagglz/Design/figma-index.md` | Human-readable Master-Index (Quelldokument) |

---

## Datei-Kategorisierung

### Kanonisch (Active-Liste, 10 Dateien)

Migrations-Priorität; von `--all` standardmäßig exportiert:

| Kategorie | Dateien | Keys |
|-----------|---------|------|
| product | Wireframes, B2B Software, CVs, Proto TXErnZeob | 7RI3..., NO7z..., NmlK..., TXEr... |
| pitch | Banken, Investoren v1, v2, PitchDeck Template | X9Dz..., 5Fp2..., FnhM..., PMh6... |
| workshop | Co-Founders Workshop (FigJam) | VmWA... |
| research | Wufflz App Market Research (FigJam) | IXxr... |

### Deprecated / Optional (7 Dateien)

Ältere oder ersetzte Versionen; nur mit `--include-deprecated` exportiert.

### Kits / Referenz (3 Dateien)

Drittanbieter UI-Kits (Ant Design, Nucleus Plus, theProjekts); nur mit `--include-kits` exportiert.

---

## Aktueller Status (Stand 2026-06-14)

| Metrik | Wert |
|--------|------|
| Kanonische Dateien gesamt | 10 |
| Vollständig exportiert | **1** (Wireframes — 18 PNGs) |
| Ausstehend | 9 |
| Letzter Fehler | HTTP 429 (Rate-Limit) bei B2B Software |
| Nächster Schritt | Batch-Export mit Pause zwischen Dateien |

> ⚠️ **Rate-Limit-Hinweis:** Die Figma API gibt bei zu häufigen Anfragen HTTP 429 zurück. Empfohlener Abstand: ~1 Datei / 2–5 Minuten. Für FigJam-Dateien kleinere `--batch-size 5` verwenden.

---

## Proto-URL-Hinweis

Figma-Prototype-URLs (`/proto/{key}/`) verwenden denselben File Key wie Design-URLs (`/design/{key}/`) und dieselbe REST-API. Der Katalog kann optional `proto_url` zusätzlich zur Design-URL speichern. Für den Export ist nur der File Key relevant.

---

## Beziehung zu bestehenden Wiki-Seiten

Die Migration füttert direkt folgende Wiki-Seiten:

| Wiki-Seite | Quelle |
|------------|--------|
| [[25 Wufflz Wireframes Figma Manifest]] | `wufflz/Figma-Manifest-25-wufflz-wireframes.md` — **18 PNGs vorhanden** |
| [[25 B2B Software Figma Manifest]] | `wufflz/Figma-Manifest-25-b2b-software.md` — Export ausstehend |
| [[Figma Index Wagglz Source]] | `figma-index.md` — dieser Quelldokument-Index |

Nach erfolgreichem Export werden für alle 10 Dateien analoge Wiki-Seiten angelegt.

---

## Verwandte Seiten

- [[Figma Index Wagglz Source]] — vollständiger Quelldokument-Katalog
- [[25 Wufflz Wireframes Figma Manifest]] — einzige vollständig exportierte Datei
- [[25 B2B Software Figma Manifest]] — kanonisch; Export ausstehend
- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Design-Produktlinie
- [[Oleg Personal Context]] — Projektverantwortlicher
