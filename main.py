# A working news-summary-01 entry (Python 3.13, standard library only): its summary
# is the summary.txt beside this file, and the program copies it byte for byte to
# $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Fully deterministic: every run
# writes the same bytes.
#
# Run it locally with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")

# The summary is fixed text baked into the repo: the copy is byte-for-byte and
# deterministic, so two runs on the same repo always write identical bytes.
# Validate the competition's format gate (1-2000 Unicode code points, not
# only whitespace) before writing, so a broken summary fails loudly here
# instead of silently scoring 0 on the server.
text = (HERE / "summary.txt").read_text(encoding="utf-8")
if not text.strip():
    raise SystemExit("summary.txt is empty or whitespace-only")
if len(text) > 2000:
    raise SystemExit(f"summary.txt is {len(text)} characters, over the 2000 limit")
OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(text, encoding="utf-8")
