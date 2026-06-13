# Intelligence Hub — Alle TODOs

> Stand: 2026-06-13 · Scope: **privat** (kein Doctolib, kein Relocation aktiv)

---

## 🔴 Einmalig — Obsidian & Browser (~15 Min)

- [x] **Marp** — BRAT → `JichouP/obsidian-marp-plugin` → aktivieren
- [x] **Periodic Notes** — Weekly Template: `templates/Weekly Review.md`
- [x] **Obsidian Git** — installiert, Auto-Backup konfiguriert
- [ ] **GitHub Remote verbinden** — siehe unten ⬇️
- [ ] **Web Clipper** Zielordner prüfen: `Clippings/` oder `raw/inbox/`
- [ ] **`Cmd+Shift+D`** testen: Clipping öffnen → Bilder nach `raw/assets/`

### GitHub verbinden (noch offen — kein Remote gesetzt)

**Status:** Lokaler Commit ✅ · GitHub Remote ❌

1. https://github.com/new → **Private** Repo: `intelligence-hub`
2. Kein README/gitignore hinzufügen
3. Im Terminal:

```bash
cd "/Users/oleg.k/Library/Mobile Documents/com~apple~CloudDocs/Intelligence Hub"
git remote add origin git@github.com:DEIN-USERNAME/intelligence-hub.git
git push -u origin main
```

4. Obsidian Git → Auto commit-and-sync interval: **60** Min ✅ (bereits gesetzt)

**Git-Identity setzen** (für saubere Commits in Obsidian):
```bash
git config user.name "Oleg Kober"
git config user.email "deine@email.com"
```

## 🔴 Einmalig — Inhalt ausfüllen (~25 Min)

- [ ] **`raw/inbox/00-Master-Context.md`** — TODO-Abschnitte ergänzen (Einkommen, Wearables, …)
- [ ] **Finanz-Monatsübersicht Juni 2026** aus `templates/Finance Monthly Summary.md` erstellen
- [ ] **Hyrox-Wettkampfdatum** recherchieren und eintragen

## 🔴 Einmalig — Sicherheit

- [ ] Alte API-Keys in [Anthropic Console](https://console.anthropic.com/settings/keys) **löschen**
- [ ] API-Key nur in `.env`, nie in Chat/Git

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

## 🔮 Später (wenn Wiki >80 Artikel)

- [ ] [qmd](https://github.com/tobi/qmd) für bessere Suche
- [ ] Make/n8n: Web-Clip → Auto-Ingest
- [ ] Wearable-Exporte nach `raw/data/`
