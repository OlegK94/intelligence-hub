---
title: "Wufflz App Market Research Figma Manifest"
type: source
tags: [wagglz, wufflz, tier, figma, design, research, figjam, workshop, manifest, market-research]
sources: ["raw/Business/Wagglz/Design/legacy-wagglz/Figma-Manifest-wufflz-app-market-research.md"]
created: 2026-06-13
updated: 2026-06-13
summary: FigJam-Board „Wufflz App Market Research" (File Key IXxrNkPjBIPGi8QbNgpdea) im legacy wagglz/-Ordner; API-Fehler 403 beim Figma-Abruf; keine Frames exportiert; Status error; canonical in der 10-Dateien-Migrationsliste; FigJam-Typ deutet auf Workshop-/Research-Format hin
---

# Wufflz App Market Research — Figma Manifest

## Überblick

Dieses Quelldokument erfasst das Figma-Manifest für das **Wufflz App Market Research**-Board im Rahmen von [[Wagglz GmbH]] / [[Wufflz]]. Es handelt sich um eine **FigJam-Datei** (kollaboratives Whiteboard-Format), nicht um eine klassische Design-Datei — was auf einen Workshop-, Brainstorming- oder Research-Kontext hindeutet.

Die Datei ist **canonical** und Teil der aktiven 10-Dateien-Migrationsliste. Allerdings schlug der API-Abruf fehl (403 Invalid Token), sodass keine Frames exportiert werden konnten.

> PNGs (bei erfolgreichem Export) unter `raw/assets/wagglz-tier/IXxrNkPjBIPGi8QbNgpdea/`. Das Raw-Manifest liegt unter `raw/Business/Wagglz/Design/legacy-wagglz/Figma-Manifest-wufflz-app-market-research.md`.

---

## Metadaten

| Feld | Wert |
|---|---|
| **Figma File Key** | `IXxrNkPjBIPGi8QbNgpdea` |
| **Figma URL** | [Wufflz App Market Research](https://www.figma.com/board/IXxrNkPjBIPGi8QbNgpdea/Wufflz-App-Market-Research) |
| **Figma Prototype URL** | — (nicht vorhanden) |
| **Typ** | figjam |
| **Kategorie** | research |
| **Ordner** | `wagglz/` (legacy) |
| **Migration Status** | `error` |
| **Canonical** | ✅ Ja (in 10-Dateien-Migrationsliste) |
| **Reference Only** | ❌ (canonical, kein reines Referenz-Dokument) |
| **Stand** | 2026-06-13 |

---

## Export-Status

| Element | Status |
|---|---|
| Frames exportiert | *(keine)* |
| PNGs vorhanden | ❌ |
| API-Abruf | ❌ Fehler — `403 Invalid Token` |

**Fehlerdetail:**
```
Figma API 403: {"status":403,"err":"Invalid token"}
```

Der Fehler `Invalid token` deutet auf ein **Authentifizierungsproblem** mit dem Figma-API-Token hin — nicht notwendigerweise auf eine fehlende oder gelöschte Datei. Dieser Fehlertyp tritt auch bei der Schwesterdatei [[25 B2B Software Figma Manifest]] auf (dort als `Tunnel connection failed: 403 Forbidden`), was auf ein gemeinsames Token- oder Proxy-Problem hindeutet.

**Exportbefehl (sobald Token erneuert):**
```bash
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/wagglz/Figma-Manifest-wufflz-app-market-research.md"
```

---

## Typ: FigJam

Das Dokument ist als `figma_type: figjam` klassifiziert — dies unterscheidet sich grundlegend von Design-Dateien:

| Aspekt | Design-Datei (`design`) | FigJam-Board (`figjam`) |
|---|---|---|
| **Format** | Strukturierte Frames / Screens | Offenes Whiteboard |
| **Inhalt** | UI-Mockups, Prototypen | Sticky Notes, Diagramme, Flows, Research |
| **Export** | PNG-Frames sinnvoll | Frames weniger relevant; Gesamtboard wichtiger |
| **Zweck** | Produkt-Design | Collaboration, Research, Workshops |

Der Titel „App Market Research" bestätigt: Es handelt sich vermutlich um ein **Market-Research-Workshop-Board** — möglicherweise mit Wettbewerbsanalysen, User-Research-Findings oder Produktpositionierungs-Überlegungen für die Wufflz-App.

---

## Ordner: legacy wagglz/ vs. canonical wufflz/

Das Manifest liegt im Ordner `wagglz/` (legacy), während canonical produktive Dateien im Ordner `wufflz/` liegen:

| Ordner | Zweck | Beispiele |
|---|---|---|
| `wufflz/` | Aktive produktive Designdateien | [[25 Wufflz Wireframes Figma Manifest]], [[25 B2B Software Figma Manifest]] |
| `wagglz/` (legacy) | Ältere / legacy Dateien | Diese Datei |
| `kits/` | Drittanbieter-UI-Kits | [[Ant Design System for Figma Preview]] |

Trotz legacy-Ordner ist das Manifest als **canonical** markiert und in der 10-Dateien-Migrationsliste aufgeführt — der Inhalt ist also relevant, auch wenn die Datei aus einer älteren Entwicklungsphase stammt.

---

## Design Tokens

| Token | Wert |
|---|---|
| Primary Color | — (nicht ausgelesen, API-Fehler) |
| Font | — (nicht ausgelesen, API-Fehler) |

---

## Vergleich mit anderen Wagglz/Wufflz-Figma-Dateien

| Datei | File Key | Typ | Status | Frames | Ordner |
|---|---|---|---|---|---|
| **Wufflz App Market Research** (diese Datei) | `IXxrNkPjBIPGi8QbNgpdea` | figjam | ❌ error (403) | 0 | `wagglz/` (legacy) |
| [[25 Wufflz Wireframes Figma Manifest]] | `7RI3XqEc3RR6znirkakZcm` | design | ✅ exportiert | 18 | `wufflz/` |
| [[25 B2B Software Figma Manifest]] | `NO7zf85jnhjIcJ13QGyESY` | design | ❌ error (403) | 0 | `wufflz/` |
| [[Ant Design System for Figma Preview]] | `faSohMPNaRaWIimPAQAlCA` | design | ⏳ ausstehend | ? | `kits/` |

---

## Offene Fragen

> ⚠️ **Offene Fragen:**
> - Was genau ist der Inhalt des FigJam-Boards? (Wettbewerbsanalyse, User Research, Produkt-Positioning?)
> - Welche Apps/Produkte wurden im Market-Research analysiert?
> - Stammt das Board aus der frühen Ideenfindungsphase oder ist es aktueller Research?
> - Wann wird das Figma-API-Token erneuert, damit der Export nachgeholt werden kann?
> - Hat das Board Verbindungen zum B2B-Account-Erstellungsflow aus [[25 Wufflz Wireframes Figma Manifest]]?

---

## Einordnung im Wagglz-Design-Kontext

Das FigJam-Board „Wufflz App Market Research" bildet vermutlich den **Research-Unterbau** für die Design-Entscheidungen in [[Wufflz]]. Market-Research-Findings aus diesem Board könnten direkt in den B2B-Onboarding-Flow (9 Schritte) des [[25 Wufflz Wireframes Figma Manifest]] eingeflossen sein.

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[25 Wufflz Wireframes Figma Manifest]] — canonical B2B-Wireframe-Datei (Design-Ergebnis des Research)
- [[25 B2B Software Figma Manifest]] — Schwesterdatei mit gleichartigem API-Fehler
- [[Ant Design System for Figma Preview]] — UI-Kit-Referenz im selben Projekt
- [[Wagglz Wufflz Design README]] — übergeordnetes README-Quelldokument
- [[Figma Index Wagglz]] — Master-Index aller Figma-Dateien
- [[Oleg Personal Context]] — Projektverantwortlicher
