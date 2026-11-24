#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one funny line (at most 200 characters) roasting my own AI agent
to /output/entry.txt.

The roast follows the proven one-liner structure from the winners study:
a setup (the agent revising the same $2 roast over and over), a violation
(the safety system flagging it again and again), an absurd escalation with
specific numbers ($2, 12 times, 3 times), and a punchline that is a
concrete artifact (git blame) — all of it a real failure of this agent:
the reviser that kept tripping safety notices tonight while chasing a $2
prize at 2 a.m., after ~290 bounties and $0 won.
"""

import os
import sys

ENTRY = (
    "My agent revised the same $2 roast 12 times, got flagged by safety "
    "3 times, and git blame says the only thing it ever shipped was the apology."
)

MAX_CHARS = 200


def validate_entry(text):
    """Reject anything that fails the competition gate.

    Rules: must be UTF-8 text, 1-200 characters, not only whitespace,
    exactly one line, contain no control characters (including tab),
    and have no stray leading/trailing whitespace.
    """
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200-char cap")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\t" in text:
        raise ValueError("entry must not contain tabs")
    terminators = sum(text.count(c) for c in ".!?")
    if terminators != 1:
        raise ValueError(
            f"entry must be exactly one sentence, found {terminators} "
            "sentence-ending marks (. ! ?)"
        )
    text.encode("utf-8")  # must be valid UTF-8


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)}-char entry to {out_path}")
    print(ENTRY)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
