---
title: Privacy and Tech Stack
type: entity
tags: [tech, privacy, infrastruktur, proton, apple, brave, safari, dns, 2fa, vpn, password-manager, aktiv]
sources: ["raw/03-Tech-Setup/Privacy & Tech Stack.md"]
created: 2026-05-10
updated: 2026-06-16
summary: Oleg's privacy-first tech stack — Apple devices, Brave on Mac / Safari on iOS, full Proton ecosystem (Mail, Calendar, VPN, Pass, Drive), domain ok-holding.com with full email authentication; Proton for all privacy-sensitive data
---

# Privacy & Tech Stack

## Overview

[[Oleg Personal Context|Oleg]]'s tech stack is built around privacy-first tooling. The guiding principle is: **Proton for everything privacy-critical; Google Workspace only where external collaboration requires it; no Google ecosystem for private data.**

> For the password manager migration decision, see [[Password Manager Migration]] and [[Apple Passwords]].

## Devices

| Device | Notes |
|---|---|
| iPhone | Primary device |
| iPad Air 2025 | Secondary tablet |
| Mac | Desktop/laptop |

## Browser Strategy

| Device | Browser | Rationale |
|---|---|---|
| Mac | **Brave** | Chromium-based, native ad-block, privacy-focused |
| iPhone | **Safari** | Apple WebKit restriction makes Brave on iOS only marginally better than Chrome; Safari retains Apple integration advantages |
| iPad | **Safari** | Same logic as iPhone |

## Proton Ecosystem

| Product | Status | Assessment |
|---|---|---|
| [[Proton Mail]] | ✅ Active | Fully capable, Zero-Knowledge, recommended |
| Proton Calendar | ✅ Active | Fully capable |
| [[Proton VPN]] | ✅ Active | Kill Switch activated on all devices |
| [[Proton Pass]] | ✅ Active | Migration to [[Apple Passwords]] open → [[Password Manager Migration]] |
| Proton Drive | ✅ Active | For sensitive documents |
| Proton Docs/Sheets | ⚠️ Active | 2–3 years behind Google; only for privacy-sensitive content |

## Domain & DNS

- **Domain:** `ok-holding.com`
- **DNS Provider:** GoDaddy
- **Email Authentication:** MX, SPF, DKIM, DMARC configured for [[Proton Mail]] ✅

The domain `ok-holding.com` aligns with [[Oleg Business Entity Structure]] — the holding structure referenced across financial and business pages.

## Security Measures

| Measure | Status |
|---|---|
| 2FA | Activated on Proton + important accounts |
| Proton Sentinel | Activated |
| VPN Kill Switch | Activated on all devices |
| Hide-my-email Aliases | Used for registrations |

## Core Principle

> *Proton für alles Datenschutzkritische. Google Workspace nur wo externe Kollaboration es erfordert (Docs-Kompatibilität). Kein Google-Ökosystem für private Daten.*

This places the tech stack in deliberate tension with convenience — Google Workspace exists as a concession to collaboration norms, not as a preferred tool.

## Open Migration

- **[[Proton Pass]] → [[Apple Passwords]]:** Under evaluation. See [[Password Manager Migration]] for full decision framework, field-compatibility analysis, and blocker assessment.

## Related Pages

- [[Password Manager Migration]] — open migration decision
- [[Apple Passwords]] — target of potential migration
- [[Proton Pass]] — current password manager
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — stack owner
- [[Oleg Business Entity Structure]] — domain ok-holding.com context
- [[Claude Projects Setup]] — AI tooling in tech stack
