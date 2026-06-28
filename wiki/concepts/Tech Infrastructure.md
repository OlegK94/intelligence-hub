---
title: "Tech Infrastructure"
type: concept
tags: [infrastructure, domain, dns, mail, vpn, devices, networking, backup, hosting]
sources: ["raw/raw/_archiv/legacy-numbered-folders/00-MOC/MOC Tech & Setup.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Persönliche Tech-Infrastruktur — Domain ok-holding.com (DNS via GoDaddy), Proton Mail, Proton VPN, Devices (iPhone, iPad Air 2025, Mac); zentralisiert auf ok-holding.com als Basis-Domain für E-Mail-Aliasing und Identitäts-Management
---

# Tech Infrastructure

## Überblick

Die **Tech Infrastructure** bildet das fundamentale Rückgrat für persönliche und geschäftliche Kommunikation, Identitätsmanagement und Gerätesynchr​onisation. Das System ist bewusst **minimalist und zentralisiert auf ok-holding.com als Anchor-Domain**.

> **Architektur-Prinzip:** Einzige Domain für alle E-Mail-Kontexte; Devices sind ephemeral (austauschbar); Services sind minimalisiert (nur essenzielle Betriebsmittel).

---

## Domain & DNS

### **ok-holding.com**
- **Registrar:** GoDaddy
- **Purpose:** Einzige Umbrella-Domain für alle E-Mail-Aliasing, persönliche Identität, ggf. zukünftige Subdomains
- **DNS Management:** GoDaddy-Standard (nicht CNAME'd zu externem Anbieter)
- **E-Mail-Handling:** MX-Record zeigt auf **Proton Mail** (externe Verwaltung)
  - `MX 10 mail.proton.me.` (Proton Mail Primary)
  - `MX 20 mailsec.proton.me.` (Proton Mail Backup/Secondary)
- **SPF/DKIM/DMARC:**
  - **SPF:** `v=spf1 include:proton.me ~all` (Proton Mail authorized senders)
  - **DKIM:** Keys via Proton Mail console (Proton manages DKIM)
  - **DMARC:** `v=DMARC1; p=quarantine; rua=mailto:dmarc@ok-holding.com` (Reporting)
- **DNSSEC:** Nicht aktiviert (GoDaddy-Default); Aktivierung zukünftig erwägen

### **Subdomains** (zukünftig)
- `admin.ok-holding.com` — Administrative Services (wenn notwendig)
- `api.ok-holding.com` — API-Endpoints (falls SaaS-Projekt startet)
- Weitere je nach Geschäftsanforderung (vorsichtig, keine Überengineering)

---

## E-Mail-System

### **Proton Mail (Primary)**
- **Account:** Admin-Mailbox (primär)
- **Plan:** Proton Unlimited (oder äquivalent)
- **Aliases:** Mehrere Adressen unter ok-holding.com
  - `admin@ok-holding.com`
  - `work@ok-holding.com`
  - `personal@ok-holding.com`
  - `noreply@ok-holding.com` (für automatisierte Kommunikation)
  - Ggf. throwaway Adressen für Tests
- **Forwarding:** Alle ok-holding.com-Adressen werden zu Proton-Postfach weitergeleitet
- **Encryption:** End-to-End-verschlüsselt; externe Empfänger können Proton-Nachrichten lesen (mit PGP-Key)

### **Fallback-Email** (kein aktives Setup, aber dokumentiert)
- Falls Proton Mail ausfällt: `@protonmail.com` als Fallback (gleicher Account, nur anderer Hostname)

---

## VPN & Network Security

### **Proton VPN**
- **Primary Tunnel:** Aktiviert für Tagesnutzung
- **Server-Auswahl:** Automatisch (Proton wählt schnellstes basierend auf Standort)
- **DNS:** Proton DNS (verhindert externe DNS-Leaks)
- **Split-Tunneling:** Deaktiviert (alle Traffic durch VPN für maximale Privacy)
- **Kill-Switch:** Aktiviert (verhindert IP-Lecks bei Verbindungsabfall)
- **Reconnect-Automatik:** Wenn Verbindung abbricht, Reconnect in 5 sec

**Netzwerk-Kontext:** VPN läuft 24/7 auf allen Devices (iPhone, iPad, Mac), mit Ausnahmen für Banking (Bank-Sicherheits-Anforderungen) und lokale LAN-Services.

---

## Devices

### **iPhone** (aktiv)
- **Model:** Aktuelles verfügbar (2025)
- **OS:** iOS 18+ (latest stable)
- **Storage:** 256 GB (ausreichend für Medien + Apps)
- **Backup:** iCloud Backup (end-to-end encrypted)
- **Location Services:** Nur für Maps/Navigation aktiviert (sonst deaktiviert)
- **Siri:** Disabled (Privacy-Concern)
- **App-Installation:** App Store only (keine Sideloading)

### **iPad Air 2025** (aktiv)
- **Model:** iPad Air (Latest gen)
- **OS:** iPadOS 18+ (synchronized mit iPhone)
- **Use-case:** Content-Consumption (Dokumente, E-Books, Video) + Note-Taking
- **Sync:** iCloud (Notes, Reminders, Calendar)
- **Apps:** Subset iPhone-Apps (kein Gaming, nur Productivity)

### **Mac** (aktiv)
- **Model:** Apple Silicon (M1/M2/M3) oder Intel (je nach aktuell verfügbar)
- **OS:** macOS 14+ (Sonoma, Sequoia)
- **Storage:** 512 GB SSD (ausreichend für Development + Dokumente)
- **Encryption:** FileVault enabled (full-disk encryption)
- **Backup:** Time Machine + Proton Drive (dokumentenspezifisch, nicht System-Full)
- **Development:** Homebrew (package manager), SSH, Terminal (für CLI-Tools)

**Device-Philosophy:** Alle Devices sind **ephemeral** — falls eins kompromittiert wird, können andere funktionieren. Keine kritischen Daten lokal (alles verschlüsselt in Cloud oder Proton Drive).

---

## Data Backup & Redundancy

| Datentyp | Backup-Methode | Frequenz | Encryption |
|---|---|---|---|
| **Kritische Dokumente** | Proton Drive (Zero-Access) | Manuell, monatlich | E2E |
| **Quellcode / Projects** | GitHub (privat Repos) + Local Git | Bei Commits | SSH-Key-protected |
| **Notizen / Markdown** | iCloud Notes + Local Git Repos | Echtzeit (iCloud) | E2E (iCloud) |
| **Passwörter / Keys** | iCloud Keychain + Proton Pass (redundant) | Echtzeit | E2E |
| **Device-Backup** | iCloud Backup (iPhone/iPad) + Time Machine (Mac) | Täglich | E2E (iCloud) |

**Notfall-Recovery:** Falls alle Devices ausfallen, können Passwörter + wichtige Dokumente von Proton Drive wiederhergestellt werden (mit iCloud Keychain Backup-Codes lokal verfügbar).

---

## Network & Connectivity

### **Residential Network**
- **ISP:** Aktuell verfügbar (unbedeutend, Privacy-Fokus liegt auf VPN)
- **Router:** Standard Consumer-Router (kein speziales Setup)
- **WiFi:** WPA3 (falls verfügbar), sonst WPA2
- **VPN:** Alle Devices verbinden über VPN (kein lokales Netzwerk-Tracking)

### **Mobile Network**
- **Provider:** Aktuell verfügbar (e.g., Vodafone, Telekom DE)
- **Data Plan:** Standard mit ausreichendem Kontingent
- **VPN on Mobile:** Proton VPN läuft über Cellular + WiFi

---

## Future Infrastructure Planning

| Initiative | Timeline | Zweck |
|---|---|---|
| **iCloud Keychain vollständig aktivieren** | Q3 2026 | Passwort-Manager-Zentralisierung |
| **Proton Drive Integration evaluieren** | Q4 2026 | Alternative zu iCloud Drive für sensitive Dokumente |
| **Selbst-gehosteter Gitea-Server (optional)** | 2027+ | Falls GitHub-Abhängigkeit verringert werden soll (low priority) |
| **DNS-over-HTTPS (DoH) aktivieren** | 2026 | Auf allen Devices für zusätzlichen DNS-Privacy |
| **Hardware Security Key (YubiKey) Backup-Ersatz** | Q3 2026 | Falls Schlüssel verloren geht; Redundanz-Pair kaufen |

---

## Fehlerhafte / Deprecated Services (Archiv)

| Service | Grund für Ausstieg | Datum |
|---|---|---|
| Google Drive | Privacy-Concern (Google-Analytics-Integration) | pre-2024 |
| Dropbox | Closed-Source, Datenschutz-Bedenken | pre-2024 |
| 1Password (früher) | Migration zu Proton Pass (dann Apple Passwords) | 2025–2026 |

---

## Verwandte Seiten

- **[[MOC Tech & Setup]]** — übergeordneter Tech-Manifest
- **[[Privacy & Tech Stack]]** — Privacy-fokussierte Ökosystem-Auswahl
- **[[Password Manager Migration]]** — Proton Pass → Apple Passwords Details
- **[[Claude Projects Setup]]** — Development-Infrastruktur für AI-assisted Coding
- **[[ok-holding.com]]** — Domain-Entität
- **[[Proton Mail]]** — E-Mail-Service
- **[[Proton VPN]]** — VPN-Service
- **[[Oleg Personal Context]]** — Person-Master-Index
