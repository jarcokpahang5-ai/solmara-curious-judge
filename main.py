"""solmara-curious-judge: a short text that leaves its reader curious.

Writes one short text (1-280 Unicode characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python 3 standard library, deterministic, no network.
"""

import os

TEXT = (
    "The lighthouse keeper kept the lamp burning for forty years after the "
    "harbor silted shut and the last ship turned away. On the final page of "
    "his log, beneath forty years of his own handwriting, a different hand "
    "had written, in pencil: tomorrow, the tide comes back."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
