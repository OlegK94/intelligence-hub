# Intelligence Hub — Alle TODOs

> Stand: 2026-06-13 · Scope: **privat** (kein Doctolib, kein Relocation aktiv)

---

## 🔴 Einmalig — Obsidian & Browser (~15 Min)

- [x] **Marp** — BRAT → `JichouP/obsidian-marp-plugin` → aktivieren
- [x] **Periodic Notes** — Weekly Template: `templates/Weekly Review.md`
- [x] **Obsidian Git** — installiert, Auto-Backup konfiguriert
- [x] **GitHub Remote** — `OlegK94/intelligence-hub` (`.git` neu initialisiert, Push ausstehend)
- [ ] **`.env` anlegen** — `cp .env.example .env` + API-Key eintragen (für Ingest/Lint)
- [ ] **Web Clipper** Zielordner prüfen: `Clippings/` oder `raw/inbox/`
- [ ] **`Cmd+Shift+D`** testen: Clipping öffnen → Bilder nach `raw/assets/`

### GitHub — Push nach lokalem Commit

```bash
cd "/Users/oleg.k/Library/Mobile Documents/com~apple~CloudDocs/Intelligence Hub"
git add -A && git commit -m "vault: QMD search, master context, obsidian root fix"
git pull origin main --allow-unrelated-histories --no-edit
git push -u origin main
```

**Git-Identity setzen** (für saubere Commits in Obsidian):
```bash
git config user.name "Oleg Kober"
git config user.email "deine@email.com"
```

## 🔴 Einmalig — Inhalt ausfüllen (~25 Min)

- [x] **`raw/inbox/00-Master-Context.md`** — aus Vault-Daten ergänzt (Einkommen, Deadlines)
- [x] **Finanz-Monatsübersicht Juni 2026** → `raw/inbox/2026-06 Finance Monthly.md`
- [ ] **Hyrox-Wettkampfdatum** — nach Anmeldung eintragen
- [ ] **Kontoauszug Juni** — Monatsübersicht verfeinern

## 🔴 Einmalig — Sicherheit

- [ ] Alte API-Keys in [Anthropic Console](https://console.anthropic.com/settings/keys) **löschen**
- [ ] API-Key nur in `.env`, nie in Chat/Git

## 🟡 QMD — Lokale Suche (~15 Min)

- [ ] **Node 22+** installieren: `brew install node sqlite`
- [ ] **QMD einrichten:** `bash scripts/qmd-setup.sh`
- [ ] **Embeddings** (optional, ~2GB Download): `bash scripts/qmd-setup.sh --embed`
- [ ] Test: `python3 tools/search.py "Hyrox training"`

Nach jedem Ingest: `bash scripts/qmd-sync.sh` (läuft auch automatisch nach `batch_ingest.py`)

## 🟡 Nach Batch-Ende (~10 Min)

- [ ] Obsidian: `wiki/Dashboard.md` + Graph View prüfen
- [ ] `python3 tools/lint.py` ausführen
- [ ] Optional: `python3 tools/query.py "Was sind meine Top-3 privaten Prioritäten?"`

## 🟡 Aktive private Tasks (aus Inbox)

- [ ] **Café Planning Session** vorbereiten 📅 2026-06-14 ⏫
- [ ] **Password Manager** Entscheidung 🔼
- [ ] **Allianz** 3 Angebote anfordern 🔼
- [ ] **Hyrox** anmelden 🔼
- [ ] **Scaneca 3D-Scan** planen 📅 2026-09-01 🔽

## 🟢 Wöchentliche Routine (~10 Min)

1. [ ] `templates/Weekly Review.md` ausfüllen → `raw/inbox/`
2. [ ] `./scripts/ingest-inbox.sh` oder `python3 tools/ingest.py`
3. [ ] Offene Fragen an Claudian/Cursor stellen

## ⚪ Someday / Maybe

- [ ] Auswandern / Cyprus (in paar Jahren)
- [ ] Proton Drive Backup-Struktur
- [ ] iPad Air: Tastatur + Case
- [ ] GmbH Buchhaltung + Jahresabschluss 2025 prüfen

## ❌ Bewusst NICHT in diesem Vault

- DoktorLib / Doctolib Automations → **Arbeits-Workspace**
- Cyprus Relocation aktiv tracken → **pausiert**
- 775 Finanz-PDFs bulk-ingesten → nur **Monatsübersichten**

## 🔮 Später

- [ ] Make/n8n: Web-Clip → Auto-Ingest
- [ ] Wearable-Exporte nach `raw/data/`
