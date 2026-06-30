# raw/ — Quellen (immutable nach Ingest)

> Rohdaten — niemals bearbeiten. Claude liest hier, schreibt in `wiki/`.

---

## ⬇️ NEU ABLEGEN → `inbox/`

Alles was analysiert oder ins Wiki soll kommt in **`inbox/`** — Claude verteilt es automatisch.

---

## Vollständige Struktur

```
raw/
│
├── 📥 inbox/                  ← EINGANG — hier alles reinwerfen
│
├── Business/                  ← Alle Unternehmens- & Berufsinhalte
│   ├── Wagglz/                # Wagglz GmbH — Docs, Finanzen, Screenshots, Wireframes
│   ├── Doctolib/              # Doctolib Demo-Account — 47 App-Screenshots (JPG)
│   ├── PerformanceCafe/       # Performance Coffee Brand — vollständiges Projekt
│   ├── Cafe/                  # Café Berlin — Masterplan, Partnership Hai
│   ├── OK-Capital/            # OK Capital UG — Finanzen, Rangrücktritt
│   └── AppDev/                # App-Entwicklung — Referenz-Screenshots
│
├── Privat/                    ← Persönliche Inhalte
│   ├── Finanzen/              # Konten, Steuern, Fixkosten, Rehab-Plan
│   ├── Performance/           # Health, Hyrox, Supplements, Scans, LinkedIn
│   ├── Tech/                  # Tools, Privacy Stack, Password Manager
│   ├── Versicherungen/        # Allianz, Uelzener, ARAG
│   ├── Recherchen/            # Ad-hoc Recherchen (Matratze etc.)
│   ├── MOC/                   # Maps of Content — Übersichten
│   └── Auswandern/            # Someday/Maybe — Cyprus (pausiert)
│
├── Clippings/                 ← Web-Clips & Artikel (Safari, Obsidian Web Clipper)
├── Excalidraw/                ← Zeichnungen & Diagramme (nur Referenz)
├── assets/                    ← Bilder, Logos, Wireframes (wagglz-tier/)
├── articles/                  ← Archivierte Artikel
├── data/                      ← CSV-Exporte, Wearable-Daten
└── Claude Memory/             ← Claude Projektkontexte (gitignored, nur lokal)
```

---

## LLM Wiki Workflow

```
raw/inbox/     →   python3 tools/ingest.py          →   wiki/sources/
raw/Clippings/ →   python3 tools/ingest.py --scope clippings
raw/ (gesamt)  →   python3 tools/ingest.py --scope raw
```

Nach dem Ingest landet alles strukturiert in:
- `wiki/sources/` — eine Seite pro Quelldokument
- `wiki/entities/` — Personen, Firmen, Produkte
- `wiki/syntheses/` — übergreifende Analysen
