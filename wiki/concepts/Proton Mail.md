---
title: Proton Mail
type: concept
tags: [email, privacy, proton, zero-knowledge, encryption, tool, aktiv]
sources: ["raw/Privat/Tech/Privacy & Tech Stack.md"]
created: 2026-06-16
updated: 2026-06-16
summary: Datenschutzorientierter, Ende-zu-Ende verschlüsselter E-Mail-Dienst von Proton AG (Schweiz) — Zero-Knowledge-Architektur; wird als Olegs primäre E-Mail-Adresse mit der Domain ok-holding.com genutzt
---

# Proton Mail

## Überblick

**Proton Mail** ist ein Ende-zu-Ende verschlüsselter E-Mail-Dienst von Proton AG (Schweiz). Er verwendet eine **Zero-Knowledge**-Architektur — Proton kann keine Nutzer-E-Mails lesen, da Nachrichten vor der Speicherung clientseitig verschlüsselt werden.

## Nutzung in Olegs Stack

- **Status:** ✅ Aktiv — voll funktionsfähig, empfohlen
- **Domain:** `ok-holding.com` (benutzerdefinierte Domain konfiguriert)
- **Authentifizierung:** MX, SPF, DKIM, DMARC alle konfiguriert ✅
- **Sicherheit:** Proton Sentinel aktiviert
- **Kontext:** Primäre E-Mail-Adresse für alle datenschutzsensiblen Kommunikationen

Siehe [[Privacy and Tech Stack]] für den vollständigen Ökosystem-Kontext.

## Wichtige Eigenschaften

- **Ende-zu-Ende-Verschlüsselung:** E-Mails werden mit PGP verschlüsselt; Proton kann sie nicht entschlüsseln
- **Zero-Knowledge:** Kein Metadaten-Mining oder Werbe-Profiling
- **Schweizer Rechtsprechung:** Die Schweiz verfügt über starke Datenschutzgesetze außerhalb der EU/US-Datenteilungsabkommen
- **Open-Source-Clients:** Apps sind Open-Source und prüfbar

## Verwandte Seiten

- [[Privacy and Tech Stack|Datenschutz & Tech-Stack]] — Stack-Kontext
- [[Proton Pass]] — Passwort-Manager im selben Ökosystem
- [[Proton VPN]] — VPN im selben Ökosystem
- [[MOC Tech und Setup]] — übergeordnete MOC
- [[Oleg Personal Context|Olegs persönlicher Kontext]] — Nutzer