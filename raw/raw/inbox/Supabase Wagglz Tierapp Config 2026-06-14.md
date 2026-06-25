---
tags: [supabase, wagglz, tierapp, tech, inbox]
created: 2026-06-14
updated: 2026-06-14
status: draft
supersedes: raw/inbox/Supabase Wagglz Tierapp Config.md
---

# Supabase — Wagglz Tierapp Konfiguration (Update 2026-06-14)

> Ergänzung zur ingested Quelle [[Supabase Wagglz Tierapp Config]] — Org-URL und **Projekt-Ref/URLs** bekannt.
> **API-Keys:** nur in `~/Developer/Wagglz-App/.env.local` (gitignored) — **nie** in Vault/Git.
> Ingest: `python3 tools/ingest.py --file "raw/inbox/Supabase Wagglz Tierapp Config 2026-06-14.md"`

## Supabase Organisation

- **Org-Dashboard:** https://supabase.com/dashboard/org/bomdwqpapksffwjvawal
- **Org-ID:** `bomdwqpapksffwjvawal`

## Supabase Projekt

- **Projekt-Dashboard:** https://supabase.com/dashboard/project/oohxauyuukkjjzrmmnax
- **Projekt-Ref:** `oohxauyuukkjjzrmmnax`
- **Projekt-URL (API):** https://oohxauyuukkjjzrmmnax.supabase.co
- **Region:** *(bitte eintragen — Settings → General)*

## GitHub

- **Repo:** https://github.com/OlegK94/Wagglz-App ✓ (private)
- **Owner:** OlegK94
- **Name:** Wagglz-App
- **Branch production:** main ✓ (2026-06-14 gepusht — `supabase/config.toml`, `supabase/migrations/`)
- **Branch preview:** *(offen)*
- **Supabase-GitHub-Integration:** verbunden (Dashboard ggf. neu synchronisieren nach main-Push)

## Frontend (noch offen)

- [ ] Next.js
- [ ] React SPA
- [ ] Anderes:

## Lokale Entwicklung

```bash
# Projektverzeichnis (nicht Intelligence Hub)
cd ~/Developer/Wagglz-App

# .env.local (gitignored — nie committen)
NEXT_PUBLIC_SUPABASE_URL=https://oohxauyuukkjjzrmmnax.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=   # Settings → API → anon/publishable key — nur lokal
```

## Notizen

- **2026-06-14:** Supabase Org-URL dokumentiert (`bomdwqpapksffwjvawal`)
- **2026-06-14:** Projekt-Ref `oohxauyuukkjjzrmmnax`, Dashboard- und API-URL eingetragen
- **Offen:** Region, Preview-Branch-Strategie, Frontend-Stack
- Lokales Projekt: `~/Developer/Wagglz-App`
- App-Code gehört **nicht** in Intelligence Hub
