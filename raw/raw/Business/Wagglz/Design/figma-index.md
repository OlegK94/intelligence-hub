---
title: "Wagglz / Wufflz — Figma Master Index"
type: source
tags: [wagglz, wufflz, tier, figma, design, migration]
created: 2026-06-13
updated: 2026-06-14
summary: Master catalog of all Figma files for Wagglz/Wufflz/Tier migration to Obsidian
---

# Figma → Obsidian Migration Index

> Maschinenlesbarer Katalog: [[figma-catalog.json]] · Export-Tool: `tools/figma_export.py`

**Stand:** 2026-06-14 (13:23 Retry) · **FIGMA_TOKEN:** ja · **Kanonische Active-Liste:** 10 Dateien · **Export-Status:** 1/10 exportiert (18 PNGs), 9/10 ausstehend — erneuter Lauf: 429 bei `NO7zf85jnhjIcJ13QGyESY` (25 B2B Software), Phase-2 PNG nicht gestartet

## Schnellstart

```bash
# 1. Token in .env (https://www.figma.com/developers/api#access-tokens)
echo 'FIGMA_TOKEN=figd_...' >> .env

# 2. Alle kanonischen Dateien exportieren (10 active, ohne Kits/Deprecated)
python3 tools/figma_export.py --all

# 3. Optional: auch Referenz-Kits + deprecated Einträge
python3 tools/figma_export.py --all --include-kits --include-deprecated

# 4. Einzeldatei (design-, board- oder proto-URL / file key)
python3 tools/figma_export.py 7RI3XqEc3RR6znirkakZcm
python3 tools/figma_export.py https://www.figma.com/proto/5Fp2RQjupexSkR1eFe638X/
```

PNGs landen in `raw/assets/wagglz-tier/{file_key}/`. Pro Datei ein Manifest unter dem jeweiligen Unterordner.

**Proto-Hinweis:** `/proto/{key}/`-Links nutzen denselben File Key und dieselbe REST-API wie `/design/{key}/`. Der Katalog speichert optional `proto_url` zusätzlich zur Design-URL.

---

## Kanonische Active-Liste (10)

> Diese 10 Dateien sind die aktuelle Migrations-Priorität. `--all` exportiert standardmäßig nur diese.

| # | Name | Key | Typ | Ordner | Kategorie | PNGs | Manifest |
|---|------|-----|-----|--------|-----------|------|----------|
| 1 | 25 Wufflz Wireframes | `7RI3XqEc3RR6znirkakZcm` | design | wufflz | product | **18** | [[wufflz/Figma-Manifest-25-wufflz-wireframes]] |
| 2 | 25 B2B Software | `NO7zf85jnhjIcJ13QGyESY` | design | wufflz | product | 0 | [[wufflz/Figma-Manifest-25-b2b-software]] |
| 3 | Pitch Deck Wufflz GmbH Editor Banken | `X9DzUUoJwilVPOlkqLiI2b` | design | wufflz | pitch | 0 | [[wufflz/Figma-Manifest-pitch-deck-wufflz-gmbh-editor-banken]] |
| 4 | Co-Founders Workshop | `VmWAOTBCe1hSspmmQY6S14` | **figjam** | workshop | workshop | 0 | [[workshop/Figma-Manifest-co-founders-workshop]] |
| 5 | Wufflz CVs | `NmlKQIeKhRJiPzIMTDmCN3` | design | wufflz | product | 0 | [[wufflz/Figma-Manifest-wufflz-cvs]] |
| 6 | Wufflz App Market Research | `IXxrNkPjBIPGi8QbNgpdea` | **figjam** | wagglz | research | 0 | [[wagglz/Figma-Manifest-wufflz-app-market-research]] |
| 7 | Wufflz PitchDeck Template | `PMh6Xc8BKLbapcfrKGL8VW` | design | wufflz | pitch | 0 | [[wufflz/Figma-Manifest-wufflz-pitchdeck-template]] |
| 8 | Proto TXErnZeob | `TXErnZeobIuX4hEIvko0Fe` | design | wufflz | product | 0 | [[wufflz/Figma-Manifest-proto-txernzeob]] |
| 9 | Pitch Deck Investoren v2 | `FnhmUL3cHzDIM2HOFF2306` | design | wufflz | pitch | 0 | [[wufflz/Figma-Manifest-pitch-deck-investoren-v2]] |
| 10 | Pitch Deck Investoren v1 | `5Fp2RQjupexSkR1eFe638X` | design | wufflz | pitch | 0 | [[wufflz/Figma-Manifest-pitch-deck-investoren-v1]] |

URLs (Design/Editor):
- [Wireframes](https://www.figma.com/design/7RI3XqEc3RR6znirkakZcm/25_Wufflz_Wireframes--Copy-)
- [B2B Software](https://www.figma.com/design/NO7zf85jnhjIcJ13QGyESY/25_B2B-SOFTWARE)
- [Pitch Banken](https://www.figma.com/design/X9DzUUoJwilVPOlkqLiI2b/Pitch-Deck-%7C-Wufflz-GmbH-%7C-Editor--Banken---Copy-)
- [Co-Founders Workshop (FigJam)](https://www.figma.com/board/VmWAOTBCe1hSspmmQY6S14/Co-Founders-Workshop--Copy-)
- [Wufflz CVs](https://www.figma.com/design/NmlKQIeKhRJiPzIMTDmCN3/Wufflz-CVs)
- [Market Research (FigJam)](https://www.figma.com/board/IXxrNkPjBIPGi8QbNgpdea/Wufflz-App-Market-Research)
- [PitchDeck Template](https://www.figma.com/design/PMh6Xc8BKLbapcfrKGL8VW/Wufflz_PitchDeck_Template)
- [Proto TXErnZeob](https://www.figma.com/design/TXErnZeobIuX4hEIvko0Fe/) · [Proto-Ansicht](https://www.figma.com/proto/TXErnZeobIuX4hEIvko0Fe/)
- [Pitch Investoren v2](https://www.figma.com/design/FnhmUL3cHzDIM2HOFF2306/Pitch-Deck-)
- [Pitch Investoren v1](https://www.figma.com/design/5Fp2RQjupexSkR1eFe638X/Pitch-Deck-) · [Proto-Ansicht](https://www.figma.com/proto/5Fp2RQjupexSkR1eFe638X/)

---

## Deprecated / Optional (nicht in Active-Liste)

> Noch im Katalog für Referenz, aber nicht Teil der 10 kanonischen Dateien. Export mit `--include-deprecated`.

| Name | Key | Ordner | Grund |
|------|-----|--------|-------|
| Wagglz Dogwalking | `JjJ4CgJCqURgjohhbvcOrZ` | wagglz | ältere Dogwalking-Designs |
| Wagglz App Dogwalking | `MUvsIoZBIT0kOdIQjdn0s9` | wagglz | ältere App-Version |
| Wagglz Research Dogwalking | `23wUJ3p6E7Y6Om6qo5GF5w` | wagglz | ersetzt durch Market Research Board |
| My Rex (Copy) | `7yBGOpEg0ETNXR3cQ4bOl4` | wagglz | Research-Artefakt |
| Wufflz Website Design Dogwalking | `r8locNzgmU9mw67i5xBiRT` | wufflz | Website nicht in Active-Liste |
| Wufflz Website Design (Copy) | `I1dvZP8iRPLhO4iT6ykXid` | wufflz | Duplikat → r8loc… |
| Pitch Deck Investoren v3 | `1gagrLvuEVLZEuZr9adlhz` | wufflz | neuere v2 in Active-Liste |

---

## kits/ — Drittanbieter UI-Kits (Referenz / Preview)

> **Niedrige Priorität.** Export mit `--include-kits`.

| Name | Key | Status | Manifest |
|------|-----|--------|----------|
| Ant Design System for Figma (Preview) | `faSohMPNaRaWIimPAQAlCA` | referenz | [[kits/Figma-Manifest-ant-design-system-for-figma-preview]] |
| Nucleus Plus | `wzKhS5oRrI1FgK3cIRfCiP` | referenz | [[kits/Figma-Manifest-nucleus-plus]] |
| theProjekts Design System V2 | `YCUvHIoaxSoQSPveySgTLP` | referenz | [[kits/Figma-Manifest-theprojekts-design-system-v2]] |

---

## Migrations-Übersicht

| Status | Anzahl | Beschreibung |
|--------|--------|--------------|
| **Kanonisch (active)** | **10** | Priorität für `--all` |
| Deprecated / optional | 7 | `--include-deprecated` |
| Referenz only (Kit) | 3 | `--include-kits` |
| Duplikat (skip) | 1 | I1dvZP8iRPLhO4iT6ykXid |
| Exportiert (vollständig) | 1 | [[wufflz/Figma-Manifest-25-wufflz-wireframes]] — 18 PNGs |
| Ausstehend (kanonisch) | 9 | Rate-Limit nach erstem Batch-Lauf |
| Fehler (retry) | 9 | Manifeste auf `error` — erneut exportieren |

## Nach Export: Ingest

Einzeldatei fortsetzen (Rate-Limit beachten — ~1 Datei / 2–5 Min. Abstand):

```bash
python3 tools/figma_export.py NO7zf85jnhjIcJ13QGyESY --scale 1 --batch-size 8
python3 tools/figma_export.py X9DzUUoJwilVPOlkqLiI2b --scale 1 --batch-size 8
python3 tools/figma_export.py VmWAOTBCe1hSspmmQY6S14 --scale 1 --batch-size 5
python3 tools/figma_export.py NmlKQIeKhRJiPzIMTDmCN3 --scale 1 --batch-size 8
python3 tools/figma_export.py IXxrNkPjBIPGi8QbNgpdea --scale 1 --batch-size 5
python3 tools/figma_export.py PMh6Xc8BKLbapcfrKGL8VW --scale 1 --batch-size 8
python3 tools/figma_export.py TXErnZeobIuX4hEIvko0Fe --scale 1 --batch-size 8
python3 tools/figma_export.py FnhmUL3cHzDIM2HOFF2306 --scale 1 --batch-size 8
python3 tools/figma_export.py 5Fp2RQjupexSkR1eFe638X --scale 1 --batch-size 8
```

Ingest nach jedem erfolgreichen Export:

```bash
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/wufflz/Figma-Manifest-25-wufflz-wireframes.md"
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/wufflz/Figma-Manifest-25-b2b-software.md"
# … weitere Manifeste aus der kanonischen Liste
```
