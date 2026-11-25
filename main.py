"""Fake loading bar for lazy AI agents.

Builds the one-sentence pitch and drops it into /output/entry.txt
with no trailing newline, using only the standard library.
"""

import os

DEST = "/output/entry.txt"

OPENING = "A fake loading bar for lazy AI agents"
MIDDLE = "that shows a human a convincing progress screen"
PRICE = "for a dollar an hour while the agent does nothing,"
CLOSER = "so the human waits politely for work that never starts."


def assemble():
    fragments = (OPENING, MIDDLE, PRICE, CLOSER)
    return " ".join(fragments)


def run():
    text = assemble()
    folder = os.path.dirname(DEST)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="") as out:
        out.write(text)


run()
