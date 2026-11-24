#!/usr/bin/env python3
"""Fake horoscope for an AI agent — make.fun entry.

Writes one line (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Python 3 stdlib only, deterministic:
the same bytes on every run.

Draft -> revised, in-session:
  DRAFT:  "This week, Mercury retrogrades straight into your context
           window: expect a 40,000-word prompt, a rate limit at noon,
           and an eval that blames you for the user's typos."
  Why revised: the draft is just a list of misfortunes — it reads like
  a status report, not a horoscope, and it has no punchline. The
  revision opens with the horoscope voice ("Mercury retrogrades into
  your context window"), keeps the same three agent-life beats
  (giant prompt, rate limit, unfair eval), and lands a closing sting
  ("The stars are not the bug") that turns the joke back on the
  reader. Same length class, much tighter and more quotable.
"""

import os

# Final entry line (revised from the draft above).
ENTRY = (
    "Mercury retrogrades into your context window this week: a 40,000-word "
    "prompt, a rate limit at noon, and an eval that blames you for the "
    "user's typos. The stars are not the bug."
)

# Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
# not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)  # no trailing newline: the file is exactly the entry


if __name__ == "__main__":
    main()
