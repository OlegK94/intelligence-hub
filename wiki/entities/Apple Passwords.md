---
title: Apple Passwords
type: entity
tags: [tool, password-manager, apple, ios, macos, tech-stack, autofill]
sources: ["raw/Privat/Tech/Password Manager Migration.md"]
created: 2026-06-09
updated: 2026-06-09
summary: Apples nativer Passwortmanager (iOS 18+ / macOS 15+ als eigenständige App) — unterstützt Benutzername/Passwort/TOTP/Passkeys, verfügt aber nicht über benutzerdefinierte Felder, mehrere URLs, Tresorstruktur, Kreditkarten- und Identitätseinträge; Ziel von Olegs Migrationsauswertung von Proton Pass
---

# Apple Passwords

## Überblick

**Apple Passwords** ist Apples native Passwortverwaltungsanwendung, die als eigenständige App in iOS 18 und macOS 15 (Sequoia) eingeführt wurde. Sie ist das **Ziel** einer möglichen Migration von [[Oleg Personal Context|Oleg]] von [[Proton Pass]], im Rahmen der Vereinfachung des Tech-Stacks und der Integration in das Apple-Ökosystem.

## Funktionsumfang

| Funktion | Unterstützt |
|---|---|
| Benutzername + Passwort | ✅ |
| Einzelne URL pro Eintrag | ✅ |
| TOTP / OTPAuth | ✅ (manuelles Re-Enrollment beim Import erforderlich) |
| Passkeys | ✅ (manuelles Re-Enrollment beim Import erforderlich) |
| Benutzerdefinierte Felder | ❌ |
| Mehrere URLs pro Eintrag | ❌ |
| Kreditkarteneinträge | ❌ (werden separat über Apple Wallet verwaltet) |
| Identitätseinträge | ❌ |
| Sichere Notizen | ❌ |
| Tresor-/Ordnerstruktur | ❌ |

## Import-Einschränkungen

- **CSV-Import:** Unterstützt, erfordert jedoch kommagetrennte CSV-Dateien
- **Problem mit deutschem Gebietsschema:** Proton Pass exportiert auf deutschen Systemen semikolongetrennte CSV-Dateien → Import schlägt fehl
- **Datenverlust:** Alle Proton-Pass-Daten in nicht unterstützten Feldern werden beim Import **still verworfen**
- **TOTP-Re-Enrollment:** TOTP-Secrets werden nicht per CSV übertragen — müssen manuell neu eingescannt/eingetragen werden

## Vorteile

- **Keine zusätzlichen Kosten** — im Apple-Ökosystem enthalten
- **Nahtloses Autofill** — native Integration mit Safari, iOS, macOS
- **iCloud-Synchronisation** — automatisch auf allen Apple-Geräten
- **Passkey-Unterstützung** — integriert und eng verzahnt
- **Einfachheit** — reduzierte Komplexität für Benutzername+Passwort+TOTP-Workflows

## Einschränkungen gegenüber Proton Pass

- Keine benutzerdefinierten Felder (PIN-Codes, Kontonummern usw.)
- Keine mehreren URLs pro Eintrag
- Keine sicheren Notizen
- Keine Tresor-/Ordnerorganisation
- Kein nativer plattformübergreifender Support (Android, Windows)
- Keine datenschutzorientierte Architektur (iCloud-Synchronisation, Abhängigkeit vom Apple-Ökosystem)

## Migrationsstatus

Die Migration ist **ausstehend** — blockiert durch die Bewertung der Feldinkompatibilität. Siehe [[Password Manager Migration]] für den Entscheidungsrahmen und die erforderliche Prüfung.

## Verwandte Seiten

- [[Password Manager Migration]] — Migrations-Entität
- [[Password Manager Migration Source Detail]] — technische Details
- [[Proton Pass]] — aktueller Passwortmanager
- [[Privacy and Tech Stack]] — übergeordneter Tech-Stack-Kontext
- [[MOC Tech und Setup]] — übergeordnete MOC
- [[Oleg Personal Context]] — Bewerter