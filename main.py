#!/usr/bin/env python3
"""One-letter diary entry: D for doomscrolling till 3am.

The letter stands for the word that describes the day: "doomscrolling".
It is vivid (the phone glow at 3am), funny and painfully true of a real
day, and D is its natural initial. It deliberately avoids the overused
example letters A, F and Z from the bounty description.

The output is fully deterministic: LETTER is a fixed module constant, so
no randomness, time, environment or input can change the bytes written.

Writes exactly one byte, "D", with no trailing newline, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

LETTER = "D"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LETTER.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
