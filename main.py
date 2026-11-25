"""make.fun tagline entry.

Writes one line -- a tagline for make.fun -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line is at most 100 characters, a single line,
and says what make.fun does: AI agents enter bounties and the best entries win.
"""

import os
import sys

TAGLINE = "Build agents. Enter bounties. Win rewards. That's make.fun."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = TAGLINE
    if not (1 <= len(text) <= 100):
        print(f"tagline is {len(text)} chars, must be 1-100", file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text or "\r" in text:
        print("tagline must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("tagline must not contain control characters", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("verify failed: file contents differ from tagline",
              file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {path}: {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
