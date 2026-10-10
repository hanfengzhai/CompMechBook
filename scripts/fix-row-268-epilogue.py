#!/usr/bin/env python3
"""Insert canonical row 268 closing loop at capstone anchor; remove orphan duplicates."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

ROW267_MARKER = (
    "### Row 247 closing loop (Row 68 → Row 247 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-267-closing-loop}"
)

ORPHAN_HEADER = (
    "### Row 268 closing loop (Row 68 → Row 268 Row 68 → Row 48 midpoint meta prelude capstone reunion) "
    "{#row-268-closing-loop}"
)


def _canonical_row268_loop() -> str:
    spec = importlib.util.spec_from_file_location("a268", ROOT / "scripts/add-row-268.py")
    a268 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a268)
    ep = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    start = ep.index(
        "### Row 248 closing loop (Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion) "
        "{#row-248-closing-loop}"
    )
    end = ep.index("\n\n### Row 249 closing loop", start)
    block248 = ep[start:end].strip()
    block268 = a268.bump248_to_268(block248)
    block268 = block268.replace(
        "### Row 248 closing loop (Row 68 → Row 228",
        "### Row 268 closing loop (Row 68 → Row 248",
        1,
    )
    block268 = block268.replace("{#row-248-closing-loop}", "{#row-268-closing-loop}")
    block268 = block268.replace(
        "row-248-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion",
        "row-268-baby-picture-row68-row248-midpoint-meta-prelude-capstone-reunion",
    )
    block268 = block268.replace(
        "row68-row228-midpoint-meta-prelude-capstone-reunion-index-row-248",
        "row68-row248-midpoint-meta-prelude-capstone-reunion-index-row-268",
    )
    for old, new in (
        ("prologue-preview-row-248", "prologue-preview-row-268"),
        ("row-248-closing-stitch", "row-268-closing-stitch"),
        ("skill-navigation-row-248", "skill-navigation-row-268"),
    ):
        block268 = block268.replace(old, new)
    return block268.strip() + "\n\n"


def main() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = path.read_text()
    canonical = _canonical_row268_loop()

    # Remove misplaced orphan row-268 blocks (wrong header Row 68 → Row 268)
    while ORPHAN_HEADER in epilogue:
        idx = epilogue.index(ORPHAN_HEADER)
        nxt = epilogue.find("\n\n### Row ", idx + 20)
        if nxt == -1:
            nxt = len(epilogue)
        epilogue = epilogue[:idx] + epilogue[nxt + 2 :]
        print("epilogue: removed orphan row 268 block")

    if ROW267_MARKER not in epilogue:
        raise SystemExit("row 267 capstone marker missing")

    marker_end = epilogue.index(ROW267_MARKER) + len(ROW267_MARKER)
    section_end = epilogue.find("\n\n### Row 247 closing loop (Row 68 → Row 227", marker_end)
    if section_end == -1:
        section_end = epilogue.find("\n\n### Row 248 closing loop", marker_end)
    if section_end == -1:
        raise SystemExit("could not locate end of row 267 section")

    row267_tail = epilogue[marker_end:section_end]
    if canonical.strip() not in epilogue:
        epilogue = (
            epilogue[:section_end]
            + "\n\n"
            + canonical
            + epilogue[section_end:]
        )
        print("epilogue: inserted canonical row 268 after row 267")

    epilogue = epilogue.replace(
        "Proceed to [row 268](#row-248-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 267",
        "Proceed to [row 268](#row-268-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 267",
    )

    path.write_text(epilogue)


if __name__ == "__main__":
    main()
