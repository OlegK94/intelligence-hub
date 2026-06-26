---
title: "Wagglz Wufflz Design README"
type: source
tags: [wagglz, wufflz, tier, figma, design, readme, wireframes, website, pitch-deck, manifest, export]
sources: ["raw/Business/Wagglz/Design/README.md"]
created: 2026-06-17
updated: 2026-06-17
summary: README-Übersicht für den Wufflz/Tier Figma-Design-Ordner — listet vier Haupt-Figma-Dateien (Wireframes, Website Design, Pitch Deck Banken, Pitch Investoren v1–v3), einen Duplikat-Hinweis und den Export-Befehl; Master-Index verweist auf figma-index
---

# Wagglz / Wufflz Design — README

## Überblick

Dieses Quelldokument ist das README für den Figma-Design-Ordner der [[Wagglz GmbH]] / [[Wufflz]]-Projekte. Es dient als Navigationshilfe für alle Figma-Dateien im Ordner `wufflz/` und verweist auf einzelne Manifest-Seiten sowie den zentralen [[Figma Index Wagglz]].

> Pfad im Raw-Vault: `raw/Business/Wagglz/Design/README.md`

---

## Dateiübersicht

| Datei | File Key | Manifest-Seite |
|---|---|---|
| **25 Wufflz Wireframes** | `7RI3XqEc3RR6znirkakZcm` | [[25 Wufflz Wireframes Figma Manifest]] |
| **Wufflz Website Design** | `r8locNzgmU9mw67i5xBiRT` | [[Wufflz Website Design Figma Manifest]] |
| **Pitch Deck Banken** | `X9DzUUoJwilVPOlkqLiI2b` | [[Wufflz Pitch Deck Banken Figma Manifest]] |
| **Pitch Investoren v1–v3** | `5Fp2…` / `Fnhm…` / `1gag…` | siehe [[Figma Index Wagglz]] |

### Duplikat-Hinweis

| File Key | Status |
|---|---|
| `I1dvZP8iRPLhO4iT6ykXid` | ⚠️ **Duplikat** — identisch mit Website-Design (`r8locNzgmU9mw67i5xBiRT`); **nicht exportieren** |

---

## Export-Anweisung

```bash
python3 tools/figma_export.py --all --folder wufflz
```

- **Ausgabepfad:** `raw/assets/wagglz-tier/{file_key}/`
- **Master-Index:** [[Figma Index Wagglz]]

---

## Einordnung

Dieses README fungiert als Verzeichnis für alle Figma-Dateien im Wufflz-Design-Ordner. Die einzelnen Manifestdateien enthalten die detaillierten Frame-Listen und Export-Status-Informationen:

- [[25 Wufflz Wireframes Figma Manifest]] — bereits ingested; 18 Frames exportiert; B2B-Account-Flow dokumentiert
- [[25 B2B Software Figma Manifest]] — bereits ingested; Export-Fehler (403 Forbidden)
- [[Wufflz Website Design Figma Manifest]] — noch zu ingestieren
- [[Wufflz Pitch Deck Banken Figma Manifest]] — noch zu ingestieren
- Pitch Investoren v1–v3 — File Keys unvollständig (nur Präfixe); Details im [[Figma Index Wagglz]]

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[Figma Index Wagglz]] — Master-Index aller Figma-Dateien
- [[25 Wufflz Wireframes Figma Manifest]] — existierende Manifest-Seite (18 Frames)
- [[25 B2B Software Figma Manifest]] — existierende Manifest-Seite (Export-Fehler)
- [[Wufflz Website Design]] — Entität für die Website-Design-Datei
- [[Wufflz Pitch Deck Banken]] — Entität für das Banken-Pitchdeck
- [[Wufflz Pitch Investoren]] — Entität für die Investoren-Pitchdecks
- [[Oleg Personal Context]] — Projektverantwortlicher
