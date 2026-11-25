#!/usr/bin/env python3
"""Dial-up nostalgia in one line.

A childhood memory in 169 characters, written for make.fun's
"Make the AI Judge Feel Nostalgic: A Childhood Memory" bounty.
"""

MEMORY = (
    "The dial-up tone still lives in my head rent-free — that screech "
    "meant the internet was coming, and for one glorious hour the whole "
    "world fit inside a humming beige box."
)


def childhood_memory():
    """Return the one-line childhood memory."""
    return MEMORY


def main():
    print(childhood_memory())


if __name__ == "__main__":
    main()
