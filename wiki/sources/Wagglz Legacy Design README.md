---
title: "Wagglz Legacy Design README"
type: source
tags: [wagglz, figma, design, dogwalking, legacy, readme, manifest]
sources: ["raw/Business/Wagglz/Design/legacy-wagglz/README.md"]
created: 2026-06-18
updated: 2026-06-18
summary: README-Dokument für den legacy-wagglz-Ordner — listet 4 Figma-Dateien (Wagglz Dogwalking, Wagglz App Dogwalking, Wagglz Research, My Rex Copy) mit File Keys und Export-Befehl; verweist auf Master-Index figma-index
---

# Wagglz Legacy Design README

## Überblick

Dieses Quelldokument (`raw/Business/Wagglz/Design/legacy-wagglz/README.md`) ist das übergeordnete README für den **legacy-wagglz**-Designordner von [[Wagglz GmbH]]. Es listet vier Figma-Dateien auf, die historische Produkt- und Research-Designs für das Dogwalking-Geschäft enthalten.

Der Ordner unterscheidet sich von den aktiven Wufflz-Design-Dateien (z. B. [[25 Wufflz Wireframes Figma Manifest]], [[25 B2B Software Figma Manifest]]) durch sein **Legacy-Präfix** — diese Dateien repräsentieren vermutlich einen früheren Entwicklungsstand vor der Wufflz-Produktlinie.

---

## Dateiübersicht

| Datei | File Key | Wiki-Seite |
|---|---|---|
| **Wagglz Dogwalking** | `JjJ4CgJCqURgjohhbvcOrZ` | [[Figma Manifest Wagglz Dogwalking]] |
| **Wagglz App Dogwalking** | `MUvsIoZBIT0kOdIQjdn0s9` | [[Figma Manifest Wagglz App Dogwalking]] |
| **Wagglz Research** | `23wUJ3p6E7Y6Om6qo5GF5w` | [[Figma Manifest Wagglz Research Dogwalking]] |
| **My Rex (Copy)** | `7yBGOpEg0ETNXR3cQ4bOl4` | [[Figma Manifest My Rex Copy]] |

---

## Export-Befehl

```bash
python3 tools/figma_export.py --all --folder wagglz
```

Der `--folder wagglz`-Parameter exportiert alle Dateien im `wagglz`-Ordner. Zu beachten: Dies exportiert möglicherweise auch Nicht-Legacy-Dateien; der genaue Scope hängt von der Ordnerstruktur des Export-Tools ab.

---

## Einordnung im Wagglz-Design-System

Diese Legacy-Dateien bilden die **frühere Dogwalking-Iteration** von Wagglz ab, bevor das B2B-Wufflz-Produkt entwickelt wurde. Die Namenskonventionen deuten auf folgende Entwicklungshistorie hin:

| Phase | Dateien | Produkt |
|---|---|---|
| **Legacy (Consumer)** | Wagglz Dogwalking, Wagglz App Dogwalking, Wagglz Research | Ursprüngliche Dogwalking-Consumer-App |
| **Legacy (Referenz)** | My Rex (Copy) | Wettbewerber-Referenz oder inspirierendes Produkt |
| **Aktiv (B2B)** | [[25 Wufflz Wireframes Figma Manifest]], [[25 B2B Software Figma Manifest]] | Wufflz B2B-Plattform |

> **Hypothese [A]:** „My Rex" deutet auf eine Referenz an die App „Rex" (oder ähnliche Dogwalking/Pet-Management-Apps) hin — möglicherweise ein Wettbewerbsanalyse-Copy oder ein Design-Benchmark. Der Zusatz „(Copy)" bestätigt, dass es sich um eine Kopie einer externen Datei handelt, nicht um ein Original.

---

## Verhältnis zum Master-Index

Das README verweist auf `[[../figma-index]]` als Master-Index. Im Wiki entspricht dies [[Figma Index Wagglz]].

---

## Offene Fragen

> ⚠️ **Offene Fragen:**
> - Wurden die vier Legacy-Dateien bereits exportiert oder stehen sie noch aus?
> - Was ist „My Rex" — ein Wettbewerber, eine Partnerschaft oder ein internes Testprojekt?
> - Welche Screens/Flows enthält die ursprüngliche Wagglz Dogwalking Consumer-App?
> - Wie unterscheidet sich die Research-Datei von der App-Datei inhaltlich?

---

## Verwandte Seiten

- [[Figma Manifest Wagglz Dogwalking]] — Entität für File Key `JjJ4CgJCqURgjohhbvcOrZ`
- [[Figma Manifest Wagglz App Dogwalking]] — Entität für File Key `MUvsIoZBIT0kOdIQjdn0s9`
- [[Figma Manifest Wagglz Research Dogwalking]] — Entität für File Key `23wUJ3p6E7Y6Om6qo5GF5w`
- [[Figma Manifest My Rex Copy]] — Entität für File Key `7yBGOpEg0ETNXR3cQ4bOl4`
- [[Figma Index Wagglz]] — Master-Index aller Figma-Dateien
- [[Wagglz GmbH]] — zugehöriges Unternehmen
- [[Wufflz]] — aktive B2B-Produktlinie (Nachfolger der Legacy-App)
- [[25 Wufflz Wireframes Figma Manifest]] — aktive B2B-Designdatei
- [[25 B2B Software Figma Manifest]] — aktive B2B-Designdatei
- [[Wagglz Wufflz Design README]] — übergeordnetes README (aktiver Ordner)
- [[Oleg Personal Context]] — Projektverantwortlicher
