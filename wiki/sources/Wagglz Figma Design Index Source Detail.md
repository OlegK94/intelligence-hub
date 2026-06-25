---
title: Wagglz Figma Design Index
type: source
tags: [wagglz, wufflz, figma, design, ui, wireframes, pitch-deck, migration]
sources: ["raw/raw/Business/Wagglz/Design/figma-index.md"]
created: 2026-06-25
updated: 2026-06-25
summary: Master-Katalog aller 10 aktiven Figma-Dateien für Wagglz/Wufflz — Wireframes, Pitch Decks, B2B Software Design; Stand Juni 2026
---

# Wagglz Figma Design Index — Quelldokument

Master-Katalog aller Figma-Dateien im Wagglz/Wufflz-Design-System. Erstellt als Migrations-Index von Figma nach Obsidian. Exportiert via `tools/figma_export.py`.

**Stand:** 2026-06-14 · **Status:** 1/10 exportiert (18 PNGs aus Wireframes), 9/10 ausstehend (429-Fehler bei API)

## 10 Kanonische Active-Dateien

| # | Name | Typ | Kategorie |
|---|------|-----|-----------|
| 1 | 25 Wufflz Wireframes | design | product |
| 2 | 25 B2B Software | design | product |
| 3 | Pitch Deck Wufflz GmbH Editor Banken | design | pitch |
| 4 | Co-Founders Workshop | FigJam | workshop |
| 5 | Wufflz CVs | design | product |
| 6 | Wufflz App Market Research | FigJam | research |
| 7 | Wufflz PitchDeck Template | design | pitch |
| 8 | Proto TXErnZeob | design | product |
| 9 | Pitch Deck Investoren v2 | design | pitch |
| 10 | Pitch Deck Investoren v1 | design | pitch |

**Bereits exportiert:** Datei 1 (25 Wufflz Wireframes) — 18 PNGs in `raw/assets/wagglz-tier/7RI3XqEc3RR6znirkakZcm/`

## Deprecated Dateien (nicht in Active-Liste)

Ältere Wagglz-Dogwalking-Designs, Wufflz-Website-Design (Dogwalking-Version), Research-Artefakte — im Katalog für Referenz.

## Export-Workflow

```bash
python3 tools/figma_export.py --all                           # 10 kanonische Dateien
python3 tools/figma_export.py --all --include-kits --include-deprecated
python3 tools/figma_export.py <file-key>                      # Einzeldatei
```

PNGs landen in `raw/assets/wagglz-tier/{file_key}/`. FIGMA_TOKEN in `.env` erforderlich.

## Kontext

Die Figma-Dateien dokumentieren die vollständige Designgeschichte von Wagglz/Wufflz: vom ursprünglichen Dogwalking-App-Konzept über die Pivot-Phase (Wufflz = Tierarzt-Plattform) bis zu den aktuellen B2B SaaS Wireframes und Investoren-Pitch-Decks. Die Wireframes-Analyse (Datei 1) war Grundlage für die [[Wagglz App UI Screens]] wiki-Seite.

## Verknüpfte Seiten

- [[Wagglz GmbH]] — Betriebsunternehmen
- [[Wagglz App UI Screens]] — analysierte Wireframes (Datei 1)
- [[Wagglz-Brand]] — Markenidentität
