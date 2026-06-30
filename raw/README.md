# raw/ — Quellen (immutable nach Ingest)

## ⬇️ NEU ABLEGEN → `inbox/`

Alles was du analysieren oder ins Wiki aufnehmen willst kommt in **`inbox/`**.
Claude verteilt es dann automatisch in die richtige Unterstruktur.

---

## Struktur nach dem Ingest

```
raw/
├── 📥 inbox/           ← EINGANG — hier alles reinwerfen
│
├── Business/
│   ├── Wagglz/         # GmbH, Finanzen, Screenshots, Wireframes
│   ├── Cafe/           # Café Berlin, Masterplan
│   ├── PerformanceCafe/ # Performance Coffee Brand (vollständig)
│   └── OK-Capital/     # UG, Finanzen, Rangrücktritt
│
├── Privat/
│   ├── Finanzen/       # Konten, Steuern, Fixkosten, Archiv
│   ├── Performance/    # Health, Hyrox, Supplements, Scans, LinkedIn
│   ├── Tech/           # Tools, Privacy, Password Manager
│   ├── Versicherungen/
│   ├── Recherchen/
│   └── Auswandern/     # Someday (pausiert)
│
├── Business/
│   ├── Doctolib/       # 47 Demo-Account Screenshots (JPG)
├── assets/             # Wagglz Wireframes, Bilder, Logos
├── articles/           # Archivierte Web-Artikel
├── data/               # CSV/Exports (Wearables, etc.)
└── _archiv/            # Inaktive Themen
```

## Workflow

```bash
# Eingang verarbeiten
python3 tools/ingest.py                    # alles in inbox/
python3 tools/ingest.py --scope clippings  # Clippings/ Ordner
python3 tools/ingest.py --scope raw        # alle nicht-ingestierten Dateien
```
