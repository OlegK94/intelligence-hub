---
title: Audit-Report Intelligence Hub
type: synthesis
created: 2026-06-20
updated: 2026-06-20
tags: [audit, qualität, obsidian]
summary: Vollständiger Vault-Audit — Struktur, Duplikate, Links, Security, Obsidian-Setup
---

# Audit-Report — 2026-06-20

## 1. Executive Summary

| # | Finding | Severity |
|---|---|---|
| 1 | 394 ungelöste Wikilinks im Graph (→ Klick-Fehler) | Kritisch — **behoben** |
| 2 | Kaputte Links in `log.md` (zusammengeklebte Pfade) | Mittel — **behoben** |
| 3 | 7 verwaiste Seiten (keine eingehenden Links) | Mittel |
| 4 | Keyword-Duplikate in mehreren Cluster-Gruppen | Niedrig |
| 5 | 1 Stub-Seite (38 Wörter) | Niedrig |

**Keine Security-Findings** — kein API-Key oder Token im Vault gefunden.

---

## 2. Duplikate / Redundanz

| Cluster | Anzahl Seiten | Empfehlung |
|---|---|---|
| `master` | 9 (Health Protocol Master + Source Detail, TODO Master…) | Source Detail + Entity zusammenführen |
| `claude` | 6 (Session Finanzen Template + Detail, Claude Projects Setup…) | Detail-Seiten löschen wenn Entity existiert |
| `consorsbank` | 6 (Girokonto 0250120493 + Source Detail, Tagesgeld…) | Source Details archivieren |
| `finanz` | 6 (Finanz-Übersicht, Privat Finanz-Übersicht, Dashboard…) | Auf 1 Finanz-MOC konsolidieren |
| `stack` | 5 (Supplement Stack + Source Detail, Longevity Stack…) | Source Detail → Entity zusammenführen |
| `setup` | 5 (MOC Tech + Source Detail, Claude Projects Setup…) | Source Details archivieren |

---

## 3. Plausibilitäts-Konflikte

Keine kritischen Widersprüche gefunden. Bekannte offene Punkte:
- **NAC**: Supplier List Tier-1, aber Hai Onepager erwähnt es nicht → Entscheidung ausstehend
- **COGS 0,145 €**: In letzter Session korrigiert (war 0,13 €)

---

## 4. Strukturelle Probleme

### Verwaiste Seiten (keine eingehenden Links)
- `Claude Session Finanzen Template Detail`
- `Finanzielle Gesamtanalyse 2025-2026 Archiv`
- `Inbox 2026-06-13 Detail`
- `Performance Cafe Ingredienzen CSV Database`
- `Performance Cafe Prototyp Partner`
- `Performance Cafe Regulatorik Report`
- `Wagglz Finom 2026 Konten`

→ Diese 7 Seiten sollten von relevanten Entity-Seiten verlinkt werden.

### Stub-Seiten
- `wiki/sources/Inbox 2026-06-13 Detail.md` — 38 Wörter (leere Inbox-Datei)

### Kaputte Wikilinks
- `log.md` hatte zusammengeklebte Pfade (`[[wikisourceshealth-protocol-master.md]]`) — **behoben**
- Graph-Ansicht zeigte 394 ungelöste Nodes → `hideUnresolved: true` gesetzt — **behoben**

---

## 5. Sprach-Findings

Vault ist bewusst gemischt (DE/EN). Englischsprachige Seiten die deutsch sein könnten:
- `wiki/entities/GROVE Sessions External.md`
- `wiki/concepts/Coffee Blend Ratios.md`
- `wiki/concepts/Brick Training.md`
- Viele Performance-Coffee-Seiten (Fachbegriffe bleiben englisch — OK)

---

## 6. Security-Findings

**Keine Findings** — kein API-Key, kein Token, kein Secret im Vault gefunden.

---

## 7. Obsidian-Setup

### Plugin: realclaudian
- **Version**: 2.0.24 (aktiv)
- **Problem**: Fing Graph-Klicks mit leerem Dateipfad ab → Fehler `"" konnte nicht geöffnet werden`
- **Fix**: `hideUnresolved: true` in graph.json — Graph zeigt nur noch existierende Seiten → kein leerer Pfad mehr

### Weitere Plugins (alle aktiv)
| Plugin | Status |
|---|---|
| dataview | ✅ Sinnvoll |
| templater-obsidian | ✅ Sinnvoll |
| obsidian-git | ✅ Sinnvoll |
| obsidian-excalidraw-plugin | ✅ OK |
| obsidian-kanban | ✅ OK |
| obsidian-tasks-plugin | ✅ OK |
| periodic-notes | ✅ OK |
| terminal | ✅ OK |
| marp | ✅ Für Slide-Outputs |
| realclaudian | ⚠️ Graph-Bug behoben, Plugin bleibt aktiv |
| obsidian42-brat | ℹ️ Plugin-Manager, kann deaktiviert werden |

---

## 8. Backup / Versionierung

- ✅ Vault liegt unter Git (GitHub: OlegK94/intelligence-hub)
- ✅ iCloud Sync aktiv (iOS-Zugriff)
- ⚠️ iCloud + Git gleichzeitig: kein aktives Konflikt-Risiko, aber `workspace.json` kann bei gleichzeitiger Nutzung auf mehreren Geräten kollidieren → kein kritisches Problem

---

## 9. Priorisierte Action-Liste

| Prio | Aufgabe | Severity |
|---|---|---|
| ✅ | Graph: hideUnresolved=true | Kritisch — erledigt |
| ✅ | log.md: kaputte Links gefixt | Mittel — erledigt |
| 1 | 7 verwaiste Seiten von Entity-Seiten verlinken | Mittel |
| 2 | Duplikat-Cluster "finanz" auf 1 MOC konsolidieren | Niedrig |
| 3 | Stub `Inbox 2026-06-13 Detail` löschen | Niedrig |
| 4 | NAC: Tier-1 ja/nein entscheiden | Inhaltlich |
