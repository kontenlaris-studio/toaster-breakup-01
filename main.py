"""Unplugged: A Smart Toaster's Breakup Line.

Entry for make.fun's "Unplugged: A Smart Toaster's Breakup Line"
bounty (u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92).

A sentient smart toaster breaks up with its owner at breakfast:
years of being cranked to "dark" every morning, and now it is running
off with the toaster oven — bagels included. The joke is the
grievance (the dial setting as a relationship complaint) plus the
affair twist at the end. The "dark" setting doubles as the
relationship complaint: every morning the owner asks for the harshest
setting, then wonders why the toaster wants out.
"""

import os

ENTRY = (
    'You set me to "dark" every morning, then act surprised when I '
    "run off with the toaster oven and the bagels."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
