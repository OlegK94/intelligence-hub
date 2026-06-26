---
title: "Wagglz UI-Kits README"
type: source
tags: [wagglz, wufflz, figma, design, ui-kit, drittanbieter, reference, kits, ant-design, nucleus-plus, theprojekts, manifest]
sources: ["raw/Business/Wagglz/Design/kits/README.md"]
created: 2026-06-17
updated: 2026-06-17
summary: README für den kits/-Ordner im Wagglz/Wufflz-Design-Bereich — listet 3 Drittanbieter-UI-Kits (Ant Design System Preview, Nucleus Plus, theProjekts Design System V2) mit ihren Figma-File-Keys; niedrige Migrationspriorität; optionaler Export via --include-kits Flag
---

# Wagglz UI-Kits README

## Überblick

Dieses Quelldokument (`raw/Business/Wagglz/Design/kits/README.md`) ist das übergeordnete README für den `kits/`-Unterordner im Wagglz/Wufflz-Design-Bereich. Es listet **drei Drittanbieter-UI-Kits** als externe Referenzen auf und legt explizit fest, dass diese **niedrige Migrationspriorität** haben.

> Für das übergeordnete Design-README siehe [[Wagglz Wufflz Design README]].
> Für canonical Produktdesigns (wufflz/-Ordner) siehe [[25 Wufflz Wireframes Figma Manifest]] und [[25 B2B Software Figma Manifest]].

---

## Registrierte UI-Kits

| Kit | Figma File Key |
|---|---|
| **Ant Design System (Preview)** | `faSohMPNaRaWIimPAQAlCA` |
| **Nucleus Plus** | `wzKhS5oRrI1FgK3cIRfCiP` |
| **theProjekts Design System V2** | `YCUvHIoaxSoQSPveySgTLP` |

### Einzelseiten der Kits

- [[Ant Design System for Figma Preview]] — bereits vollständig dokumentiert (File Key `faSohMPNaRaWIimPAQAlCA`)
- [[Nucleus Plus Figma Kit]] — noch nicht dokumentiert (File Key `wzKhS5oRrI1FgK3cIRfCiP`)
- [[theProjekts Design System V2]] — noch nicht dokumentiert (File Key `YCUvHIoaxSoQSPveySgTLP`)

---

## Export-Strategie

Laut README werden diese Dateien vom **Standard-Export übersprungen**:

```bash
# Standard-Export (kits/ wird ausgelassen):
python3 tools/figma_export.py

# Optionaler Export aller Dateien inkl. Kits:
python3 tools/figma_export.py --all --include-kits
```

**Begründung:** Für Obsidian-Zwecke genügen URL und Manifest-Metadaten. Ein vollständiger PNG-Export ist für reine Referenz-Kits nicht erforderlich.

**Kein Figma-Abonnement erforderlich**, solange die Kits nur als externe Referenz archiviert werden.

---

## Einordnung: kits/ vs. wufflz/

| Aspekt | `wufflz/`-Dateien | `kits/`-Dateien |
|---|---|---|
| **Art** | Eigene Produktdesigns | Drittanbieter-UI-Kits |
| **Canonical** | ✅ Ja | ❌ Nein |
| **Export-Priorität** | Hoch | 🔽 Niedrig |
| **Standard-Export** | ✅ Enthalten | ❌ Übersprungen |
| **Für Obsidian** | Vollständige Dokumentation | URL + Metadaten ausreichend |

---

## Verwandte Seiten

- [[Ant Design System for Figma Preview]] — vollständig dokumentiertes Kit
- [[Nucleus Plus Figma Kit]] — ausstehende Dokumentation
- [[theProjekts Design System V2]] — ausstehende Dokumentation
- [[Wagglz Wufflz Design README]] — übergeordnetes Design-README
- [[Figma Index Wagglz]] — Master-Index aller Figma-Dateien
- [[25 Wufflz Wireframes Figma Manifest]] — canonical Produktdesign
- [[25 B2B Software Figma Manifest]] — canonical Produktdesign
- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — Subprojekt / Produktlinie
- [[Oleg Personal Context]] — Projektverantwortlicher
