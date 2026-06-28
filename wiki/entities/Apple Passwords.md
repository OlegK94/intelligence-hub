---
title: "Apple Passwords"
type: entity
tags: [password-manager, apple, native-macos, autofill, biometric, icloud-sync, face-id, touch-id, limited-fields]
sources: ["raw/raw/_archiv/legacy-numbered-folders/03-Tech-Setup/Password Manager Migration.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Apple Passwords — Native Password Manager in macOS/iOS (seit 2024); Tight Integration mit Safari/Chrome/Firefox Autofill, Face ID/Touch ID Biometric Unlock, iCloud Sync; limitierte Feldunterstützung (kein Custom Fields, Single URL, keine Identities, keine Secure Notes, keine Vault-Struktur); Import aus CSV möglich (US-Standard-Delimiter erforderlich)
---

# Apple Passwords

## Überblick

[[Apple Passwords]] ist Apples **Native Password Manager** in macOS 15+/iOS 18+ (eingeführt 2024), mit dem Ziel einer **seamless, privacy-first Passwort-Verwaltung** im Apple-Ökosystem.

---

## Kernfeatures

| Feature | Status |
|---|---|
| **Grundlagen** | |
| Passwort-Speicherung & Verschlüsselung | ✅ iCloud Keychain (E2EE) |
| Passwort-Generator | ✅ |
| Autofill (Safari, Chrome, Firefox) | ✅ Seamless via Extension |
| Vault-Struktur | ❌ Flat List (keine Ordner) |
| **Erweiterte Felder** | |
| Custom Fields | ❌ |
| Mehrere URLs pro Eintrag | ❌ (Single URL Only) |
| Kreditkarten-Speicherung | ❌ (separat in Apple Wallet) |
| Identity-Einträge | ❌ |
| Secure Notes | ❌ |
| **Authentifizierung** | |
| TOTP/OTPAuth | ⚠️ Unterstützt, aber manuell re-enroll erforderlich |
| Passkeys | ⚠️ Unterstützt, aber manuell re-enroll erforderlich |
| **Sicherheit** | |
| End-to-End Encryption | ✅ iCloud Keychain (E2EE) |
| Biometric Unlock | ✅ Face ID / Touch ID |
| iCloud Sync | ✅ |

---

## Feldunterstützung (Limitiert)

Apple Passwords speichert per Eintrag:
- **Username / Email**
- **Password**
- **URL** (einzeln, nicht mehrfach)
- **Notes** (einfache Freitext, nicht verschlüsselt auf Cloud)

**Nicht unterstützt:**
- Custom Fields (z.B. Admin-PIN, Sicherheitsfragen)
- Multi-URL-Speicherung
- Identities (persönliche Daten-Einträge)
- Secure Notes (verschlüsselte Notizen)
- Vault-Struktur / Ordner-Kategorisierung

---

## Import aus CSV

Apple Passwords akzeptiert CSV-Import mit:
- **US-Standard CSV** (Komma-Trennzeichen)
- **Spalten:** Username, Password, URL, Notes

**Problem bei Migration von [[Proton Pass]]:**
Proton-Export mit deutschem Locale verwendet Semikolon-Trennzeichen → Fehler beim Import.

**Lösung:** Siehe [[Password Manager Migration]] — CSV-Delimiter-Fix erforderlich.

---

## Post-TOTP-Migration

Wenn Proton Pass TOTP-Codes speichert, sind diese **nicht direkt exportierbar**. Nach Apple Passwords Migration ist erforderlich:

1. **TOTP-Secrets auslesen** aus Proton Pass (bzw. aus ursprünglichen 2FA-Setup-QR-Codes)
2. **Manuell re-enroll** in Apple Passwords oder Authenticator-App (z.B. Microsoft Authenticator, Google Authenticator)

---

## Apple Wallet (separate App)

Für Kreditkarten-Speicherung von Proton Pass müssen diese manuell zu **Apple Wallet** migiert werden:
1. Apple Wallet öffnen
2. "Karte hinzufügen" → manuell eingeben
3. Nicht ideal für Migration in Batch

---

## Use Cases

- **Optimal für** Benutzer, die zu 80%+ einfache Login + Passwort + TOTP-Workflows nutzen
- **Optimal für** Apple-Only-Nutzer (MacBook + iPhone + iPad) ohne Windows/Linux-Anforderung
- **Nicht geeignet für** Komplexe Konto-Management-Anforderungen (Banking mit Admin-Panels, Multi-URL-Einträge)

---

## Vergleich mit [[Proton Pass]]

Siehe [[Password Manager Migration]] — Kompatibilitäts-Matrix.

---

## Verwandte Seiten

- **[[Proton Pass]]** — Alternativer Password Manager
- **[[Password Manager Migration]]** — Entscheidungsrahmen für Wechsel
- **[[Tech Stack & Security Decisions]]** — Übergeordnetes Framework
