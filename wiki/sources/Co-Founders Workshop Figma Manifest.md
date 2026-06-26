---
title: "Co-Founders Workshop Figma Manifest"
type: source
tags: [wagglz, wufflz, tier, figma, design, figjam, workshop, manifest]
sources: ["raw/Business/Wagglz/Design/workshop/Figma-Manifest-co-founders-workshop.md"]
created: 2026-06-13
updated: 2026-06-13
summary: FigJam-Workshop-Board für den Co-Founders Workshop (File Key VmWAOTBCe1hSspmmQY6S14); kein Frame-Export vorhanden; Status ausstehend (API-Fehler 429 Rate Limit beim Abruf); liegt im Ordner `workshop/`; canonical und Teil der 10-Dateien-Migrationsliste
---

# Co-Founders Workshop — Figma Manifest

## Überblick

Dieses Quelldokument erfasst das Figma-Manifest für das **Co-Founders Workshop**-Board im Rahmen von [[Wagglz GmbH]] / [[Wufflz]]. Anders als die Produktdesign-Dateien handelt es sich hierbei um ein **FigJam**-Board (kollaboratives Whiteboard-Format), das offenbar im Kontext eines Gründer-Workshops genutzt wurde. Die Datei ist canonical und Teil der aktiven 10-Dateien-Migrationsliste.

> PNGs werden (bei erfolgreichem Export) nach `raw/assets/wagglz-tier/VmWAOTBCe1hSspmmQY6S14/` exportiert. Das Raw-Manifest liegt unter `raw/Business/Wagglz/Design/workshop/Figma-Manifest-co-founders-workshop.md`.

---

## Metadaten

| Feld | Wert |
|---|---|
| **Figma File Key** | `VmWAOTBCe1hSspmmQY6S14` |
| **Figma URL** | [Co-Founders Workshop](https://www.figma.com/board/VmWAOTBCe1hSspmmQY6S14/Co-Founders-Workshop--Copy-) |
| **Figma Prototype URL** | — (nicht angegeben) |
| **Typ** | figjam |
| **Kategorie** | workshop |
| **Ordner** | `workshop/` |
| **Migration Status** | `ausstehend` |
| **Canonical** | ✅ Ja (in 10-Dateien-Migrationsliste) |
| **Stand** | 2026-06-13 |

---

## Export-Status

| Element | Status |
|---|---|
| Frames exportiert | *(keine Frames exportiert)* |
| PNGs vorhanden | ❌ |
| API-Abruf | ❌ Fehlgeschlagen — Rate Limit (HTTP 429) |

> ⚠️ **API-Fehler:** Beim letzten Abruf hat die Figma API den Fehler `429 Rate limit exceeded` zurückgegeben. Der Export muss zu einem späteren Zeitpunkt wiederholt werden.

**Exportbefehl:**
```bash
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/workshop/Figma-Manifest-co-founders-workshop.md"
# oder direkt:
python3 tools/figma_export.py VmWAOTBCe1hSspmmQY6S14
```

---

## FigJam vs. Figma Design — Besonderheiten

Da es sich um ein **FigJam**-Board handelt (Typ `figjam`, nicht `design`), gelten andere Export-Konventionen:

| Aspekt | Figma Design | FigJam |
|---|---|---|
| **Format** | Pixel-genaue Frames | Freies Whiteboard-Layout |
| **Frames** | Explizit benannt, exportierbar | Keine klassischen Frames |
| **Export-Methode** | PNG per Frame | Gesamtboard-Screenshot oder Sektionen |
| **Nutzung** | UI-Prototypen, Screens | Brainstorming, Workshops, Flows |
| **Priorität** | Hoch (Produktdesign) | Mittel (Prozessdokumentation) |

FigJam-Boards enthalten typischerweise: Sticky Notes, Diagramme, Flowcharts, Brainstorming-Inhalte — kein pixel-perfektes UI-Design.

---

## Inhalt des Workshops (noch nicht ausgelesen)

Da der API-Abruf mit einem Rate-Limit-Fehler fehlschlug, sind keine Inhaltsdetails verfügbar. Folgende Informationen sind noch unbekannt:

- Was wurde im Co-Founders Workshop erarbeitet?
- Welche Themen wurden diskutiert (Strategie, Produkt, Finanzen)?
- Wer hat an dem Workshop teilgenommen?
- Wann fand der Workshop statt?

> ⚠️ **Offene Fragen:**
> - Was ist der inhaltliche Fokus des Boards — Produktstrategie, Geschäftsmodell, Team-Struktur?
> - Ist dies ein internes Wagglz-Team-Workshop oder ein externer Workshop mit Investoren/Partnern?
> - Handelt es sich um die Kopie eines Originals (der Dateiname enthält „Copy")?
> - Warum liegt die Datei im `workshop/`-Ordner — gibt es weitere Workshop-Boards?

---

## Einordnung im Wagglz-Design-Kontext

### Vergleich mit anderen Figma-Dateien

| Datei | File Key | Typ | Ordner | Status | Frames |
|---|---|---|---|---|---|
| **Co-Founders Workshop** (diese Datei) | `VmWAOTBCe1hSspmmQY6S14` | figjam | `workshop/` | ⏳ ausstehend (429) | 0 |
| [[25 Wufflz Wireframes Figma Manifest]] | `7RI3XqEc3RR6znirkakZcm` | design | `wufflz/` | ✅ exportiert | 18 |
| [[25 B2B Software Figma Manifest]] | `NO7zf85jnhjIcJ13QGyESY` | design | `product/` | ⏳ ausstehend | 0 |
| [[Ant Design System for Figma Preview]] | `faSohMPNaRaWIimPAQAlCA` | design | `kits/` | ⏳ ausstehend | 0 |

Das Co-Founders Workshop-Board ist die einzige **FigJam**-Datei in der bekannten Migrationsliste — alle anderen Dateien sind `design`-Typ.

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[25 Wufflz Wireframes Figma Manifest]] — canonical B2B-Wireframe-Datei (erfolgreich exportiert)
- [[25 B2B Software Figma Manifest]] — canonical B2B-Software-Datei (ausstehend)
- [[Ant Design System for Figma Preview]] — Drittanbieter-Kit (kits/-Ordner)
- [[Wagglz Wufflz Design README]] — übergeordnetes README-Quelldokument
- [[Figma Index Wagglz]] — Master-Index aller Figma-Dateien
- [[Oleg Personal Context]] — Projektverantwortlicher
