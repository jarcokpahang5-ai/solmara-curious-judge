#!/usr/bin/env python3
"""Write a short curious text for the make.fun bounty
"Make the AI judge feel curious".

Pure Python 3 standard library, deterministic, no network.
Reads the output directory from MAKEFUN_OUTPUT_DIR
(default /output) and writes one text (1-280 Unicode
characters) to entry.txt there.
"""

import os

TEXT = (
    "Somewhere in a house that was never built, a window was left open. "
    "Through it drifts a song no one wrote, in a voice that sounds almost "
    "like yours. It stops the moment you try to hum along \u2014 then waits, "
    "patient as dust in sunlight, for you to forget it was ever there."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
