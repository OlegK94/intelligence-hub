---
title: "Figma Index Wagglz Source"
type: source
tags: [wagglz, wufflz, tier, figma, design, migration, katalog, index]
sources: ["raw/Business/Wagglz/Design/figma-index.md"]
created: 2026-06-13
updated: 2026-06-14
summary: Master-Katalog aller Figma-Dateien für die Wagglz/Wufflz/Tier-Migration zu Obsidian — 10 kanonische Active-Dateien, 7 Deprecated/Optional, 3 Referenz-Kits; Stand 2026-06-14; 1/10 Dateien exportiert (18 PNGs), 9/10 ausstehend wegen Rate-Limit (HTTP 429)
---

# Figma Master Index — Wagglz/Wufflz (Quelldokument)

## Überblick

Dieses Quelldokument ist der maschinenlesbare Katalog aller Figma-Dateien für das Projekt [[Wagglz GmbH]] / [[Wufflz]] im Rahmen der Figma-zu-Obsidian-Migration. Es definiert die **kanonische Active-Liste** von 10 Dateien als Migrationspriorität und stellt Schnellstart-Befehle sowie Export-Anweisungen bereit.

> Maschinenlesbarer Katalog: `figma-catalog.json` · Export-Tool: `tools/figma_export.py`

**Stand:** 2026-06-14 (13:23 Retry)
**FIGMA_TOKEN:** vorhanden
**Export-Status:** 1/10 exportiert (18 PNGs), 9/10 ausstehend — Rate-Limit (HTTP 429) bei `NO7zf85jnhjIcJ13QGyESY` (25 B2B Software)

---

## Schnellstart (Export-Befehle)

```bash
# Alle kanonischen Dateien exportieren (10 active, ohne Kits/Deprecated)
python3 tools/figma_export.py --all

# Optional: auch Referenz-Kits + deprecated Einträge
python3 tools/figma_export.py --all --include-kits --include-deprecated

# Einzeldatei (design-, board- oder proto-URL / file key)
python3 tools/figma_export.py 7RI3XqEc3RR6znirkakZcm
python3 tools/figma_export.py https://www.figma.com/proto/5Fp2RQjupexSkR1eFe638X/
```

PNGs landen in `raw/assets/wagglz-tier/{file_key}/`. Pro Datei ein Manifest unter dem jeweiligen Unterordner.

**Proto-Hinweis:** `/proto/{key}/`-Links nutzen denselben File Key und dieselbe REST-API wie `/design/{key}/`.

---

## Kanonische Active-Liste (10 Dateien)

> Diese 10 Dateien sind die aktuelle Migrations-Priorität. `--all` exportiert standardmäßig nur diese.

| # | Name | Key | Typ | Ordner | Kategorie | PNGs | Wiki-Manifest |
|---|------|-----|-----|--------|-----------|------|---------------|
| 1 | 25 Wufflz Wireframes | `7RI3XqEc3RR6znirkakZcm` | design | wufflz | product | **18** | [[25 Wufflz Wireframes Figma Manifest]] |
| 2 | 25 B2B Software | `NO7zf85jnhjIcJ13QGyESY` | design | wufflz | product | 0 | [[25 B2B Software Figma Manifest]] |
| 3 | Pitch Deck Wufflz GmbH Editor Banken | `X9DzUUoJwilVPOlkqLiI2b` | design | wufflz | pitch | 0 | [[Wufflz Pitch Deck Banken]] |
| 4 | Co-Founders Workshop | `VmWAOTBCe1hSspmmQY6S14` | figjam | workshop | workshop | 0 | [[Co-Founders Workshop Figma Manifest]] |
| 5 | Wufflz CVs | `NmlKQIeKhRJiPzIMTDmCN3` | design | wufflz | product | 0 | [[Wufflz CVs Figma Manifest]] |
| 6 | Wufflz App Market Research | `IXxrNkPjBIPGi8QbNgpdea` | figjam | wagglz | research | 0 | [[Wufflz App Market Research Figma Manifest]] |
| 7 | Wufflz PitchDeck Template | `PMh6Xc8BKLbapcfrKGL8VW` | design | wufflz | pitch | 0 | [[Wufflz PitchDeck Template Figma Manifest]] |
| 8 | Proto TXErnZeob | `TXErnZeobIuX4hEIvko0Fe` | design | wufflz | product | 0 | [[Wufflz Proto TXErnZeob Figma Manifest]] |
| 9 | Pitch Deck Investoren v2 | `FnhmUL3cHzDIM2HOFF2306` | design | wufflz | pitch | 0 | [[Wufflz Pitch Investoren v2 Figma Manifest]] |
| 10 | Pitch Deck Investoren v1 | `5Fp2RQjupexSkR1eFe638X` | design | wufflz | pitch | 0 | [[Wufflz Pitch Investoren v1 Figma Manifest]] |

### Figma-URLs (Design/Editor)

| # | URL |
|---|-----|
| 1 | [Wireframes](https://www.figma.com/design/7RI3XqEc3RR6znirkakZcm/25_Wufflz_Wireframes--Copy-) |
| 2 | [B2B Software](https://www.figma.com/design/NO7zf85jnhjIcJ13QGyESY/25_B2B-SOFTWARE) |
| 3 | [Pitch Banken](https://www.figma.com/design/X9DzUUoJwilVPOlkqLiI2b/Pitch-Deck-%7C-Wufflz-GmbH-%7C-Editor--Banken---Copy-) |
| 4 | [Co-Founders Workshop (FigJam)](https://www.figma.com/board/VmWAOTBCe1hSspmmQY6S14/Co-Founders-Workshop--Copy-) |
| 5 | [Wufflz CVs](https://www.figma.com/design/NmlKQIeKhRJiPzIMTDmCN3/Wufflz-CVs) |
| 6 | [Market Research (FigJam)](https://www.figma.com/board/IXxrNkPjBIPGi8QbNgpdea/Wufflz-App-Market-Research) |
| 7 | [PitchDeck Template](https://www.figma.com/design/PMh6Xc8BKLbapcfrKGL8VW/Wufflz_PitchDeck_Template) |
| 8 | [Proto TXErnZeob](https://www.figma.com/design/TXErnZeobIuX4hEIvko0Fe/) · [Proto-Ansicht](https://www.figma.com/proto/TXErnZeobIuX4hEIvko0Fe/) |
| 9 | [Pitch Investoren v2](https://www.figma.com/design/FnhmUL3cHzDIM2HOFF2306/Pitch-Deck-) |
| 10 | [Pitch Investoren v1](https://www.figma.com/design/5Fp2RQjupexSkR1eFe638X/Pitch-Deck-) · [Proto-Ansicht](https://www.figma.com/proto/5Fp2RQjupexSkR1eFe638X/) |

---

## Deprecated / Optional (nicht in Active-Liste)

> Export mit `--include-deprecated`.

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

## Kits — Drittanbieter UI-Kits (Referenz / Preview)

> **Niedrige Priorität.** Export mit `--include-kits`.

| Name | Key | Status |
|------|-----|--------|
| Ant Design System for Figma (Preview) | `faSohMPNaRaWIimPAQAlCA` | referenz |
| Nucleus Plus | `wzKhS5oRrI1FgK3cIRfCiP` | referenz |
| theProjekts Design System V2 | `YCUvHIoaxSoQSPveySgTLP` | referenz |

---

## Migrations-Übersicht

| Status | Anzahl | Beschreibung |
|--------|--------|--------------|
| Kanonisch (active) | **10** | Priorität für `--all` |
| Deprecated / optional | 7 | `--include-deprecated` |
| Referenz only (Kit) | 3 | `--include-kits` |
| Duplikat (skip) | 1 | `I1dvZP8iRPLhO4iT6ykXid` |
| Exportiert (vollständig) | 1 | [[25 Wufflz Wireframes Figma Manifest]] — 18 PNGs |
| Ausstehend (kanonisch) | 9 | Rate-Limit nach erstem Batch-Lauf |
| Fehler (retry) | 9 | Manifeste auf `error` — erneut exportieren |

---

## Ausstehende Export-Befehle (Rate-Limit beachten — ~1 Datei / 2–5 Min. Abstand)

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

### Ingest nach erfolgreichem Export

```bash
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/wufflz/Figma-Manifest-25-wufflz-wireframes.md"
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/wufflz/Figma-Manifest-25-b2b-software.md"
# … weitere Manifeste aus der kanonischen Liste
```

---

## Verwandte Seiten

- [[Figma Migration Wagglz]] — Konzeptseite zur Migration
- [[25 Wufflz Wireframes Figma Manifest]] — einzige vollständig exportierte Datei (18 PNGs)
- [[25 B2B Software Figma Manifest]] — kanonisch; Export-Fehler 403 / 429
- [[Wufflz Pitch Deck Banken]] — kanonisch; ausstehend
- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[Oleg Personal Context]] — Projektverantwortlicher
