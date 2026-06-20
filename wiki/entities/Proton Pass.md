---
title: Proton Pass
type: entity
tags: [tool, password-manager, security, privacy, proton, tech-stack]
sources: ["raw/Privat/Tech/Password Manager Migration.md"]
created: 2026-06-09
updated: 2026-06-09
summary: Datenschutzorientierter Passwort-Manager von Proton AG — Teil der Proton-Suite; unterstützt benutzerdefinierte Felder, mehrere URLs, Vault-Struktur, Kreditkarten-, Identitäts-Einträge und sichere Notizen; wird derzeit von Oleg genutzt, steht aber unter Migrationsprüfung
---

# Proton Pass

## Überblick

**Proton Pass** ist ein Passwort-Manager, der von Proton AG (Schweiz) entwickelt wurde und Teil der umfassenderen Proton-Datenschutz-Suite ist (zusammen mit Proton Mail, Proton VPN, Proton Drive). Es ist [[Oleg Personal Context|Olegs]] **aktueller** Passwort-Manager (Stand Juni 2026), der derzeit auf eine mögliche Migration zu [[Apple Passwords]] hin geprüft wird.

## Funktionsumfang

| Funktion | Unterstützt |
|---|---|
| Benutzerdefinierte Felder | ✅ |
| Mehrere URLs pro Eintrag | ✅ |
| Kreditkarten-Einträge | ✅ |
| Identitäts-Einträge | ✅ |
| Sichere Notizen | ✅ |
| Vault-Struktur (Ordner) | ✅ |
| TOTP / OTPAuth | ✅ |
| Passkeys | ✅ |

## Datenexport

- **Format:** CSV
- **Bekanntes Problem:** Auf Systemen mit deutschem Gebietsschema ist das CSV-Trennzeichen ein **Semikolon** (`;`) statt dem Standard-Komma (`,`)
- Dies führte zum Importfehler in Apple Passwords — siehe [[Password Manager Migration Source Detail]] für den VS Code-Fix

## Datenschutzprofil

- **Rechtsraum:** Schweiz (starke Datenschutzgesetze)
- **Verschlüsselung:** Ende-zu-Ende-verschlüsselt
- **Open Source:** Auditiert
- **Plattformübergreifend:** iOS, macOS, Windows, Android, Browser-Erweiterungen

## Migrationsstatus

Derzeit wird eine Migration zu [[Apple Passwords]] geprüft. Die Entscheidung steht noch aus, bis überprüft wurde, wie viele Einträge die erweiterten Funktionen (benutzerdefinierte Felder, mehrere URLs, Vault-Struktur) aktiv nutzen. Siehe [[Password Manager Migration]] für den Entscheidungsrahmen.

## Verwandte Seiten

- [[Password Manager Migration]] — Migrationsprojekt
- [[Password Manager Migration Source Detail]] — technische Details
- [[Apple Passwords]] — potenzielles Migrationsziel
- [[Privacy and Tech Stack]] — übergeordneter Tech-Stack-Kontext
- [[MOC Tech und Setup]] — übergeordnete MOC
- [[Oleg Personal Context]] — aktueller Nutzer