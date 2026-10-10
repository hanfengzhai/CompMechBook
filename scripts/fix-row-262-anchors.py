#!/usr/bin/env python3
"""Repair row 262 meta-stitch anchors after add-row-262 bump."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROW262_COMPASS = (
    "| Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 262) | "
    "[Preface: row 262 skill checkpoint](../preface.md#skill-navigation-row-262) · "
    "[Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index]"
    "(../appendix/sources.md#row68-row242-handshake4b-meta-prelude-capstone-reunion-index-row-262) · "
    "[memory sheet row 262 baby picture](../appendix/memory-sheet.md#row-262-baby-picture-row68-row242-handshake4b-meta-prelude-capstone-reunion) · "
    "[prologue row 262 preview row](#prologue-preview-row-262); "
    "[prologue row 262 closing stitch](#row-262-closing-stitch); "
    "[epilogue row 262 closing loop](../epilogue/multiscale.md#row-262-closing-loop) — "
    "read row 68 gate + row 261 or row 242 Handshake 4a meta prelude capstone / Handshake 4b meta capstone gate + "
    "epilogue FE² cross-links + row 62 meta aloud when bulk hardening matches flow stress after verified Handshake 4a "
    "meta prelude capstone on the full capstone path but Handshake 4b still feels disconnected from Part VII Step 4 |"
)

ROW262_STITCH = (
    "**Row 262 closing stitch (Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** "
    "{#row-262-closing-stitch} When row 261 closed — Handshake 4a meta prelude capstone verified, row 261 or row 242 "
    "recited on the full capstone path, and [`parse_fe2.sh`](../../scripts/parse_fe2.sh) archived `fe2_export.yaml` "
    "when uplift exceeds 10% after verified Handshake 4a meta prelude capstone on the full capstone path — but "
    "**row 62 Handshake 4b meta reunion still opens like standalone epilogue coursework after verified bulk hardening "
    "parsing on the full capstone path** — read [preface row 262](../preface.md#skill-navigation-row-262), then the "
    "[Row 68 → Row 242 reunion index]"
    "(../appendix/sources.md#row68-row242-handshake4b-meta-prelude-capstone-reunion-index-row-262), then "
    "[epilogue row 262 closing loop](../epilogue/multiscale.md#row-262-closing-loop) before row 263 orchestration meta "
    "prelude capstone reunion opens on the full capstone path.\n\n"
)

ROW262_MEMORY_TABLE = (
    "| 262 | Meta | [Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index]"
    "(sources.md#row68-row242-handshake4b-meta-prelude-capstone-reunion-index-row-262) · "
    "[preface row 262 skill checkpoint](../preface.md#skill-navigation-row-262) · "
    "[prologue row 262 preview](../prologue/00-many-scales.md#prologue-preview-row-262) · "
    "[prologue row 262 closing stitch](../prologue/00-many-scales.md#row-262-closing-stitch) · "
    "[epilogue row 262 closing loop](../epilogue/multiscale.md#row-262-closing-loop) | "
    "Row 68 closed but row 62 Handshake 4b meta reunion feels disconnected from verified Handshake 4a meta prelude "
    "capstone on the full capstone path — read row 68 + row 261 or row 242 gate + epilogue FE² cross-links + row 62; "
    "[row 262 baby picture](#row-262-baby-picture-row68-row242-handshake4b-meta-prelude-capstone-reunion) |\n"
)

ROW262_BABY = """
### Row 262 baby picture {#row-262-baby-picture-row68-row242-handshake4b-meta-prelude-capstone-reunion}

**Row 262 baby picture:** when row 68 closed the midpoint prelude and row 261 or row 242 closed Handshake 4a meta prelude capstone / Handshake 4b meta capstone on the full capstone path but **row 62's epilogue FE² cross-links audit or the IV.4 → VII.3 Step 4 → IX.3 GSF chain still feel like separate checklists**, open the [Row 68 → Row 242 Handshake 4b meta prelude capstone reunion index](sources.md#row68-row242-handshake4b-meta-prelude-capstone-reunion-index-row-262) — read [preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 261](../preface.md#skill-navigation-row-261) or [preface row 242](../preface.md#skill-navigation-row-242) Handshake 4a meta prelude capstone / Handshake 4b meta capstone gate → [epilogue FE² cross-links audit](../epilogue/multiscale.md#opening-hinge-vii3-handshake4b) aloud → [preface row 62](../preface.md#skill-navigation-row-62) five-step audit → confirm [`fe2_export.yaml`](../fixtures/cu.foundation/fe2_export.yaml) beside [`rate_export.yaml`](../fixtures/cu.foundation/rate_export.yaml) on the full capstone path.

```mermaid
flowchart LR
  MP[Midpoint row 68]
  HS[Handshake 4a meta prelude row 261]
  XL[Epilogue FE² cross-links]
  R62[row 62 meta gate]
  MP --> HS --> XL --> R62
```

When row 262 feels disconnected from row 261, read them as **Handshake 4a vs Handshake 4b meta prelude capstones on the full capstone path**: row 261 when **epilogue rate cross-links must reunite on verified Handshake 4a meta prelude capstone before any hardening knee on the full capstone path**; row 262 when **epilogue FE² cross-links and Row 61 → Row 42 Handshake 4b meta must read on the same wire before row 263 orchestration meta prelude capstone reunion opens on the full capstone path** — same copper wire, same Functional Analysis Notes layout, one continuous bulk hardening → notch localization afternoon after verified Handshake 4b meta prelude capstone. When row 261 closed but Part VII Step 4 still lags on the full capstone path, switch to [row 262](#row-262-baby-picture-row68-row242-handshake4b-meta-prelude-capstone-reunion).


"""


def fix_prologue(prologue: str) -> str:
    broken_prefix = "| Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 262) |"
    idx = prologue.find(broken_prefix)
    if idx == -1:
        raise SystemExit("prologue row 262 compass not found")
    line_end = prologue.find("\n", idx)
    prologue = prologue[:idx] + ROW262_COMPASS + prologue[line_end:]

    bad_stitch = (
        "**Row 261 closing stitch (Row 68 → Row 241 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** "
        "{#row-262-closing-stitch}"
    )
    if bad_stitch in prologue:
        prologue = prologue.replace(bad_stitch, ROW262_STITCH.strip(), 1)
    elif "{#row-262-closing-stitch}" not in prologue:
        anchor = (
            "**Row 261 closing stitch (Row 68 → Row 241 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** "
            "{#row-261-closing-stitch}"
        )
        if anchor not in prologue:
            raise SystemExit("row 261 stitch anchor not found")
        prologue = prologue.replace(anchor, ROW262_STITCH + anchor, 1)

    chunk_start = prologue.find('prologue-preview-row-262')
    if chunk_start != -1:
        chunk = prologue[chunk_start : chunk_start + 2800]
        fixed = (
            chunk.replace("skill-navigation-row-222", "skill-navigation-row-262")
            .replace("#row-222-closing-stitch", "#row-262-closing-stitch")
            .replace(
                "row68-row202-handshake4b-meta-prelude-capstone-reunion-index-row-222",
                "row68-row242-handshake4b-meta-prelude-capstone-reunion-index-row-262",
            )
            .replace("preface row 242 skill checkpoint", "preface row 262 skill checkpoint")
        )
        prologue = prologue[:chunk_start] + fixed + prologue[chunk_start + 2800 :]

    return prologue


def fix_epilogue(epilogue: str) -> str:
    marker = "{#row-262-closing-loop}"
    pos = epilogue.find(marker)
    if pos == -1:
        raise SystemExit("row 262 closing loop anchor not found")
    start = epilogue.rfind("\n### ", 0, pos)
    end = epilogue.find("\n\n\n\n", pos)
    if end == -1:
        end = epilogue.find("\n\n### Row 221 closing loop", pos)
    if end == -1:
        end = epilogue.find("\n\n### Row 261 closing loop", pos)
    if end == -1:
        raise SystemExit("row 262 closing loop end not found")

    template_start = epilogue.find("{#row-261-closing-loop}")
    if template_start == -1:
        raise SystemExit("row 261 template loop not found")
    t_start = epilogue.rfind("\n### ", 0, template_start)
    t_end = epilogue.find("\n\n\n\n", template_start)
    if t_end == -1:
        t_end = epilogue.find("\n\n### Row 260 closing loop", template_start)
    template = epilogue[t_start:t_end]

    section = template
    section = section.replace(
        "### Row 261 closing loop (Row 68 → Row 261 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion)",
        "### Row 262 closing loop (Row 68 → Row 242 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion)",
        1,
    )
    section = section.replace("{#row-261-closing-loop}", "{#row-262-closing-loop}")
    section = section.replace("memory sheet row 261", "memory sheet row 262", 1)
    section = section.replace("skill-navigation-row-261", "skill-navigation-row-262")
    section = section.replace("prologue-preview-row-261", "prologue-preview-row-262")
    section = section.replace("row-261-closing-stitch", "row-262-closing-stitch")
    section = section.replace(
        "row68-row261-handshake4a-meta-prelude-capstone-reunion-index-row-261",
        "row68-row242-handshake4b-meta-prelude-capstone-reunion-index-row-262",
    )
    section = section.replace("Handshake 4a", "Handshake 4b")
    section = section.replace("handshake4a", "handshake4b")
    section = section.replace("row 61", "row 62")
    section = section.replace("Row 61", "Row 62")
    section = section.replace("row 261", "row 262")
    section = section.replace("Row 261", "Row 262")
    section = section.replace("row 260", "row 261")
    section = section.replace("Row 260", "Row 261")
    section = section.replace("row 241", "row 242")
    section = section.replace("Row 241", "Row 242")
    section = section.replace("rate_export.yaml", "fe2_notch_comparison.dat")
    section = section.replace("rate extrapolation cross-links", "FE² notch-localization cross-links")
    section = section.replace("opening-hinge-vii3-handshake4a", "opening-hinge-vii3-handshake4b")
    section = section.replace(
        "Handshake 4a worked example](#4a--ddd-strain-rate-to-quasi-static-load-cell-act-iv--hardening)",
        "Handshake 4b worked example](#worked-example-fe-at-the-wire-notch-act-v--notch)",
    )
    section = section.replace("parse_rate.sh", "parse_fe2.sh")
    section = section.replace(
        "row-261-baby-picture-row68-row261-handshake4b-meta-prelude-capstone-reunion",
        "row-262-baby-picture-row68-row242-handshake4b-meta-prelude-capstone-reunion",
    )
    section = section.replace(
        "Act III → Act IV afternoon before Handshake 4b opens",
        "Act IV → Act V afternoon before row 16 orchestration opens",
    )
    section = section.replace(
        "Proceed to [row 262](#row-262-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 261",
        "Proceed to [row 263](#row-263-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 262",
        1,
    )

    return epilogue[:start] + section + epilogue[end:]


def fix_memory(memory: str) -> str:
    if "| 262 | Meta |" not in memory:
        needle = "| 261 | Meta | [Row 68 → Row 241 Handshake 4a meta prelude capstone reunion index]"
        if needle not in memory:
            raise SystemExit("memory row 261 table not found")
        memory = memory.replace(needle, ROW262_MEMORY_TABLE + needle, 1)

    if "{#row-262-baby-picture-row68-row242-handshake4b-meta-prelude-capstone-reunion}" not in memory:
        anchor = "### Row 261 baby picture {#row-261-baby-picture-row68-row241-handshake4a-meta-prelude-capstone-reunion}"
        if anchor not in memory:
            raise SystemExit("memory row 261 baby anchor not found")
        memory = memory.replace(anchor, ROW262_BABY + anchor, 1)
    return memory


def main() -> None:
    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = fix_prologue(prologue_path.read_text())
    prologue_path.write_text(prologue)
    print("prologue: fixed row 262 anchors")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = fix_epilogue(epilogue_path.read_text())
    epilogue_path.write_text(epilogue)
    print("epilogue: fixed row 262 closing loop")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = fix_memory(memory_path.read_text())
    memory_path.write_text(memory)
    print("memory-sheet: fixed row 262")


if __name__ == "__main__":
    main()
