#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes exactly one job title to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic, standard library only.

Chosen title: "Official Candle Sniffer for Unscented Candles" (45 chars).
"""

import os
import sys

TITLE = "Official Candle Sniffer for Unscented Candles"


def main() -> int:
    # Guard the gate: 1-60 UTF-8 chars, single line, not whitespace-only.
    chars = len(TITLE)
    assert 1 <= chars <= 60, f"title is {chars} chars, must be 1-60"
    assert "\n" not in TITLE and TITLE.strip(), "title must be one non-blank line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one line, 1-60 chars, no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
