---
title: Datenschutz und Tech-Stack Quelldokument
type: source
tags: [tech, privacy, infrastruktur, proton, apple, brave, safari, dns, 2fa, vpn, password-manager, aktiv]
sources: ["raw/Privat/Tech/Privacy & Tech Stack.md"]
created: 2026-05-10
updated: 2026-06-16
summary: Rohdatenquelle für Olegs Datenschutz & Tech-Stack — Geräte, Browser-Begründung je Gerät, vollständige Proton-Ökosystem-Statustabelle, Domain/DNS-Konfiguration und Sicherheitsmaßnahmen
---

# Datenschutz & Tech-Stack — Quelldokument

## Überblick

Dieses Quelldokument (Status: Aktiv, erstellt: 2026-05-10) erfasst [[Oleg Personal Context|Olegs]] datenschutzorientierte Tech-Stack-Konfiguration über Geräte, Browser, das Proton-Ökosystem, Domain/DNS-Einrichtung und Sicherheitshärtung hinweg.

> Für die Entitätszusammenfassung und den strategischen Kontext siehe [[Privacy and Tech Stack]].

## Geräte (Devices)

- iPhone (primär / primary)
- iPad Air 2025
- Mac

## Browser

| Gerät | Browser | Begründung |
|---|---|---|
| Mac | Brave | Chromium-Basis, nativer Ad-Block, Privacy |
| iPhone | Safari | Apples WebKit-Beschränkung macht Brave auf iOS nur marginal besser als Chrome; Safari bleibt durch Apple-Integration vorteilhafter |
| iPad | Safari | Gleiche Logik |

**Wichtige Erkenntnis:** Auf iOS sind alle Browser gezwungen, WebKit (Apples Rendering-Engine) zu verwenden, wodurch die Datenschutzunterschiede zwischen Brave und Safari geringer sind als auf dem Desktop. Safari behält den Vorteil der tiefen Apple-Ökosystem-Integration (Handoff, iCloud Keychain usw.).

## Proton Ecosystem

| Produkt | Status | Bewertung |
|---|---|---|
| Proton Mail | ✅ Aktiv | Vollwertig, Zero-Knowledge, empfohlen |
| Proton Calendar | ✅ Aktiv | Vollwertig |
| Proton VPN | ✅ Aktiv | Kill Switch aktiviert auf allen Geräten |
| Proton Pass | ✅ Aktiv | Migration zu Apple Passwords offen → [[Password Manager Migration]] |
| Proton Drive | ✅ Aktiv | Für sensible Dokumente |
| Proton Docs/Sheets | ⚠️ Aktiv | 2–3 Jahre hinter Google; nur für datenschutzsensible Inhalte |

**Status Proton Docs/Sheets:** Das `⚠️` weist auf eingeschränkten Funktionsumfang hin — diese Tools hinken Google Workspace funktional um 2–3 Jahre hinterher und werden nur dort eingesetzt, wo Datenschutz das ausschlaggebende Kriterium ist. Für externe Zusammenarbeit wird standardmäßig Google Workspace genutzt.

## Domain & DNS

- **Domain:** `ok-holding.com`
- **DNS-Provider:** GoDaddy
- **Konfiguration:** MX, SPF, DKIM, DMARC für Proton Mail ✅

Der vollständige E-Mail-Authentifizierungsstack (SPF + DKIM + DMARC) ist konfiguriert — dies verhindert E-Mail-Spoofing und verbessert die Zustellbarkeit für die mit Proton Mail genutzte Domain `ok-holding.com`.

## Sicherheit (Security)

| Maßnahme | Status |
|---|---|
| 2FA | Aktiviert (Proton + wichtige Accounts) |
| Proton Sentinel | Aktiviert |
| VPN Kill Switch | Aktiviert auf allen Geräten |
| Hide-my-email Aliases | Genutzt für Registrierungen |

- **Proton Sentinel:** Protons erweitertes Kontoschutz-Feature — überwacht verdächtige Anmeldeversuche und fügt zusätzliche Verifizierungsschritte hinzu
- **Hide-my-email Aliases:** Wird genutzt, um sich auf Websites zu registrieren, ohne die primäre E-Mail-Adresse preiszugeben — reduziert Spam und die Exposition bei Datenpannen

## Prinzip (Guiding Principle)

> *Proton für alles Datenschutzkritische. Google Workspace nur wo externe Kollaboration es erfordert (Docs-Kompatibilität). Kein Google-Ökosystem für private Daten.*

## Offene Punkte (aus Quelle)

- [[Password Manager Migration]]: Die Migration Proton Pass → Apple Passwords ist ausdrücklich als offen markiert

## Verwandte Seiten

- [[Privacy and Tech Stack]] — Entitätszusammenfassung
- [[Password Manager Migration]] — offene Migration
- [[Apple Passwords]] — Migrationsziel
- [[Proton Pass]] — aktueller Passwort-Manager
- [[MOC Tech und Setup]] — übergeordnetes MOC
- [[Oleg Personal Context]] — Stack-Inhaber