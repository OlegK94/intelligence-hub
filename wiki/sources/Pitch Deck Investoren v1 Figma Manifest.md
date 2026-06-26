---
title: "Pitch Deck Investoren v1 Figma Manifest"
type: source
tags: [wagglz, wufflz, tier, figma, design, pitch, manifest, investoren]
sources: ["raw/Business/Wagglz/Design/Figma-Manifest-pitch-deck-investoren-v1.md"]
created: 2026-06-13
updated: 2026-06-13
summary: Figma-Design-Datei für das Investor-Pitch-Deck von Wagglz/Wufflz (File Key 5Fp2RQjupexSkR1eFe638X) — kein Frame-Export vorhanden; API-Fehler beim Abruf (403 Invalid Token); Status ausstehend; gehört zur 10-Dateien-Migrationsliste; Kategorie pitch, Ordner wufflz/
---

# Pitch Deck Investoren v1 — Figma Manifest

## Überblick

Dieses Quelldokument erfasst das Figma-Design-Manifest für das **Investor-Pitch-Deck** des Projekts [[Wagglz GmbH]] / [[Wufflz]]. Die Datei ist canonical und Teil der aktiven 10-Dateien-Migrationsliste. Sie liegt im Ordner `wufflz/` und ist als Kategorie `pitch` klassifiziert — im Gegensatz zu den Schwesterdateien [[25 B2B Software Figma Manifest]] (Kategorie `product`) und [[25 Wufflz Wireframes Figma Manifest]] (Kategorie `product`).

> PNGs werden nach `raw/assets/wagglz-tier/5Fp2RQjupexSkR1eFe638X/` exportiert. Das vollständige Raw-Manifest liegt unter `raw/Business/Wagglz/Design/wufflz/Figma-Manifest-pitch-deck-investoren-v1.md`.

---

## Metadaten

| Feld | Wert |
|---|---|
| **Figma File Key** | `5Fp2RQjupexSkR1eFe638X` |
| **Figma URL** | [Pitch Deck Investoren v1](https://www.figma.com/design/5Fp2RQjupexSkR1eFe638X/Pitch-Deck-) |
| **Figma Prototype URL** | [Pitch Deck Investoren v1 (Proto)](https://www.figma.com/proto/5Fp2RQjupexSkR1eFe638X/) |
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
| API-Abruf | ❌ Fehler — 403 Forbidden (Invalid token) |

**Fehlerursache:** Beim Abruf über die Figma API trat ein Authentifizierungsfehler auf:
```
Figma API 403: {"status":403,"err":"Invalid token"}
```

Dies deutet auf ein Token-Problem hin (abgelaufenes oder ungültiges API-Token), nicht auf eine fehlende Datei. Sobald das Token erneuert wurde, sollte der Export nachgeholt werden.

---

## Screens & User Flows

- **Screens:** Keine Frames exportiert (Export ausstehend / blockiert durch API-Fehler)
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

Diese Datei unterscheidet sich von den anderen Figma-Manifesten in der 10-Dateien-Migrationsliste durch ihre **Kategorie `pitch`**. Während die anderen Dateien Design-Artefakte für das Produkt (B2B-Software, Wireframes) abbilden, enthält diese Datei das **Investor-Pitch-Deck** für [[Wagglz GmbH]] / [[Wufflz]]. Das Pitch Deck ist damit ein strategisches Kommunikationsmittel für externe Investoren und gibt potenziell Aufschluss über:

- Geschäftsmodell und Vision von Wagglz/Wufflz
- Marktpositionierung und Zielkunden
- Finanzprojektionen und Wachstumsstrategie
- Funding-Ziele und Investorenargumente

> ⚠️ **Offene Fragen:**
> - Was ist der aktuelle Stand des Investor-Prozesses bei Wagglz?
> - Welche Investitionssumme wird angestrebt?
> - Gibt es eine Verbindung zwischen dem Pitch-Deck-Inhalt und dem B2B-Veterinär-Kontext aus den [[25 Wufflz Wireframes Figma Manifest|Wireframes]]?
> - Wann wird der API-Token erneuert und der Export nachgeholt?

---

## Vergleich mit Schwesterdateien

| Datei | File Key | Kategorie | Status | Frames |
|---|---|---|---|---|
| **Pitch Deck Investoren v1** (diese Datei) | `5Fp2RQjupexSkR1eFe638X` | pitch | ❌ error (403) | 0 |
| [[25 B2B Software Figma Manifest]] | `NO7zf85jnhjIcJ13QGyESY` | product | ❌ error (403) | 0 |
| [[25 Wufflz Wireframes Figma Manifest]] | `7RI3XqEc3RR6znirkakZcm` | product | ✅ exportiert | 18 |

**Gemeinsamkeit der Fehler:** Beide error-Dateien scheitern an 403-Fehlern, jedoch mit unterschiedlichen Fehlermeldungen:
- Diese Datei: `{"status":403,"err":"Invalid token"}` — Token-Problem
- 25 B2B Software: `Tunnel connection failed: 403 Forbidden` — Netzwerk-/Proxy-Problem

Dies deutet auf möglicherweise unterschiedliche Ursachen hin, die separat behoben werden müssen.

---

## Ingest-Befehl

```bash
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/wufflz/Figma-Manifest-pitch-deck-investoren-v1.md"
```

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[25 B2B Software Figma Manifest]] — Schwesterdatei (Export-Fehler, Netzwerkproblem)
- [[25 Wufflz Wireframes Figma Manifest]] — Schwesterdatei (erfolgreich exportiert, 18 Frames)
- [[Oleg Personal Context]] — Projektverantwortlicher
