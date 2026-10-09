#!/usr/bin/env python3
"""Repair row 261 meta-stitch anchors after add-row-261 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW261_COMPASS = (
    "| Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 261) | "
    "[Preface: row 261 skill checkpoint](../preface.md#skill-navigation-row-261) · "
    "[Row 68 → Row 261 Handshake 4a meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261) · "
    "[memory sheet row 261 baby picture](../appendix/memory-sheet.md#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion) · "
    "[prologue row 261 preview row](#prologue-preview-row-261); "
    "[prologue row 261 closing stitch](#row-261-closing-stitch); "
    "[epilogue row 261 closing loop](../epilogue/multiscale.md#row-261-closing-loop) — "
    "read row 68 gate + row 260 or row 241 Handshake 3 meta prelude capstone / Handshake 4a meta capstone gate + "
    "epilogue rate cross-links + row 61 meta aloud when bulk hardening parses at lab grip rate after verified "
    "Handshake 4a meta prelude capstone on the full capstone path but Handshake 4a still feels disconnected from Part VII |"
)

ROW261_STITCH = (
    "**Row 261 closing stitch (Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** "
    "{#row-261-closing-stitch} When row 260 closed — Handshake 3 meta prelude capstone verified, row 260 or row 241 "
    "recited on the full capstone path, and [`parse_rate.sh`](../../scripts/parse_rate.sh) archived `rate_export.yaml` "
    "with `lab_target_strain_rate_s-1: 1.0e-3` after verified Handshake 4a meta prelude capstone — but **row 61 "
    "Handshake 4a meta reunion still opens like standalone epilogue coursework after the hardening chapter hinge on "
    "the full capstone path** — read [preface row 261](../preface.md#skill-navigation-row-261), then the "
    "[Row 68 → Row 261 reunion index](../appendix/sources.md#row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261), "
    "then [epilogue row 261 closing loop](../epilogue/multiscale.md#row-261-closing-loop) before row 262 Handshake 4b "
    "meta prelude capstone reunion opens on the full capstone path.\n\n"
)

ROW261_MEMORY_TABLE = (
    "| 261 | Meta | [Row 68 → Row 241 Handshake 4a meta prelude capstone reunion index]"
    "(sources.md#row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261) · "
    "[preface row 261 skill checkpoint](../preface.md#skill-navigation-row-261) · "
    "[prologue row 261 preview](../prologue/00-many-scales.md#prologue-preview-row-261) · "
    "[prologue row 261 closing stitch](../prologue/00-many-scales.md#row-261-closing-stitch) · "
    "[epilogue row 261 closing loop](../epilogue/multiscale.md#row-261-closing-loop) | "
    "Row 68 closed but row 61 Handshake 4a meta reunion feels disconnected from verified Handshake 4a meta prelude "
    "capstone on the full capstone path — read row 68 + row 260 or row 241 gate + epilogue rate cross-links + row 61; "
    "[row 261 baby picture](#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion) |\n"
)

ROW261_BABY = """
### Row 261 baby picture {#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion}

**Row 261 baby picture:** when row 68 closed the midpoint prelude and row 260 or row 241 closed Handshake 3 meta prelude capstone / Handshake 4a meta capstone on the full capstone path but **row 61's epilogue rate cross-links audit or the VI.4 → VII.3 → IX.0 descent chain still feel like separate checklists**, open the [Row 68 → Row 261 Handshake 4a meta prelude capstone reunion index](sources.md#row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261) — read [preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 260](../preface.md#skill-navigation-row-260) or [preface row 241](../preface.md#skill-navigation-row-241) Handshake 3 meta prelude capstone / Handshake 4a meta capstone gate → [epilogue rate cross-links audit](../epilogue/multiscale.md#opening-hinge-vii3-handshake4a) aloud → [preface row 61](../preface.md#skill-navigation-row-61) five-step audit → confirm [VII.3 rate handshake](../part07-defects/03-polycrystal-and-fem-handoff.md#scale-boundary-handshake-ddd-strain-rate-to-quasi-static-fem) and [`parse_rate.sh`](../scripts/parse_rate.sh) at lab grip rate on the full capstone path.

```mermaid
flowchart LR
  MP[Midpoint row 68]
  HS[Handshake 4a meta prelude row 260]
  XL[Epilogue rate cross-links]
  R61[row 61 meta gate]
  MP --> HS --> XL --> R61
```

When row 261 feels disconnected from row 260, read them as **Handshake 3 meta prelude capstone vs Handshake 4a meta prelude capstones on the full capstone path**: row 260 when **epilogue α cross-links must reunite on verified Handshake 3 meta prelude capstone before any rate table on the full capstone path**; row 261 when **epilogue rate cross-links and Row 60 → Row 41 Handshake 4a meta must read on the same wire before row 262 Handshake 4b meta prelude capstone reunion opens on the full capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous thermal pre-stress → Act III–IV afternoon after verified Handshake 4a meta prelude capstone. When row 260 closed but Part VII still lags on the full capstone path, switch to [row 261](#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion).


"""


def fix_prologue(prologue: str) -> str:
    if ROW261_COMPASS in prologue:
        pass
    else:
        broken_prefix = (
            "| Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 261) |"
        )
        idx = prologue.find(broken_prefix)
        if idx == -1:
            raise SystemExit("prologue row 261 compass not found")
        line_end = prologue.find("\n", idx)
        prologue = prologue[:idx] + ROW261_COMPASS + prologue[line_end:]

    if "{#row-261-closing-stitch}" not in prologue:
        anchor = (
            "**Row 260 closing stitch (Row 68 → Row 240 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** "
            "{#row-260-closing-stitch}"
        )
        if anchor not in prologue:
            raise SystemExit("row 260 stitch anchor not found")
        prologue = prologue.replace(anchor, ROW261_STITCH + anchor, 1)

    prologue = prologue.replace(
        '<span id="prologue-preview-row-260"></span>Row 261 preview',
        '<span id="prologue-preview-row-261"></span>Row 261 preview',
        1,
    )
    chunk_start = prologue.find("prologue-preview-row-261")
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 2500]
        fixed = (
            chunk.replace("skill-navigation-row-241", "skill-navigation-row-261")
            .replace("#row-241-closing-stitch", "#row-261-closing-stitch")
            .replace(
                "row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241",
                "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261",
            )
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 2500 :]
    return prologue


def fix_epilogue(epilogue: str) -> str:
    marker = "{#row-261-closing-loop}"
    pos = epilogue.find(marker)
    if pos == -1:
        raise SystemExit("row 261 closing loop anchor not found")
    start = epilogue.rfind("\n### ", 0, pos)
    end = epilogue.find("\n\n\n\n", pos)
    if end == -1:
        end = epilogue.find("\n\n### Row 260 closing loop", pos)
    if end == -1:
        raise SystemExit("row 261 closing loop end not found")
    section = epilogue[start:end]
    section = section.replace(
        "### Row 241 closing loop (Row 68 → Row 261 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
        "### Row 261 closing loop (Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
        1,
    )
    section = section.replace("memory sheet row 241", "memory sheet row 261")
    section = section.replace("prologue row 241 preview", "prologue row 261 preview")
    section = section.replace("prologue row 241 closing stitch", "prologue row 261 closing stitch")
    section = section.replace("[Preface row 241]", "[Preface row 261]")
    section = section.replace("([row 241]", "([row 261]")
    section = section.replace("row 240 closed Handshake 4a", "row 260 closed Handshake 3 meta prelude capstone")
    section = section.replace("closure (row 240)", "closure (row 260)")
    section = section.replace("after row 240 alone", "after row 260 alone")
    section = section.replace("memory sheet row 241 baby", "memory sheet row 261 baby")
    section = section.replace("Do not conflate row 241 (row 68 ↔ row 61 reunion on the full capstone path) with row 241 (opening-hinge capstone stitch alone) — row 241 names **Row 68 → Row 221", "Do not conflate row 261 (row 68 ↔ row 61 reunion on the full capstone path) with row 241 (opening-hinge capstone stitch alone) — row 241 names **Row 68 → Row 221")
    section = section.replace("; row 241 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 240)", "; row 261 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 260)")
    section = section.replace("after row 241 on the full capstone path", "after row 261 on the full capstone path")
    section = section.replace("skill-navigation-row-241", "skill-navigation-row-261")
    section = section.replace("prologue-preview-row-241", "prologue-preview-row-261")
    section = section.replace("row-241-closing-stitch", "row-261-closing-stitch")
    section = section.replace(
        "row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241",
        "row68-row241-handshake4a-meta-prelude-capstone-reunion-index-row-261",
    )
    section = section.replace(
        "#row-241-baby-picture-row68-row221-handshake4a-meta-prelude-capstone-reunion",
        "#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion",
    )
    section = section.replace(
        "Row 241 closes the **Handshake 4a meta prelude capstone",
        "Row 261 closes the **Handshake 4a meta prelude capstone",
        1,
    )
    section = section.replace(
        "Row 68 → Row 61 meta (row 241) must read",
        "Row 68 → Row 61 meta (row 61) must read",
        1,
    )
    return epilogue[:start] + section + epilogue[end:]


def fix_memory(memory: str) -> str:
    bad261 = "| 261 | Meta | [Row 68 → Row 261 Handshake 4a meta prelude capstone reunion index](sources.md#row68-row221-handshake4a-meta-prelude-capstone-reunion-index-row-241)"
    if bad261 in memory:
        end = memory.find("\n", memory.index(bad261))
        memory = memory[: memory.index(bad261)] + ROW261_MEMORY_TABLE.rstrip() + memory[end:]
    elif "| 261 | Meta |" not in memory:
        needle = "| 260 | Meta | [Row 68 → Row 240 Handshake 3 meta prelude capstone reunion index]"
        if needle not in memory:
            raise SystemExit("memory row 260 table not found")
        memory = memory.replace(needle, ROW261_MEMORY_TABLE + needle, 1)

    if "{#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion}" not in memory:
        anchor = "### Row 260 baby picture {#row-260-baby-picture-row68-row240-handshake3-meta-prelude-capstone-reunion}"
        if anchor not in memory:
            raise SystemExit("memory row 260 baby anchor not found")
        memory = memory.replace(anchor, ROW261_BABY + anchor, 1)
    memory = memory.replace(
        "before row 241 Handshake 4a meta prelude capstone reunion opens on the full capstone path",
        "before row 261 Handshake 4a meta prelude capstone reunion opens on the full capstone path",
    )
    return memory


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 261 anchors")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = fix_epilogue(epilogue_path.read_text())
    epilogue_path.write_text(epilogue)
    print("epilogue: fixed row 261 closing loop")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = fix_memory(memory_path.read_text())
    memory_path.write_text(memory)
    print("memory-sheet: fixed row 261")


if __name__ == "__main__":
    main()
