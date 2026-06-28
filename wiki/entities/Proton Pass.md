---
title: "Proton Pass"
type: entity
tags: [password-manager, proton, security, encryption, end-to-end, multi-url, custom-fields, totp, passkeys, vault]
sources: ["raw/raw/_archiv/legacy-numbered-folders/03-Tech-Setup/Password Manager Migration.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Proton Pass — Full-Featured Password Manager von Proton AG (Schweiz); Support für Custom Fields, Multi-URL pro Eintrag, Kreditkarten, Identity-Einträge, Secure Notes, Vault-Struktur, TOTP/OTPAuth, Passkeys; Export via CSV (Deutsches Locale Semikolon-Delimiter)
---

# Proton Pass

## Überblick

[[Proton Pass]] ist ein **Full-Featured, End-to-End Encrypted Password Manager** von Proton AG (Schweiz), verfügbar für Windows, macOS, Linux, iOS, Android, und Browser-Erweiterungen.

---

## Kernfeatures

| Feature | Status |
|---|---|
| **Grundlagen** | |
| Passwort-Speicherung & Verschlüsselung | ✅ E2EE (AES-256) |
| Passwort-Generator | ✅ |
| Autofill (Browser-Ext.) | ✅ Chrome, Firefox, Safari |
| Vault-Struktur (Ordner/Kategorien) | ✅ |
| **Erweiterte Felder** | |
| Custom Fields | ✅ Unbegrenzt |
| Mehrere URLs pro Eintrag | ✅ |
| Kreditkarten-Speicherung | ✅ |
| Identity-Einträge (Persönliche Daten) | ✅ |
| Secure Notes | ✅ Verschlüsselte Freitext-Notizen |
| **Authentifizierung** | |
| TOTP/OTPAuth | ✅ Builtin |
| Passkeys | ✅ (WebAuthn-Support) |
| **Sicherheit** | |
| End-to-End Encryption | ✅ |
| Zero-Knowledge Architecture | ✅ |
| Audit-Logs | ✅ |

---

## CSV-Export (mit Locale-Besonderheit)

**Standard-CSV-Export** mit folgendem Verhalten:

### Deutsches Locale
- **Feldtrennzeichen:** Semikolon (`;`) statt Komma
- **Dezimalzahl-Trennzeichen:** Komma (`,`)
- **Impact:** Viele andere Password Manager erwarten US-Standard-CSV (Komma-Trennzeichen)

### Workaround
Siehe [[Password Manager Migration]] — CSV in VS Code mit Find & Replace beheben:
```
; → ,  (mit Vorsicht bei Feldern, die selbst ; oder , enthalten)
```

---

## Vault-Struktur

Proton Pass unterstützt **beliebig verschachtelte Vault-Ordner** zur Kategorisierung:
- Personal
- Work
- Banking
- (beliebige eigene Kategorien)

Diese Struktur wird **nicht exportiert** in der CSV, was zu Datenverlust bei Migration führt.

---

## Use Cases

- **Primär für** Komplexe Konto-Management-Anforderungen (Banking, Custom-Fields für Admin-PINs)
- **Nicht optimal für** Benutzer, die nur Login + Passwort + TOTP benötigen und auf native macOS-Integration wert legen

---

## Vergleich mit [[Apple Passwords]]

Siehe [[Password Manager Migration]] — Kompatibilitäts-Matrix.

---

## Verwandte Seiten

- **[[Apple Passwords]]** — Alternativer Password Manager
- **[[Password Manager Migration]]** — Entscheidungsrahmen für Wechsel
- **[[Tech Stack & Security Decisions]]** — Übergeordnetes Framework
