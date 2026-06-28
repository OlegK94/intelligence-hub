---
title: "Privacy & Tech Stack"
type: concept
tags: [privacy, tech-stack, security, browser, vpn, password-manager, encryption, device-management]
sources: ["raw/raw/_archiv/legacy-numbered-folders/00-MOC/MOC Tech & Setup.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Persönlicher Tech-Stack mit Fokus auf Privacy und Sicherheit — Browser (Brave/Safari), VPN (Proton), Passwort-Manager (Proton Pass → Apple Passwords Migration), Verschlüsselte E-Mail (Proton Mail); Basis-Prinzip zero-tracking, end-to-end-encryption, kontinuierliche Migration zu Apple-Ökosystem
---

# Privacy & Tech Stack

## Überblick

Der persönliche Privacy & Tech Stack ist ein **bewusst gewähltes Ökosystem aus Privacy-fokussierten Tools**, das dem Prinzip **"Datenminimierung + Verschlüsselung + Dezentralisierung"** folgt. Das System ist nicht statisch — es gibt eine aktive **Migration von Proton-Ökosystem zu Apple-nativen Alternativen** (mit Beibehaltung von Proton Mail als E-Mail-Backbone, solange Sicherheit gewährleistet ist).

> **Kernprinzip:** Keine unnötigen Daten an Third-Party-Plattformen; E2E-Verschlüsselung als Standard; Vertrauen zu minimalen, transparenten Anbietern.

---

## Browser-Strategie

### Desktop: **Brave**
- **Warum Brave?** Privacy-fokussiert, Chromium-Basis (schnell), native Cookie-Blocking, Fingerprinting-Schutz
- **Tracker-Blocking:** Aggressive (Standard), mit manuellen Whitelist-Exceptions für notwendige Sites
- **Sync-Backend:** Dezentralisiert über Brave Sync (kein zentraler Google/Microsoft Account)
- **Anmerkung:** Brave-Rewards deaktiviert (keine Datenmonetisierung)

### Mobile (iOS): **Safari**
- **Warum Safari?** Apple-Integrationslevel am höchsten; Privacy-Labels in App Store; Locale-Datenspeicherung ohne Cloud-Sync
- **iCloud Private Relay:** Aktiviert (Apple-VPN-Layer für DNS-Schutz)
- **Sync-Backend:** iCloud Keychain, begrenzt auf Apple-Ökosystem (kein Google-Account erforderlich)

**Keine Chrome, Firefox oder andere Ad-Tech-nahe Browser.**

---

## VPN-Lösung: **Proton VPN**

| Aspekt | Auswahl | Begründung |
|---|---|---|
| **Anbieter** | Proton VPN (Zero-Logs) | Swiss Headquarters, Open-Source-Audits, No-Log-Verifizierung durch unabhängige Audits |
| **Protocol** | WireGuard (schnell) oder OpenVPN (robust) | WireGuard für tägliche Nutzung (schneller, moderner) |
| **Kill-Switch** | Aktiviert | Verhindert Daten-Lecks bei VPN-Verbindungsabfall |
| **Split-Tunneling** | Fallweise aktiviert | Lokale Bankings-Apps müssen oft ohne VPN laufen; selective routing |
| **DNS over VPN** | Proton DNS (default) | Keine externen DNS-Leaks; Proton-Ökosystem-Integration |

**Datenschutz-Annahme:** Proton VPN ist **Zero-Logs-zertifiziert**, aber das setzt Vertrauen in die Organisation voraus. Audit-Reports sind öffentlich verfügbar.

---

## Passwort-Manager: Migration **Proton Pass → Apple Passwords**

### Status quo (Juni 2026)
- **Aktuell:** Proton Pass (mit einigen Passwörtern)
- **Ziel:** Apple Passwords (iCloud Keychain basiert)
- **Timeline:** Q3 2026 angestrebt
- **Grund für Migration:**
  - **Tighter Apple-Integration:** Safari, macOS, iOS Autofill nahtlos
  - **Weniger Abhängigkeit:** Weniger Dritter verwaltet sensitive Keys (nur Apple)
  - **2FA-Integration:** Apple Passwords hat native 2FA-Code-Generator (ähnlich Authenticator)

### Migration-Checkliste
- [ ] Alle Proton-Pass-Passwörter in iCloud Keychain importieren
- [ ] Test: Autofill-Funktion auf iPhone, iPad, Mac (3–5 Test-Logins)
- [ ] Kritische Passwörter (Bank, E-Mail) zweifach verifizieren
- [ ] Proton Pass deinstallieren oder zur Backup-Only-Verwendung reduzieren
- [ ] 2FA-Codes migrieren (Authenticator App → Apple Passwords / Authenticator hybrid)

**Risiko:** Apple Passwords sind iCloud-gebunden; falls iCloud-Account kompromittiert, sind alle Passwörter exponiert. Mitigation: Apple 2FA mit Sicherheitsschlüssel (YubiKey etc.) aktivieren.

---

## E-Mail: **Proton Mail** (keine Migration geplant)

| Aspekt | Auswahl | Begründung |
|---|---|---|
| **Provider** | Proton Mail | E2E-verschlüsselt; Proton-Ökosystem-Integration (Proton Pass, Proton Drive) |
| **Plan** | Proton Unlimited (oder ähnlich) | Für mehrere Mailboxen, Proton Drive, VPN-Integration |
| **2FA** | U2F / Sicherheitsschlüssel | Nicht nur TOTP (Authenticator App) |
| **Alias-Struktur** | Mehrere Mailadressen via Alias | Verschiedene Kontexte (Work, Personal, Throwaway) von einer Mailbox aus |
| **Synchronisation** | IMAP-Zugabe prüfen | Falls notwendig; aber native Proton Mail App bevorzugt |

**Warum kein Wechsel zu Apple iCloud Mail?** iCloud Mail hat weniger E2E-Verschlüsselung für externe Empfänger; Proton Mail ist transparenter mit seinen Crypto-Claims und hat unabhängige Audits.

---

## Gerätemanagement

### **iPhone + iPad Air 2025**
- **OS:** iOS 18+ (letztes verfügbar)
- **iCloud Sync:** Aktiviert für Keychain, Notes, Reminders, Calendar (aber nicht für Photos, Documents — lokal only)
- **2FA Backup:** U2F-Sicherheitsschlüssel (Yubikey) + Backup-Codes lokal in Proton Drive gespeichert
- **Appstore:** Ausschließlich verifizierte Apps; keine sideloaded APKs

### **Mac (Apple Silicon / Intel)**
- **OS:** macOS 14+ (Sonoma, Sequoia)
- **FileVault:** Aktiviert (Vollverschlüsselung)
- **iCloud Sync:** Wie iPhone (Keychain, Notes)
- **Homebrew / Package Manager:** Nur signierte Packages; regelmäßige Audits
- **Terminal / SSH:** SSH-Keys in Secure Enclave (Apple Silicon) oder verschlüsselt in FileVault (Intel)

### **Domain & Webmail**
- **Domain:** ok-holding.com (via GoDaddy)
- **Mail-Handling:** Weitergeleitet zu Proton Mail (externe Verwaltung über GoDaddy DNS)
- **DNSSEC:** Aktivieren (zukünftig) für zusätzliche Domain-Authentifizierung

---

## 2FA & Sicherheitsschlüssel-Strategie

| Account-Typ | 2FA-Methode | Hardware | Backup |
|---|---|---|---|
| **E-Mail (Proton Mail)** | U2F Sicherheitsschlüssel | YubiKey 5 (2× vorhanden) | Backup-Codes in Proton Drive |
| **Apple ID** | U2F + Trusted Devices | YubiKey 5 | Wiederherstellungscodes lokal |
| **Banking** | mTAN / Authentifier | Hardware-Token (Bank) | Notfall-Kodes bei Bank |
| **Allgemeine Accounts** | TOTP (Authenticator) | Apple Passwords (ab Migration) | Backup-Codes in Secure Note |

**Best Practice:**
- Keine SMS-basierte 2FA (SIM-Swapping-Risiko)
- Wo möglich: Hardware-Schlüssel (YubiKey) oder Apple U2F
- Backup-Codes lokal und in Proton Drive duplizieren (verschlüsselt)

---

## Daten-Minimisierungsprinzipien

### Was wird **aktiv vermieden**:
- ❌ Google Analytics, Facebook Pixel (auch nicht über Brave Shielding)
- ❌ Convenience-Sign-Ups (Google/Apple/Facebook Login) — nur notwendig für vertrauenswürdige Apps
- ❌ Standort-Tracking (Location Services nur für Maps/Navigation aktiviert)
- ❌ Cloud-Photo-Synchronisierung (Photos bleiben lokal auf Devices; iCloud Photos optional disabled)
- ❌ Siri-Daten-Übertragung (Siri nur offline oder absolut notwendig)

### Was ist **akzeptiert** (mit Trade-offs):
- ✅ iCloud Backup (für Device-Sicherheit, aber nur iCloud-encrypted Items)
- ✅ Proton Mail (Proton sieht Metadaten, aber nicht E-Mail-Inhalt durch E2E)
- ✅ Proton VPN Logs (Zero-Logs-Zertifikat, aber Trust required)
- ✅ Brave Browser Telemetrie (anonymisiert; Brave verpflichtet sich zu No-Tracking)

---

## Regelmäßige Audits & Maintenance

| Aufgabe | Frequenz | Verantwortung |
|---|---|---|
| **Passwort-Audit** | Monatlich | Check für wiederholte/schwache Passwörter (Apple Passwords integrierter Check) |
| **2FA-Überprüfung** | Quartal | Sicherheitsschlüssel funktionieren? Backup-Codes aktuell? |
| **Proton Mail Security-Report** | Quartal | Proton bietet wöchentliche Reports; Check auf unerwünschte Zugriffe |
| **OS & App Updates** | Wöchentlich | Auto-Updates aktiviert; kritische Updates sofort |
| **Browser-Plugin-Audit** | Quartal | Nur notwendige Extensions; alle anderen deinstallieren (Sicherheitsrisiko) |

---

## Integration mit Arbeitskontexten

### **Work (Doctolib, Provision-Einnahmen)**
- Separate E-Mail-Alias für Work (z.B. work@ok-holding.com)
- Kein persönliches Passwort-Manager-Zugriff auf Work-Account (separate iCloud?)
- VPN kann deaktiviert sein für Arbeitskontexte (Banking-equivalent Sicherheit erforderlich)

### **Personal / Finanzen**
- Maximale Privacy-Maßnahmen
- Bankings-Zugänge nur ohne VPN (Bank-Security-Requirements)
- Separate Hardware-Schlüssel für sensitive Accounts (Banking, Proton Mail)

---

## Zukünftige Migrations-Pläne

1. **Q3 2026:** Proton Pass → Apple Passwords (vollständig)
2. **Q4 2026:** Evaluierung von Proton Drive → iCloud Drive (mit Verschlüsselung-Trade-off)
3. **2027+:** Möglicher Wechsel zu Bitwarden (open-source, weniger Proton-Abhängigkeit) — aber nur falls notwendig

---

## Verwandte Seiten

- **[[MOC Tech & Setup]]** — übergeordneter Tech-Manifest
- **[[Claude Projects Setup]]** — Claude Code-Integration mit Privacy-Überlegungen
- **[[Password Manager Migration]]** — detaillierte Migrationscheckliste
- **[[Proton Mail]]** — E-Mail-Backbone
- **[[Brave Browser]]** — Desktop-Browser
- **[[Safari]]** — Mobile-Browser
- **[[iCloud Keychain]]** — Passwort-Manager-Ziel
- **[[Oleg Personal Context]]** — Person-Master-Index
