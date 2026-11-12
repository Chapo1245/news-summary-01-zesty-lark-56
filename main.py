# A working news-summary-01 entry (Python 3.13, standard library only): its summary
# is the summary.txt beside this file, and the program copies it byte for byte to
# $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Fully deterministic: every run
# writes the same bytes.
#
# Run it locally with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "summary.txt", OUT_DIR / "entry.txt")
