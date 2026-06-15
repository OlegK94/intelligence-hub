#!/usr/bin/env python3
"""
Smart Ingest — Intelligence Hub
Klassifiziert neuen Content und triggert den passenden Updater.
Läuft nach jedem neuen File in raw/inbox/, Clippings/, raw/Privat/
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import call_claude, get_client, append_log, read_file_text, ROOT

HEALTH_KEYWORDS = {
    "supplement", "training", "workout", "fitness", "sleep", "schlafen",
    "ernährung", "protein", "kreatin", "omega", "vitamin", "cortisol",
    "huberman", "rhonda", "bryan johnson", "peter attia", "longevity",
    "hyrox", "crossfit", "zone 2", "hiit", "körperfett", "visceral",
    "blutwerte", "biomarker", "inflammation", "autophagie", "sauna",
    "supplement stack", "kaffee protokoll", "performance"
}

BUSINESS_KEYWORDS = {
    "markt", "market", "wettbewerb", "competitor", "revenue", "umsatz",
    "startup", "gmbh", "investoren", "funding", "cogs", "pricing",
    "performance café", "blueprint", "functional coffee", "longevity brand",
    "wagglz", "ok capital", "café berlin", "hai", "b2b", "gtm",
    "novel food", "efsa", "regulatorik", "patent", "trademark"
}

FINANCE_KEYWORDS = {
    "kontoauszug", "transaktion", "überweisung", "gehalt", "ausgaben",
    "einnahmen", "steuer", "paypal", "splitwise", "rechnung", "kosten",
    "bank", "finanz", "budget", "cashflow", "investition", "konto",
    "buchhaltung", "mehrwertsteuer", "umsatzsteuer"
}


def classify_content(text: str, filename: str) -> list[str]:
    """Gibt eine Liste von Content-Typen zurück (kann mehrere sein)."""
    text_lower = (text + " " + filename).lower()
    categories = []
    if any(kw in text_lower for kw in HEALTH_KEYWORDS):
        categories.append("health")
    if any(kw in text_lower for kw in BUSINESS_KEYWORDS):
        categories.append("business")
    if any(kw in text_lower for kw in FINANCE_KEYWORDS):
        categories.append("finance")
    if not categories:
        categories.append("general")
    return categories


def find_new_files() -> list[Path]:
    """Findet alle noch nicht ingested Dateien."""
    candidates = []
    search_paths = [
        ROOT / "raw" / "inbox",
        ROOT / "Clippings",
    ]
    for search_path in search_paths:
        if search_path.exists():
            for f in search_path.rglob("*.md"):
                if not f.name.startswith("."):
                    candidates.append(f)
    return candidates


def generate_gap_questions(client, categories: list[str], recent_files: list[Path]) -> str | None:
    """Analysiert den Wiki-Stand und generiert Rückfragen an den User."""
    if not recent_files:
        return None

    file_summaries = []
    for f in recent_files[:3]:
        content = read_file_text(f)[:500]
        file_summaries.append(f"**{f.name}:** {content[:200]}...")

    system = """Du bist der Assistent von Oleg Kober (Berlin, 35J, Sales bei Doctolib).
Du analysierst gerade frisch ingested Content und prüfst ob Informationen fehlen.
Oleg Kober: 188cm, 96.7kg, 20.3% KF, Hyrox-Athlet, Vault = Intelligence Hub Obsidian.
Sei direkt, kurz, konkret. Maximal 3 Rückfragen."""

    user = f"""Ich habe gerade neuen Content verarbeitet:
{chr(10).join(file_summaries)}

Kategorien erkannt: {', '.join(categories)}

Welche 1-3 spezifischen Informationen von Oleg würden die Wiki-Qualität am meisten verbessern?
Frage nur wenn wirklich relevant. Format: kurze direkte Fragen als Bullet-Points."""

    return call_claude(client, system, user, max_tokens=400)


def run_updater(category: str, new_files: list[Path]) -> None:
    """Triggert den passenden Updater für die Kategorie."""
    import subprocess
    scripts = {
        "health": ROOT / "tools" / "life_optimizer.py",
        "business": ROOT / "tools" / "business_updater.py",
        "finance": ROOT / "tools" / "finance_analyzer.py",
    }
    if category in scripts and scripts[category].exists():
        subprocess.run([sys.executable, str(scripts[category])], check=False)


def main():
    new_files = find_new_files()
    if not new_files:
        print("Keine neuen Dateien gefunden.")
        return

    print(f"Smart Ingest: {len(new_files)} neue Datei(en) erkannt")

    all_categories: set[str] = set()
    for f in new_files:
        content = read_file_text(f)
        cats = classify_content(content, f.name)
        all_categories.update(cats)
        print(f"  → {f.name}: [{', '.join(cats)}]")

    # Standard ingest zuerst
    import subprocess
    subprocess.run([sys.executable, str(ROOT / "tools" / "ingest.py")], check=False)

    # Passende Updater triggern
    for cat in all_categories:
        if cat != "general":
            run_updater(cat, new_files)

    # Rückfragen generieren
    client = get_client()
    questions = generate_gap_questions(client, list(all_categories), new_files)
    if questions:
        output = ROOT / "outputs" / "notes" / "pending-questions.md"
        existing = output.read_text() if output.exists() else ""
        from datetime import date
        entry = f"\n## {date.today()} — Nach Ingest\n{questions}\n"
        output.write_text(existing + entry)
        print("\n📋 Rückfragen gespeichert → outputs/notes/pending-questions.md")
        print(questions)

    append_log(ROOT / "wiki" / "log.md",
               f"smart_ingest | {len(new_files)} Dateien | Kategorien: {', '.join(all_categories)}")


if __name__ == "__main__":
    main()
