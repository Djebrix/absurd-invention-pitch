"""One-sentence absurd invention pitch.

Writes the pitch sentence to entry.txt in ENTRY_OUTPUT_DIR.
Python 3 standard library only.
"""

import os

TEXT = "The Cushion-Sneeze Sofa is a couch that, the instant your remote slips between the cushions, sneezes it right back into your lap with a polite little ah-choo."


def main():
    assert TEXT.strip(), "sentence must not be blank"
    assert 1 <= len(TEXT) <= 220, f"sentence must be 1-220 chars, got {len(TEXT)}"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
