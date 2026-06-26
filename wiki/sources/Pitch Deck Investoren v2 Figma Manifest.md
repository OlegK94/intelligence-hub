---
title: "Pitch Deck Investoren v2 Figma Manifest"
type: source
tags: [wagglz, wufflz, tier, figma, design, pitch, manifest, investoren]
sources: ["raw/Business/Wagglz/Design/Figma-Manifest-pitch-deck-investoren-v2.md"]
created: 2026-06-13
updated: 2026-06-13
summary: Figma-Design-Manifest für das Wagglz/Wufflz Investor Pitch Deck v2 (File Key FnhmUL3cHzDIM2HOFF2306) — kein Frame-Export vorhanden; API-Fehler beim Abruf (403 Invalid token); Status ausstehend; canonical, Teil der 10-Dateien-Migrationsliste; Kategorie pitch
---

# Pitch Deck Investoren v2 — Figma Manifest

## Überblick

Dieses Quelldokument erfasst das Figma-Design-Manifest für das **Investor Pitch Deck v2** im Rahmen von [[Wagglz GmbH]] / [[Wufflz]]. Die Datei ist canonical und Teil der aktiven 10-Dateien-Migrationsliste. Sie liegt im Ordner `wufflz/`.

> PNGs werden nach `raw/assets/wagglz-tier/FnhmUL3cHzDIM2HOFF2306/` exportiert. Das vollständige Raw-Manifest liegt unter `raw/Business/Wagglz/Design/wufflz/Figma-Manifest-pitch-deck-investoren-v2.md`.

---

## Metadaten

| Feld | Wert |
|---|---|
| **Figma File Key** | `FnhmUL3cHzDIM2HOFF2306` |
| **Figma URL** | [Pitch Deck Investoren v2](https://www.figma.com/design/FnhmUL3cHzDIM2HOFF2306/Pitch-Deck-) |
| **Figma Prototype URL** | — (nicht angegeben) |
| **Typ** | design |
| **Kategorie** | pitch |
| **Ordner** | `wufflz/` |
| **Migration Status** | `error` |
| **Canonical** | ✅ Ja (in 10-Dateien-Migrationsliste) |
| **Stand** | 2026-06-13 |

---

## Export-Status

| Element | Status |
|---|---|
| Frames exportiert | *(keine)* |
| PNGs vorhanden | ❌ |
| API-Abruf | ❌ Fehler — 403 Invalid token |

**Fehlerursache:** Beim Abruf über die Figma API trat ein Authentifizierungsfehler auf:
```
Figma API 403: {"status":403,"err":"Invalid token"}
```

Dies deutet auf ein Problem mit dem verwendeten API-Token hin, nicht auf eine fehlende oder nicht existierende Figma-Datei. Der Fehlertyp unterscheidet sich leicht von den anderen fehlgeschlagenen Manifesten in der Migrationsliste, bei denen ein Netzwerkfehler (Tunnel connection failed) auftrat — hier ist es ein expliziter `Invalid token`-Fehler.

---

## Screens & User Flows

- **Screens:** Keine Frames exportiert (Export ausstehend)
- **User Flows:** Nicht dokumentiert (ausstehend)

---

## Design Tokens

| Token | Wert |
|---|---|
| Primary Color | — (nicht ausgelesen) |
| Font | — (nicht ausgelesen) |

Alle Token-Informationen sind wegen des API-Fehlers noch nicht verfügbar.

---

## Einordnung im Wagglz-Design-Kontext

Diese Datei ist das **Investor Pitch Deck** für [[Wagglz GmbH]] / [[Wufflz]] und unterscheidet sich von den anderen Figma-Manifesten in der Migrationsliste durch die Kategorie `pitch` (statt `product`). Während die anderen Dateien UX/UI-Produktdesigns darstellen, ist dieses Deck für Investorenpräsentationen bestimmt.

> ⚠️ **Offene Fragen:**
> - Welche Inhalte enthält das Pitch Deck v2? (Marktgröße, Produktvision, Finanzierungsbedarf, Wettbewerbsanalyse?)
> - Was ist der Unterschied zwischen v1 und v2 des Pitch Decks?
> - Wann wird der API-Token-Fehler behoben und der Export nachgeholt?
> - Ist dieses Pitch Deck für laufende Investorengespräche aktiv in Verwendung?

---

## Vergleich mit Schwesterdateien in der Migrationsliste

| Datei | File Key | Status | Frames | Kategorie |
|---|---|---|---|---|
| **Pitch Deck Investoren v2** (diese Datei) | `FnhmUL3cHzDIM2HOFF2306` | ❌ error (403 Invalid token) | 0 | pitch |
| [[25 B2B Software Figma Manifest]] | `NO7zf85jnhjIcJ13QGyESY` | ❌ error (403 Forbidden) | 0 | product |
| [[25 Wufflz Wireframes Figma Manifest]] | `7RI3XqEc3RR6znirkakZcm` | ✅ exportiert | 18 | product |

> **Fehlertyp-Unterschied:** Die anderen Fehler-Manifeste zeigen einen Netzwerkfehler (`Tunnel connection failed: 403 Forbidden`), während diese Datei explizit `{"status":403,"err":"Invalid token"}` zurückgibt. Dies könnte auf unterschiedliche Zugriffsberechtigungen des verwendeten API-Tokens hindeuten.

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie, zu der diese Datei gehört
- [[25 B2B Software Figma Manifest]] — Schwesterdatei (Export-Fehler 403)
- [[25 Wufflz Wireframes Figma Manifest]] — Schwesterdatei (erfolgreich exportiert, 18 Frames)
- [[Oleg Personal Context]] — Projektverantwortlicher
