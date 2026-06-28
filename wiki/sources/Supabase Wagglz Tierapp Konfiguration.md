---
title: "Supabase Wagglz Tierapp — Konfiguration & Projekt-Setup"
type: source
tags: [supabase, wagglz, tierapp, backend, database, github-integration, auth, api, configuration, technical-setup, infrastructure]
sources: ["raw/inbox/Supabase Wagglz Tierapp Config.md"]
created: 2026-06-14
updated: 2026-06-14
summary: Supabase-Backend-Konfiguration für Wagglz Tierapp; Projekt-URL/Ref/Region ausstehend; GitHub-Integration (OlegK94/Wagglz-App private Repo, main branch), Migrations + config.toml gepusht; Frontend TBD (Next.js/React SPA); lokale Entwicklung (.env.local mit SUPABASE_URL + ANON_KEY); Jahresabschluss-Rückstand &amp; Lizenzberater-Kontakt ausstehend
---

# Supabase Wagglz Tierapp — Konfiguration & Projekt-Setup

## Überblick

Dieses Quelldokument erfasst die **technische Konfiguration des Supabase-Projekts** für die [[Wagglz GmbH]] Tierapp (Wufflz). Die Konfiguration umfasst Backend-Setup, GitHub-Integration, Datenbankmigrationen und lokale Entwicklungsumgebung.

**Status:** Scaffolding-Phase; Projekt-Metadaten (URL, Ref, Region) ausstehend; GitHub-Integration aktiv; Frontend-Entscheidung offen (Next.js vs. React SPA).

---

## Supabase Projekt-Metadaten

| Parameter | Wert | Status |
|---|---|---|
| **Projekt-URL** | — | ⏳ Ausstehend (bitte eintragen — Dashboard → Settings → API → Project URL) |
| **Projekt-Ref** | — | ⏳ Ausstehend (bitte eintragen — Dashboard → Settings → General) |
| **Region** | — | ⏳ Ausstehend (bitte eintragen) |
| **Dashboard** | — | ⏳ Ausstehend (bitte eintragen) |

> **Hinweis:** Diese Felder können direkt im Supabase-Dashboard unter *Settings → API* und *Settings → General* abgerufen werden.

---

## GitHub-Integration

### Repository-Details

| Feld | Wert | Status |
|---|---|---|
| **Repository-URL** | https://github.com/OlegK94/Wagglz-App | ✅ Aktiv (private) |
| **Owner** | OlegK94 | ✅ Bestätigt |
| **Repository-Name** | Wagglz-App | ✅ Bestätigt |
| **Primary Branch** | main | ✅ Vorhanden (2026-06-14 gepusht) |
| **Preview Branch** | — | ⏳ Offen |

### Gepushte Inhalte (2026-06-14)

- ✅ `supabase/config.toml` — Supabase-Konfigurationsdatei
- ✅ `supabase/migrations/` — Datenbankmigrationen (`.gitkeep`)
- ✅ `README.md` — Projektbeschreibung
- ✅ `.gitignore` — Git-Ignore-Regeln
- ✅ `package.json` — Node.js-Abhängigkeiten

### GitHub ↔ Supabase Integration

| Aspekt | Status | Anmerkung |
|---|---|---|
| **Supabase-GitHub-App verbunden** | ✅ Ja | Dashboard → Integrations → Wagglz-App |
| **Main Branch Integration Status** | ✅ Aktiv | Früher pending (fehlendes main branch); jetzt Sync verfügbar |
| **Dashboard Synchronisierung** | ⏳ Empfohlen | Nach main-Push Supabase Dashboard neu synchronisieren / manuellen Sync auslösen |
| **Preview Deployments** | ⏳ Offen | Preview-Branch noch nicht konfiguriert |

---

## Frontend-Entscheidung

| Option | Status | Notiz |
|---|---|---|
| **Next.js** | ⏳ Evaluierung | Empfohlen für Supabase-Integration; Full-Stack-Capabilities |
| **React SPA** | ⏳ Evaluierung | Leichtgewichtig; separate Backend-Architektur erforderlich |
| **Anderes** | ⏳ Offen | — |

**Empfehlung:** Next.js bietet beste Integration mit Supabase (Auth, RLS-Policies, Real-Time-Subscriptions).

---

## Lokale Entwicklung

### Projektverzeichnis

```bash
# Nicht im Intelligence Hub Repo — separates Projektverzeichnis
cd ~/Developer/Wagglz-App
```

> ⚠️ **Wichtig:** Der Wagglz-App-Code gehört **nicht** in das Intelligence Hub Git-Repository. Separates Projektverzeichnis verwenden.

### Umgebungskonfiguration (`.env.local`)

```bash
# .env.local (gitignored; NOT checked in)
SUPABASE_URL=<PLACEHOLDER>
SUPABASE_ANON_KEY=<PLACEHOLDER>
```

**Beschaffung:**
1. Supabase Dashboard öffnen → Projekt → Settings → API
2. `Project URL` kopieren → `SUPABASE_URL`
3. `anon` public API Key kopieren → `SUPABASE_ANON_KEY`
4. In `.env.local` eintragen (von Hand oder via Supabase CLI)

### CLI-Setup (optional)

```bash
# Supabase CLI installieren
npm install -g supabase

# Login zur Wagglz-App
supabase login

# Link lokales Projekt zu Supabase
cd ~/Developer/Wagglz-App
supabase link --project-ref <PROJECT_REF>

# Migrationen ausführen
supabase migration up
```

---

## Datenbankmigrationen

**Ort:** `supabase/migrations/`

**Status:** `.gitkeep` nur; keine Migrationen gespeichert. Schema-Definitionen müssen noch erstellt werden.

**Workflow:**
1. Schema lokal in Supabase Studio designen (GUI)
2. Migration via `supabase migration create <name>` generieren
3. `.sql`-Datei in `supabase/migrations/` speichern
4. In GitHub pushen
5. Supabase Dashboard neu synchronisieren für Deployment auf Live-Projekt

---

## Technische Spezifikationen

### Authentifizierung (Auth)
- **Standard:** Supabase Auth (Postgres-basiert)
- **Social Sign-In:** optional (Google, GitHub, etc.)
- **Session Management:** JWT-Token

### Datenbank (PostgreSQL)
- **Host:** Supabase-verwaltete PostgreSQL
- **Access Control:** Row-Level Security (RLS) Policies
- **Real-Time:** Optional (Supabase Real-Time-Subscriptions)

### Storage (Dateiablage)
- **S3-ähnlich:** Supabase Storage Buckets
- **Use Case:** Animal/Facility Fotos, Dokumente

### API
- **RESTful:** Automatisch generiert von Supabase
- **GraphQL:** Optional aktivierbar
- **Webhooks:** Real-Time-Events zu externen Systemen

---

## Abhängigkeiten & Blockers

| Abhängigkeit | Status | Auswirkung |
|---|---|---|
| **Supabase Projekt-URL/Ref/Region** | ⏳ Ausstehend | Blockiert: `.env.local` Ausfüllung, lokale Entwicklung |
| **Frontend-Framework-Entscheidung** | ⏳ Offen | Blockiert: Frontend-Repo Setup, `pages/` oder `app/` Struktur |
| **GitHub-Integrations-Sync** | ✅ Aktiv | Deployment-Automation bei Push auf main |
| **Jahresabschluss Wagglz GmbH** | ⏳ Ausstehend | Nicht direkt blockierend, aber finanzielle Grundlage unklar |

---

## Nächste Schritte

1. **Sofort:**
   - [ ] Supabase Projekt-URL/Ref/Region ausfüllen (Dashboard → Settings)
   - [ ] `.env.local` mit korrekten Werten in `~/Developer/Wagglz-App/` erstellen
   - [ ] Frontend-Entscheidung treffen (Next.js vs. React SPA)

2. **Diese Woche:**
   - [ ] Lokale Entwicklungsumgebung testen (`npm install`, `npm run dev`)
   - [ ] Supabase CLI Anmeldung + Projekt-Link durchführen
   - [ ] Initiale DB-Schema in Supabase Studio planen

3. **Vor MVP-Launch:**
   - [ ] RLS-Policies für Multi-Tenant-Isolation schreiben (Facility-basierte Zugriffskontrolle)
   - [ ] Storage-Buckets konfigurieren (Fotos, Dokumente)
   - [ ] GitHub Actions für automatische Migrationen prüfen

---

## Verknüpfungen

- [[Wagglz GmbH]] — Mutter-Unternehmen; Backend-Infrastruktur, finanzielle Unterstützung
- [[Wufflz]] — B2B Tierverwaltungs-Plattform (Produktname)
- [[Oleg Kober]] — Projektverantwortlicher, GitHub-Owner
- [[Supabase]] — Backend-as-a-Service (BaaS) Plattform
- [[GitHub]] — Git-Repository + Integrations-Hosting
- [[OlegK94/Wagglz-App]] — Private GitHub-Repository
- [[Next.js]], [[React]] — Frontend-Framework-Kandidaten
- [[00 Finanz-Übersicht]] — finanzielle Situation Wagglz GmbH (relevant für Supabase-Hosting-Kosten)

---

*Quelldokument erstellt: 2026-06-14*
*Status: Scaffolding-Phase; Projekt-Konfiguration ausstehend*
