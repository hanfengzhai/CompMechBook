#!/usr/bin/env python3
"""Repair row 157 prologue compass/preview/stitch after add-row-157."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    needle156 = (
        "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |"
    )
    needle157 = (
        "| Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 157) |"
    )
    text = re.sub(
        rf"({re.escape(needle156)}[^\n]*\n)(?:{re.escape(needle157)}[^\n]*\n)+",
        r"\1",
        text,
        count=1,
    )
    if needle157 not in text and needle156 in text:
        idx = text.find(needle156)
        line_end = text.find("\n", idx)
        # Re-lift from row 137 compass line if present
        line137 = "| Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion (row 137) |"
        idx137 = text.find(line137)
        if idx137 >= 0:
            import runpy

            ns = runpy.run_path(str(ROOT / "scripts/add-row-157.py"))
            le = text.find("\n", idx137)
            new_line = ns["lift_137_to_157"](text[idx137:le]) + "\n"
            text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    if "prologue-preview-row-157" not in text:
        anchor = '| <span id="prologue-preview-row-156"></span>'
        idx = text.find(anchor)
        if idx >= 0:
            line_end = text.find("\n", idx)
            preview = (
                '| <span id="prologue-preview-row-157"></span>Row 157 preview (Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion) | '
                "Explain why midpoint closure (row 68) and IX.1 → IX.2 meta (row 57) must be read together with the Bridge → Kohn–Sham SCF chain after verified Born–Oppenheimer meta prelude capstone on the full capstone path before cutoff sweeps feel like a separate course | "
                'One sentence: "read row 68 gate + row 156 or row 137 Born–Oppenheimer meta prelude capstone / Kohn–Sham opening gate + IX.1 Bridge → opening hinge → IX.2 Kohn–Sham SCF + row 57 meta aloud when Murnaghan fits are clean on the full capstone path but Kohn–Sham SCF still feels like standalone quantum chemistry after verified Born–Oppenheimer meta prelude capstone" — '
                "[preface row 157 skill checkpoint](../preface.md#skill-navigation-row-157); "
                "[prologue row 157 closing stitch](#row-157-closing-stitch); "
                "[Row 68 → Row 137 reunion index](../appendix/sources.md#row68-row137-kohn-sham-meta-prelude-capstone-reunion-index-row-157); "
                "[memory sheet row 157 baby picture](../appendix/memory-sheet.md#row-157-baby-picture-row68-row137-kohn-sham-meta-prelude-capstone-reunion) |"
            )
            text = text[: line_end + 1] + preview + "\n" + text[line_end + 1 :]
    path.write_text(text)
    print("prologue row 157 repaired")


if __name__ == "__main__":
    main()
