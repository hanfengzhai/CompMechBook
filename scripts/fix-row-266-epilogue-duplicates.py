#!/usr/bin/env python3
"""Remove duplicate row 266 / mis-tagged row 246 epilogue closing loops; keep canonical row 266 block."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CANONICAL_HEADER = (
    "### Row 266 closing loop (Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) "
    "{#row-266-closing-loop}"
)

BAD_BLOCK_START = "### Row 246 closing loop (Row 68 → Row 246 Row 68 → Row 66 Writings canonical meta prelude capstone reunion) {#row-266-closing-loop}"


def main() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = path.read_text()
    if BAD_BLOCK_START in epilogue:
        start = epilogue.index(BAD_BLOCK_START)
        end = epilogue.find("\n\n### Row 266 closing loop", start + 10)
        if end != -1:
            epilogue = epilogue[:start] + epilogue[end + 2 :]
            print("epilogue: removed mis-tagged row 246 block")

    # Drop duplicate row 266 sections (keep first canonical)
    first = epilogue.find(CANONICAL_HEADER)
    if first != -1:
        second = epilogue.find(CANONICAL_HEADER, first + len(CANONICAL_HEADER))
        while second != -1:
            third = epilogue.find("\n\n### Row ", second + 10)
            if third == -1:
                third = len(epilogue)
            bad = epilogue[second:third]
            if "Row 68 → Row 266 Row 68" in bad or "Row 68 → Row 226 Row 68" in bad:
                epilogue = epilogue[:second] + epilogue[third:]
                print("epilogue: removed duplicate row 266 variant")
            else:
                break
            second = epilogue.find(CANONICAL_HEADER, first + len(CANONICAL_HEADER))

    path.write_text(epilogue)


if __name__ == "__main__":
    main()
