---
title: "Wagglz Tierapp"
type: entity
tags: [wagglz, tierapp, tech, backend, supabase, nextjs, github, project]
sources: ["raw/raw/inbox/Supabase Wagglz Tierapp Config 2026-06-14.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Technical project — Wagglz Tierapp (animal management SaaS backend); Supabase PostgreSQL + Auth, GitHub OlegK94/Wagglz-App (private), Next.js or React SPA frontend decision pending; Org bomdwqpapksffwjvawal, Project Ref oohxauyuukkjjzrmmnax; local dev in ~/Developer/Wagglz-App; belongs to Wagglz GmbH organizational structure.
---

# Wagglz Tierapp — Technisches Projekt

## Überblick

**Wagglz Tierapp** ist ein technisches Backend-Projekt innerhalb von [[Wagglz GmbH]] — eine Tierverwaltungs- / Tiergesundheits-Anwendung mit [[Supabase]] als Backend-Plattform.

Das Projekt wird parallel zu [[Wufflz]] (B2B SaaS für Tierpflegebetriebe) entwickelt und teilt möglicherweise Infrastruktur oder ist eine Schwesterlösung mit unterschiedlichem Fokus (Consumer vs. B2B).

---

## Infrastruktur

### Backend

| Component | Konfiguration |
|---|---|
| **Plattform** | [[Supabase]] (PostgreSQL + Auth + Realtime) |
| **Org-Dashboard** | https://supabase.com/dashboard/org/bomdwqpapksffwjvawal |
| **Projekt-Ref** | `oohxauyuukkjjzrmmnax` |
| **API-URL** | https://oohxauyuukkjjzrmmnax.supabase.co |
| **Region** | *(ausstehend)* |

### Version Control

| Field | Value |
|---|---|
| **Repository** | https://github.com/OlegK94/Wagglz-App (private) |
| **Owner** | OlegK94 |
| **Main Branch** | production |
| **Last Push** | 2026-06-14 (`supabase/config.toml`, `supabase/migrations/`) |
| **GitHub-Supabase Integration** | ✅ Connected |

### Frontend (Decision Pending)

- [ ] **Next.js** — recommended for performance & SSR
- [ ] **React SPA** — client-only alternative
- [ ] **Other** — TBD

---

## Local Development

**Workspace:** `~/Developer/Wagglz-App` (separate from Intelligence Hub)

**Environment File:** `.env.local` (gitignored, never commit)
```bash
NEXT_PUBLIC_SUPABASE_URL=https://oohxauyuukkjjzrmmnax.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=<ANON_KEY>
```

---

## Status & Dependencies

| Item | Status | Notes |
|---|---|---|
| Supabase Org | ✅ Active | Linked to GitHub |
| Project Setup | ✅ Complete | migrations/ pushed |
| Frontend Stack | ⏳ Pending | Next.js vs. React SPA |
| Region Config | ⏳ Pending | EU/US selection |
| Production Ready | ❌ No | API keys, Region, deployment pipeline TBD |

---

## Ownership & Stakeholders

| Role | Person |
|---|---|
| **Lead Developer** | [[Oleg Kober]] |
| **Organization** | [[Wagglz GmbH]] |

---

## Verwandte Seiten

- [[Supabase Wagglz Tierapp Config 2026-06-14]] — Current technical configuration
- [[Wufflz]] — Sibling B2B SaaS project (animal care management)
- [[Wagglz GmbH]] — Parent organization
- [[Oleg Personal Context]] — Project lead
