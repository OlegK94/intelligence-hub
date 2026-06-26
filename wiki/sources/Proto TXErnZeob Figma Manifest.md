---
title: "Proto TXErnZeob Figma Manifest"
type: source
tags: [wagglz, wufflz, tier, figma, design, manifest, proto, api-fehler]
sources: ["raw/Business/Wagglz/Design/Figma-Manifest-proto-txernzeob.md"]
created: 2026-06-13
updated: 2026-06-13
summary: Figma-Design-Datei Proto TXErnZeob (File Key TXErnZeobIuX4hEIvko0Fe) — kein Frame-Export vorhanden; API-Fehler beim Abruf (403 Invalid token); canonical; Teil der 10-Dateien-Migrationsliste; Ordner wufflz/
---

# Proto TXErnZeob — Figma Manifest

## Überblick

Dieses Quelldokument erfasst das Figma-Design-Manifest für das Projekt **Proto TXErnZeob** im Rahmen von [[Wagglz GmbH]] / [[Wufflz]]. Die Datei ist canonical und Teil der aktiven 10-Dateien-Migrationsliste. Sie liegt im Ordner `wufflz/`.

> PNGs werden nach `raw/assets/wagglz-tier/TXErnZeobIuX4hEIvko0Fe/` exportiert. Das vollständige Raw-Manifest liegt unter `raw/Business/Wagglz/Design/wufflz/Figma-Manifest-proto-txernzeob.md`.

---

## Metadaten

| Feld | Wert |
|---|---|
| **Figma File Key** | `TXErnZeobIuX4hEIvko0Fe` |
| **Figma URL** | [Proto TXErnZeob](https://www.figma.com/design/TXErnZeobIuX4hEIvko0Fe/) |
| **Figma Prototype URL** | [Proto TXErnZeob (Proto)](https://www.figma.com/proto/TXErnZeobIuX4hEIvko0Fe/) |
| **Typ** | design |
| **Kategorie** | product |
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

Dies unterscheidet sich geringfügig vom Fehler bei [[25 B2B Software Figma Manifest]] (Netzwerkfehler / Tunnel connection failed 403 Forbidden): Hier liegt ein explizit ungültiges Token vor — der verwendete Figma-API-Token ist abgelaufen oder falsch konfiguriert.

---

## Screens & User Flows

- **Screens:** Keine Frames exportiert (Export ausstehend)
- **User Flows:** Nicht dokumentiert (Quelldokument leer — ausstehend)

---

## Design Tokens

| Token | Wert |
|---|---|
| Primary Color | — (nicht ausgelesen) |
| Font | — (nicht ausgelesen) |

Alle Token-Informationen sind wegen des API-Fehlers noch nicht verfügbar.

---

## Vergleich mit Schwesterdateien

| Datei | File Key | Status | Frames | Fehlertyp |
|---|---|---|---|---|
| **Proto TXErnZeob** (diese Datei) | `TXErnZeobIuX4hEIvko0Fe` | ❌ error | 0 | 403 Invalid token |
| [[25 B2B Software Figma Manifest]] | `NO7zf85jnhjIcJ13QGyESY` | ❌ error | 0 | 403 Tunnel connection failed |
| [[25 Wufflz Wireframes Figma Manifest]] | `7RI3XqEc3RR6znirkakZcm` | ✅ exportiert | 18 | — |

Alle drei Dateien gehören zur gleichen 10-Dateien-Migrationsliste und zum `wufflz/`-Ordner. Nur die Wireframes-Datei wurde bisher erfolgreich exportiert.

---

## Besonderheit: Proto-URL vorhanden

Im Gegensatz zu [[25 B2B Software Figma Manifest]] und [[25 Wufflz Wireframes Figma Manifest]] enthält dieses Manifest **eine dedizierte Prototype-URL**:

- **Design-URL:** `https://www.figma.com/design/TXErnZeobIuX4hEIvko0Fe/`
- **Proto-URL:** `https://www.figma.com/proto/TXErnZeobIuX4hEIvko0Fe/`

Die Existenz einer Proto-URL deutet darauf hin, dass dieses Figma-File **interaktive Prototype-Flows** enthält — ein Hinweis, dass es sich um ein fortgeschritteneres Design-Artefakt handelt als ein reines Wireframe oder ein statisches Design-File.

---

## Offene Fragen

> ⚠️ **Offene Fragen:**
> - Was zeigt der Prototype inhaltlich? (Welche User Flows sind interaktiv verlinkt?)
> - Zu welchem Produkt- oder Feature-Bereich gehört „Proto TXErnZeob"? (Onboarding, Dashboard, Feature-X?)
> - Wann wird der API-Token erneuert, sodass der Export nachgeholt werden kann?
> - Welche der verbleibenden 7 Dateien der 10-Dateien-Migrationsliste sind ebenfalls mit API-Fehlern behaftet?

---

## Einordnung im Wagglz-Design-Kontext

Diese Datei gehört zum **Wufflz-Design-System** innerhalb von [[Wagglz GmbH]]. Das Vorhandensein einer Prototype-URL legt nahe, dass dieses File nicht nur statische Screens enthält, sondern **verknüpfte, interaktive Flows** — möglicherweise ein Click-Through-Prototype für User-Testing oder Stakeholder-Präsentationen.

Die Namensgebung „Proto" (statt „Wireframes" wie bei der Schwesterdatei) bestätigt diesen Prototype-Charakter.

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[25 B2B Software Figma Manifest]] — Schwesterdatei (403-Fehler, kein Frame)
- [[25 Wufflz Wireframes Figma Manifest]] — Schwesterdatei (18 Frames erfolgreich exportiert)
- [[Oleg Personal Context]] — Projektverantwortlicher
