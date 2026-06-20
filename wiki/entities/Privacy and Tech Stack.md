---
title: Datenschutz und Tech Stack
type: entity
tags: [tech, privacy, infrastruktur, proton, apple, brave, safari, dns, 2fa, vpn, password-manager, aktiv]
sources: ["raw/Privat/Tech/Privacy & Tech Stack.md"]
created: 2026-05-10
updated: 2026-06-16
summary: Olegs datenschutzorientierter Tech Stack — Apple-Geräte, Brave auf Mac / Safari auf iOS, vollständiges Proton-Ökosystem (Mail, Calendar, VPN, Pass, Drive), Domain ok-holding.com mit vollständiger E-Mail-Authentifizierung; Proton für alle datenschutzsensiblen Daten
---

# Datenschutz & Tech Stack

## Überblick

[[Oleg Personal Context|Olegs]] Tech Stack ist auf datenschutzorientierte Werkzeuge ausgerichtet. Das Leitprinzip lautet: **Proton für alles Datenschutzkritische; Google Workspace nur dort, wo externe Kollaboration es erfordert; kein Google-Ökosystem für private Daten.**

> Zur Entscheidung über die Passwortmanager-Migration siehe [[Password Manager Migration]] und [[Apple Passwords]].

## Geräte

| Gerät | Hinweise |
|---|---|
| iPhone | Primärgerät |
| iPad Air 2025 | Sekundäres Tablet |
| Mac | Desktop/Laptop |

## Browser-Strategie

| Gerät | Browser | Begründung |
|---|---|---|
| Mac | **Brave** | Chromium-basiert, nativer Werbeblocker, datenschutzorientiert |
| iPhone | **Safari** | Apples WebKit-Beschränkung macht Brave auf iOS nur marginal besser als Chrome; Safari behält die Vorteile der Apple-Integration |
| iPad | **Safari** | Gleiche Logik wie beim iPhone |

## Proton-Ökosystem

| Produkt | Status | Bewertung |
|---|---|---|
| [[Proton Mail]] | ✅ Aktiv | Vollständig leistungsfähig, Zero-Knowledge, empfohlen |
| Proton Calendar | ✅ Aktiv | Vollständig leistungsfähig |
| [[Proton VPN]] | ✅ Aktiv | Kill Switch auf allen Geräten aktiviert |
| [[Proton Pass]] | ✅ Aktiv | Migration zu [[Apple Passwords]] offen → [[Password Manager Migration]] |
| Proton Drive | ✅ Aktiv | Für sensible Dokumente |
| Proton Docs/Sheets | ⚠️ Aktiv | 2–3 Jahre hinter Google; nur für datenschutzsensible Inhalte |

## Domain & DNS

- **Domain:** `ok-holding.com`
- **DNS-Anbieter:** GoDaddy
- **E-Mail-Authentifizierung:** MX, SPF, DKIM, DMARC für [[Proton Mail]] konfiguriert ✅

Die Domain `ok-holding.com` ist auf [[Oleg Business Entity Structure]] abgestimmt — die Holding-Struktur, auf die in den Finanz- und Geschäftsseiten verwiesen wird.

## Sicherheitsmaßnahmen

| Maßnahme | Status |
|---|---|
| 2FA | Auf Proton und wichtigen Konten aktiviert |
| Proton Sentinel | Aktiviert |
| VPN Kill Switch | Auf allen Geräten aktiviert |
| Hide-my-email-Aliase | Werden für Registrierungen verwendet |

## Kernprinzip

> *Proton für alles Datenschutzkritische. Google Workspace nur wo externe Kollaboration es erfordert (Docs-Kompatibilität). Kein Google-Ökosystem für private Daten.*

Dies versetzt den Tech Stack in ein bewusstes Spannungsverhältnis zur Bequemlichkeit — Google Workspace existiert als Zugeständnis an Kollaborationsnormen, nicht als bevorzugtes Werkzeug.

## Offene Migration

- **[[Proton Pass]] → [[Apple Passwords]]:** In Prüfung. Siehe [[Password Manager Migration]] für den vollständigen Entscheidungsrahmen, die Feldkompatibilitätsanalyse und die Blockerbewertung.

## Verwandte Seiten

- [[Password Manager Migration]] — offene Migrationsentscheidung
- [[Apple Passwords]] — Ziel der möglichen Migration
- [[Proton Pass]] — aktueller Passwortmanager
- [[MOC Tech und Setup]] — übergeordnete MOC
- [[Oleg Personal Context]] — Stack-Inhaber
- [[Oleg Business Entity Structure]] — Kontext der Domain ok-holding.com
- [[Claude Projects Setup]] — KI-Werkzeuge im Tech Stack