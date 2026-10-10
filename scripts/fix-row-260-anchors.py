#!/usr/bin/env python3
"""Repair row 260 meta-stitch anchors after add-row-260 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW260_COMPASS = (
    "| Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 260) | "
    "[Preface: row 260 skill checkpoint](../preface.md#skill-navigation-row-260) · "
    "[Row 68 → Row 260 Handshake 3 meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260) · "
    "[memory sheet row 260 baby picture](../appendix/memory-sheet.md#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion) · "
    "[prologue row 260 preview row](#prologue-preview-row-260); "
    "[prologue row 260 closing stitch](#row-260-closing-stitch); "
    "[epilogue row 260 closing loop](../epilogue/multiscale.md#row-260-closing-loop) — "
    "read row 68 gate + row 259 or row 240 Handshake 3 meta prelude capstone / Handshake 3 meta capstone gate + "
    "epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) after verified Handshake 3 meta "
    "prelude capstone on the full capstone path but Handshake 3 still feels disconnected from Parts III–VI |"
)

ROW260_STITCH = (
    "**Row 260 closing stitch (Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** "
    "{#row-260-closing-stitch} When row 259 closed — Handshake 3 meta prelude capstone verified, row 259 or row 240 "
    "recited on the full capstone path, and [`parse_alpha.sh`](../../scripts/parse_alpha.sh) archived `alpha_export.yaml` "
    "matching [`fixtures/cht_export.yaml`](../../fixtures/cht_export.yaml) at \\(T_w = 311.48\\,\\text{K}\\) after verified "
    "Handshake 3 meta prelude capstone — but **row 60 Handshake 3 meta reunion still opens like standalone epilogue "
    "coursework after the load-cell chapter hinge on the full capstone path** — read [preface row 260]"
    "(../preface.md#skill-navigation-row-260), then the [Row 68 → Row 260 reunion index]"
    "(../appendix/sources.md#row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260), then "
    "[epilogue row 260 closing loop](../epilogue/multiscale.md#row-260-closing-loop) before row 261 Handshake 4a meta "
    "prelude capstone reunion opens on the full capstone path.\n\n"
)

ROW260_MEMORY_TABLE = (
    "| 260 | Meta | [Row 68 → Row 240 Handshake 3 meta prelude capstone reunion index]"
    "(sources.md#row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260) · "
    "[preface row 260 skill checkpoint](../preface.md#skill-navigation-row-260) · "
    "[prologue row 260 preview](../prologue/00-many-scales.md#prologue-preview-row-260) · "
    "[prologue row 260 closing stitch](../prologue/00-many-scales.md#row-260-closing-stitch) · "
    "[epilogue row 260 closing loop](../epilogue/multiscale.md#row-260-closing-loop) | "
    "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected from verified Handshake 3 meta prelude "
    "capstone on the full capstone path — read row 68 + row 259 or row 240 gate + epilogue α cross-links + row 60; "
    "[row 260 baby picture](#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion) |\n"
)

ROW260_BABY = """
### Row 260 baby picture {#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion}

**Row 260 baby picture:** when row 68 closed the midpoint prelude and row 259 or row 240 closed Handshake 3 meta prelude capstone / Handshake 3 meta capstone on the full capstone path but **row 60's epilogue α cross-links audit or the III.4 → IV.4 → V.4 → VI.2 ascent chain still feel like separate checklists**, open the [Row 68 → Row 260 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260) — read [preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 259](../preface.md#skill-navigation-row-259) or [preface row 240](../preface.md#skill-navigation-row-240) Handshake 3 meta prelude capstone / meta capstone gate → [epilogue α cross-links audit](../epilogue/multiscale.md#opening-hinge-ix3-handshake3) aloud → [preface row 60](../preface.md#skill-navigation-row-60) five-step audit → confirm [V.4 Picard CHT Lab act](../part05-fvm/04-navier-stokes-cfd.md#lab-act-extension-two-domain-picard-loop-with-a-1d-fem-solid) and [VI.2 \\(\\alpha\\) handshake](../part06-continuum/02-stress-balance.md#scale-boundary-handshake-thermal-expansion-alpha) at \\(T_w\\) on the full capstone path.

```mermaid
flowchart LR
  MP[Midpoint row 68]
  HS[Handshake 3 meta prelude row 259]
  XL[Epilogue α cross-links]
  R60[row 60 meta gate]
  MP --> HS --> XL --> R60
```

When row 260 feels disconnected from row 259, read them as **Handshake 3 opening vs Handshake 3 meta prelude capstones on the full capstone path**: row 259 when **IX.3 → Handshake 3 must reunite on foundation archive at \\(T_w\\) before any cross-links table on the full capstone path**; row 260 when **epilogue α cross-links and Row 59 → Row 40 Handshake 3 meta must read on the same wire before row 261 Handshake 4a meta prelude capstone reunion opens on the full capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous \\(\\alpha(T_w)\\) → Act II–III afternoon after verified Handshake 3 meta prelude capstone. When row 259 closed but Parts III–VI still lag on the full capstone path, switch to [row 260](#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion).


"""


def fix_prologue(prologue: str) -> str:
    broken_prefix = "| Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 260) |"
    idx = prologue.find(broken_prefix)
    if idx == -1:
        raise SystemExit("prologue row 260 compass not found")
    line_end = prologue.find("\n", idx)
    prologue = prologue[:idx] + ROW260_COMPASS + prologue[line_end:]

    if "{#row-260-closing-stitch}" not in prologue:
        anchor = "**Row 259 closing stitch (Row 68 → Row 259 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion).** {#row-259-closing-stitch}"
        if anchor not in prologue:
            raise SystemExit("row 259 stitch anchor not found")
        prologue = prologue.replace(anchor, ROW260_STITCH + anchor, 1)

    prologue = prologue.replace(
        '<span id="prologue-preview-row-240"></span>Row 260 preview',
        '<span id="prologue-preview-row-260"></span>Row 260 preview',
        1,
    )
    # Fix preview table links for row 260 only (first occurrence after row 260 span)
    chunk_start = prologue.find('prologue-preview-row-260')
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 2500]
        fixed = (
            chunk.replace("skill-navigation-row-240", "skill-navigation-row-260")
            .replace("#row-240-closing-stitch", "#row-260-closing-stitch")
            .replace(
                "row68-row240-handshake3-meta-prelude-capstone-reunion-index-row-260",
                "row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260",
            )
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 2500 :]

    prologue = prologue.replace(
        "before row 240 Handshake 3 meta prelude capstone opens on the full capstone path.",
        "before row 260 Handshake 3 meta prelude capstone reunion opens on the full capstone path.",
        1,
    )
    return prologue


def fix_epilogue(epilogue: str) -> str:
    marker = "{#row-260-closing-loop}"
    pos = epilogue.find(marker)
    if pos == -1:
        raise SystemExit("row 260 closing loop anchor not found")
    start = epilogue.rfind("\n### ", 0, pos)
    end = epilogue.find("\n\n\n\n", pos)
    if end == -1:
        end = epilogue.find("\n\n### Row 259 closing loop", pos)
    if end == -1:
        raise SystemExit("row 260 closing loop end not found")
    section = epilogue[start:end]
    section = section.replace(
        "### Row 240 closing loop (Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
        "### Row 260 closing loop (Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion)",
        1,
    )
    section = section.replace("skill-navigation-row-240", "skill-navigation-row-260")
    section = section.replace("prologue-preview-row-240", "prologue-preview-row-260")
    section = section.replace("row-240-closing-stitch", "row-260-closing-stitch")
    section = section.replace(
        "row68-row240-handshake3-meta-prelude-capstone-reunion-index-row-260",
        "row68-row260-handshake3-meta-prelude-capstone-reunion-index-row-260",
    )
    section = section.replace(
        "#row-240-baby-picture-row68-row220-handshake3-meta-prelude-capstone-reunion",
        "#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion",
    )
    section = section.replace(
        "Row 240 closes the **Handshake 3 meta prelude capstone",
        "Row 260 closes the **Handshake 3 meta prelude capstone",
        1,
    )
    section = section.replace(
        "Row 68 → Row 60 meta (row 240) must read",
        "Row 68 → Row 60 meta (row 60) must read",
        1,
    )
    return epilogue[:start] + section + epilogue[end:]


def fix_memory(memory: str) -> str:
    if "| 260 | Meta |" not in memory:
        needle = "| 259 | Meta | [Row 68 → Row 239 Handshake 3 meta prelude capstone reunion index]"
        if needle not in memory:
            raise SystemExit("memory row 259 table not found")
        memory = memory.replace(needle, ROW260_MEMORY_TABLE + needle, 1)

    if "{#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion}" not in memory:
        anchor = "### Row 259 baby picture {#row-259-baby-picture-row68-row239-handshake3-meta-prelude-capstone-reunion}"
        if anchor not in memory:
            raise SystemExit("memory row 259 baby anchor not found")
        memory = memory.replace(anchor, ROW260_BABY + anchor, 1)
    return memory


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 260 anchors")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = fix_epilogue(epilogue_path.read_text())
    epilogue_path.write_text(epilogue)
    print("epilogue: fixed row 260 closing loop")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = fix_memory(memory_path.read_text())
    memory_path.write_text(memory)
    print("memory-sheet: fixed row 260")


if __name__ == "__main__":
    main()
