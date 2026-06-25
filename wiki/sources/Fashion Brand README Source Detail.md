---
title: Fashion Brand README Quelldokument-Detail
type: source
tags: [fashion-brand, lieferanten, blanks, textilproduktion, accessoires, business, readme, projektstruktur]
sources: ["raw/Business/Fashion-Brand/README.md"]
created: 2026-06-20
updated: 2026-06-20
summary: Quelldokument für das Fashion-Brand-Projekt — beschreibt die Verzeichnisstruktur, den Ingest-Workflow und verweist auf die kuratierte Lieferantenliste als primären Einstiegspunkt
---

# Fashion Brand README — Quelldokument-Detail

## Überblick

Dieses Quelldokument (`raw/Business/Fashion-Brand/README.md`) ist die Projektübersicht des Fashion-Brand-Projekts. Es beschreibt die Verzeichnisstruktur, den Ingest-Prozess und dient als Einstiegspunkt in die kuratierte Lieferantenliste.

> Für die Projektentität mit allen Lieferanten und Kategorien siehe [[Fashion Brand]].
> Für die kuratierte Lieferantenliste (primäres Arbeitsdokument) siehe [[Fashion Brand Lieferanten]] und [[Fashion Brand Suppliers Source Detail]].

## Projektstruktur (aus Quelle)

```
Fashion-Brand/
├── README.md                    ← Diese Datei
└── Fashion Brand Suppliers.md   ← Kuratierte Lieferantenliste (Start hier)
```

Das Quelldokument benennt `Fashion Brand Suppliers.md` explizit als **primären Einstiegspunkt** für das Projekt.

## Ingest-Workflow (aus Quelle)

Das README dokumentiert den empfohlenen Ingest-Befehl für neue Dateien:

```bash
python3 tools/ingest.py --file "raw/Business/Fashion-Brand/Fashion Brand Suppliers.md"
```

Neue Quellmaterialien sollen im Verzeichnis abgelegt und anschließend über diesen Befehl in den Ingest-Prozess gegeben werden.

## Wiki-Verlinkungen (aus Quelle)

Das README enthält explizite Wiki-Link-Empfehlungen nach erfolgtem Ingest:
- [[Fashion Brand]] — Projekt-Entitätsseite
- [[Fashion Brand Suppliers Source Detail]] — Detail-Quelldokument der Lieferantenliste

## Verhältnis zu bestehenden Wiki-Seiten

Dieses README ist ein **Metadokument** — es enthält selbst keine Lieferanten- oder Produktdaten, sondern beschreibt die Projektstruktur. Die inhaltlichen Daten befinden sich in `Fashion Brand Suppliers.md`, das bereits als [[Fashion Brand Suppliers Source Detail]] und [[Fashion Brand Lieferanten]] im Wiki vorhanden ist.

**Keine Widersprüche** mit bestehenden Wiki-Inhalten gefunden. Das README bestätigt die bereits bekannte Projektstruktur.

## Verwandte Seiten

- [[Fashion Brand]] — Projekt-Entitätsseite
- [[Fashion Brand Lieferanten]] — Entitätsseite der Lieferantenliste
- [[Fashion Brand Suppliers Source Detail]] — Detail-Quelldokument der Lieferantenliste
- [[AS Colour]] — Lieferant: Blanks/Jackets
- [[Stanley Stella]] — Lieferant: Nachhaltige Blanks
- [[Arsonists]] — Lieferant: Custom Textile Production
- [[Mr. Socks]] — Lieferant: Accessories
- [[Mended]] — Brand-Plattform im Projekt
- [[Oleg Personal Context]] — Projektverantwortlicher
