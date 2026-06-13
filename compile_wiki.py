#!/usr/bin/env python3
"""
compile_wiki.py — convenience entry point for Karpathy-style wiki ingest.

Delegates to tools/ingest.py. Raw sources stay immutable in raw/.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

INGEST = Path(__file__).resolve().parent / "tools" / "ingest.py"
sys.argv[0] = str(INGEST)
runpy.run_path(str(INGEST), run_name="__main__")
