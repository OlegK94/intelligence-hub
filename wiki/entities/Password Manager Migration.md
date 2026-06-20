---
title: Passwort-Manager-Migration
type: entity
tags: [tool, password-manager, proton-pass, apple-passwords, migration, privacy, tech-stack, decision, open]
sources: ["raw/00-MOC/MOC Tech & Setup.md", "raw/Privat/Tech/Password Manager Migration.md", "raw/inbox/_merged/📥 Offene Actions.md"]
created: 2026-06-09
updated: 2026-06-13
summary: Offene Entscheidung, ob von Proton Pass zu Apple Passwords migriert werden soll — blockiert durch Custom-Fields-Audit; der entscheidende Faktor ist die Anzahl der Einträge, die tatsächlich Custom Fields verwenden
---

# Passwort-Manager-Migration

## Überblick

Dies ist [[Oleg Personal Context|Olegs]] offene Bewertung, ob er seinen Passwort-Manager von [[Proton Pass]] (aktuell) zu [[Apple Passwords]] (Ziel) migrieren soll. Die Entscheidung steht noch aus bis zum Abschluss eines Custom-Fields-Audits.

## Status

- **Status:** Offen — Audit ausstehend
- **Priorität:** 🟡 Kurzfristig (gemäß [[Offene Actions Inbox]])
- **Blockierender Faktor:** Wie viele Proton-Pass-Einträge nutzen Custom Fields?

## Entscheidungsrahmen

| Kriterium | Proton Pass | Apple Passwords |
|---|---|---|
| Custom Fields | ✅ Unterstützt | ❌ Nicht unterstützt |
| Mehrere URLs | ✅ | ❌ |
| Vault-/Ordnerstruktur | ✅ | ❌ |
| Sichere Notizen | ✅ | ❌ |
| Kreditkarteneinträge | ✅ | ❌ |
| Keine zusätzlichen Kosten | ❌ (kostenpflichtig) | ✅ |
| Apple-Ökosystem-Integration | Teilweise | ✅ Nativ |
| Plattformübergreifend | ✅ | ❌ |
| Privacy-first | ✅ | ❌ (iCloud) |

## Gate-Kriterium

**Erforderliche Aktion (kurzfristig):**
- [ ] Proton Pass durchgehen: Wie viele Einträge nutzen Custom Fields wirklich?
- [ ] Dann: Bleiben (stay with Proton Pass) oder migrieren (migrate to Apple Passwords)

Wenn wenige Einträge Custom Fields nutzen → Migration sinnvoll.
Wenn viele Einträge Custom Fields nutzen → Migration führt zu Datenverlust → bei Proton Pass bleiben.

## Import-Einschränkungen (bei Migration)

- CSV-Export aus Proton Pass auf deutschsprachigen Systemen ist **semikolon-getrennt** → Apple Passwords erfordert **komma-getrennte** Dateien → Import schlägt ohne Umwandlung fehl
- TOTP-Secrets werden über CSV **nicht** übertragen → manuelle Neueinrichtung pro Eintrag erforderlich
- Alle Custom-Field-Daten gehen beim Import **stillschweigend verloren**

## Verwandte Seiten

- [[Proton Pass]] — aktueller Passwort-Manager
- [[Apple Passwords]] — Migrationsziel
- [[Password Manager Migration Source Detail|Technische Details zur Passwort-Manager-Migration]] — technische Einzelheiten
- [[MOC Tech und Setup]] — übergeordnete MOC
- [[Offene Actions Inbox]] — Aktionsquelle
- [[Oleg Personal Context]] — Bewerter