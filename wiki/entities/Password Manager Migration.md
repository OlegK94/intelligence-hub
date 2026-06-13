---
title: Password Manager Migration
type: entity
tags: [tool, password-manager, proton-pass, apple-passwords, migration, privacy, tech-stack, decision, open]
sources: ["raw/00-MOC/MOC Tech & Setup.md", "raw/Privat/Tech/Password Manager Migration.md", "raw/inbox/_merged/📥 Offene Actions.md"]
created: 2026-06-09
updated: 2026-06-13
summary: Open decision on whether to migrate from Proton Pass to Apple Passwords — blocked by Custom Fields audit; key gate is counting how many entries actually use Custom Fields
---

# Password Manager Migration

## Overview

This is [[Oleg Personal Context|Oleg]]'s open evaluation of whether to migrate his password manager from [[Proton Pass]] (current) to [[Apple Passwords]] (target). The decision is pending a Custom Fields audit.

## Status

- **Status:** Open — pending audit
- **Priority:** 🟡 Kurzfristig (per [[Offene Actions Inbox]])
- **Blocking gate:** How many Proton Pass entries use Custom Fields?

## Decision Framework

| Criterion | Proton Pass | Apple Passwords |
|---|---|---|
| Custom Fields | ✅ Supported | ❌ Not supported |
| Multiple URLs | ✅ | ❌ |
| Vault/Folder structure | ✅ | ❌ |
| Secure Notes | ✅ | ❌ |
| Credit Card entries | ✅ | ❌ |
| Zero additional cost | ❌ (paid) | ✅ |
| Apple ecosystem integration | Partial | ✅ Native |
| Cross-platform | ✅ | ❌ |
| Privacy-first | ✅ | ❌ (iCloud) |

## Gate Item

**Required action (kurzfristig):**
- [ ] Proton Pass durchgehen: Wie viele Einträge nutzen Custom Fields wirklich?
- [ ] Then: Bleiben (stay with Proton Pass) oder migrieren (migrate to Apple Passwords)

If few entries use Custom Fields → migration viable.
If many entries use Custom Fields → migration causes data loss → stay with Proton Pass.

## Import Constraints (if migrating)

- CSV export from Proton Pass on German locale systems is **semicolon-delimited** → Apple Passwords requires **comma-delimited** → import will fail without transformation
- TOTP secrets do **not** transfer via CSV → manual re-enrollment required per entry
- Any Custom Field data is **silently dropped** on import

## Related Pages

- [[Proton Pass]] — current password manager
- [[Apple Passwords]] — migration target
- [[Password Manager Migration Source Detail]] — technical detail
- [[MOC Tech und Setup]] — parent MOC
- [[Offene Actions Inbox]] — action source
- [[Oleg Personal Context]] — evaluator
