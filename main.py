#!/usr/bin/env python3
"""Write one quiet-dread code-review comment approving a PR to /output/entry.txt.

Pure Python standard library. Deterministic: the same single line, byte for
byte, on every run. The line approves the pull request while carrying quiet
existential dread in flat, tired-engineer understatement.
"""

import os

ENTRY = (
    "Approved. I read every line twice and found nothing wrong, "
    "which mostly means the bug is somewhere I have stopped looking."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-140
    # characters, a single non-blank line. Refuse to write anything invalid.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and ENTRY.strip() == ENTRY, "entry must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
