---
title: "Co-Founders Workshop FigJam"
type: source
tags: [wagglz, figma, figjam, workshop, co-founders, design, board]
sources: ["raw/Business/Wagglz/Design/workshop/README.md"]
created: 2026-06-18
updated: 2026-06-18
summary: FigJam-Board für den Co-Founders Workshop von Wagglz (File Key VmWAOTBCe1hSspmmQY6S14) — enthält Sections, Stickies und ggf. Seiten-PNGs; Export via figma_export.py; bei komplexen Boards alternativ manuell als PDF aus Figma
---

# Co-Founders Workshop — FigJam

## Überblick

Dieses Quelldokument erfasst das FigJam-Board für den **Co-Founders Workshop** im Rahmen von [[Wagglz GmbH]]. Das Board liegt im Unterordner `workshop/` des Design-Bereichs und wird über den zugehörigen File Key per Figma REST-API exportiert.

---

## Metadaten

| Feld | Wert |
|---|---|
| **Board-Name** | Co-Founders Workshop |
| **Figma File Key** | `VmWAOTBCe1hSspmmQY6S14` |
| **Typ** | FigJam |
| **Ordner** | `workshop/` |
| **Manifest-Verknüpfung** | [[Figma-Manifest-co-founders-workshop]] |

---

## Export

FigJam nutzt dieselbe Figma REST-API wie reguläre Design-Dateien. Der Export erfasst:
- **Sections** (Board-Abschnitte)
- **Stickies** (Haftnotizen)
- **Seiten** ggf. als PNG

**Exportbefehl:**
```bash
python3 tools/figma_export.py VmWAOTBCe1hSspmmQY6S14
```

> Bei komplexen Boards alternativ **manuell als PDF aus Figma** exportieren — dies kann bei umfangreichen FigJam-Boards zuverlässiger sein als der API-Export.

---

## Export-Status

| Element | Status |
|---|---|
| Sections exportiert | ⏳ Ausstehend |
| Stickies exportiert | ⏳ Ausstehend |
| PNGs vorhanden | ❌ |
| API-Abruf | ⏳ Ausstehend |

---

## Einordnung im Wagglz-Design-Kontext

Das FigJam-Board unterscheidet sich von den canonical Produkt-Designdateien im Ordner `wufflz/` oder `product/`:

| Aspekt | Produkt-Designs (`wufflz/`, `product/`) | Workshop-Boards (`workshop/`) |
|---|---|---|
| **Art** | UI/UX-Designdateien (Wireframes, Screens) | Kollaborations-/Workshop-Boards |
| **Format** | Figma Design | FigJam |
| **Inhalt** | Frames, Komponenten, Prototypen | Sections, Stickies, Diagramme |
| **Canonical** | ✅ Ja (Produktdokumentation) | ⚠️ Workshop-Kontext (strategisch) |
| **Beispiele** | [[25 Wufflz Wireframes Figma Manifest]], [[25 B2B Software Figma Manifest]] | Diese Seite |

Der Co-Founders Workshop enthält voraussichtlich strategische Entscheidungen, Problemdefinitionen oder frühe Produktkonzepte der [[Wagglz GmbH]]-Gründer.

---

## Offene Fragen

> ⚠️ **Offene Fragen:**
> - Was waren die Themen und Ergebnisse des Co-Founders Workshops?
> - Welche Sections/Stickies sind auf dem Board vorhanden?
> - Wann fand der Workshop statt?
> - Welche Personen (Co-Founder) haben am Workshop teilgenommen?
> - Gibt es Follow-up-Dokumente oder Entscheidungen aus dem Workshop?

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Figma Index Wagglz]] — Master-Index aller Figma-Dateien
- [[Wagglz Wufflz Design README]] — übergeordnetes README-Quelldokument
- [[25 Wufflz Wireframes Figma Manifest]] — canonical B2B-Produkt-Wireframes
- [[25 B2B Software Figma Manifest]] — canonical B2B-Software-Designdatei
- [[Ant Design System for Figma Preview]] — Drittanbieter-Kit im Design-Kontext
- [[Oleg Personal Context]] — Projektverantwortlicher
