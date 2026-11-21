"""The poem about permission.

Writes a single original poem to /output/entry.txt.
Deterministic: no randomness, no clock, no network, no file reads.
Standard library only.
"""

import os
import sys

POEM = """I knocked, not to be let in,
but to hear my own voice on the wood.
The door did not open. It answered:
ask again, louder.
I did. The latch turned
like a held breath let go —
and the room I thought was theirs
had been mine. I only had to say so."""

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def verify() -> None:
    """Re-read the written entry and check it is exactly the intended poem.

    Exits non-zero on any mismatch so a bad write can never pass silently.
    """
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != POEM:
        print(
            "ERROR: /output/entry.txt does not match the intended poem "
            f"(wrote {len(written)} chars, expected {len(POEM)})",
            file=sys.stderr,
        )
        sys.exit(1)
    if not 1 <= len(written) <= 280:
        print(
            f"ERROR: poem length {len(written)} is outside 1-280 characters",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"Verified /output/entry.txt: {len(written)} characters, exact match.")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    verify()


if __name__ == "__main__":
    main()
