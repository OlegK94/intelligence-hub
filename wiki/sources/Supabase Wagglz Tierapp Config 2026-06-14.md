---
title: "Supabase Wagglz Tierapp Config 2026-06-14"
type: source
tags: [supabase, wagglz-tierapp, tech, backend, config, github, nextjs, local-dev, api-keys, environment]
sources: ["raw/raw/inbox/Supabase Wagglz Tierapp Config 2026-06-14.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Current Supabase + GitHub configuration for Wagglz Tierapp (Next.js/React SPA); Org dashboard URL with ID bomdwqpapksffwjvawal; Project dashboard with Ref oohxauyuukkjjzrmmnax, API https://oohxauyuukkjjzrmmnax.supabase.co; GitHub integration active (OlegK94/Wagglz-App private, main branch production); local .env.local setup documented; Region TBD; API keys stored locally only (never in git/vault).
---

# Supabase Wagglz Tierapp — Konfiguration 2026-06-14

## Überblick

Aktualisierte Supabase- und GitHub-Konfiguration für das [[Wagglz Tierapp]]-Projekt (technische Backend-Integration). Das Dokument erfasst die Live-Verbindung zwischen Supabase Backend-as-a-Service und dem GitHub-Repository (`OlegK94/Wagglz-App`, privat), sowie die lokale Entwicklungsumgebung (.env.local Setup).

> **Wichtig:** API-Keys werden **nie** in Git oder Vault gespeichert — nur in `~/.Developer/Wagglz-App/.env.local` (gitignored).

---

## Supabase Organisationen

### Org Dashboard

- **URL:** https://supabase.com/dashboard/org/bomdwqpapksffwjvawal
- **Org-ID:** `bomdwqpapksffwjvawal`
- **Status:** Active; Supabase-GitHub-Integration konfiguriert

---

## Supabase Projekt

| Feld | Wert |
|---|---|
| **Projekt-Dashboard** | https://supabase.com/dashboard/project/oohxauyuukkjjzrmmnax |
| **Projekt-Ref** | `oohxauyuukkjjzrmmnax` |
| **Projekt-URL (API)** | https://oohxauyuukkjjzrmmnax.supabase.co |
| **Region** | *(in Settings → General eintragen — ausstehend)* |
| **Auth Method** | OAuth + API Keys (anon + service_role) |

---

## GitHub-Integration

| Feld | Wert |
|---|---|
| **Repository** | https://github.com/OlegK94/Wagglz-App ✅ (private) |
| **Owner** | OlegK94 |
| **Repository Name** | Wagglz-App |
| **Branch Production** | `main` (gepusht 2026-06-14; `supabase/config.toml`, `supabase/migrations/` enthalten) |
| **Branch Preview** | *(offen — noch nicht konfiguriert)* |
| **Supabase-GitHub-Integration** | ✅ Verbunden; Dashboard ggf. neu synchronisieren nach main-Push |

---

## Frontend Stack (entscheidungsoffen)

- [ ] **Next.js** — Server-Side Rendering + Static Generation (empfohlen für DTC Performance Coffee later)
- [ ] **React SPA** — Client-Side Only
- [ ] **Anderes** — (bitte spezifizieren)

**Status:** Decision pending; .env.local setup dokumentiert für alle Optionen.

---

## Lokale Entwicklung

### Projektverzeichnis

```bash
cd ~/Developer/Wagglz-App
```

**Hinweis:** Dieses Verzeichnis ist **nicht** im Intelligence Hub — separate lokale Workspace.

### .env.local (gitignored)

Erstelle die Datei `~/.Developer/Wagglz-App/.env.local` mit folgenden Variablen:

```bash
# Supabase Public API Configuration
NEXT_PUBLIC_SUPABASE_URL=https://oohxauyuukkjjzrmmnax.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=<ANON_KEY_HERE>

# Optional: Service Role Key (Backend nur, NIEMALS PUBLIC)
# SUPABASE_SERVICE_ROLE_KEY=<SERVICE_ROLE_KEY_HERE>
```

**API-Keys beziehen:**
- Settings → API → kopiere:
  - **anon/publishable key** → `NEXT_PUBLIC_SUPABASE_ANON_KEY`
  - **service_role key** → Nur lokal; Backend-Operationen (Node.js/CLI)

**⚠️ Sicherheit:**
- `.env.local` muss in `.gitignore` sein (default für Next.js)
- Niemals API-Keys in Code committen
- Service Role Key bleibt lokal oder in Deploy-Secrets (verwaltet von Hosting-Platform)

---

## Supabase Migrations & Config

| Datei | Ort | Status |
|---|---|---|
| `supabase/config.toml` | Repo root | ✅ 2026-06-14 gepusht |
| `supabase/migrations/` | Repo root | ✅ 2026-06-14 gepusht |

**Synchronisierung:** Nach Push zu main sollte Supabase-Dashboard automatisch oder manuell (Settings → Linked Projects) refreshen, um neue Migrationen zu erfassen.

---

## Offene Konfigurationen

| Item | Status | Aktion |
|---|---|---|
| **Region** | *(in Settings → General ausstehend)* | Wählen: EU (Frankfurt), EU (Dublin), USA (us-east-1), APAC etc. |
| **Preview Branch** | *(nicht konfiguriert)* | Optional: Separate preview DB für development |
| **Domain Alias** | *(nicht konfiguriert)* | Optional: Custom domain statt supabase.co subdomain |
| **Backup Schedule** | *(Default)* | Check Supabase dashboard für Retention Policy |
| **Real-time Subscriptions** | *(TBD)* | Aktivieren falls Frontend subscriptions benötigt |

---

## Deployment-Vorbereitung

Vor Production-Deployment zu prüfen:
- [ ] Region finalisiert (latency, compliance)
- [ ] Environment Variables in Hosting-Platform (Vercel, Netlify, etc.) gespeichert
- [ ] Service Role Key sicher verwaltet (nur Backend-Umgebung)
- [ ] Supabase Backup Policy dokumentiert
- [ ] CORS & Row Level Security (RLS) konfiguriert für anon-Key

---

## Verwandte Seiten

- [[Wagglz Tierapp]] — Projekt-Entität (technische Übersicht)
- [[Oleg Personal Context]] — Projektverantwortlicher
- [[Wagglz GmbH]] — Organisation (gehört zu)

---

*Quelldokument aktualisiert: 2026-06-14*
*Letzte Synchronisierung GitHub → Supabase: 2026-06-14 (main branch)*
