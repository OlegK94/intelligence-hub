TAGS: [raw, quellen, struktur, inbox, assets, dateiorganisation, immutable, workflow]
SOURCES: ["raw/raw/README.md"]
CREATED: 2026-06-17
UPDATED: 2026-06-17
SUMMARY: Verzeichnis-Struktur und Workflow für raw/ Quellenordner — Inbox für neue Notizen, Assets für Bilder/Anhänge, Data für CSV/Wearables, Privat/Business/Archiv-Kategorien; Workflow: Datei in Inbox → python3 tools/ingest.py → Wiki wächst in wiki/; Quellen bleiben immutable nach Ingest
---

# raw — Quellenverzeichnis

## Überblick

Die `raw/`-Ordnerstruktur organisiert alle immutable (unveränderbaren) Quelldateien für die Ingest-Pipeline. Nach dem Ingest werden Inhalte in die strukturierte [[Intelligence Hub Wiki]] integriert — die Quelldateien selbst ändern sich nicht mehr.

## Verzeichnis-Struktur

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

## Kategorie-Beschreibungen

| Ordner | Inhalt | Funktion |
|---|---|---|
| **inbox/** | Neue Notizen, Clips, Ad-hoc-Notizen | Staging-Bereich für den Ingest-Prozess |
| **assets/** | PNG, JPG, PDF, Videos | Bilddateien + Anhänge (von hier wird auf wiki/assets/ referenziert) |
| **data/** | CSV, JSON (Wearables, Scans, Metriken) | Strukturierte Datenexporte (z.B. Fitbit, Oura, Scaneca-Daten) |
| **MOC/** | Persönliche Vault-Homepage | Übergeordnete Index-/Navigations-Notiz |
| **Privat/** | Alles Persönliche | — |
| **Privat/Performance/** | Trainingspläne, Health-Protokolle, 3D-Scan-Rohdaten | Körperkomposition, Fitnessdaten, Scanning |
| **Privat/Tech/** | Technologie-Notizen, Sicherheit, Tools | IT-Setup, Passwortmanagement, Privacy |
| **Privat/Finanzen/** | Kontoauszüge, Steuern, Budgets | Finanzplanung, Privat-Banking |
| **Privat/Versicherungen/** | Versicherungs-Policen, -Korrespondenz | Versicherungs-Management |
| **Privat/Recherchen/** | Ad-hoc-Recherchen, nicht-Business | Persönliche Forschung |
| **Privat/Auswandern/** | Auswander-Planung (pausiert) | Langfristige Planung |
| **Business/** | Geschäfts-Quelldokumente | — |
| **Business/Wagglz/** | Wagglz GmbH Finanzen, BWA, Struktur | Unternehmens-Dokumentation |
| **Business/Cafe/** | Café Berlin Masterplan, Pitches | Archiviertes Gastronomie-Projekt |
| **Business/OK-Capital/** | OK Capital UG Finanzen | UG-Dokumentation |
| **_archiv/** | Historische Work-Themen, nicht aktiv | Doctolib, DoktorLib, inaktive Projekte |

## Workflow: Ingest-Pipeline

```
1. Neue Notiz erzeugen
   → 2. in raw/inbox/ ablegen
   → 3. python3 tools/ingest.py ausführen
   → 4. Tool parst Quelldatei
   → 5. Wiki-Seiten generieren/aktualisieren
   → 6. Wikilinks + Frontmatter hinzufügen
   → 7. Quelldateien bleiben unverändert (immutable)
   → 8. Wiki wächst organisch
```

**Eigenschaften:**
- **Quelldateien sind immutable:** Nach Ingest werden Sie nicht editiert
- **Wiki ist mutable:** Wird durch Ingest aktualisiert + manuelle Bearbeitung
- **1-zu-viele:** Eine Quelldatei kann in mehrere Wiki-Seiten ingestion werden
- **Kontext-bewusst:** Ingest-Tool erkennt Struktur und Relations

## Ingest-Befehle

```bash
# Alle neuen Dateien aus inbox/ ingestion
python3 tools/ingest.py

# Spezifische Quelldatei ingestion
python3 tools/ingest.py --file "raw/Privat/Performance/00_Performance-Übersicht.md"

# Claude Code Modul ausführen (für Placeholder-Quelldokumente)
python3 tools/ingest.py --claude-code 02_ingredienzen_db
```

## Quelldateien sind immutable

### Warum?

1. **Audit Trail:** Ursprüngliche Quelle bleibt dokumentiert
2. **Reproduzierbarkeit:** Ingest kann wiederholt werden (z.B. bei Tool-Updates)
3. **Separation of Concerns:** Rohdaten vs. verarbeitete Wiki-Seiten sind klar getrennt
4. **Version Control:** raw/ wird in Git nicht häufig geändert; wiki/ ist dynamisch

### Was ist erlaubt?

- ✅ **Neue Dateien hinzufügen** (inbox/ oder kategorisierte Ordner)
- ✅ **Quelldatei-Inhalt ergänzen** (neue Abschnitte, wenn nicht bereits ingested)
- ❌ **Quelldatei-Inhalt löschen** (würde historischen Kontext verlieren)
- ❌ **Bereits ingested Quelldateien editieren** (verursacht Widersprüche mit Wiki)

## Best Practices

1. **Inbox-Staging:** Neue, unsortierte Notizen gehen zuerst nach `inbox/`
2. **Kategorisierung:** Nach Sorting in `Privat/` oder `Business/` verschieben
3. **Dokumentation:** Jede Quelldatei mit YAML-Frontmatter + Kontext-Info
4. **Versionierung:** Git-Commits für raw/ sind selten; wiki/ ist dynamic
5. **Backup:** raw/ wird regelmäßig gesichert (immutable-as-archive)

## Verwandte Seiten

- [[Intelligence Hub Wiki]] — Zielstruktur nach Ingest
- [[00 Auftragsbrief Performance Coffee]] — Beispiel-Quelldokument (raw/Business/PerformanceCafe/recherche/00_Auftragsbrief.md)
- [[00 Finanz-Übersicht]] — Beispiel-Quelldokument (raw/Privat/Finanzen/00_MOC_Finanzen.md)
- [[00 Performance-Übersicht]] — Beispiel-Quelldokument (raw/Privat/Performance/_vault/00_Performance-Übersicht.md)
- [[Ingest Pipeline]] — Tool-Dokumentation

---

**Erstellt:** 2026-06-17  
**Status:** Aktive Dokumentation
