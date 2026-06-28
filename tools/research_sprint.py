#!/usr/bin/env python3
"""
research_sprint.py - Power Researcher CLI

Strukturierter Research-Sprint: Frage -> Web-Suche -> Synthese -> Wiki -> Output.

Usage:
  python3 tools/research_sprint.py "Was ist der beste NAD+-Precursor?"
  python3 tools/research_sprint.py "NR vs NMN vs Trigonellin" --type comparison
  python3 tools/research_sprint.py "Koelner Liste" --output slides
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    INDEX_FILE,
    append_log,
    apply_wiki_articles,
    call_claude,
    dated_output_path,
    ensure_layout,
    extract_json,
    get_client,
    load_wiki_content,
    write_index,
)

RESEARCH_SYSTEM = """\
Du bist ein Elite-Research-Analyst. Kein Bullshit, nur Fakten mit Quellen.

Fuer jeden Claim:
- Quelle nennen (Autor, Jahr, DOI wenn verfuegbar)
- Konfidenz: HOCH (Meta-Analyse/repliziert) | MITTEL (1-2 Studien) | NIEDRIG (vorlaeufig/Anekdote)
- Aktiv Gegenpositionen suchen - nicht nur bestaetigen

Research-Prozess:
1. Frage in 3-5 Teilfragen zerlegen
2. Fuer jede Teilfrage: beste verfuegbare Evidenz
3. Konflikte und Unsicherheiten explizit benennen
4. Praktische Implikation: Was bedeutet das konkret?
5. Naechste offene Fragen identifizieren

Output ONLY valid JSON:
{
  "sprint_title": "Klarer Titel",
  "sub_questions": ["Teilfrage 1", "Teilfrage 2"],
  "findings": [
    {
      "question": "Teilfrage",
      "answer": "Antwort mit Quellen",
      "confidence": "HOCH|MITTEL|NIEDRIG",
      "sources": ["Quelle 1"],
      "counterposition": "Gegenmeinung / Einschraenkung"
    }
  ],
  "synthesis": "Gesamtzusammenfassung",
  "action_items": ["Naechste Schritte"],
  "open_questions": ["Was ist noch unklar?"],
  "wiki_articles": [
    {"name": "Seitenname", "type": "synthesis|comparison|concept", "content": "Vollstaendiger Markdown"}
  ],
  "index_md": null,
  "answer_md": "Vollstaendige Markdown-Antwort",
  "slug": "kurzer-dateiname"
}
"""


def build_research_prompt(question: str, sprint_type: str, wiki_content: str, index: str) -> str:
    return f"""\
Research-Sprint: {question}
Typ: {sprint_type}

Recherchiere gruendlich. Suche aktiv nach:
- Primaerstudien und Meta-Analysen
- Regulatorische Dokumente (EFSA, BVL, EU)
- Gegenpositionen und kritische Stimmen
- Aktuelle Entwicklungen (2023-2026)

=== BESTEHENDES WIKI ===
INDEX:
{index}

WIKI-CONTENT:
{wiki_content}

Integriere neue Erkenntnisse ins Wiki. Verlinke bestehende Seiten mit [[Wikilinks]].
Wenn Typ=comparison: Erstelle strukturierten Vergleich mit Kriterien-Matrix.
"""


def format_sprint_output(data: dict, question: str) -> str:
    title = data.get("sprint_title", question)
    findings = data.get("findings", [])
    synthesis = data.get("synthesis", "")
    actions = data.get("action_items", [])
    open_q = data.get("open_questions", [])

    confidence_icon = {"HOCH": "GRN", "MITTEL": "YLW", "NIEDRIG": "RED"}

    lines = [
        f"# Research Sprint: {title}",
        "",
        f"> **Frage:** {question}",
        "",
        "## Teilfragen & Findings",
        "",
    ]

    for f in findings:
        icon = confidence_icon.get(f.get("confidence", ""), "?")
        lines += [
            f"### {f.get('question', '')}",
            "",
            f.get("answer", ""),
            "",
            f"**Konfidenz:** [{icon}] {f.get('confidence', '-')}",
        ]
        sources = f.get("sources", [])
        if sources:
            lines.append(f"**Quellen:** {', '.join(sources)}")
        counter = f.get("counterposition", "")
        if counter:
            lines += ["", f"> **Gegenposition:** {counter}"]
        lines.append("")

    lines += [
        "## Synthese",
        "",
        synthesis,
        "",
        "## Naechste Schritte",
        "",
    ]
    for a in actions:
        lines.append(f"- [ ] {a}")
    lines += ["", "## Offene Fragen", ""]
    for q_item in open_q:
        lines.append(f"- {q_item}")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Power Researcher Sprint")
    parser.add_argument("question", help="Research-Frage oder Thema")
    parser.add_argument(
        "--type",
        choices=["synthesis", "comparison", "deep-dive"],
        default="synthesis",
    )
    parser.add_argument(
        "--output",
        choices=["notes", "slides"],
        default="notes",
    )
    args = parser.parse_args()

    ensure_layout()
    client = get_client()

    index = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    wiki = load_wiki_content()

    print(f"Research Sprint: {args.question!r}")
    print(f"Typ: {args.type} | Output: {args.output}")

    response = call_claude(
        client,
        RESEARCH_SYSTEM,
        build_research_prompt(args.question, args.type, wiki, index),
        max_tokens=16384,
    )
    data = extract_json(response)

    answer_md = data.get("answer_md") or format_sprint_output(data, args.question)
    slug = data.get("slug", "research-sprint")
    out_path = dated_output_path(args.output, slug)
    out_path.write_text(answer_md.strip() + "\n", encoding="utf-8")
    print(f"Output: {out_path}")

    if data.get("wiki_articles"):
        touched = apply_wiki_articles(data["wiki_articles"])
        if data.get("index_md"):
            write_index(data["index_md"])
        pages = ", ".join(f"[[{n}]]" for n in touched)
        print(f"Wiki: {pages}")
        append_log(
            f'research_sprint | "{args.question[:80]}"\n'
            f"- Type: {args.type}\n"
            f"- Output: {out_path.name}\n"
            f"- Wiki pages: {pages}"
        )
    else:
        append_log(
            f'research_sprint | "{args.question[:80]}"\n'
            f"- Type: {args.type}\n"
            f"- Output: {out_path.name}"
        )


if __name__ == "__main__":
    main()
