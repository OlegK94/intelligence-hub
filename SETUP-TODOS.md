# Intelligence Hub — Alle TODOs

> Stand: 2026-06-13 · Scope: **privat**

---

## ✅ Erledigt

- [x] Marp, Periodic Notes, Obsidian Git
- [x] `.env` + API-Key (funktioniert)
- [x] `raw/` strukturiert: **Privat/** + **Business/** (Wagglz, Cafe, OK-Capital)
- [x] Clippings an Vault-Root, Obsidian-Config (Attachments, Hotkeys, Graph)
- [x] Master Context + Finanz-Monatsübersicht Juni
- [x] QMD-Scripts + `tools/search.py`
- [x] GitHub: Commit lokal (Push siehe unten)

## 🔴 Noch offen — du (~10 Min)

- [ ] **Git-Email setzen:** `git config user.email "deine@email.com"`
- [ ] **Web Clipper** testen → Ziel: `Clippings/` oder `raw/inbox/`
- [ ] **`Cmd+Shift+D`** testen (Bilder → `raw/assets/`)
- [ ] **Alte API-Keys** in [Anthropic Console](https://console.anthropic.com/settings/keys) löschen
- [ ] **Hyrox-Wettkampfdatum** nach Anmeldung eintragen
- [ ] **Kontoauszug Juni** → `raw/inbox/2026-06 Finance Monthly.md` verfeinern

## 🟡 QMD — braucht Homebrew

```bash
# Einmalig installieren: https://brew.sh
brew install node sqlite
bash scripts/qmd-setup.sh
```

## 🟡 Läuft / nach Batch

- [ ] Batch-Ingest (~32 Dateien pending) — `outputs/notes/batch-ingest-log.md`
- [ ] `python3 tools/lint.py`
- [ ] Graph View in Obsidian prüfen

## 🟡 Aktive Tasks

- [ ] **Café Planning Session** 📅 2026-06-14 ⏫
- [ ] Password Manager Entscheidung 🔼
- [ ] Allianz 3 Angebote 🔼
- [ ] Hyrox anmelden 🔼

## Ordnerstruktur

```
raw/Privat/     Performance, Tech, Finanzen, Versicherungen
raw/Business/   Wagglz/, Cafe/, OK-Capital/
raw/inbox/      neue Quellen
Clippings/      Web Clipper
```

→ `raw/README.md`
