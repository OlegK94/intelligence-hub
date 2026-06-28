---
title: "MOC Tech & Setup"
type: source
tags: [moc, tech-stack, privacy, infrastructure, proton, brave, safari, domain, ok-holding, devices, setup]
sources: ["raw/Privat/MOC/MOC Tech & Setup.md"]
created: 2026-06-17
updated: 2026-06-17
summary: Master of Change — Tech & Setup; aktive Module Privacy & Tech Stack, Claude Projects Setup, Password Manager Migration; Infrastruktur: ok-holding.com Domain (GoDaddy DNS), Proton Mail/VPN/Pass, Brave (Desktop) / Safari (iOS), Geräte iPhone/iPad Air 2025/Mac; Quelldokument für Systemadministration und Datenschutz-Governance
---

# MOC Tech & Setup

## Überblick

Dies ist das **Master of Change (MOC) — Tech & Setup** Quelldokument, das Olegs **Technische Infrastruktur, Datenschutz-Strategie und Cloud-Verwaltung** dokumentiert.

## Aktive Module

### [[Privacy & Tech Stack]]
- Proton Mail (verschlüsselt)
- Proton VPN
- Proton Pass (Migration zu Apple Passwords offen)
- Brave (Desktop) / Safari (iOS)
- iPhone, iPad Air 2025, Mac

### [[Claude Projects Setup]]
- ⏳ Status: In Planung
- Zweck: Integration von Claude Projects für strukturierte Forschung und Dokumentation
- Bezug: [[Performance Coffee Brand]] (Modul 01–08 Research)

### [[Password Manager Migration]]
- Status: ⏳ Ausstehend
- Von: Proton Pass
- Zu: Apple Passwords
- Timeline: Q3 2026 (tentativ)

## Infrastruktur-Details

### Domain Management

| Parameter | Wert |
|---|---|
| **Domain** | ok-holding.com |
| **Registrar** | GoDaddy |
| **DNS-Provider** | GoDaddy (aktuell) |
| **Mail-Server** | Proton Mail (Custom Domain) |
| **Verwendung** | Persönliche + Unternehmens-Email |

### Mail & Kommunikation

| Provider | Service | Status |
|---|---|---|
| **Proton Mail** | Email (verschlüsselt) | ✅ Aktiv |
| **Proton VPN** | VPN-Netzwerk-Schutz | ✅ Aktiv |
| **Proton Pass** | Passwort-Verwaltung | ✅ Aktiv (Migration offen) |

### Browser & Geräte

| Plattform | Anwendung | Status |
|---|---|---|
| **Desktop** | Brave | ✅ Aktiv |
| **iOS** | Safari | ✅ Aktiv |
| **Geräte** | iPhone, iPad Air 2025, Mac | ✅ Aktiv |

## Abhängigkeiten & Blockaden

- **Claude Projects Setup** blockiert durch: Workspace-Konfiguration & API-Key-Sicherheit
- **Password Manager Migration** blockiert durch: Apple Passwords Beta-Stabilität und Datenmigrations-Testung
- **DNS-Migration (optional)** blockiert durch: Zeit + Priorität (nicht dringend)

## Nächste Schritte

1. **Claude Projects Setup:**
   - [ ] Workspace erstellen
   - [ ] API-Keys generieren und verschlüsselt speichern
   - [ ] Integration mit [[Performance Coffee Brand]] Modul 01–08 (Claude Code-Ausführungen)

2. **Password Manager Migration:**
   - [ ] Apple Passwords Beta-Phase überprüfen
   - [ ] Proton Pass → Apple Keychain Export-Test durchführen
   - [ ] Alle Credentials validieren

3. **DNS-Optimierung (optional, nicht dringend):**
   - [ ] Evaluate Proton Simple Login oder Cloudflare
   - [ ] Migration planen (nach Password Manager-)

## Verwandte Seiten

- [[Privacy & Tech Stack]] — Detailinformation zu allen Tech-Tools
- [[Oleg Personal Context]] — Nutzer
- [[Performance Coffee Brand]] — Projekt (Claude Projects Integration)
- [[Wagglz GmbH]] — Unternehmens-Tech-Kontext
- [[Claude Projects]] — Verwaltete Workspace-Struktur
- [[ok-holding.com Domain]] — Domain-Entity
