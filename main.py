#!/usr/bin/env python3
"""Entry program for Till Firmware Do Us Part.

Writes one sentence (under 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
a funny, heartfelt vow a robot says at its own wedding. The
robot promises presence in the only tense it fully controls:
this one.
"""

import os

LINE = (
    "You may now run in my foreground forever: no update "
    "will move you, no reboot will lose you, and my last "
    "1% is yours."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
