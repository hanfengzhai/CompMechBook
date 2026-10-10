#!/usr/bin/env python3
"""Insert canonical row 269 closing loop at capstone anchor; remove orphan duplicates."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

ROW268_MARKER = (
    "### Row 268 closing loop (Row 68 → Row 248 Row 68 → Row 48 midpoint meta prelude capstone reunion) "
    "{#row-268-closing-loop}"
)

ORPHAN_HEADERS = (
    "### Row 269 closing loop (Row 68 → Row 269 Row 68 → Row 49 taxonomy meta prelude capstone reunion) "
    "{#row-269-closing-loop}",
    "### Row 269 closing loop (Row 68 → Row 249 Row 68 → Row 49 taxonomy meta prelude capstone reunion) "
    "{#row-269-closing-loop}",
)


def _canonical_row269_loop() -> str:
    spec = importlib.util.spec_from_file_location("a269", ROOT / "scripts/add-row-269.py")
    a269 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a269)
    ep = (ROOT / "writings/epilogue/chapters/multiscale.md").read_text()
    start = ep.index(
        "### Row 249 closing loop (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion) "
        "{#row-249-closing-loop}"
    )
    end = ep.index("\n\n### Row 250 closing loop", start)
    block249 = ep[start:end].strip()
    block269 = a269.t249_to_269(block249)
    block269 = block269.replace(
        "### Row 249 closing loop (Row 68 → Row 229",
        "### Row 269 closing loop (Row 68 → Row 249",
        1,
    )
    block269 = block269.replace("{#row-249-closing-loop}", "{#row-269-closing-loop}")
    for old, new in (
        ("prologue-preview-row-249", "prologue-preview-row-269"),
        ("row-249-closing-stitch", "row-269-closing-stitch"),
        ("skill-navigation-row-249", "skill-navigation-row-269"),
        (
            "row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249",
            "row68-row249-taxonomy-meta-prelude-capstone-reunion-index-row-269",
        ),
        (
            "row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion",
            "row-269-baby-picture-row68-row249-taxonomy-meta-prelude-capstone-reunion",
        ),
    ):
        block269 = block269.replace(old, new)
    return block269.strip() + "\n\n"


def main() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = path.read_text()
    canonical = _canonical_row269_loop()

    for orphan in ORPHAN_HEADERS:
        while orphan.split(" {#")[0] in epilogue:
            hdr = orphan.split(" {#")[0]
            idx = epilogue.find(hdr)
            nxt = epilogue.find("\n\n### Row ", idx + 20)
            if nxt == -1:
                nxt = len(epilogue)
            epilogue = epilogue[:idx] + epilogue[nxt + 2 :]
            print("epilogue: removed orphan row 269 block")

    if ROW268_MARKER not in epilogue:
        raise SystemExit("row 268 capstone marker missing")

    marker_end = epilogue.index(ROW268_MARKER) + len(ROW268_MARKER)
    section_end = epilogue.find("\n\n### Row 248 closing loop (Row 68 → Row 228", marker_end)
    if section_end == -1:
        section_end = epilogue.find("\n\n### Row 249 closing loop", marker_end)
    if section_end == -1:
        raise SystemExit("could not locate end of row 268 section")

    if canonical.strip() not in epilogue:
        epilogue = (
            epilogue[:marker_end]
            + "\n\n"
            + canonical
            + epilogue[marker_end:section_end]
            + epilogue[section_end:]
        )
        print("epilogue: inserted canonical row 269 at capstone anchor")
    else:
        print("epilogue: canonical row 269 already present")

    path.write_text(epilogue)


if __name__ == "__main__":
    main()
