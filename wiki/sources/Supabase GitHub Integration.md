---
title: "Supabase GitHub Integration"
type: source
tags: [supabase, github, backend, integration, infrastructure, wufflz, wagglz, edge-functions, database-migration, deployment, status]
sources: ["raw/raw/Privat/Tech/Supabase GitHub Integration.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Supabase-Backend mit GitHub verknüpft — vermutlich für Wufflz-App oder Wagglz-Stack (Postgres, Edge Functions, DB-Migrationen); Projekt-URL, -Ref, GitHub-Repo noch zu dokumentieren; typische Nutzung Branch-Previews, CI via Supabase CLI; Secrets Management best practice (keine Keys in Vault)
---

# Supabase ↔ GitHub Integration

## Überblick

Ein Supabase-Projekt ist mit GitHub verknüpft — vermutlich zur Unterstützung der **[[Wufflz]]-App** oder des [[Wagglz]]-Tech-Stacks. Diese Seite dokumentiert die Integration, Anforderungen und Best Practices.

> **Status:** Angelegt 2026-06-14 · Details vom User erforderlich
> Siehe [[Wagglz GmbH]] für Kontext und [[Health Protocol Master]] falls Performance Coffee-Backend-Integration geplant ist.

---

## Integrations-Übersicht

### Zweck

Die Supabase-GitHub-Verknüpfung ermöglicht:

1. **Database-Migrations-Versionskontrolle** — Schema-Änderungen im Git-Repo
2. **CI/CD-Pipelines** — Automatische Tests und Deployments via GitHub Actions + Supabase CLI
3. **Preview Branches** — Ephemere Umgebungen für Feature-Testing (Pull-Requests)
4. **Edge Functions Deployment** — Automatisches Deploy von TypeScript/JavaScript Serverless Functions
5. **Secrets Management** — Environment Variables via GitHub Secrets (nicht im Repo committen)

---

## Konfiguration (Platzhalter)

| Feld | Wert | Status |
|---|---|---|
| **Supabase-Projekt-URL** | `https://YOUR-PROJECT.supabase.co` | ⏳ zu dokumentieren |
| **Supabase-Projekt-Ref** | — | ⏳ zu dokumentieren |
| **GitHub-Organization** | — | ⏳ zu dokumentieren |
| **GitHub-Repo-Name** | — | ⏳ zu dokumentieren |
| **Repo-Typ** | Monorepo (Wufflz) / Separate Repo | ⏳ zu klären |
| **Branch für Production** | `main` / `production` | ⏳ zu festlegen |
| **Branch für Staging** | `develop` / `staging` | ⏳ zu festlegen |
| **Preview Branches aktiv** | ja / nein | ⏳ zu klären |

---

## Setup-Schritte (Allgemein)

### 1. Supabase Dashboard

```
Project Settings → Integrations → GitHub
```

Autorisiere die Supabase-App für deinen GitHub-Account/Organization:
- Supabase bittet um Zugriff auf Repositories (Read/Write)
- Genehmige für das spezifische Repo (z.B. `wagglz/wufflz` oder `oleg-kober/performance-coffee`)

### 2. GitHub Actions + Supabase CLI

Erstelle `.github/workflows/deploy.yml` (Beispiel):

```yaml
name: Deploy to Supabase

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [develop]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Supabase migrations
        run: |
          npx supabase@latest migration list --linked
          npx supabase@latest db push
      
      - name: Deploy Edge Functions
        run: |
          npx supabase@latest functions deploy
```

**Secrets erforderlich:**
- `SUPABASE_ACCESS_TOKEN` — via GitHub Secrets (nicht committen!)
- `SUPABASE_PROJECT_ID` — Projekt-Ref aus Dashboard

### 3. Database Migrations

Struktur im Repo:

```
supabase/
├── migrations/
│   ├── 20260614_create_tables.sql
│   ├── 20260615_add_auth_schema.sql
│   └── ...
├── functions/
│   ├── hello-world/
│   │   └── index.ts
│   └── ...
└── config.toml
```

**Best Practice:** Jede Migration ist eine separate `.sql`-Datei mit Timestamp; `supabase db push` deployed automatisch.

### 4. Edge Functions

TypeScript/JavaScript Functions deploybar via Git Push:

```
supabase/functions/send-email/
├── index.ts
├── deno.json
└── ...
```

Push nach `main` → GitHub Actions → Supabase CLI deployt automatisch.

---

## Offene Fragen (Wufflz / Performance Coffee Kontext)

- [ ] **Ist die Integration bereits aktiv?** (GitHub-Repo auflisten, Commits prüfen)
- [ ] **Welches Repo ist verknüpft?** (Monorepo wagglz/wufflz oder separates Repo?)
- [ ] **Sind Preview Branches konfiguriert?** (Test-Umgebungen pro PR)
- [ ] **Migration-Workflow?** (lokal `supabase db push` vs. GitHub Actions)
- [ ] **Edge Functions deployed?** (z.B. Email-Versand, Payment-Webhooks?)
- [ ] **Secrets sicher verwahrt?** (Access Tokens nur in GitHub Secrets, nicht im Code)

---

## Best Practices

### Secrets Management ⚠️

**❌ NICHT TUN:**
```javascript
// FALSCH — Keys im Code/Repo
const supabaseKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...";
```

**✅ TUN:**
```bash
# 1. In GitHub Secrets speichern (Organization/Repo Settings)
# SUPABASE_ACCESS_TOKEN = "..."
# SUPABASE_PROJECT_ID = "..."

# 2. In Workflow abrufen
env:
  SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
  SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}
```

### Branch-Strategie

| Branch | Umgebung | Policy |
|---|---|---|
| `main` | **Production** | Protected; PR-Review required; Auto-Deploy nach Merge |
| `develop` | **Staging** | Entwicklungs-Integration; Auto-Deploy |
| `feature/*` | **Preview** | Ephemere Umgebung pro PR (optional) |

### Database Migrations

```bash
# Lokal: neue Migration erstellen
supabase migration new create_users_table

# Bearbeite supabase/migrations/[timestamp]_create_users_table.sql

# Local Testing
supabase db push

# Git Push → GitHub Actions → Auto-Deploy Production
```

---

## Performance Coffee Backend-Integration (Falls geplant)

Falls [[Performance Coffee Brand]] ein Backend benötigt (DTC Shopify + ggf. eigene Kundenverwaltung):

### Mögliche Supabase-Nutzung:
1. **Benutzer-Authentifizierung** (Shopify OAuth oder native Auth)
2. **Kundendaten** (Adresse, Vorlieben, Subscription-Status)
3. **Analytics/Events** (Page Views, Add-to-Cart, Checkout-Funnel)
4. **Edge Functions für Webhooks** (Shopify-Events, Payment-Processing)

### Integration Roadmap:
- **Phase 1:** Shopify-native auth/daten (keine Supabase erforderlich)
- **Phase 2:** Kundenverwaltung in Supabase + Edge Functions für Automation
- **Phase 3+:** Advanced (Longevity-Tracking, Customer Health-Data Integration)

---

## Verknüpfungen

- [[Wagglz GmbH]] — zugehöriges Unternehmen / Backend-Betreiber
- [[Wufflz]] — B2B SaaS, wahrscheinliche Supabase-Nutznießer
- [[Performance Coffee Brand]] — mögliche künftige Nutznießer (falls Backend-Integration geplant)
- [[GitHub]] — Versionskontroll-Partner
- [[Supabase]] — Backend-as-a-Service-Provider
- [[Oleg Personal Context]] — Projektverantwortlicher

---

## Nächste Schritte

1. **Dokumentation ausfüllen:**
   - [ ] Supabase-Projekt-URL und -Ref
   - [ ] GitHub-Repo-Name und -Struktur
   - [ ] Aktive Branches und Umgebungen

2. **Setup-Audit:**
   - [ ] Integration aktiv? (Dashboard prüfen)
   - [ ] Secrets sicher? (GitHub Secrets vs. Code-Commits)
   - [ ] CI/CD-Workflow existiert? (GitHub Actions prüfen)

3. **Roadmap klären:**
   - [ ] Performance Coffee Backend-Integration erforderlich?
   - [ ] Weitere Wufflz-Features geplant? (z.B. Mobile App, Real-time Sync)
   - [ ] Skalierungsanforderungen (Datenbank-Größe, Funktions-Latenz)?
