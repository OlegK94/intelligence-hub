#!/usr/bin/env python3
"""
Life Optimizer — Health & Performance
Wird getriggert wenn Health-Content ingested wird.
Liest den aktuellen Health-Masterplan + Wiki und prüft ob Updates nötig sind.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import call_claude, get_client, read_file_text, ROOT, append_log

HEALTH_PAGES = [
    ROOT / "outputs" / "notes" / "2026-06-14-oleg-health-masterplan.md",
    ROOT / "wiki" / "entities" / "Rhonda Patrick.md",
    ROOT / "wiki" / "concepts" / "Performance Coffee.md",
    ROOT / "raw" / "Privat" / "Performance" / "Supplement Stack.md",
    ROOT / "raw" / "Privat" / "Performance" / "Health Protocol — Master.md",
    ROOT / "raw" / "Privat" / "Performance" / "Hyrox — 10-Week Training.md",
]

OLEG_CONTEXT = """
Oleg Kober, 35J, Berlin, 188cm, 96.7kg, 20.3% Körperfett, Lean Mass 77.1kg.
Visceral Bauch: 101.4cm (grenzwertig, Ziel <90cm).
Ziel: 6kg Visceral Fat verlieren, Lean Mass halten, Hyrox-Performance.
Aufstehen 05:00, Schlaf 20:30. Training 4-5×/Woche Kraft + 2× HIIT + Zone-2 So.
Supplement Stack: Momentous (Kreatin 5g→10g Upgrade läuft, Omega-3, Mag-L-Threonate, L-Theanin, Alpha-GPC) + Sulforaphane Sunday Natural.
Frameworks: Huberman, Rhonda Patrick, Bryan Johnson, Peter Attia.
"""


def load_recent_health_wiki() -> str:
    """Lädt relevante Health-Wiki-Seiten."""
    content_parts = []
    for page in HEALTH_PAGES:
        if page.exists():
            text = read_file_text(page)
            content_parts.append(f"### {page.name}\n{text[:1500]}")
    return "\n\n".join(content_parts)


def find_new_health_clippings() -> list[Path]:
    """Findet neue Health-Clippings die noch nicht analysiert wurden."""
    clippings_dir = ROOT / "Clippings"
    if not clippings_dir.exists():
        return []
    files = list(clippings_dir.glob("*.md"))
    # Nur die 3 neuesten
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return files[:3]


def main():
    print("Life Optimizer: Analysiere neuen Health-Content...")
    client = get_client()

    current_state = load_recent_health_wiki()
    new_clippings = find_new_health_clippings()

    new_content = ""
    if new_clippings:
        parts = []
        for f in new_clippings:
            parts.append(f"**{f.name}:**\n{read_file_text(f)[:2000]}")
        new_content = "\n\n".join(parts)

    system = f"""Du bist der Gesundheits- und Performance-Optimizer für Oleg Kober.
Deine Aufgabe: Prüfe ob neues wissenschaftliches Wissen Olegs bestehende Protokolle verbessert.

KONTEXT OLEG:
{OLEG_CONTEXT}

Sei konkret, evidenzbasiert, direkt. Keine Allgemeinplätze.
Priorisiere nach Impact. Format: Markdown mit klaren Aktionspunkten."""

    user = f"""BESTEHENDE PROTOKOLLE (Zusammenfassung):
{current_state[:3000]}

NEUER CONTENT (letzte Clippings):
{new_content[:2000] if new_content else "Kein neuer Content — führe allgemeine Protokoll-Prüfung durch."}

Aufgabe:
1. Gibt es Widersprüche zwischen neuem Content und bestehenden Protokollen?
2. Gibt es konkrete Upgrades die Oleg SOFORT umsetzen soll? (Max 3, mit Begründung)
3. Welche Protokoll-Seiten sollten aktualisiert werden?
4. Fehlt etwas Wichtiges in Olegs aktuellem Stack basierend auf neuester Forschung?

Format:
## Sofortige Updates (falls vorhanden)
## Bestätigtes (was funktioniert)
## Offene Punkte / Rückfragen"""

    result = call_claude(client, system, user, max_tokens=1500)

    # Output speichern
    today = date.today().isoformat()
    output_path = ROOT / "outputs" / "notes" / f"{today}-health-optimizer-update.md"
    output_path.write_text(f"""---
date: {today}
type: auto-generated
source: life_optimizer.py
---

# Health Protocol Update — {today}

{result}
""")

    print(f"✓ Health-Update gespeichert → {output_path.name}")
    print(result[:500] + "...")
    append_log(ROOT / "wiki" / "log.md", f"life_optimizer | Health-Protocol-Update generiert | {today}")


if __name__ == "__main__":
    main()
