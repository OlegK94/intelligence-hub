---
tags: [supabase, wagglz, tierapp, tech, inbox]
created: 2026-06-14
status: draft
---

# Supabase — Wagglz Tierapp Konfiguration

> Ausfüllen → `python3 tools/ingest.py --file raw/inbox/Supabase Wagglz Tierapp Config.md`

## Supabase Projekt

- **Projekt-URL:** *(bitte eintragen — Dashboard → Settings → API → Project URL)*
- **Projekt-Ref:** *(bitte eintragen — Dashboard → Settings → General)*
- **Region:** *(bitte eintragen)*
- **Dashboard:** *(bitte eintragen)*

## GitHub

- **Repo:** https://github.com/OlegK94/Wagglz-App ✓ (private)
- **Owner:** OlegK94
- **Name:** Wagglz-App
- **Branch production:** main ✓ (2026-06-14 gepusht — `supabase/config.toml`, `supabase/migrations/`)
- **Branch preview:** *(offen)*
- **Supabase-GitHub-Integration:** verbunden (pending main branch fix → **main branch jetzt vorhanden**; Dashboard ggf. neu synchronisieren)

## Frontend (noch offen)

- [ ] Next.js
- [ ] React SPA
- [ ] Anderes: 

## Lokale Entwicklung

```bash
# Projektverzeichnis (nicht Intelligence Hub)
cd ~/Developer/Wagglz-App

# .env.local (gitignored)
SUPABASE_URL=
SUPABASE_ANON_KEY=
```

## Notizen

- GitHub-Repo erstellt 2026-06-14 (private)
- **2026-06-14:** Initial scaffold gepusht auf `main` — README, `.gitignore`, `package.json`, `supabase/config.toml`, `supabase/migrations/.gitkeep`
- Lokales Projekt: `~/Developer/Wagglz-App`
- App-Code gehört **nicht** in Intelligence Hub — separates Projektverzeichnis
- Supabase Dashboard → Integrations → Wagglz-App: nach `main`-Push erneut prüfen / Sync auslösen
- **Offen:** Supabase Projekt-URL, Ref und Region vom User eintragen lassen
