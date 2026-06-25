# Supabase ↔ GitHub Integration

> **Status:** Angelegt 2026-06-14 · Details vom User ergänzen

## Kontext

Supabase-Projekt mit GitHub verbunden — vermutlich für zukünftige [[Wufflz]]-App oder Wagglz-Stack (Backend, Auth, Edge Functions, DB-Migrationen).

## Platzhalter (ausfüllen)

| Feld | Wert |
|------|------|
| Supabase-Projekt-URL | `https://YOUR-PROJECT.supabase.co` |
| Supabase-Projekt-Ref | |
| GitHub-Repo | |
| Branch (Preview/Prod) | |
| Verknüpfte Umgebungen | staging / production |
| Zweck | z. B. Auth, Postgres, Storage, Edge Functions |

## Notizen

- Integration in Supabase Dashboard unter **Project Settings → Integrations → GitHub**
- Typische Nutzung: DB-Schema als Migrationen im Repo, CI für Supabase CLI, Branch-Previews
- **Keine Secrets in dieses Vault** — Service-Role-Keys nur in `.env` lokal, nie committen

## Offene Fragen

- [ ] Welches Repo ist verknüpft?
- [ ] Preview Branches aktiv?
- [ ] Migration-Workflow (lokal vs. GitHub Actions)?
