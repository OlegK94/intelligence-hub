---
title: Password Manager Migration Source Detail
type: source
tags: [tech, passwords, migration, proton-pass, apple-passwords, csv, locale, entscheidung-offen]
sources: ["raw/Privat/Tech/Password Manager Migration.md"]
created: 2026-06-09
updated: 2026-06-09
summary: Source document for the attempted Proton Pass → Apple Passwords migration — CSV delimiter issue (German locale), field incompatibility analysis, decision framework, and CSV fix via VS Code
---

# Password Manager Migration — Source Detail

## Overview

This source document (status: Entscheidung ausstehend, created 2026-06-09) captures the attempted migration from [[Proton Pass]] to [[Apple Passwords]], the technical blockers encountered, a structured decision framework, and a technical workaround for the CSV delimiter problem.

> For the entity summary and decision status, see [[Password Manager Migration]].

## Attempted Migration Steps

1. CSV-Export aus [[Proton Pass]]
2. Import in [[Apple Passwords]] gescheitert
3. Problem 1: **Deutsches Locale** → CSV-Delimiter ist Semikolon (`;`) statt Komma (`,`)
4. Problem 2: **Feldinkompatibilität** → Apple Passwords kann mehrere Felder nicht abbilden

## Fehlende Felder (Field Incompatibility)

| Feld | Proton Pass | Apple Passwords |
|---|---|---|
| Custom Fields | ✅ | ❌ |
| Mehrere URLs pro Eintrag | ✅ | ❌ |
| Kreditkarten | ✅ | ❌ (separat in Wallet) |
| Identity-Einträge | ✅ | ❌ |
| Secure Notes | ✅ | ❌ |
| Vault-Struktur | ✅ | ❌ |
| TOTP/OTPAuth | ✅ | ✅ (aber manuell re-enroll erforderlich) |
| Passkeys | ✅ | ✅ (aber manuell re-enroll erforderlich) |

**Key finding:** Apple Passwords is effectively a username + password + TOTP manager only. Proton Pass supports a significantly broader data model.

## Entscheidungsrahmen (Decision Framework)

### Bei Proton Pass bleiben, wenn:
- Custom Fields aktiv genutzt (z.B. Kontofeldnummern, PINs, etc.)
- Mehrere URLs pro Eintrag aktiv genutzt
- Kreditkarten, Identities, Secure Notes aktiv genutzt
- Vault-Struktur (Ordnung) aktiv genutzt

### Wechsel zu Apple Passwords sinnvoll, wenn:
- Obige Felder größtenteils **legacy / ungenutzte** Daten sind
- Workflow fast ausschließlich Benutzername + Passwort + TOTP
- Volle **Apple-Integration** gewünscht (Autofill seamless, kein Extra-App)

## Noch zu klären (Open Tasks)

- [ ] Durchgehen: Wie viele Proton Pass Einträge nutzen tatsächlich Custom Fields / Multi-URL / Notes aktiv?
- [ ] Wenn <20% aktive Nutzung: Cleanup + Migration machbar
- [ ] Wenn >50% aktive Nutzung: Bei Proton Pass bleiben

## Technisches Fix (falls Migration fortgesetzt wird)

**Problem:** German locale exports CSV with semicolon delimiter — Apple Passwords expects comma delimiter.

**Lösung via VS Code:**
1. CSV in VS Code öffnen
2. Find & Replace: `;` → `,`
3. ⚠️ Achte auf Felder, die selbst Kommas enthalten → diese müssen mit Anführungszeichen (Quotes) gewrappt sein

> **Note:** Simple find-and-replace risks corrupting fields that contain literal semicolons or commas within their values. A more robust approach would use a CSV-aware tool or Python script to re-delimiter the file properly.

## Related Pages

- [[Password Manager Migration]] — entity page and decision status
- [[Proton Pass]] — source password manager
- [[Apple Passwords]] — target password manager
- [[Privacy and Tech Stack]] — broader tech context (linked in source)
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — decision maker
