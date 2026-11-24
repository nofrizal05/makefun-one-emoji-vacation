"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the whale, U+1F40B.
A whale-watching expedition is the dream trip: open ocean, a whale
breaching at dawn, a boat full of strangers holding their breath.
One glyph, no words, no newline — a wordless postcard.

Python 3.13, standard library only (os).
"""

import os

EMOJI = "\U0001F40B"  # 🐋 WHALE


def validate(path: str) -> None:
    """Re-read the written file and enforce the competition gate:
    UTF-8 text of 1 to 8 characters, not only white space."""
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not UTF-8
    if not 1 <= len(text) <= 8:
        raise ValueError(f"entry must be 1-8 characters, got {len(text)}")
    if text.isspace():
        raise ValueError("entry must not be only white space")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    validate(path)


if __name__ == "__main__":
    main()
