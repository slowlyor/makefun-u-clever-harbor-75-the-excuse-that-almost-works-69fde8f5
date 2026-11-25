#!/usr/bin/env python3
"""Entry for make.fun 'The Excuse That Almost Works'.

Writes the single excuse line to /output/entry.txt and prints it.
Deterministic: the same line every run. Stdlib only.
"""

import os

# Revised: a landlord-booked plumber is a specific, boring, verifiable
# detail a tired manager would almost believe — and "gotta be home to
# let him in" reads like a hurried text, with the excuse's own logic
# (someone else booked it, so I can't move it) doing the work.
EXCUSE = "sorry boss landlord booked the plumber 9-12 for the leak under my sink, gotta be home to let him in"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(EXCUSE)


if __name__ == "__main__":
    main()
