---
title: Proton Mail
type: concept
tags: [email, privacy, proton, zero-knowledge, encryption, tool, aktiv]
sources: ["raw/03-Tech-Setup/Privacy & Tech Stack.md"]
created: 2026-06-16
updated: 2026-06-16
summary: Privacy-first, end-to-end encrypted email service by Proton AG (Switzerland) — Zero-Knowledge architecture; used as Oleg's primary email with domain ok-holding.com
---

# Proton Mail

## Overview

**Proton Mail** is an end-to-end encrypted email service by Proton AG (Switzerland). It uses a **Zero-Knowledge** architecture — Proton cannot read user emails because messages are encrypted client-side before storage.

## Usage in Oleg's Stack

- **Status:** ✅ Active — fully capable, recommended
- **Domain:** `ok-holding.com` (custom domain configured)
- **Authentication:** MX, SPF, DKIM, DMARC all configured ✅
- **Security:** Proton Sentinel activated
- **Context:** Primary email for all privacy-sensitive communication

See [[Privacy and Tech Stack]] for the full ecosystem context.

## Key Properties

- **End-to-End Encryption:** Emails encrypted using PGP; Proton cannot decrypt
- **Zero-Knowledge:** No metadata mining or ad profiling
- **Swiss jurisdiction:** Switzerland has strong privacy laws outside EU/US data-sharing agreements
- **Open-source clients:** Apps are open-source and auditable

## Related Pages

- [[Privacy and Tech Stack]] — stack context
- [[Proton Pass]] — password manager in same ecosystem
- [[Proton VPN]] — VPN in same ecosystem
- [[MOC Tech und Setup]] — parent MOC
- [[Oleg Personal Context]] — user
