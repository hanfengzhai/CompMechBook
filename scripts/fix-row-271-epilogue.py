#!/usr/bin/env python3
"""Insert canonical row 271 closing loop at capstone anchor; remove orphan duplicates."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

ROW270_MARKER = (
    "### Row 270 closing loop (Row 68 → Row 250 Row 68 → Row 50 DDD meta prelude capstone reunion) "
    "{#row-270-closing-loop}"
)

ORPHAN_HEADERS = (
    "### Row 271 closing loop (Row 68 → Row 271 Row 68 → Row 51 homogenization meta prelude capstone reunion) "
    "{#row-271-closing-loop}",
    "### Row 251 closing loop (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion) "
    "{#row-271-closing-loop}",
)


def _canonical_row271_loop() -> str:
    spec = importlib.util.spec_from_file_location("a271", ROOT / "scripts/add-row-271.py")
    a271 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a271)
    return a271._build_blocks()["epilogue_loop"].strip() + "\n\n"


def main() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = path.read_text()
    canonical = _canonical_row271_loop()

    for orphan in ORPHAN_HEADERS:
        hdr = orphan.split(" {#")[0]
        while hdr in epilogue:
            idx = epilogue.find(hdr)
            nxt = epilogue.find("\n\n### Row ", idx + 20)
            if nxt == -1:
                nxt = len(epilogue)
            epilogue = epilogue[:idx] + epilogue[nxt + 2 :]
            print("epilogue: removed orphan row 271 block")

    if ROW270_MARKER not in epilogue:
        raise SystemExit("row 270 capstone marker missing")

    marker_end = epilogue.index(ROW270_MARKER) + len(ROW270_MARKER)
    section_end = epilogue.find("\n\n### Row 250 closing loop (Row 68 → Row 230", marker_end)
    if section_end == -1:
        section_end = epilogue.find("\n\n### Row 251 closing loop", marker_end)
    if section_end == -1:
        raise SystemExit("could not locate end of row 270 section")

    hdr271 = (
        "### Row 271 closing loop (Row 68 → Row 251 Row 68 → Row 51 homogenization meta prelude capstone reunion)"
    )
    while hdr271 in epilogue:
        idx = epilogue.index(hdr271)
        nxt = epilogue.find("\n\nThis subsection is the **downstream half** of [memory sheet row 270]", idx)
        if nxt == -1:
            nxt = epilogue.find("\n\n### Row 270 closing loop", idx + 10)
        if nxt == -1:
            nxt = epilogue.find("\n\n### Row ", idx + 10)
        if nxt == -1:
            raise SystemExit("could not trim row 271 section")
        epilogue = epilogue[:idx] + epilogue[nxt + 2 :]
        print("epilogue: removed row 271 section for reinsert")

    epilogue = (
        epilogue[:marker_end]
        + "\n\n"
        + canonical
        + epilogue[marker_end:]
    )
    print("epilogue: inserted canonical row 271 at capstone anchor")

    path.write_text(epilogue)


if __name__ == "__main__":
    main()
