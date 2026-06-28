---
title: "Tech Stack (DoktorLib / No-Code)"
type: concept
tags: [tech, no-code, automation, workflow, make, tally, notion, salesforce, dust, integration, stack, claude-projects]
sources: ["raw/raw/Privat/Tech/Claude Projects Setup.md"]
created: 2026-06-07
updated: 2026-06-17
summary: No-Code tech stack for client projects; Make (workflow automation), Tally (forms), Notion (knowledge base), Salesforce (CRM), Dust (LLM integration); constraint: no custom code, no server provisioning; Master-of-Change in [[MOC Tech & Setup]]
---

# Tech Stack (DoktorLib / No-Code)

## Überblick

Das **DoktorLib Tech Stack** ist ein reines **No-Code-Setup** zur Automation, Datenmanagement und LLM-Integration über 5 zentrale Tools. Die Philosophie: Maximale Funktionalität ohne Custom-Code, Server-Management oder DevOps-Overhead.

---

## Core Tools

### 1. Make (Workflow Automation)

**Funktion:** Zentrale Automation Hub für API-Integrationen und Datenflüsse.

**Anwendungen:**
- Shopify → Notion: neue Orders in Kundendatenbank eintragen
- Emaileingang → Task-Parsing: Kundenfeedback aus E-Mails automatisch in Trello
- Formularen (Tally) → CRM (Salesforce): Lead-Capture automatisiert
- Webhooks für Performance Coffee DTC (Shopify-Abo-Events)

**Constraints:**
- Rate-limiting auf höheren Workflows
- Komplexe Logik wird schnell unübersichtlich
- **Fallback:** Dust für komplexere Datenverarbeitung

### 2. Tally (Form & Data Capture)

**Funktion:** Einfacher, schöner Form-Builder ohne Code.

**Anwendungen:**
- Performance Coffee Waitlist (Email-Capture, Preferenzen)
- Café Feedback-Formulare
- B2B-Onboarding-Forms (Wufflz alternative zu Typeform)
- Customer Survey-Einbindung

**Vorteile:**
- Eingebettet auf Website möglich
- Conditional Logic für branching forms
- Direkte Integrationen mit Make, Webhooks

### 3. Notion (Knowledge Base + Database)

**Funktion:** Flexible Datenbank und Content-Management (Alternative zu separaten Wiki, falls Obsidian ausfällt).

**Anwendungen:**
- Kunde-Portalzugang (Dokumentation, FAQs, Onboarding)
- Projektplanungsdatenbank (Tasks, Timelines, Dependencies)
- Investoren-Info-Hub (für Café / Performance Coffee Funding-Runden)
- Employee-Wiki (falls Team wächst)

**Integration mit Make:** Notion-Seiten automatisch aus Datenquellen generieren.

### 4. Salesforce (CRM)

**Funktion:** Enterprise-CRM für B2B-Kundenmanagement und Vertriebspipeline.

**Anwendungen:**
- Café B2B-Lieferanten-Management (Rohkaffee-Supplier, Bestände)
- Performance Coffee Phase 2 Gym-Partner-Netzwerk (Wholesale-Kundenmanagement)
- Wufflz B2B-Kundenverwaltung (Tierarztpraxen, Tierpfleger-Studios)
- Investor-Tracking (Fundraising CRM)

**Warum Salesforce?** Skalierbarkeit, erprobte Customization, Investor-Appeal (wenn Richtung Fundraising).

### 5. Dust (LLM Integration)

**Funktion:** Agentic Workflows für LLM-basierte Datenverarbeitung und Report-Generierung.

**Anwendungen:**
- Recherche-Automation (Claude Code für Performance Coffee Modul 01–08)
- Automatische Report-Erstellung aus Rohdaten (COGS-Kalkulationen, Marktanalyse-Zusammenfassungen)
- Document-Parsing (Lieferanten-Quotes → strukturierte Datenbank)
- Workflow-Triggering basierend auf natürlichem Text-Input

**Integration:** Dust-Workflows können Make-Webhooks triggern und Ergebnisse in Notion/Salesforce speichern.

---

## Integrationsfluss (Example: Performance Coffee DTC)

```
Shopify Store
    ↓ (Make webhook)
Customer Order Event
    ↓ (Extract + Transform in Make)
Notion Database (Orders)
    ↓ (Tally Feedback Form embedded on Thank You)
Customer Feedback
    ↓ (Dust NLP for sentiment)
Salesforce Opportunity (repeat purchase tracking)
    ↓ (Make scheduled task)
Email Campaign Trigger (Reorder incentive)
```

---

## Constraints & Fallbacks

| Limit | Constraint | Fallback |
|---|---|---|
| **Complex Conditionals** | Make workflows werden unlesbar ab 20+ steps | Dust für Logic-Heavy Workflows |
| **Rate Limiting** | Make hat Execution Caps auf Free/Pro | Zapier (ähnlich, teilweise bessere Limits) |
| **Custom Calculation** | Notion Formulas reichen nicht für komplexe Math | Python Script (aber breaks No-Code promise) |
| **Large File Processing** | Notion + Make begrenzt auf <100 MB | Selbstgehostete S3-Alternative (AWS, aber paid) |
| **Real-time Sync** | Alle Tools haben Verzögerungen (1–5 min) | Hardcoded API-Integrationen (breaks No-Code) |

**Philosophie:** Wenn No-Code nicht reicht, eher **Dust LLM-Workflow** nutzen statt Custom-Code.

---

## Master-of-Change

Siehe **[[MOC Tech & Setup]]** für detaillierte Roadmap zur erweiterten Tech-Stack-Integration (z.B. selbstgehostete Datenbanken, Microservices, wenn skaliert).

---

## Verwandte Seiten

- [[Claude Projects Setup]] — übergeordnete Projekt-Struktur
- [[MOC Tech & Setup]] — Master-of-Change für Tech-Infrastruktur
- [[Make]] — Automation Hub (Detailseite)
- [[Tally]] — Forms & Data Capture (Detailseite)
- [[Notion]] — Knowledge Base (Detailseite)
- [[Salesforce]] — CRM (Detailseite)
- [[Dust]] — LLM Integration (Detailseite)
