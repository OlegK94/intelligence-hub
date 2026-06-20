#!/usr/bin/env python3
"""Translate English/mixed wiki pages to German — batch tool.

Preserves: [[wikilinks]], frontmatter keys, sources/tags/dates, numbers,
URLs, code blocks, filenames. Only prose, headings and the summary value
are translated. Technical terms (Performance Coffee, Longevity, EFSA, …)
stay as-is.

Usage:
  python3 tools/translate_wiki.py --dry-run        # list candidates only
  python3 tools/translate_wiki.py --limit 10       # translate first 10
  python3 tools/translate_wiki.py                  # translate all EN/mixed
  python3 tools/translate_wiki.py --file "wiki/entities/Wagglz GmbH.md"
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import call_claude, get_client, WIKI_DIR

EN = {'the','and','of','for','with','that','this','are','was','have','from',
      'will','their','which','these','would','about','there','when','what'}
DE = {'und','der','die','das','ist','für','mit','von','auch','nicht','ein',
      'eine','sich','werden','wird','bei','dem','den','sind','wurde','kann'}

SYSTEM = """\
Du bist Übersetzer für ein deutschsprachiges Obsidian-Wiki (Karpathy LLM Wiki).
Übersetze die übergebene Markdown-Wiki-Seite ins Deutsche.

ABSOLUT UNVERÄNDERT lassen (NICHT übersetzen, NICHT umformatieren):
- Alle Obsidian-Wikilinks: [[Exakter Name]] und [[Name|Alias]] — der Teil VOR dem | bleibt 1:1 (das ist ein Dateiname!). Nur einen Alias NACH dem | darfst du eindeutschen.
- Den kompletten YAML-Frontmatter-Block (zwischen den --- ) AUSSER dem Wert von `summary:` und `title:` — diese beiden Werte ins Deutsche übersetzen, alle anderen Felder (tags, sources, created, updated, type) exakt lassen.
- Alle Zahlen, Währungen, Daten, IBANs, Prozente, Einheiten
- Alle URLs und Code-Blöcke (``` … ```), Inline-Code (`…`)
- Fachbegriffe/Eigennamen die etabliert englisch sind: Performance Coffee, Longevity, Blueprint, EFSA, Novel Food, Hyrox, Zone 2, NSDR, COGS, Cashflow, etc. — diese bleiben englisch.

Übersetze: Fließtext, Überschriften, Aufzählungen, Tabellen-Inhalte (außer Zahlen), den summary- und title-Wert.

Gib AUSSCHLIESSLICH die fertige deutsche Markdown-Seite zurück — kein Vorwort, keine Code-Fence drumherum, keine Erklärung.
"""


def lang_ratio(text: str) -> float:
    """Return EN ratio (0..1). >0.5 = predominantly English."""
    body = re.sub(r'^---.*?---', '', text, count=1, flags=re.DOTALL)
    words = re.findall(r'[a-zäöü]+', body.lower())
    en = sum(1 for w in words if w in EN)
    de = sum(1 for w in words if w in DE)
    tot = en + de
    return en / tot if tot >= 5 else 0.0


def is_candidate(text: str) -> bool:
    return lang_ratio(text) > 0.40


def translate_page(client, path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not is_candidate(text):
        return False
    result = call_claude(client, SYSTEM, text, max_tokens=8192).strip()
    # Strip accidental code fences
    result = re.sub(r'^```(?:markdown)?\n', '', result)
    result = re.sub(r'\n```$', '', result)
    # Safety: result must still contain the frontmatter and be non-trivial
    if not result.startswith('---') or len(result) < len(text) * 0.4:
        print(f"  ⚠ SKIP (verdächtiges Ergebnis): {path.name}", file=sys.stderr)
        return False
    # Safety: wikilink targets must be preserved
    orig_links = set(re.findall(r'\[\[([^\]|]+)', text))
    new_links = set(re.findall(r'\[\[([^\]|]+)', result))
    if orig_links - new_links:
        print(f"  ⚠ SKIP (Wikilinks verändert): {path.name} — fehlt: {orig_links - new_links}", file=sys.stderr)
        return False
    path.write_text(result, encoding="utf-8")
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description="Translate EN wiki pages to German")
    ap.add_argument("--dry-run", action="store_true", help="List candidates only")
    ap.add_argument("--limit", type=int, default=0, help="Max pages to translate")
    ap.add_argument("--file", help="Translate one specific file")
    args = ap.parse_args()

    if args.file:
        candidates = [Path(args.file)]
    else:
        candidates = []
        for p in sorted(WIKI_DIR.rglob("*.md")):
            if p.name in ("log.md", "index.md", "Dashboard.md"):
                continue
            if is_candidate(p.read_text(encoding="utf-8", errors="ignore")):
                candidates.append(p)

    print(f"Kandidaten (EN/mixed): {len(candidates)}")
    if args.dry_run:
        for p in candidates:
            r = lang_ratio(p.read_text(errors='ignore'))
            print(f"  {r:.2f} EN  {p.relative_to(WIKI_DIR)}")
        return

    if args.limit:
        candidates = candidates[: args.limit]

    client = get_client()
    done = 0
    for i, p in enumerate(candidates, 1):
        try:
            if translate_page(client, p):
                done += 1
                print(f"[{i}/{len(candidates)}] ✓ {p.relative_to(WIKI_DIR)}")
            else:
                print(f"[{i}/{len(candidates)}] — übersprungen: {p.relative_to(WIKI_DIR)}")
        except Exception as e:
            print(f"[{i}/{len(candidates)}] ✗ Fehler {p.name}: {e}", file=sys.stderr)

    print(f"\nFertig: {done} Seiten ins Deutsche übersetzt.")
    print("Danach: bash scripts/qmd-sync.sh && qmd embed   # Index aktualisieren")


if __name__ == "__main__":
    main()
