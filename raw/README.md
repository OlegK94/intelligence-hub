# raw/ — Quellen (immutable nach Ingest)

```
raw/
├── inbox/              # Neue Notizen → hier ablegen, dann ingest
├── assets/             # Bilder & Anhänge
├── data/               # CSV/Exports (Wearables, etc.)
├── MOC/                # Vault-Home
│
├── Privat/             # Alles Persönliche
│   ├── MOC/
│   ├── Performance/    # Health, Hyrox, Supplements, Scans
│   ├── Tech/           # Tools, Privacy, Password Manager
│   ├── Finanzen/       # Privatkonten, Steuern, Fixkosten
│   ├── Versicherungen/
│   ├── Recherchen/
│   └── Auswandern/     # Someday (pausiert)
│
├── Business/
│   ├── MOC/
│   ├── Wagglz/         # GmbH, Finanzen, BWAs
│   ├── Cafe/           # Café Berlin, Masterplan, Decks
│   └── OK-Capital/     # UG, Finanzen
│
└── _archiv/            # Work-Themen, nicht aktiv ingesten
    └── Work/           # z.B. Doctolib/DoktorLib
```

**Workflow:** Datei in `inbox/` → `python3 tools/ingest.py` → Wiki wächst in `wiki/`.
