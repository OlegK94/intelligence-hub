---
title: Proton Pass
type: entity
tags: [tool, password-manager, security, privacy, proton, tech-stack]
sources: ["raw/Privat/Tech/Password Manager Migration.md"]
created: 2026-06-09
updated: 2026-06-09
summary: Privacy-first password manager by Proton AG — part of the Proton suite; supports Custom Fields, multi-URL, Vault structure, Credit Cards, Identity entries, and Secure Notes; currently used by Oleg but under migration review
---

# Proton Pass

## Overview

**Proton Pass** is a password manager developed by Proton AG (Switzerland), part of the broader Proton privacy suite (alongside Proton Mail, Proton VPN, Proton Drive). It is [[Oleg Personal Context|Oleg]]'s **current** password manager as of June 2026, currently under review for potential migration to [[Apple Passwords]].

## Feature Set

| Feature | Supported |
|---|---|
| Custom Fields | ✅ |
| Multiple URLs per entry | ✅ |
| Credit Card entries | ✅ |
| Identity entries | ✅ |
| Secure Notes | ✅ |
| Vault Structure (folders) | ✅ |
| TOTP / OTPAuth | ✅ |
| Passkeys | ✅ |

## Data Export

- **Format:** CSV
- **Known issue:** On German locale systems, the CSV delimiter is **semicolon** (`;`) rather than the standard comma (`,`)
- This caused the import failure into Apple Passwords — see [[Password Manager Migration Source Detail]] for the VS Code fix

## Privacy Profile

- **Jurisdiction:** Switzerland (strong privacy laws)
- **Encryption:** End-to-end encrypted
- **Open source:** Audited
- **Cross-platform:** iOS, macOS, Windows, Android, browser extensions

## Migration Status

Currently under review for migration to [[Apple Passwords]]. Decision is pending an audit of how many entries actively use the advanced features (Custom Fields, multi-URL, Vault structure). See [[Password Manager Migration]] for the decision framework.

## Related Pages

- [[Password Manager Migration]] — migration project
- [[Password Manager Migration Source Detail]] — technical detail
- [[Apple Passwords]] — potential migration target
- [[Privacy and Tech Stack]] — broader tech stack context
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — current user
