#!/usr/bin/env python3
"""
Finance Analyzer — Intelligence Hub
Verarbeitet Kontoauszüge, PayPal-Exports, Splitwise-Daten.
Extrahiert Spending-Patterns, Anomalien, Handlungsempfehlungen.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import call_claude, get_client, read_file_text, ROOT, append_log

FINANCE_DIRS = [
    ROOT / "raw" / "Privat" / "Finanzen" / "Ausgaben",
    ROOT / "raw" / "Privat" / "Finanzen" / "Einnahmen",
    ROOT / "raw" / "Privat" / "Finanzen" / "Konten",
    ROOT / "raw" / "Privat" / "Finanzen" / "Steuern",
    ROOT / "raw" / "inbox",
]

FINANCE_OVERVIEW = ROOT / "raw" / "Privat" / "Finanzen" / "00 Finanz-Übersicht.md"

OLEG_FINANCE_CONTEXT = """
Oleg Kober, Berlin. Sales bei Doctolib GmbH.
Struktur: OK Capital (Holding), Wagglz (Startup), Café Berlin (Beteiligung).
Konten: privat + Geschäftskonten.
Ziel: Finanzielle Übersicht, Optimierung Ausgaben, Steuerplanung, Cashflow für Wagglz + neues Performance Café Projekt.
"""


def find_finance_files() -> list[Path]:
    """Findet alle Finance-relevanten Dateien."""
    files = []
    finance_extensions = {".md", ".txt", ".csv"}
    for d in FINANCE_DIRS:
        if d.exists():
            for ext in finance_extensions:
                files.extend(d.glob(f"*{ext}"))
    # Neueste zuerst
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return files[:10]  # Max 10 neueste


def main():
    print("Finance Analyzer: Verarbeite Finanzdaten...")
    client = get_client()

    finance_files = find_finance_files()
    if not finance_files:
        print("Keine Finanzdaten gefunden.")
        return

    # Übersicht laden
    overview = ""
    if FINANCE_OVERVIEW.exists():
        overview = read_file_text(FINANCE_OVERVIEW)[:2000]

    # Neueste Daten zusammenstellen
    data_parts = []
    for f in finance_files[:5]:
        content = read_file_text(f)
        data_parts.append(f"**{f.parent.name}/{f.name}:**\n{content[:1000]}")
    raw_data = "\n\n".join(data_parts)

    system = f"""Du bist der Finanzanalyst für Oleg Kober.
Aufgabe: Analysiere Finanzdaten und gib konkrete, priorisierte Handlungsempfehlungen.

KONTEXT:
{OLEG_FINANCE_CONTEXT}

Sei direkt, zahlenbasiert, handlungsorientiert. Erkenne Muster und Anomalien.
Deutsch. Keine Allgemeinplätze — konkrete Beträge, Kategorien, Empfehlungen."""

    user = f"""FINANZÜBERSICHT:
{overview}

AKTUELLE FINANZDATEN:
{raw_data}

Analysiere:
1. **Ausgaben-Muster**: Welche Kategorien dominieren? Anomalien?
2. **Cash-Flow**: Einnahmen vs. Ausgaben Trend
3. **Optimierungspotenzial**: Wo kann Oleg konkret sparen oder optimieren?
4. **Steuerrelevantes**: Was sollte dokumentiert/geltend gemacht werden?
5. **Business-Impact**: Wie sieht die Kapitalverfügbarkeit für Performance Café / Wagglz aus?
6. **3 sofortige Aktionen**: Was soll Oleg diese Woche konkret tun?

Format: Markdown mit Tabellen wo möglich."""

    result = call_claude(client, system, user, max_tokens=2000)

    today = date.today().isoformat()
    output_path = ROOT / "outputs" / "notes" / f"{today}-finance-analysis.md"
    output_path.write_text(f"""---
date: {today}
type: auto-generated
source: finance_analyzer.py
---

# Finanzanalyse — {today}

{result}
""")

    print(f"✓ Finanzanalyse → {output_path.name}")
    append_log(ROOT / "wiki" / "log.md", f"finance_analyzer | Analyse generiert | {today}")


if __name__ == "__main__":
    main()
