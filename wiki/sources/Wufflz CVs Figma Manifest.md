---
title: "Wufflz CVs Figma Manifest"
type: source
tags: [wagglz, wufflz, tier, figma, design, manifest, cvs, api-fehler]
sources: ["raw/Business/Wagglz/Design/Figma-Manifest-wufflz-cvs.md"]
created: 2026-06-13
updated: 2026-06-13
summary: Figma-Design-Datei für Wufflz CVs (File Key NmlKQIeKhRJiPzIMTDmCN3) — kein Frame-Export vorhanden; API-Fehler beim Abruf (403 Invalid token); Status ausstehend; canonical, Teil der 10-Dateien-Migrationsliste; Ordner wufflz/
---

# Wufflz CVs — Figma Manifest

## Überblick

Dieses Quelldokument erfasst das Figma-Design-Manifest für das Projekt **Wufflz CVs** im Rahmen von [[Wagglz GmbH]] / [[Wufflz]]. Die Datei ist als **canonical** markiert und gehört zur aktiven 10-Dateien-Migrationsliste. Sie liegt im Ordner `wufflz/` — gemeinsam mit den Schwesterdateien [[25 B2B Software Figma Manifest]] und [[25 Wufflz Wireframes Figma Manifest]].

> PNGs werden nach `raw/assets/wagglz-tier/NmlKQIeKhRJiPzIMTDmCN3/` exportiert. Das vollständige Raw-Manifest liegt unter `raw/Business/Wagglz/Design/wufflz/Figma-Manifest-wufflz-cvs.md`.

---

## Metadaten

| Feld | Wert |
|---|---|
| **Figma File Key** | `NmlKQIeKhRJiPzIMTDmCN3` |
| **Figma URL** | [Wufflz CVs](https://www.figma.com/design/NmlKQIeKhRJiPzIMTDmCN3/Wufflz-CVs) |
| **Figma Prototype URL** | — (nicht angegeben) |
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
| API-Abruf | ❌ Fehler — 403 Forbidden (Invalid token) |

**Fehlerursache:** Beim Abruf über die Figma API trat ein Authentifizierungsfehler auf:
```
Figma API 403: {"status":403,"err":"Invalid token"}
```

Dies deutet auf ein ungültiges oder abgelaufenes Figma-API-Token hin — kein Netzwerkproblem wie bei [[25 B2B Software Figma Manifest]] (Tunnel connection failed), sondern eine direkte Authentifizierungsablehnung durch die Figma-API.

---

## Screens & User Flows

- **Screens:** Keine Frames exportiert (Export ausstehend / blockiert durch API-Fehler)
- **User Flows:** Nicht dokumentiert (ausstehend)

Der Dateiname „Wufflz CVs" lässt auf Inhalte im Zusammenhang mit **Lebensläufen oder Kompetenzprofilen** schließen — möglicherweise Mitarbeiter- oder Tierärzte-Profile innerhalb der Wufflz-Plattform. Dies ist jedoch eine Interpretation; der genaue Inhalt ist wegen des API-Fehlers unbekannt.

---

## Design Tokens

| Token | Wert |
|---|---|
| Primary Color | — (nicht ausgelesen, API-Fehler) |
| Font | — (nicht ausgelesen, API-Fehler) |

Alle Token-Informationen sind wegen des API-Fehlers noch nicht verfügbar.

---

## Fehlervergleich mit Schwesterdateien

| Datei | File Key | Fehlertyp | Status |
|---|---|---|---|
| **Wufflz CVs** (diese Datei) | `NmlKQIeKhRJiPzIMTDmCN3` | 403 Invalid token | ❌ error |
| [[25 B2B Software Figma Manifest]] | `NO7zf85jnhjIcJ13QGyESY` | 403 Tunnel connection failed | ❌ error |
| [[25 Wufflz Wireframes Figma Manifest]] | `7RI3XqEc3RR6znirkakZcm` | — (kein Fehler) | ✅ exportiert (18 Frames) |

Beide fehlgeschlagenen Dateien geben HTTP-403-Fehler zurück, jedoch mit unterschiedlichen Fehlerbeschreibungen:
- **Invalid token** (diese Datei) → API-Token ungültig oder abgelaufen
- **Tunnel connection failed** ([[25 B2B Software Figma Manifest]]) → Proxy-/Netzwerkproblem

---

## Einordnung im Wagglz-Design-Kontext

Diese Datei ist Teil des **Wufflz-Design-Systems** innerhalb von [[Wagglz GmbH]]. Basierend auf dem Projektnamen „Wufflz CVs" und dem Kontext aus [[25 Wufflz Wireframes Figma Manifest]] (Schritt 01_5: Veterinarian Information, Schritt 01_8/01_9: Add Employee Profiles) könnte diese Datei folgende Inhalte abbilden:

- **Tierarzt-Profile / CV-Darstellungen** für das Matching-Feature der Plattform
- **Mitarbeiter-Profilekarten** im B2B-Dashboard
- **Kompetenz-/Qualifikationsansichten** für Tierpflege-Fachkräfte

> ⚠️ **Offene Fragen:**
> - Was genau bildet „Wufflz CVs" ab? (Tierarzt-Profile, Mitarbeiter-CVs, Matching-Ansicht?)
> - Wie lässt sich der API-Fehler (Invalid token) beheben?
> - Welche anderen Dateien gehören zur 10-Dateien-Migrationsliste?
> - Wann wird das Token erneuert und der Export nachgeholt?

---

## Ingest-Befehl

```bash
python3 tools/ingest.py --file "raw/Business/Wagglz/Design/wufflz/Figma-Manifest-wufflz-cvs.md"
```

---

## Verwandte Seiten

- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[25 B2B Software Figma Manifest]] — Schwesterdatei (Export-Fehler 403, Tunnel)
- [[25 Wufflz Wireframes Figma Manifest]] — Schwesterdatei (18 Frames erfolgreich exportiert)
- [[Oleg Personal Context]] — Projektverantwortlicher
