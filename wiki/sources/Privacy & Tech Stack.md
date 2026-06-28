---
title: "Privacy & Tech Stack"
type: source
tags: [tech, privacy, infrastruktur, geräte, browser, proton, vpn, email, password-manager, domain, 2fa, ok-holding]
sources: ["raw/_archiv/legacy-numbered-folders/03-Tech-Setup/Privacy & Tech Stack.md"]
created: 2026-05-10
updated: 2026-06-17
summary: Tech-Stack und Privacy-Konfiguration für Oleg Kober — iPhone/iPad Air 2025/Mac; Browser Brave (Mac) + Safari (iOS); Proton Ecosystem (Mail/Calendar/VPN/Pass/Drive/Docs) vollständig; Domain ok-holding.com über GoDaddy; 2FA + Sentinel aktiviert; KillSwitch auf allen VPN-Geräten; Hide-my-email-Aliases für Registrierungen; Migration Proton Pass → Apple Passwords offen
---

# Privacy & Tech Stack

## Geräte

| Gerät | Rolle | Priorität |
|---|---|---|
| iPhone | Primär | tägliche Nutzung |
| iPad Air 2025 | Sekundär | Produktivität |
| Mac | Tertiär | Entwicklung / Content |

## Browser-Stack

| Gerät | Browser | Begründung |
|---|---|---|
| **Mac** | Brave | Chromium-Basis; native Ad-Block; Privacy-fokussiert |
| **iPhone** | Safari | Apple WebKit-Restriktion; Brave bietet nur marginal besserer Privacy; Safari integriert besser mit Ecosystem |
| **iPad** | Safari | Gleiche Logik wie iPhone |

**Prinzip:** Auf Apple-Hardware WebKit-Engine bevorzugt wegen Hardware-Integration und Privacy-Symmetrie.

## Proton Ecosystem

| Produkt | Status | Bewertung |
|---|---|---|
| **Proton Mail** | ✅ Aktiv | Vollwertig, Zero-Knowledge, empfohlen |
| **Proton Calendar** | ✅ Aktiv | Vollwertig, sync-fähig |
| **Proton VPN** | ✅ Aktiv | Kill Switch aktiviert auf allen Geräten; lokale Verschlüsselung |
| **Proton Pass** | ✅ Aktiv | Migration zu [[Apple Passwords]] offen → siehe [[Password Manager Migration]] |
| **Proton Drive** | ✅ Aktiv | Für sensible Dokumente; Ende-zu-Ende-verschlüsselt |
| **Proton Docs/Sheets** | ⚠️ Aktiv | 2–3 Jahre hinter Google; nur für privacy-sensitive Inhalte |

## Domain & DNS

| Element | Konfiguration |
|---|---|
| **Domain** | `ok-holding.com` |
| **DNS-Provider** | GoDaddy |
| **MX-Records** | ✅ für Proton Mail konfiguriert |
| **SPF** | ✅ konfiguriert |
| **DKIM** | ✅ konfiguriert |
| **DMARC** | ✅ konfiguriert |

**Zweck:** Enterprise-E-Mail-Authentifizierung; verhindert Spoofing.

## Sicherheit & Authentisierung

| Mechanismus | Status | Konfiguration |
|---|---|---|
| **2FA** | ✅ Aktiviert | Auf Proton + wichtige Accounts (Banking, Social) |
| **Proton Sentinel** | ✅ Aktiviert | Breach-Monitoring |
| **VPN Kill Switch** | ✅ Aktiviert | Auf allen Geräten; Daten-Leak-Prävention bei VPN-Disconnect |
| **Hide-my-email Aliases** | ✅ Genutzt | Für Third-Party-Registrierungen (Datenlecks isolieren) |

## Architektur-Prinzipien

### Privacy by Default
- Proton für alles **datenschutzkritische:** E-Mail, Kalender, Dokumente
- Google Workspace **nur wo externe Kollaboration erforderlich** (Docs-Kompatibilität)
- Kein Google-Ökosystem für private Daten

### Separation of Concerns
- Persönliche Daten: Proton
- Work-Kollaboration: Google (als notwendiges Übel)
- Bezahlungen: Apple Pay (gekoppelt an ok-holding.com)

### Fallback & Redundanz
- Proton Mail + lokale Archivierung (verschlüsseltes Backup)
- 2FA auf Proton + Authenticator-App (nicht nur SMS)

## Offene Punkte

| Punkt | Status | Aktion |
|---|---|---|
| **Proton Pass → Apple Passwords Migration** | ⏳ offen | Evaluieren ob vorteilhaft (Ecosystem-Integration vs. Portabilität) |
| **Proton Docs Performance** | ⚠️ Akzeptabel | Monitoring; Evtl. Hybrid mit Google Docs für Performance-kritische Projekte |
| **iCloud Keychain vs. Proton Pass** | ⏳ Entscheidung | Apple Passwords ist tighter integriert; Proton Pass ist portabler |

## Verknüpfungen

- **[[Password Manager Migration]]** — Migration Proton Pass → Apple Passwords Evaluierung
- **[[MOC Tech & Setup]]** — Master-Index für Tech-Infrastruktur
- **[[Oleg Personal Context]]** — Träger dieser Konfiguration
- **[[Proton Mail]]** — Konzept-Seite
- **[[Apple Passwords]]** — Alternative zu Proton Pass
- **[[Brave Browser]]** — Privacy-fokussierter Browser für Mac

---

*Seite erstellt: 2026-06-17*
*Status: Aktiv*
