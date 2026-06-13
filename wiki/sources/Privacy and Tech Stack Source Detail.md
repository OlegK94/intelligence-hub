---
title: Privacy and Tech Stack Source Detail
type: source
tags: [tech, privacy, infrastruktur, proton, apple, brave, safari, dns, 2fa, vpn, password-manager, aktiv]
sources: ["raw/03-Tech-Setup/Privacy & Tech Stack.md"]
created: 2026-05-10
updated: 2026-06-16
summary: Raw source for Oleg's Privacy & Tech Stack — devices, browser rationale per device, full Proton ecosystem status table, domain/DNS config, and security measures
---

# Privacy & Tech Stack — Source Detail

## Overview

This source document (status: Aktiv, created: 2026-05-10) captures [[Oleg Personal Context|Oleg]]'s privacy-focused tech stack configuration across devices, browsers, the Proton ecosystem, domain/DNS setup, and security hardening.

> For the entity summary and strategic context, see [[Privacy and Tech Stack]].

## Geräte (Devices)

- iPhone (primär / primary)
- iPad Air 2025
- Mac

## Browser

| Gerät | Browser | Begründung |
|---|---|---|
| Mac | Brave | Chromium-Basis, native Ad-Block, Privacy |
| iPhone | Safari | Apple WebKit-Restriktion macht Brave auf iOS marginal besser als Chrome; Safari bleibt vorteilhafter für Apple-Integration |
| iPad | Safari | Gleiche Logik |

**Key insight:** On iOS, all browsers are forced to use WebKit (Apple's rendering engine), making privacy differences between Brave and Safari smaller than on desktop. Safari retains the advantage of deep Apple ecosystem integration (Handoff, iCloud Keychain, etc.).

## Proton Ecosystem

| Produkt | Status | Bewertung |
|---|---|---|
| Proton Mail | ✅ Aktiv | Vollwertig, Zero-Knowledge, empfohlen |
| Proton Calendar | ✅ Aktiv | Vollwertig |
| Proton VPN | ✅ Aktiv | Kill Switch aktiviert auf allen Geräten |
| Proton Pass | ✅ Aktiv | Migration zu Apple Passwords offen → [[Password Manager Migration]] |
| Proton Drive | ✅ Aktiv | Für sensible Dokumente |
| Proton Docs/Sheets | ⚠️ Aktiv | 2–3 Jahre hinter Google; nur für privacy-sensitive Inhalte |

**Proton Docs/Sheets status:** The `⚠️` indicates limited capability — these tools lag Google Workspace by 2–3 years in features and are used only where privacy is the overriding concern. External collaboration defaults to Google Workspace.

## Domain & DNS

- **Domain:** `ok-holding.com`
- **DNS-Provider:** GoDaddy
- **Konfiguration:** MX, SPF, DKIM, DMARC für Proton Mail ✅

Full email authentication stack (SPF + DKIM + DMARC) is configured — this prevents email spoofing and improves deliverability for the `ok-holding.com` domain used with Proton Mail.

## Sicherheit (Security)

| Maßnahme | Status |
|---|---|
| 2FA | Aktiviert (Proton + wichtige Accounts) |
| Proton Sentinel | Aktiviert |
| VPN Kill Switch | Aktiviert auf allen Geräten |
| Hide-my-email Aliases | Genutzt für Registrierungen |

- **Proton Sentinel:** Proton's advanced account protection feature — monitors for suspicious login attempts and adds extra verification steps
- **Hide-my-email Aliases:** Used to register on websites without exposing the primary email address — reduces spam and data breach exposure

## Prinzip (Guiding Principle)

> *Proton für alles Datenschutzkritische. Google Workspace nur wo externe Kollaboration es erfordert (Docs-Kompatibilität). Kein Google-Ökosystem für private Daten.*

## Open Items (from Source)

- [[Password Manager Migration]]: Proton Pass → Apple Passwords migration is explicitly flagged as open

## Related Pages

- [[Privacy and Tech Stack]] — entity summary
- [[Password Manager Migration]] — open migration
- [[Apple Passwords]] — migration target
- [[Proton Pass]] — current password manager
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — stack owner
