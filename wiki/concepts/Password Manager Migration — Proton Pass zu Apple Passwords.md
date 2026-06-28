---
title: "Password Manager Migration — Proton Pass zu Apple Passwords"
type: concept
tags: [tech, passwords, migration, entscheidung-offen, proton-pass, apple-passwords, feldinkompatibilität, csv-delimiter, mac-integration]
sources: ["raw/raw/_archiv/legacy-numbered-folders/03-Tech-Setup/Password Manager Migration.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Entscheidungsrahmen für Migration von Proton Pass zu Apple Passwords; Blockierende Probleme: Feldinkompatibilität (Custom Fields, Multi-URL, Kreditkarten, Identity-Einträge, Secure Notes, Vault-Struktur), CSV-Delimiter-Problem (Deutsches Locale Semikolon statt Komma); Go/No-Go-Kriterium basierend auf Audit Legacy-Datennutzung (<20% aktiv → Wechsel sinnvoll; >50% → Bleiben bei Proton); technisches Fix: CSV Find & Replace in VS Code
---

# Password Manager Migration — Proton Pass zu Apple Passwords

## Status: Entscheidung ausstehend

Das Quelldokument dokumentiert einen unvollendeten Migrationsprozess aus Proton Pass zu Apple Passwords. Der Status ist **Entscheidung ausstehend** — die Migration ist nicht blockiert durch technische Unmöglichkeit, sondern durch ein **Go/No-Go-Audit:** Werden die fehlenden Proton-Pass-Felder tatsächlich aktiv genutzt?

---

## Problem 1: Feldinkompatibilität (Strukturell)

Apple Passwords unterstützt ein **begrenzteres Feldset** als Proton Pass. Die wichtigsten fehlenden Felder:

| Feld | Proton Pass | Apple Passwords | Impact |
|---|---|---|---|
| **Custom Fields** | ✅ | ❌ | z.B. Kontonummern, PINs, Sicherheitsfragen → verloren |
| **Mehrere URLs pro Eintrag** | ✅ | ❌ | z.B. Login-URL + Admin-Panel → nur eine URL |
| **Kreditkarten** | ✅ | ❌ (separat in Wallet) | Zahlungsdaten → manuell zu Apple Wallet migrieren |
| **Identity-Einträge** | ✅ | ❌ | Persönliche Daten (Name, Adresse, etc.) → verloren oder manuell gemanagt |
| **Secure Notes** | ✅ | ❌ | Freitext-Notizen → verloren |
| **Vault-Struktur (Ordnung)** | ✅ | ❌ | Kategorisierung (Work, Personal, Banking) → flache Liste in Apple |

**Konsequenz:** Eine naive CSV-Import-Migration würde alle diese Felder **verlieren**.

---

## Problem 2: CSV-Delimiter-Problem (Operativ)

### Ursache
Das deutsche Locale in Proton Pass exportiert CSVs mit **Semikolon (`;`)** statt Komma (`,`)** als Feldtrennzeichen. Dies ist eine Windows/DE-System-Einstellung.

### Impact
- Apple Passwords erwartet US-Standard-CSV (Komma-Trennzeichen)
- Import schlägt fehl oder liest Felder falsch ein
- Manueller Fix erforderlich vor Import

### Lösung (Technischer Fix)
Implementiert in VS Code:

1. CSV in VS Code öffnen
2. **Find & Replace:** Alle `;` → `,`
3. **Achtung:** Felder die selbst Kommas enthalten (z.B. Adresse mit Straße, PLZ, Ort) → müssen manuell mit Quotes `"` gewrapped werden
4. Speichern und neu probieren

**Beispiel:**
```
Vorher (Proton DE):
Username;Password;URL;Custom:"My PIN"
john.doe;pass123;example.com;1234

Nachher (Apple-kompatibel):
Username,Password,URL,Custom:"My PIN"
john.doe,pass123,example.com,1234
```

---

## Go/No-Go-Entscheidungsrahmen

### ✅ Wechsel zu Apple Passwords sinnvoll, wenn:
- Custom Fields, Multi-URL, Identity-Einträge, Secure Notes sind **größtenteils Legacy / ungenutzte Daten**
- Workflow ist zu >80% **Benutzername + Passwort + TOTP**
- **Sealing-Faktor:** Volle Apple-Integration (Autofill auf MacBook/iPhone/iPad seamless)
- Bereitschaft für einmaligen **Cleanup-Aufwand** (~2–4 Stunden Audit + CSV-Fix + Manuelles Wrapping)

### ❌ Bleiben bei Proton Pass, wenn:
- Custom Fields werden **aktiv genutzt** (z.B. Backup-Codes, Admin-PINs, Kontoinformationen)
- Mehrere URLs pro Eintrag sind **wichtig** (z.B. Banking: Login-URL + Kontoverwaltungs-URL + Support-Portal)
- Kreditkarten / Identity-Einträge / Secure Notes sind **nicht negligible**
- Vault-Struktur ist **Workflow-kritisch** (z.B. Trennung Work/Personal/Banking)

---

## Audit-Checkliste (Vorbereitung der Entscheidung)

Vor der Migration: **Folgende Punkte durchgehen:**

1. **Custom Fields in Proton-Pass-Einträgen:**
   - [ ] Wie viele Einträge haben Custom Fields?
   - [ ] Was enthalten sie? (Sicherheitsfragen, PINs, Kontonummern?)
   - [ ] Werden diese Fields regelmäßig abgerufen oder sind es Legacy-Daten?

2. **Multi-URL-Einträge:**
   - [ ] Welche Konten nutzen mehrere URLs?
   - [ ] Ist die Sekundär-URL essenziell oder nur "nice-to-have"?

3. **Identities & Secure Notes:**
   - [ ] Wie viele Identity-Einträge gibt es?
   - [ ] Sind die Secure Notes strukturiert genug, um sie in Apple Notes zu migrieren?

4. **Vault-Struktur:**
   - [ ] Wird die Kategorisierung (Work/Personal/Banking) aktiv für Akquisition / Filterung genutzt?
   - [ ] Oder ist es nur "nice-to-have" Organization?

**Schwellenwerte:**
- **<20% der Einträge** nutzen die fehlenden Felder → **Migration sinnvoll**
- **20–50%** → **Hybrid-Ansatz:** Proton bleiben für komplexe Konten, Apple für 80/20-Konto-Management
- **>50%** → **Nicht migrieren**, bei Proton bleiben

---

## Workflow-Verbesserung: Apple Passwords auf Mac

### Native Vorteile
- **Autofill in Safari, Chrome, Firefox:** Passwort-Eintrag → direkt in Autofill-Menü
- **Biometric Unlock:** Face ID / Touch ID für schnelle Zugänge
- **iCloud Sync:** Automatisch auf MacBook, iPhone, iPad
- **Kein Drittanbieter-Abhängigkeit:** Tight Integration mit macOS/iOS

### Nachteile
- **Weniger Feldflexibilität** (siehe Kompatibilitätstabelle oben)
- **Apple-only:** Kein Windows/Linux-Support (nur iCloud-Web-Interface)
- **Backup-Komplexität:** Apple-Ökosystem-abhängig

---

## Entscheidungsempfehlung (wenn Audit <20% zeigt)

**Wenn der Audit zeigt, dass <20% der Proton-Pass-Einträge aktiv Custom Fields, Multi-URL, oder Secure Notes nutzen:**

1. **Cleanup:** Die 20% komplexen Konten in Proton Pass behalten oder manuell in Apple Notes migrieren
2. **CSV-Fix:** Delimiter-Problem in VS Code beheben (5–10 min)
3. **Import:** Gefüllte CSV in Apple Passwords importieren
4. **Validation:** Spot-Check 10–20 Einträge nach Import
5. **Verlustvortrag:** Akzeptieren, dass die komplexen 20% nicht mitgenommen werden → Cleanup-Chance

**Post-Migration:**
- Proton Pass-Abo kündigen (monatlich)
- Apple Passwords als Primary Manager
- Apple Notes für Legacy-Identities / Custom-Data verwenden (nicht encrypted, aber einfach auffindbar)

---

## Zeitbudget für Migration

| Schritt | Zeit |
|---|---|
| Audit (Custom Fields, Multi-URL, etc.) | 1–2 Stunden |
| CSV-Export aus Proton | 5 min |
| Find & Replace Fix in VS Code | 10–15 min |
| Quote-Wrapping (falls erforderlich) | 15–30 min |
| Import in Apple Passwords | 5 min |
| Validation (Spot-Check) | 15–30 min |
| **Gesamt** | **~2–4 Stunden** |

---

## Alternative: Hybrid-Ansatz

Falls das Audit **20–50% aktive Custom-Field-Nutzung** zeigt:

1. **Proton Pass** bleibt der Primary Manager für:
   - Konten mit Custom Fields (z.B. Bank-PINs, Admin-URLs)
   - Identity-Einträge
   - Secure Notes

2. **Apple Passwords** wird der Sekundär-Manager für:
   - 80% der "einfachen" Konten (Login + Passwort + TOTP)
   - Häufig genutzte Websites (Autofill-Vorteil)

3. **Konsequenz:** Zwei Password Manager, aber klare Aufteilung

---

## Nächste Schritte (Sofort)

- [ ] **Audit durchführen:** Custom Fields, Multi-URL, Identities, Secure Notes zählen
- [ ] **Entscheidung treffen:** Basierend auf Audit-Ergebnissen
- [ ] **Falls Wechsel:** CSV-Fix + Import durchführen
- [ ] **Falls Bleiben:** Keine Aktion erforderlich; Proton Pass bleibt Primary

---

## Verwandte Seiten

- **[[Proton Pass]]** — Entity-Seite (Features, Stärken)
- **[[Apple Passwords]]** — Entity-Seite (Features, Limitationen)
- **[[Tech Stack & Security Decisions]]** — Übergeordnetes Tech-Entscheidungsframework
- **[[MOC Tech & Setup]]** — Master-Index Tech & Konfiguration
