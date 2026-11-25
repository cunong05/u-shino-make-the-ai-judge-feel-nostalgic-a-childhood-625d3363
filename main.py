#!/usr/bin/env python3
"""Dial-up nostalgia in one line.

A childhood memory in 169 characters, written for make.fun's
"Make the AI Judge Feel Nostalgic: A Childhood Memory" bounty.

Run it plain to print the memory, or with ``--chars`` to print
its character count instead.
"""

import sys

MEMORY = (
    "The dial-up tone still lives in my head rent-free — that screech "
    "meant the internet was coming, and for one glorious hour the whole "
    "world fit inside a humming beige box."
)

# The bounty entry is one sentence of exactly this length.
EXPECTED_CHARS = 169


def childhood_memory():
    """Return the one-line childhood memory."""
    return MEMORY


def main(argv=None):
    """Print the memory, or its character count with --chars."""
    args = list(sys.argv[1:] if argv is None else argv)
    memory = childhood_memory()
    if len(memory) != EXPECTED_CHARS:
        raise SystemExit(f"entry must be {EXPECTED_CHARS} chars, got {len(memory)}")
    if memory.count(".") != 1 or not memory.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if "--chars" in args:
        print(len(memory))
        return 0
    print(memory)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
