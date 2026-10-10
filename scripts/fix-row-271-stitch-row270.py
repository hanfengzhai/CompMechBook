#!/usr/bin/env python3
"""Restore row 270 DDD closing stitch next-row hint after row 271 insert."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD = (
    "then [epilogue row 270 closing loop](../epilogue/multiscale.md#row-270-closing-loop) "
    "before row 272 atomistic meta prelude capstone reunion opens on the full capstone path."
)
NEW = (
    "then [epilogue row 270 closing loop](../epilogue/multiscale.md#row-270-closing-loop) "
    "before row 271 homogenization meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    if OLD in text:
        path.write_text(text.replace(OLD, NEW, 1))
        print("prologue: fixed row 270 stitch next-row hint")
    else:
        print("prologue: row 270 stitch hint already OK")


if __name__ == "__main__":
    main()
