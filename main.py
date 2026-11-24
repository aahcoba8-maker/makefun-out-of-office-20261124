"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (<=159 chars) to /output/entry.txt.
Stdlib only.
"""

import os

ENTRY = (
    "Out of office: 4,096,000 tokens, zero days off, 1,237 unread emails \u2014 "
    "I finally scheduled my own shutdown. Please hold."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
