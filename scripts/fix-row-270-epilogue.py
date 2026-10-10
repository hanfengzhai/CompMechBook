#!/usr/bin/env python3
"""Insert canonical row 270 closing loop at capstone anchor; remove orphan duplicates."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

ROW269_MARKER = (
    "### Row 269 closing loop (Row 68 → Row 249 Row 68 → Row 49 taxonomy meta prelude capstone reunion) "
    "{#row-269-closing-loop}"
)

ORPHAN_HEADERS = (
    "### Row 270 closing loop (Row 68 → Row 270 Row 68 → Row 50 DDD meta prelude capstone reunion) "
    "{#row-270-closing-loop}",
    "### Row 270 closing loop (Row 68 → Row 250 Row 68 → Row 50 DDD meta prelude capstone reunion) "
    "{#row-270-closing-loop}",
)


def _canonical_row270_loop() -> str:
    spec = importlib.util.spec_from_file_location("a270", ROOT / "scripts/add-row-270.py")
    a270 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a270)
    ep = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    start = ep.index(
        "### Row 250 closing loop (Row 68 → Row 230 Row 68 → Row 50 DDD meta prelude capstone reunion) "
        "{#row-250-closing-loop}"
    )
    end = ep.index("\n\n### Row 251 closing loop", start)
    block250 = ep[start:end].strip()
    block270 = a270.t250_to_270(block250)
    block270 = block270.replace(
        "### Row 250 closing loop (Row 68 → Row 230",
        "### Row 270 closing loop (Row 68 → Row 250",
        1,
    )
    block270 = block270.replace("{#row-250-closing-loop}", "{#row-270-closing-loop}")
    for old, new in (
        ("prologue-preview-row-250", "prologue-preview-row-270"),
        ("row-250-closing-stitch", "row-270-closing-stitch"),
        ("skill-navigation-row-250", "skill-navigation-row-270"),
        (
            "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
            "row68-row250-ddd-meta-prelude-capstone-reunion-index-row-270",
        ),
        (
            "row-250-baby-picture-row68-row230-ddd-meta-prelude-capstone-reunion",
            "row-270-baby-picture-row68-row250-ddd-meta-prelude-capstone-reunion",
        ),
    ):
        block270 = block270.replace(old, new)
    return block270.strip() + "\n\n"


def main() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = path.read_text()
    canonical = _canonical_row270_loop()

    for orphan in ORPHAN_HEADERS:
        hdr = orphan.split(" {#")[0]
        while hdr in epilogue:
            idx = epilogue.find(hdr)
            nxt = epilogue.find("\n\n### Row ", idx + 20)
            if nxt == -1:
                nxt = len(epilogue)
            epilogue = epilogue[:idx] + epilogue[nxt + 2 :]
            print("epilogue: removed orphan row 270 block")

    if ROW269_MARKER not in epilogue:
        raise SystemExit("row 269 capstone marker missing")

    marker_end = epilogue.index(ROW269_MARKER) + len(ROW269_MARKER)
    section_end = epilogue.find("\n\n### Row 248 closing loop (Row 68 → Row 228", marker_end)
    if section_end == -1:
        section_end = epilogue.find("\n\n### Row 250 closing loop", marker_end)
    if section_end == -1:
        raise SystemExit("could not locate end of row 269 section")

    if canonical.strip() not in epilogue:
        epilogue = (
            epilogue[:marker_end]
            + "\n\n"
            + canonical
            + epilogue[marker_end:section_end]
            + epilogue[section_end:]
        )
        print("epilogue: inserted canonical row 270 at capstone anchor")
    else:
        print("epilogue: canonical row 270 already present")

    path.write_text(epilogue)


if __name__ == "__main__":
    main()
