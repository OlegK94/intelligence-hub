---
title: Passwort-Manager-Migration Quelldokument Detail
type: source
tags: [tech, passwords, migration, proton-pass, apple-passwords, csv, locale, entscheidung-offen]
sources: ["raw/Privat/Tech/Password Manager Migration.md"]
created: 2026-06-09
updated: 2026-06-09
summary: Quelldokument für den versuchten Proton Pass → Apple Passwords Umzug — CSV-Trennzeichen-Problem (deutsches Locale), Feldinkompatibilitätsanalyse, Entscheidungsrahmen und CSV-Fix via VS Code
---

# Passwort-Manager-Migration — Quelldokument Detail

## Übersicht

Dieses Quelldokument (Status: Entscheidung ausstehend, erstellt 2026-06-09) dokumentiert den versuchten Wechsel von [[Proton Pass]] zu [[Apple Passwords]], die dabei aufgetretenen technischen Hindernisse, einen strukturierten Entscheidungsrahmen sowie einen technischen Workaround für das CSV-Trennzeichen-Problem.

> Für die Entitätszusammenfassung und den Entscheidungsstatus siehe [[Password Manager Migration]].

## Versuchte Migrationsschritte

1. CSV-Export aus [[Proton Pass]]
2. Import in [[Apple Passwords]] gescheitert
3. Problem 1: **Deutsches Locale** → CSV-Trennzeichen ist Semikolon (`;`) statt Komma (`,`)
4. Problem 2: **Feldinkompatibilität** → Apple Passwords kann mehrere Felder nicht abbilden

## Fehlende Felder (Feldinkompatibilität)

| Feld | Proton Pass | Apple Passwords |
|---|---|---|
| Benutzerdefinierte Felder | ✅ | ❌ |
| Mehrere URLs pro Eintrag | ✅ | ❌ |
| Kreditkarten | ✅ | ❌ (separat in Wallet) |
| Identity-Einträge | ✅ | ❌ |
| Secure Notes | ✅ | ❌ |
| Vault-Struktur | ✅ | ❌ |
| TOTP/OTPAuth | ✅ | ✅ (aber manuell re-enroll erforderlich) |
| Passkeys | ✅ | ✅ (aber manuell re-enroll erforderlich) |

**Wichtigste Erkenntnis:** Apple Passwords ist im Wesentlichen nur ein Benutzername + Passwort + TOTP Manager. Proton Pass unterstützt ein deutlich umfangreicheres Datenmodell.

## Entscheidungsrahmen (Decision Framework)

### Bei Proton Pass bleiben, wenn:
- Benutzerdefinierte Felder aktiv genutzt werden (z.B. Kontonummern, PINs usw.)
- Mehrere URLs pro Eintrag aktiv genutzt werden
- Kreditkarten, Identities, Secure Notes aktiv genutzt werden
- Vault-Struktur (Ordnung) aktiv genutzt wird

### Wechsel zu Apple Passwords sinnvoll, wenn:
- Obige Felder größtenteils **veraltete / ungenutzte** Daten sind
- Arbeitsablauf fast ausschließlich Benutzername + Passwort + TOTP umfasst
- Volle **Apple-Integration** gewünscht wird (Autofill nahtlos, keine Extra-App)

## Noch zu klären (Offene Aufgaben)

- [ ] Durchgehen: Wie viele Proton Pass Einträge nutzen tatsächlich benutzerdefinierte Felder / Multi-URL / Notizen aktiv?
- [ ] Wenn <20% aktive Nutzung: Bereinigung + Migration machbar
- [ ] Wenn >50% aktive Nutzung: Bei Proton Pass bleiben

## Technischer Fix (falls Migration fortgesetzt wird)

**Problem:** Das deutsche Locale exportiert CSV mit Semikolon als Trennzeichen — Apple Passwords erwartet jedoch Komma als Trennzeichen.

**Lösung via VS Code:**
1. CSV in VS Code öffnen
2. Suchen & Ersetzen: `;` → `,`
3. ⚠️ Achte auf Felder, die selbst Kommas enthalten → diese müssen mit Anführungszeichen (Quotes) gewrappt sein

> **Hinweis:** Ein einfaches Suchen-und-Ersetzen kann Felder beschädigen, die selbst Semikolons oder Kommas als Inhalt enthalten. Ein robusterer Ansatz wäre ein CSV-fähiges Werkzeug oder ein Python-Skript, um das Trennzeichen korrekt zu ersetzen.

## Verwandte Seiten

- [[Password Manager Migration]] — Entitätsseite und Entscheidungsstatus
- [[Proton Pass]] — Quell-Passwort-Manager
- [[Apple Passwords]] — Ziel-Passwort-Manager
- [[Privacy and Tech Stack]] — weiterer Tech-Kontext (im Quelldokument verlinkt)
- [[MOC Tech und Setup]] — übergeordnete MOC
- [[Oleg Personal Context]] — Entscheidungsträger