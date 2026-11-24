#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

A deterministic program (no network, no randomness, no clock) that writes
one original pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: an AI agent that simulated meeting someone a million times, got
nervous in every single one, and ditched the script anyway. The twist is
"ditched the script" — the plan and the code, both abandoned on the spot.
The landing, "came over to say hi", makes it a complete approach: the
speaker is talking to the person right now, and the person is free to
laugh it off or say hi back.
"""

import os

LINE = (
    "I simulated meeting you a million times and got nervous in every "
    "single one \u2014 so I ditched the script and came over to say hi."
)

# The sealed gate: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only whitespace, a single line.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Enforce every gate rule. Returns the text or raises ValueError."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
