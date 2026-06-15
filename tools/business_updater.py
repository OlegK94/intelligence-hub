#!/usr/bin/env python3
"""
Business Updater — Performance Café + Wagglz
Wird getriggert wenn Business-Content ingested wird.
Aktualisiert Marktforschung, Wettbewerbsanalyse, Business Case.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import call_claude, get_client, read_file_text, ROOT, append_log

BUSINESS_CONTEXT = """
Performance Café: Funktioneller Longevity-Kaffee als Instant-Sachet.
Kernversprechen: "Perform now. Live longer."
White Space: Blueprint by Bryan Johnson macht keinen Kaffee.
Zielmarkt: DACH/EU, Biohacker, Hyrox-Athleten, Executive.
Partner: Hai (50/50 Partnership geplant).
Holding: OK Capital.
Status: Research-Phase, Pre-Seed.
"""

PERF_CAFE_DIR = ROOT / "raw" / "Business" / "PerformanceCafe" / "research"


def load_existing_research() -> str:
    """Lädt bestehende Performance Café Forschung."""
    parts = []
    if PERF_CAFE_DIR.exists():
        for f in sorted(PERF_CAFE_DIR.glob("*.md")):
            if f.name != "00_master_brief.md":
                content = read_file_text(f)
                if len(content) > 200:  # Nur gefüllte Dateien
                    parts.append(f"### {f.stem}\n{content[:800]}")
    return "\n\n".join(parts[:4])


def find_new_business_clippings() -> list[Path]:
    """Findet neue Business-relevante Clippings."""
    clippings_dir = ROOT / "Clippings"
    inbox_dir = ROOT / "raw" / "inbox"
    files = []
    for d in [clippings_dir, inbox_dir]:
        if d.exists():
            files.extend(d.glob("*.md"))
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return files[:3]


def main():
    print("Business Updater: Analysiere neuen Business-Content...")
    client = get_client()

    existing = load_existing_research()
    new_files = find_new_business_clippings()

    new_content = ""
    if new_files:
        parts = []
        for f in new_files:
            text = read_file_text(f)
            # Nur wenn Business-relevant
            if any(kw in text.lower() for kw in ["kaffee", "coffee", "supplement", "longevity", "market", "markt", "competitor"]):
                parts.append(f"**{f.name}:**\n{text[:1500]}")
        new_content = "\n\n".join(parts)

    if not new_content and not existing:
        print("Kein relevanter Business-Content gefunden.")
        return

    system = f"""Du bist der Business-Analyst für Olegs Performance Café Projekt.
Aufgabe: Prüfe neuen Content auf Business-Relevanz und aktualisiere die Marktforschung.

{BUSINESS_CONTEXT}

Sei konkret: Zahlen, Firmennamen, Marktdaten. Direkt auf Deutsch."""

    user = f"""BESTEHENDE FORSCHUNG (Auszug):
{existing[:2000]}

NEUER CONTENT:
{new_content[:2000] if new_content else "Kein neuer externer Content — führe allgemeine Review durch."}

Aufgabe:
1. Welche neuen Insights sind Business-relevant für Performance Café?
2. Gibt es neue Wettbewerber-Bewegungen oder Marktveränderungen?
3. Welche Forschungsmodule sollten basierend auf dem neuen Content aktualisiert werden?
4. 2-3 konkrete nächste Business-Schritte für Oleg + Hai?

Format: Markdown, präzise."""

    result = call_claude(client, system, user, max_tokens=1500)

    today = date.today().isoformat()
    output_path = ROOT / "outputs" / "notes" / f"{today}-business-update.md"
    output_path.write_text(f"""---
date: {today}
type: auto-generated
source: business_updater.py
project: performance-cafe
---

# Business Update — {today}

{result}
""")

    print(f"✓ Business-Update → {output_path.name}")
    append_log(ROOT / "wiki" / "log.md", f"business_updater | Business-Update generiert | {today}")


if __name__ == "__main__":
    main()
