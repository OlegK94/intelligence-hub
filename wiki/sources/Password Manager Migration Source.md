TAGS: [tech, password-manager, migration, proton-pass, apple-passwords, decision-framework, entscheidung-ausstehend, csv, delimiter, custom-fields]
SOURCES: ["raw/Privat/Tech/Password Manager Migration.md"]
CREATED: 2026-06-09
UPDATED: 2026-06-18
SUMMARY: Quelldokument Password Manager Migration (Proton Pass → Apple Passwords); Status: Entscheidung ausstehend; CSV-Export-Problem (deutsches Locale → Semikolon statt Komma); Feldinkompatibilität (Custom Fields, Multi-URL, Kreditkarten, Identity, Secure Notes, Vaults nicht in Apple Passwords); Decision Framework: Obige Felder >50% aktiv genutzt → Proton Pass bleiben; <20% → Migration+Cleanup machbar
SUMMARY_DE: Quelldokument zur Password-Manager-Migration von Proton Pass zu Apple Passwords; CSV-Delimiter-Problem durch deutsches Locale gelöst via VS Code Find & Replace; Kompatibilitätsmatrix zeigt signifikante Feature-Gaps in Apple Passwords (keine Custom Fields, Multi-URL, Kreditkarten, Identity-Einträge, Secure Notes, Vault-Struktur); Decision Framework abhängig von tatsächlicher Nutzungsquote der fehlenden Felder
---

# Password Manager Migration — Proton Pass → Apple Passwords

## Status: Entscheidung ausstehend

Dieses Quelldokument adressiert die Frage: **Sollte von Proton Pass zu Apple Passwords migriert werden?** Die Entscheidung hängt davon ab, wie aktiv bestimmte Felder tatsächlich genutzt werden, die in Apple Passwords nicht verfügbar sind.

## Versuchte Migration & Fehlerquellen

### CSV-Export aus Proton Pass
- CSV-Datei erfolgreich aus Proton Pass exportiert
- **Problem:** Deutsches Locale
  - Proton Pass nutzt Semikolon (`;`) als CSV-Delimiter
  - Apple Passwords erwartet Komma (`,`) als Delimiter
  - **Resultat:** Import-Fehler in Apple Passwords

### Feldinkompatibilität
Apple Passwords kann eine Reihe von Feldern nicht abbilden, die Proton Pass unterstützt:

| Feld | Proton Pass | Apple Passwords | Impact |
|---|---|---|---|
| **Custom Fields** | ✅ | ❌ | Kontofeldnummern, PINs, Custom-Notizen verloren |
| **Mehrere URLs pro Eintrag** | ✅ | ❌ | Nur 1 primäre URL möglich; Backup-URLs gelöscht |
| **Kreditkarten** | ✅ | ❌ (separat in Wallet) | Kartendaten müssen separat zu Apple Wallet migriert werden |
| **Identity-Einträge** | ✅ | ❌ | Persönliche Daten (Adresse, Geburtsdatum) verloren |
| **Secure Notes** | ✅ | ❌ | Freie Notizen nicht portierbar |
| **Vault-Struktur** (Ordnung) | ✅ | ❌ | Alle Einträge in „iCloud Keychain" flat; Kategorisierung verloren |
| **TOTP / OTPAuth** | ✅ | ✅ (aber manuell re-enroll) | 2FA-Codes müssen manuell neu hinzugefügt werden |
| **Passkeys** | ✅ | ✅ (aber manuell re-enroll) | WebAuthn-Passkeys müssen auf kompatiblen Websites neu registriert werden |

## Decision Framework

### Szenario A: Proton Pass behalten
**Bleiben bei Proton Pass**, wenn:
- Custom Fields sind **aktiv genutzt** (z.B. Kontofeldnummern, PINs, etc.) → häufig
- Mehrere URLs pro Eintrag sind **aktiv genutzt** → oft bei Multi-Account-Szenarien
- Kreditkarten, Identities oder Secure Notes sind **aktiv genutzt**
- Vault-Struktur / Ordnung ist wichtig für Workflow

**Ergebnis:** Proton Pass-Integration mit Apple Ecosystem ist suboptimal, aber Feature-Verlust ist unakzeptabel.

### Szenario B: Zu Apple Passwords migrieren
**Migration zu Apple Passwords ist sinnvoll**, wenn:
- Custom Fields sind **Legacy, größtenteils ungenutzt** (<20% der Einträge mit Custom Data)
- Mehrere URLs sind **nicht standardmäßig genutzt** (<20% der Einträge)
- Kreditkarten, Identities, Secure Notes sind **minimal oder nicht genutzt**
- Vault-Struktur ist **flach oder irrelevant** für Workflow
- Workflow ist **fast ausschließlich Benutzername + Passwort + ggf. TOTP**
- **Apple-Integration** (Autofill in Safari, iCloud Keychain Sync) ist gewünscht

**Ergebnis:** Seamless Apple-Integration ist attraktiv, aber nur wenn Feature-Verlust minimal ist.

## Zu klärende Punkte (Audit-Checkliste)

- [ ] **Durchgehen:** Wie viele Proton Pass Einträge nutzen tatsächlich Custom Fields?
- [ ] **Durchgehen:** Wie viele Einträge haben mehrere URLs?
- [ ] **Durchgehen:** Sind Kreditkarten im Einsatz?
- [ ] **Durchgehen:** Sind Identity-Einträge vorhanden?
- [ ] **Durchgehen:** Sind Secure Notes mit wichtigen Daten gefüllt?
- [ ] **Durchgehen:** Wird die Vault-Struktur als Organisationsmittel genutzt?
- [ ] **Ergebnis <20% Felder-Nutzung:** Cleanup + Migration machbar
- [ ] **Ergebnis 20–50%:** Hybrid-Ansatz oder Proton Pass behalten?
- [ ] **Ergebnis >50%:** Bei Proton Pass bleiben; Apple Passwords nicht geeignet

## Technisches Fix für CSV-Delimiter-Problem

Falls Migration fortgesetzt wird, kann das Delimiter-Problem wie folgt gelöst werden:

### Via VS Code (einfach)
1. **CSV in VS Code öffnen**
   - Datei → Öffnen: `proton-pass-export.csv`
   - Encoding: UTF-8

2. **Find & Replace durchführen**
   - Shortcut: `Ctrl+H` (Windows/Linux) oder `Cmd+H` (Mac)
   - **Find:** `;`
   - **Replace:** `,`
   - **Replace All** klicken

3. **Vorsicht: Felder mit Kommas wrappen**
   - Wenn Feldwerte selbst Kommas enthalten, müssen diese in doppelte Anführungszeichen gewrapped werden:
     - `Feldname,"Wert mit, Komma",Passwort` → `"Feldname","Wert mit, Komma","Passwort"`
   - VS Code-Replace kann dies mit Regex automatisieren (komplexer)

4. **Datei speichern** und in Apple Passwords importieren

### Via Python (robust)
```python
import csv

# Proton Pass CSV mit Semikolon-Delimiter lesen
with open('proton-pass-export.csv', 'r', encoding='utf-8') as f_in:
    reader = csv.DictReader(f_in, delimiter=';')
    rows = list(reader)

# Mit Komma-Delimiter schreiben (Apple Passwords)
with open('proton-pass-export-apple.csv', 'w', newline='', encoding='utf-8') as f_out:
    if rows:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(f_out, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(rows)
```

## TOTP & Passkeys Neu-Registrierung

Falls zu Apple Passwords migriert wird:

### TOTP (2FA-Codes)
- **Problem:** TOTP-Secrets können **nicht** direkt aus Proton Pass exportiert und in Apple Passwords importiert werden
- **Lösung:** 
  - Für jeden Dienst einzeln: 2FA neu einrichten (neuen QR-Code / Secret scannen)
  - **Aufwand:** 30–60 min für 10–20 Accounts mit TOTP
  - **Tipp:** Browser-Plugins wie Authy oder Microsoft Authenticator können Backup-Codes/Secrets speichern

### Passkeys (WebAuthn)
- **Problem:** Bestehende Passkeys in Proton Pass sind an Proton gebunden; Apple Keychain hat eigene Passkey-Infrastruktur
- **Lösung:**
  - Websites, die bereits Passkeys nutzen: Neuen Passkey mit Apple Keychain registrieren (meist über "Add security key" Option)
  - Alte Proton-Passkeys löschen (meist in Website-Sicherheitseinstellungen)
  - **Aufwand:** minimal (meist 1–2 Klicks pro Website)

## Zusammenfassung

| Aspekt | Proton Pass | Apple Passwords |
|---|---|---|
| **Feature-Reichtum** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Custom Fields** | ✅ | ❌ |
| **Mehrere URLs** | ✅ | ❌ |
| **Kreditkarten** | ✅ | ❌ (Apple Wallet) |
| **Identities** | ✅ | ❌ |
| **Secure Notes** | ✅ | ❌ |
| **Vaults** | ✅ | ❌ |
| **Apple Integration** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **iCloud Sync** | Nein | Ja |
| **Autofill Safari** | Ja (aber suboptimal) | Ja (seamless) |
| **Cross-Platform** | ⭐⭐⭐⭐ | ⭐⭐ (Apple-only) |

**Empfehlung:** Abhängig von Audit-Ergebnis (siehe Checkliste oben). Wenn <20% der Einträge spezielle Features nutzen, ist Migration zu Apple Passwords attraktiv. Wenn >50%, sollte Proton Pass beibehalten werden.

---

## Verknüpfungen

- [[Privacy & Tech Stack]] — Privacy-zentrierte Tools; Proton Suite Integration
- [[MOC Tech & Setup]] — Master of Change: Tech & Setup Übersicht
- [[Proton Pass]] — Entity-Seite
- [[Apple Passwords]] — Entity-Seite
