---
title: Apple Passwords
type: entity
tags: [tool, password-manager, apple, ios, macos, tech-stack, autofill]
sources: ["raw/03-Tech-Setup/Password Manager Migration.md"]
created: 2026-06-09
updated: 2026-06-09
summary: Apple's native password manager (iOS 18+ / macOS 15+ standalone app) — supports username/password/TOTP/Passkeys but lacks Custom Fields, multi-URL, Vault structure, Credit Cards, and Identity entries; target of Oleg's migration evaluation from Proton Pass
---

# Apple Passwords

## Overview

**Apple Passwords** is Apple's native password management application, introduced as a standalone app in iOS 18 and macOS 15 (Sequoia). It is the **target** of [[Oleg Personal Context|Oleg]]'s potential migration from [[Proton Pass]], as part of tech stack simplification and Apple ecosystem integration.

## Feature Set

| Feature | Supported |
|---|---|
| Username + Password | ✅ |
| Single URL per entry | ✅ |
| TOTP / OTPAuth | ✅ (manual re-enroll required on import) |
| Passkeys | ✅ (manual re-enroll required on import) |
| Custom Fields | ❌ |
| Multiple URLs per entry | ❌ |
| Credit Card entries | ❌ (handled separately via Apple Wallet) |
| Identity entries | ❌ |
| Secure Notes | ❌ |
| Vault / Folder Structure | ❌ |

## Import Limitations

- **CSV import:** Supported, but requires comma-delimited CSV
- **German locale issue:** Proton Pass exports semicolon-delimited CSV on German systems → import fails
- **Field loss:** Any Proton Pass data in unsupported fields is **silently dropped** on import
- **TOTP re-enrollment:** TOTP secrets do not transfer via CSV — must be manually re-scanned/entered

## Advantages

- **Zero additional cost** — included with Apple ecosystem
- **Seamless Autofill** — native integration with Safari, iOS, macOS
- **iCloud sync** — automatic across all Apple devices
- **Passkey support** — built-in and tightly integrated
- **Simplicity** — reduced complexity for username+password+TOTP workflows

## Limitations vs. Proton Pass

- No Custom Fields (PIN codes, account numbers, etc.)
- No multi-URL per entry
- No Secure Notes
- No Vault/folder organization
- No cross-platform (Android, Windows) native support
- No privacy-first architecture (iCloud sync, Apple ecosystem dependency)

## Migration Status

Migration is **pending** — blocked by the field incompatibility assessment. See [[Password Manager Migration]] for the decision framework and required audit.

## Related Pages

- [[Password Manager Migration]] — migration decision entity
- [[Password Manager Migration Source Detail]] — technical detail
- [[Proton Pass]] — current password manager
- [[Privacy and Tech Stack]] — broader tech stack context
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — evaluator
