#!/usr/bin/env python3
"""
Weekly Research Agent — Proaktive Recherche
Läuft jeden Montag via launchd.
Sucht neue Entwicklungen in: Health/Longevity, Performance Café Markt, EU Regulatorik.
Schreibt Findings direkt als neue Clippings → werden durch smart_ingest.py verarbeitet.
"""
from __future__ import annotations

import sys
import json
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import call_claude, get_client, ROOT, append_log

RESEARCH_TOPICS = [
    {
        "category": "health",
        "queries": [
            "Huberman Lab neue Folge 2026 Supplement Protokoll",
            "Rhonda Patrick FoundMyFitness neue Studie 2026",
            "Bryan Johnson Blueprint Update 2026",
            "NMN Studie 2026 NAD Longevity",
            "Kreatin neue Studie 10g Dosierung 2026",
            "Omega-3 Studie Visceral Fat 2026",
        ]
    },
    {
        "category": "business",
        "queries": [
            "Functional Coffee Markt Europa 2026",
            "Blueprint Bryan Johnson neue Produkte 2026",
            "Four Sigmatic RYZE MUD WTR news 2026",
            "NMN EU Novel Food Zulassung 2026",
            "Urolithin A Amazentis Mitopure Lizenz",
            "Longevity Supplement Startup Funding Europa",
        ]
    },
]

OLEG_CONTEXT = """
Oleg Kober, Berlin. Hauptinteressen:
- Health/Performance: Hyrox, Visceral-Fat-Abbau, Supplement-Stack-Optimierung
- Business: Performance Café (Longevity-Kaffee Startup mit Hai), Wagglz, OK Capital
- Longevity: Huberman, Rhonda Patrick, Bryan Johnson, Peter Attia Protokolle
"""


def run_research_session(client, topics: list[dict]) -> str:
    """Generiert Research-Findings (nutzt Claude's Wissen + Websearch wenn verfügbar)."""
    topic_list = []
    for t in topics:
        topic_list.append(f"**{t['category'].upper()}:** " + " | ".join(t['queries'][:3]))

    system = f"""Du bist der proaktive Research-Agent für Olegs Intelligence Hub.
Aufgabe: Liefere aktuelle Insights zu diesen Themen basierend auf deinem Wissen (Stand 2025/2026).

{OLEG_CONTEXT}

Format: Strukturiert, direkt, mit konkreten Daten. Markiere was Olegs Protokolle/Business direkt betrifft."""

    user = f"""Wöchentlicher Research-Report. Datum: {date.today()}

Recherche-Themen:
{chr(10).join(topic_list)}

Aufgabe:
1. Was gibt es Neues in diesen Bereichen (basierend auf deinem aktuellen Wissen)?
2. Was ist direkt relevant für Olegs Health-Protokoll? Gibt es Änderungen die er vornehmen soll?
3. Was ist relevant für Performance Café (Markt, Wettbewerb, Regulatorik)?
4. Top 3 Insights der Woche mit konkreten Handlungsempfehlungen.

Sei spezifisch. Wenn du keine aktuellen Daten hast, sage das klar — dann markiere es als "manuell recherchieren"."""

    return call_claude(client, system, user, max_tokens=2000)


def main():
    print(f"Weekly Research Agent: {date.today()}")
    client = get_client()

    findings = run_research_session(client, RESEARCH_TOPICS)

    today = date.today().isoformat()
    output_path = ROOT / "outputs" / "notes" / f"{today}-weekly-research.md"
    output_path.write_text(f"""---
date: {today}
type: weekly-research
source: weekly_research.py
status: processed
---

# Wöchentlicher Research Report — {today}

{findings}

---
*Auto-generiert von weekly_research.py | Nächster Run: nächsten Montag*
""")

    print(f"✓ Weekly Research → {output_path.name}")
    append_log(ROOT / "wiki" / "log.md", f"weekly_research | Wöchentlicher Report generiert | {today}")

    # Als Clipping ablegen damit smart_ingest es aufgreift
    clipping_path = ROOT / "Clippings" / f"{today}-weekly-research-clipping.md"
    clipping_path.write_text(f"""---
title: Wöchentlicher Research Report {today}
type: weekly-research
date: {today}
---

{findings}
""")
    print(f"✓ Als Clipping gespeichert → smart_ingest verarbeitet es")


if __name__ == "__main__":
    main()
