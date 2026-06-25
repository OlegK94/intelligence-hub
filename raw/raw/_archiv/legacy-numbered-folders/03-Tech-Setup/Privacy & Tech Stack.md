---
tags: [tech, privacy, infrastruktur]
status: Aktiv
created: 2026-05-10
---

# 🔒 Privacy & Tech Stack

## Geräte
- iPhone (primär)
- iPad Air 2025
- Mac

## Browser
| Gerät | Browser | Begründung |
|---|---|---|
| Mac | Brave | Chromium-Basis, native Ad-Block, Privacy |
| iPhone | Safari | Apple WebKit-Restriktion macht Brave auf iOS marginal besser als Chrome; Safari bleibt vorteilhafter für Apple-Integration |
| iPad | Safari | Gleiche Logik |

## Proton Ecosystem
| Produkt | Status | Bewertung |
|---|---|---|
| Proton Mail | ✅ Aktiv | Vollwertig, Zero-Knowledge, empfohlen |
| Proton Calendar | ✅ Aktiv | Vollwertig |
| Proton VPN | ✅ Aktiv | Kill Switch aktiviert auf allen Geräten |
| Proton Pass | ✅ Aktiv | Migration zu Apple Passwords offen → [[Password Manager Migration]] |
| Proton Drive | ✅ Aktiv | Für sensible Dokumente |
| Proton Docs/Sheets | ⚠️ Aktiv | 2–3 Jahre hinter Google; nur für privacy-sensitive Inhalte |

## Domain & DNS
- Domain: `ok-holding.com`
- DNS-Provider: GoDaddy
- Konfiguration: MX, SPF, DKIM, DMARC für Proton Mail ✅

## Sicherheit
- 2FA: Aktiviert (Proton + wichtige Accounts)
- Proton Sentinel: Aktiviert
- VPN Kill Switch: Aktiviert auf allen Geräten
- Hide-my-email Aliases: Genutzt für Registrierungen

## Prinzip
Proton für alles Datenschutzkritische. Google Workspace nur wo externe Kollaboration es erfordert (Docs-Kompatibilität). Kein Google-Ökosystem für private Daten.

---
*Verknüpft: [[Password Manager Migration]] | [[MOC Tech & Setup]]*
