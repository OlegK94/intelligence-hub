#!/usr/bin/env python3
"""One-time raw/ reorganization: Privat + Business (Wagglz, Cafe, OK-Capital)."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"

# old relative path (from raw/) -> new relative path (from raw/)
MOVES: dict[str, str] = {
    # MOC
    "00-MOC/🏠 Home.md": "MOC/🏠 Home.md",
    "00-MOC/MOC Performance & Leben.md": "Privat/MOC/MOC Performance & Leben.md",
    "00-MOC/MOC Tech & Setup.md": "Privat/MOC/MOC Tech & Setup.md",
    "00-MOC/MOC Strategie & Business.md": "Business/MOC/MOC Strategie & Business.md",
    # Privat — life & tech
    "02-Performance-Leben": "Privat/Performance",
    "03-Tech-Setup": "Privat/Tech",
    "04-Recherchen": "Privat/Recherchen",
    # Privat — insurance & someday
    "01-Strategie-Business/Allianz Insurance Consolidation.md": "Privat/Versicherungen/Allianz Insurance Consolidation.md",
    "01-Strategie-Business/Cyprus Relocation.md": "Privat/Auswandern/Cyprus Relocation.md",
    "inbox/Cyprus Relocation Tracker.md": "Privat/Auswandern/Cyprus Relocation Tracker.md",
    # Business — Cafe
    "Cafe": "Business/Cafe",
    "01-Strategie-Business/Café Berlin — Partnership Hai.md": "Business/Cafe/Café Berlin — Partnership Hai.md",
    # Work (excluded from active vault scope)
    "01-Strategie-Business/DoktorLib Automation Pipeline.md": "_archiv/Work/DoktorLib Automation Pipeline.md",
    # Inbox merge
    "05-Inbox": "inbox/_merged",
    # Finanzdaten — privat
    "Finanzdaten/Privat": "Privat/Finanzen/Daten",
    "Finanzdaten/Obsidian_Vault/Konten/Consorsbank Girokonto 0250120493.md": "Privat/Finanzen/Konten/Consorsbank Girokonto 0250120493.md",
    "Finanzdaten/Obsidian_Vault/Ausgaben": "Privat/Finanzen/Ausgaben",
    "Finanzdaten/Obsidian_Vault/Einnahmen/ALG I 2025.md": "Privat/Finanzen/Einnahmen/ALG I 2025.md",
    "Finanzdaten/Obsidian_Vault/Einnahmen/Doctolib 2026.md": "Privat/Finanzen/Einnahmen/Doctolib 2026.md",
    "Finanzdaten/Obsidian_Vault/Steuern": "Privat/Finanzen/Steuern",
    "Finanzdaten/Obsidian_Vault/Aufgaben": "Privat/Finanzen/Aufgaben",
    "Finanzdaten/Obsidian_Vault/Archiv": "Privat/Finanzen/Archiv",
    "Finanzdaten/Obsidian_Vault/00 MOC Finanzen.md": "Privat/Finanzen/00 MOC Finanzen.md",
    "Finanzdaten/ObsidianVault/Finance/00 Finanz-Übersicht.md": "Privat/Finanzen/00 Finanz-Übersicht.md",
    "Finanzdaten/ObsidianVault/Finance/Master Prompt – Gesamtanalyse.md": "Privat/Finanzen/Master Prompt – Gesamtanalyse.md",
    "Finanzdaten/ObsidianVault/Finance/Rehabilitation Plan.md": "Privat/Finanzen/Rehabilitation Plan.md",
    "Finanzdaten/ObsidianVault/Performance": "Privat/Performance/_vault",
    "Finanzdaten/ObsidianVault/Templates": "Privat/Finanzen/Templates",
    "Finanzdaten/ObsidianVault/Home.md": "Privat/MOC/Finanz-Home.md",
    "Finanzdaten/GESAMTANALYSE_Oleg_Kober_2025-2026.md": "Privat/Finanzen/Archiv/GESAMTANALYSE_Oleg_Kober_2025-2026.md",
    "Finanzdaten/Finanzdashboard_Oleg_Kober_2026.html": "Privat/Finanzen/Daten/Finanzdashboard_Oleg_Kober_2026.html",
    # Business — Wagglz
    "Finanzdaten/Business/Wagglz GmbH": "Business/Wagglz/Daten",
    "Finanzdaten/Obsidian_Vault/Unternehmen/Wagglz GmbH.md": "Business/Wagglz/Wagglz GmbH.md",
    "Finanzdaten/ObsidianVault/Finance/Wagglz GmbH.md": "Business/Wagglz/Wagglz GmbH — Finance Vault.md",
    "Finanzdaten/Obsidian_Vault/Konten/Wagglz Finom 2026.md": "Business/Wagglz/Finanzen/Konten/Wagglz Finom 2026.md",
    "Finanzdaten/Obsidian_Vault/Einnahmen/Wagglz GF-Gehalt 2025.md": "Business/Wagglz/Finanzen/Einnahmen/Wagglz GF-Gehalt 2025.md",
    # Business — OK Capital
    "Finanzdaten/Business/OK Capital UG": "Business/OK-Capital/Daten",
    "Finanzdaten/Obsidian_Vault/Unternehmen/OK Capital UG.md": "Business/OK-Capital/OK Capital UG.md",
    "Finanzdaten/ObsidianVault/Finance/OK Capital UG.md": "Business/OK-Capital/OK Capital UG — Finance Vault.md",
    "Finanzdaten/Obsidian_Vault/Konten/OK Capital Finom 2026.md": "Business/OK-Capital/Finanzen/Konten/OK Capital Finom 2026.md",
    "Finanzdaten/Obsidian_Vault/Unternehmen/Rangrücktritt §15a InsO.md": "Business/OK-Capital/Rangrücktritt §15a InsO.md",
    # Misc
    "Finanzdaten/Privat/CLAUDE.md": "Privat/Finanzen/Daten/CLAUDE.md",
    "articles": "_archiv/articles",
}


def remap_path(rel: str) -> str:
    rel = rel.replace("\\", "/")
    if rel.startswith("raw/"):
        rel = rel[4:]
    # longest prefix match for directory moves
    best = None
    for old, new in sorted(MOVES.items(), key=lambda x: -len(x[0])):
        if rel == old or rel.startswith(old + "/"):
            suffix = rel[len(old) :].lstrip("/")
            mapped = f"{new}/{suffix}" if suffix else new
            return mapped.replace("//", "/")
    return rel


def move_item(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        if src.is_dir():
            for child in src.iterdir():
                move_item(child, dst / child.name)
            src.rmdir()
        else:
            return
    else:
        shutil.move(str(src), str(dst))


def apply_moves() -> list[tuple[str, str]]:
    log: list[tuple[str, str]] = []
    for old, new in sorted(MOVES.items(), key=lambda x: -len(x[0])):
        src = RAW / old
        if not src.exists():
            continue
        dst = RAW / new
        log.append((str(src.relative_to(ROOT)), str(dst.relative_to(ROOT))))
        move_item(src, dst)
    return log


def update_manifest() -> int:
    manifest_path = ROOT / "wiki" / ".ingest_manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    updated = []
    for p in data.get("ingested", []):
        if p.startswith("raw/"):
            inner = remap_path(p)
            updated.append(f"raw/{inner}" if not inner.startswith("raw/") else inner)
        else:
            updated.append(p)
    data["ingested"] = sorted(set(updated))
    manifest_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(updated)


def update_wiki_sources() -> int:
    count = 0
    wiki = ROOT / "wiki"
    for path in wiki.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        new_text = text
        for m in re.findall(r'raw/[^\s\]"\'`]+', text):
            inner = m[4:]
            mapped = remap_path(inner)
            new_m = f"raw/{mapped}"
            if new_m != m:
                new_text = new_text.replace(m, new_m)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            count += 1
    return count


def cleanup_empty() -> None:
    for name in ("00-MOC", "01-Strategie-Business", "02-Performance-Leben", "03-Tech-Setup", "04-Recherchen", "05-Inbox", "Cafe", "Finanzdaten", "articles"):
        p = RAW / name
        if p.exists() and p.is_dir() and not any(p.rglob("*")):
            p.rmdir()
        elif p.exists() and p.is_dir():
            try:
                shutil.rmtree(p) if not list(p.rglob("*")) else None
            except OSError:
                pass
    merged = RAW / "inbox" / "_merged"
    if merged.exists():
        for f in merged.iterdir():
            target = RAW / "inbox" / f.name
            if not target.exists():
                shutil.move(str(f), str(target))
        if not any(merged.iterdir()):
            merged.rmdir()


def main() -> None:
    moves = apply_moves()
    n_manifest = update_manifest()
    n_wiki = update_wiki_sources()
    cleanup_empty()
    print(f"Moved {len(moves)} paths")
    print(f"Manifest entries: {n_manifest}")
    print(f"Wiki files updated: {n_wiki}")


if __name__ == "__main__":
    main()
