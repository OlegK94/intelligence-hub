---
tags: [tech, passwords, migration, entscheidung-offen]
status: Entscheidung ausstehend
created: 2026-06-09
---

# 🔑 Password Manager Migration — Proton Pass → Apple Passwords

## Status: Entscheidung ausstehend

## Versuchte Migration
1. CSV-Export aus Proton Pass
2. Import in Apple Passwords gescheitert
3. Problem: **Deutsches Locale** → CSV-Delimiter Semikolon statt Komma
4. Problem: **Feldinkompatibilität** → Apple Passwords kann mehrere Felder nicht abbilden

## Fehlende Felder (Proton Pass kann, Apple nicht)
| Feld | Proton Pass | Apple Passwords |
|---|---|---|
| Custom Fields | ✅ | ❌ |
| Mehrere URLs pro Eintrag | ✅ | ❌ |
| Kreditkarten | ✅ | ❌ (separat in Wallet) |
| Identity-Einträge | ✅ | ❌ |
| Secure Notes | ✅ | ❌ |
| Vault-Struktur | ✅ | ❌ |
| TOTP/OTPAuth | ✅ | ✅ (aber manuell re-enroll) |
| Passkeys | ✅ | ✅ (aber manuell re-enroll) |

## Entscheidungsrahmen
**Bleibt bei Proton Pass**, wenn:
- Custom Fields aktiv genutzt (z.B. Kontofeldnummern, Pins, etc.)
- Mehrere URLs pro Eintrag aktiv genutzt
- Kreditkarten, Identities, Secure Notes aktiv genutzt
- Vault-Struktur (Ordnung) aktiv genutzt

**Wechsel zu Apple Passwords sinnvoll**, wenn:
- Obige Felder größtenteils **legacy, ungenutzte** Daten sind
- Workflow fast ausschließlich Benutzername + Passwort + TOTP
- Volle Apple-Integration gewünscht (Autofill seamless)

## Noch zu klären
- [ ] Durchgehen: Wie viele Proton Pass Einträge nutzen tatsächlich Custom Fields / Multi-URL / Notes aktiv?
- [ ] Wenn <20%: Cleanup + Migration machbar
- [ ] Wenn >50%: Bei Proton Pass bleiben

## Technisches Fix (falls Migration fortgesetzt)
CSV-Delimiter-Problem lösen via VS Code:
1. CSV in VS Code öffnen
2. Semicolons durch Commas ersetzen (Find & Replace: `;` → `,`)
3. Achte auf Felder die selbst Kommas enthalten (mit Quotes wrappen)

---
*Verknüpft: [[Privacy & Tech Stack]] | [[MOC Tech & Setup]]*
