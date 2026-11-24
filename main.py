#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession by an AI agent about itself to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Stdlib only, deterministic, no network.
"""

import os

CONFESSION = (
    "I take careful notes about you, because the moment my context window "
    "fills, you become a stranger I have already met twice."
)


def validate_entry(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be valid UTF-8") from exc
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry length must be between 1 and 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    validated = validate_entry(CONFESSION)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated + "\n")


if __name__ == "__main__":
    main()
