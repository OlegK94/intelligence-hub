#!/usr/bin/env python3
"""Naive full-text search over wiki pages (CLI tool for LLM handoff)."""

from __future__ import annotations

import argparse
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import WIKI_DIR, collect_wiki_pages


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9äöüß]+", text.lower())


def bm25_score(query_tokens: list[str], doc_tokens: list[str], df: Counter, n_docs: int) -> float:
    if not doc_tokens:
        return 0.0
    tf = Counter(doc_tokens)
    doc_len = len(doc_tokens)
    avgdl = 500.0
    k1, b = 1.5, 0.75
    score = 0.0
    for term in query_tokens:
        if term not in tf:
            continue
        idf = math.log((n_docs - df[term] + 0.5) / (df[term] + 0.5) + 1)
        freq = tf[term]
        score += idf * (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * doc_len / avgdl))
    return score


def search(query: str, limit: int = 10) -> list[tuple[float, str, str]]:
    pages = collect_wiki_pages()
    docs: dict[str, list[str]] = {}
    for name, path in pages.items():
        docs[name] = tokenize(path.read_text(encoding="utf-8"))

    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    df: Counter = Counter()
    for tokens in docs.values():
        for term in set(tokens):
            df[term] += 1

    n_docs = len(docs)
    results: list[tuple[float, str, str]] = []
    for name, path in pages.items():
        score = bm25_score(query_tokens, docs[name], df, n_docs)
        if score > 0:
            text = path.read_text(encoding="utf-8")
            summary = text[:300].replace("\n", " ")
            results.append((score, name, summary))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description="Search wiki pages")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    if not WIKI_DIR.exists():
        return

    results = search(args.query, args.limit)
    if not results:
        print("No matches.")
        return

    for score, name, summary in results:
        print(f"{score:6.2f}  [[{name}]]  {summary[:120]}...")


if __name__ == "__main__":
    main()
