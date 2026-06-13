---
title: Proton Pass
type: concept
tags: [password-manager, privacy, proton, tool, aktiv, migration]
sources: ["raw/03-Tech-Setup/Privacy & Tech Stack.md", "raw/03-Tech-Setup/Password Manager Migration.md"]
created: 2026-06-16
updated: 2026-06-16
summary: Proton's privacy-first password manager — current password manager in Oleg's stack; migration to Apple Passwords is under evaluation; supports Custom Fields, Vaults, Secure Notes, multi-URL, Credit Cards, Identities
---

# Proton Pass

## Overview

**Proton Pass** is a password manager by Proton AG (Switzerland). It is [[Oleg Personal Context|Oleg]]'s current password manager, active across all devices. A migration to [[Apple Passwords]] is under evaluation.

## Current Status

- **Status:** ✅ Active
- **Migration:** Open — evaluation in progress → [[Password Manager Migration]]

## Feature Advantages Over Apple Passwords

| Feature | Proton Pass | Apple Passwords |
|---|---|---|
| Custom Fields | ✅ | ❌ |
| Multiple URLs per entry | ✅ | ❌ |
| Secure Notes | ✅ | ❌ |
| Vault / Folder Structure | ✅ | ❌ |
| Credit Card entries | ✅ | ❌ (Apple Wallet only) |
| Identity entries | ✅ | ❌ |
| Cross-platform (Android, Windows) | ✅ | ❌ |
| Privacy-first architecture | ✅ | Partial (iCloud) |

## Migration Blocker

The primary blockers for migrating away from Proton Pass:
1. **Custom Fields** — PIN codes, account numbers stored as custom fields would be silently dropped on import to Apple Passwords
2. **German locale CSV issue** — Proton Pass exports semicolon-delimited CSV; Apple Passwords expects comma-delimited
3. **TOTP re-enrollment** — TOTP secrets do not transfer via CSV

See [[Password Manager Migration]] and [[Apple Passwords]] for full analysis.

## Related Pages

- [[Privacy and Tech Stack]] — ecosystem context
- [[Password Manager Migration]] — migration evaluation
- [[Apple Passwords]] — migration target
- [[Proton Mail]] — co-service in Proton ecosystem
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — user
