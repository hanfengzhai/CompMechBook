#!/usr/bin/env python3
"""Add row 144 (Row 68 → Row 124 ↔ Row 64 book-loop meta prelude capstone on capstone path)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tx(s: str, pairs: list[tuple[str, str]]) -> str:
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found: {start[:80]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:40]}")
    return text[i:j]


def lift_124_to_144(s: str) -> str:
    p = [
        ("Row 125 closing loop", "__ROW125_LOOP__"),
        ("Row 124 closing loop", "Row 144 closing loop"),
        ("row-125-closing-loop", "__ROW125_LOOP_ANCHOR__"),
        ("row-124-closing-loop", "row-144-closing-loop"),
        ("Row 125 closing stitch", "__ROW125_STITCH__"),
        ("Row 124 closing stitch", "Row 144 closing stitch"),
        ("row-125-closing-stitch", "__ROW125_STITCH_ANCHOR__"),
        ("row-124-closing-stitch", "row-144-closing-stitch"),
        ("prologue-preview-row-125", "__ROW125_PREVIEW__"),
        ("prologue-preview-row-124", "prologue-preview-row-144"),
        ("Row 125 preview", "__ROW125_PREVIEW_TEXT__"),
        ("Row 124 preview", "Row 144 preview"),
        ("Row 125 skill checkpoint", "__ROW125_SKILL__"),
        ("Row 124 skill checkpoint", "Row 144 skill checkpoint"),
        ("skill-navigation-row-125", "__ROW125_SKILL_NAV__"),
        ("skill-navigation-row-124", "skill-navigation-row-144"),
        ("memory sheet row 125", "__ROW125_MEM__"),
        ("memory sheet row 124", "memory sheet row 144"),
        ("Row 125 baby picture", "__ROW125_BABY__"),
        ("Row 124 baby picture", "Row 144 baby picture"),
        ("Row 125 three-way audit", "__ROW125_AUDIT__"),
        ("Row 124 three-way audit", "Row 144 three-way audit"),
        (
            "Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone",
            "Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone",
        ),
        (
            "row68-row104-book-loop-meta-prelude-capstone-reunion-index-row-124",
            "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144",
        ),
        (
            "row-124-baby-picture-row68-row104-book-loop-meta-prelude-capstone-reunion",
            "row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion",
        ),
        ("[row 125]", "__ROW125_REF__"),
        ("[row 105]", "[row 125]"),
        ("row 105", "row 125"),
        ("Row 105", "Row 125"),
        ("__ROW125_REF__", "[row 125]"),
        ("[row 124]", "__ROW124_REF__"),
        ("[row 104]", "[row 124]"),
        ("row 104", "row 124"),
        ("Row 104", "Row 124"),
        ("__ROW124_REF__", "[row 124]"),
        ("[row 123]", "__ROW123_REF__"),
        ("[row 103]", "[row 123]"),
        ("row 103", "row 123"),
        ("Row 103", "Row 123"),
        ("__ROW123_REF__", "[row 123]"),
        ("[row 122]", "[row 142]"),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
        ("(row 124)", "(row 144)"),
        ("__ROW125_LOOP__", "Row 125 closing loop"),
        ("__ROW125_LOOP_ANCHOR__", "row-125-closing-loop"),
        ("__ROW125_STITCH__", "Row 125 closing stitch"),
        ("__ROW125_STITCH_ANCHOR__", "row-125-closing-stitch"),
        ("__ROW125_PREVIEW__", "prologue-preview-row-125"),
        ("__ROW125_PREVIEW_TEXT__", "Row 125 preview"),
        ("__ROW125_SKILL__", "Row 125 skill checkpoint"),
        ("__ROW125_SKILL_NAV__", "skill-navigation-row-125"),
        ("__ROW125_MEM__", "memory sheet row 125"),
        ("__ROW125_BABY__", "Row 125 baby picture"),
        ("__ROW125_AUDIT__", "Row 125 three-way audit"),
        (
            "orchestration meta prelude capstone / book-loop meta prelude hinge",
            "orchestration meta prelude capstone / book-loop meta prelude hinge on the capstone path",
        ),
        (
            "at the book-loop meta prelude capstone boundary inside the coupling gate",
            "at the book-loop meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 64 reunion |", "Row 68 ↔ Row 64 reunion (capstone path) |"),
        (
            "[Row 68 → Row 84 book-loop meta prelude reunion index (row 104)]",
            "[Row 68 → Row 124 book-loop meta prelude capstone reunion index (row 144)]",
        ),
        (
            "row68-row84-book-loop-meta-prelude-reunion-index-row-104",
            "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144",
        ),
        (
            "verified orchestration meta prelude capstone closure (row 123)",
            "verified orchestration meta prelude capstone closure (row 143)",
        ),
        (
            "Row 68 → Row 64 meta (row 124)",
            "Row 68 → Row 64 meta (row 144)",
        ),
        (
            "before row 45 second pass opens in workflow time",
            "before row 45 second pass opens on the capstone path in workflow time",
        ),
        (
            "When row 124 is complete, proceed to [row 125]",
            "When row 144 is complete, proceed to [row 145](preface.md#skill-navigation-row-145) when row 68 closed but second-pass meta prelude still lags on the capstone path, "
            "to [row 125](preface.md#skill-navigation-row-125) when book-loop meta prelude capstone is clean but second-pass meta prelude still lags on the opening-hinge path, "
            "to [row 105](preface.md#skill-navigation-row-105) for the Row 68 ↔ Row 65 second-pass meta prelude audit alone, "
            "to [row 104](preface.md#skill-navigation-row-104) for the Row 68 ↔ Row 64 book-loop meta prelude audit on the opening-hinge path alone, "
            "to [row 143](preface.md#skill-navigation-row-143) when orchestration meta prelude capstone still lags after verified Handshake 4b meta prelude capstone on the capstone path, "
            "to [row 84](preface.md#skill-navigation-row-84) for the Row 68 ↔ Row 64 opening prelude audit alone, "
            "to [row 64](preface.md#skill-navigation-row-64) when only book-loop meta stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_124",
        ),
        (
            "book-loop meta prelude capstone at the epilogue → prologue boundary in reading time",
            "book-loop meta prelude capstone at the epilogue → prologue boundary in reading time on the capstone path",
        ),
        (
            "When row 64 feels like epilogue homework after row 123 alone",
            "When row 64 feels like epilogue homework after row 143 alone on the capstone path",
        ),
        (
            "When row 64 feels like epilogue homework after row 143 alone",
            "When row 64 feels like epilogue homework after row 143 alone on the capstone path",
        ),
        ("Recite [preface row 123]", "Recite [preface row 143]"),
        (
            "Proceed to [row 125](#row-125-closing-loop) when row 68 closed but second-pass meta still feels disconnected after row 124",
            "Proceed to [row 145](#row-145-closing-loop) when row 68 closed but second-pass meta prelude still lags after row 144 on the capstone path, "
            "to [row 125](#row-125-closing-loop) when row 68 closed but second-pass meta still feels disconnected after row 124 on the opening-hinge path",
        ),
        (
            "when opening [row 125](preface.md#skill-navigation-row-125) before row 64 closes",
            "when opening [row 145](preface.md#skill-navigation-row-145) before row 65 closes on the capstone path",
        ),
        (
            "when `multiscale_export.yaml` exists after row 123 but the next terminal still opens with copper decks copied blindly",
            "when `multiscale_export.yaml` exists on the capstone path after row 143 but the next terminal still opens with copper decks copied blindly",
        ),
        (
            "when row 123 closed but row 64 book-loop meta still feels like epilogue homework",
            "when row 143 closed but row 64 book-loop meta still feels like epilogue homework",
        ),
        (
            "when row 123 and row 64 both verify individually",
            "when row 143 and row 64 both verify individually",
        ),
        (
            "rear-view mirror of row 123's orchestration meta → H1→OUT",
            "rear-view mirror of row 143's orchestration meta → H1→OUT",
        ),
        (
            "read row 68 gate + row 123 or row 104 orchestration meta prelude capstone / book-loop meta prelude gate + epilogue book-loop cross-links + row 64 meta aloud when orchestration verifies after orchestration meta prelude capstone but the next terminal opens with copper decks copied blindly without reopening anchor rung audit",
            "read row 68 gate + row 143 or row 124 orchestration meta prelude capstone / book-loop meta prelude gate + epilogue book-loop cross-links + row 64 meta aloud when orchestration verifies on the capstone path after orchestration meta prelude capstone but the next terminal opens with copper decks copied blindly without reopening anchor rung audit",
        ),
        (
            "before row 125 second-pass meta prelude capstone or row 65 workflow reunion opens on the capstone path",
            "before row 145 second-pass meta prelude capstone or row 65 workflow reunion opens on the capstone path",
        ),
        (
            "before row 125 second-pass meta prelude capstone opens",
            "before row 65 second-pass meta prelude opens on the capstone path",
        ),
        (
            "Confirm [row 123](preface.md#skill-navigation-row-123) or [Row 68 → Row 84 book-loop meta prelude reunion index (row 104)]",
            "Confirm [row 143](preface.md#skill-navigation-row-143) or [Row 68 → Row 124 book-loop meta prelude capstone reunion index (row 144)]",
        ),
        (
            "Row 124 does not replace row 68, row 64, row 123, row 104",
            "Row 144 does not replace row 68, row 64, row 143, row 124",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_124" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_124.*", "", out, flags=re.S)
    return out


def add_row_144() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-144" in preface and "### Row 144 skill checkpoint" in preface:
        print("preface: row 144 already present")
    else:
        m124 = re.search(
            r"(### Row 124 skill checkpoint.*?)(?=\n### Row 125 skill checkpoint)",
            preface,
            re.S,
        )
        if not m124:
            raise SystemExit("row 124 preface checkpoint missing")
        row144 = lift_124_to_144(m124.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row144 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 144")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-144-closing-loop" not in ep:
        block124 = extract_between(ep, "### Row 124 closing loop", "### Row 125 closing loop")
        block144 = lift_124_to_144(block124)
        ep = ep.replace("### Row 124 closing loop", block144 + "### Row 124 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 144 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 144) |"
    )
    if compass_line not in pro:
        line143 = (
            "| Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone reunion (row 143) |"
        )
        idx143 = pro.find(line143)
        if idx143 < 0:
            raise SystemExit("prologue compass row 143 not found")
        line_end143 = pro.find("\n", idx143)
        line124 = (
            "| Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion (row 124) |"
        )
        idx124 = pro.find(line124)
        if idx124 < 0:
            raise SystemExit("prologue compass row 124 not found")
        line_end124 = pro.find("\n", idx124)
        compass144 = lift_124_to_144(pro[idx124:line_end124]) + "\n"
        pro = pro[: line_end143 + 1] + compass144 + pro[line_end143 + 1 :]
        preview124 = extract_between(
            pro,
            '| <span id="prologue-preview-row-124"></span>',
            '\n| <span id="prologue-preview-row-125">',
        )
        preview144 = lift_124_to_144(preview124)
        pro = pro.replace(
            '| <span id="prologue-preview-row-124"></span>',
            preview144 + '| <span id="prologue-preview-row-124"></span>',
            1,
        )
        if "row-144-closing-stitch" not in pro:
            stitch = (
                "**Row 144 closing stitch (Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion).** {#row-144-closing-stitch} "
                "When row 143 closed — orchestration meta prelude capstone verified, row 142 or row 123 recited on the capstone path, and "
                "[`parse_multiscale_workflow.sh`](../../scripts/parse_multiscale_workflow.sh) archived `multiscale_export.yaml` with H1→H2→H3→H4a→H4b→OUT after verified Handshake 4b meta prelude capstone — "
                "but **row 64 book-loop meta reunion still opens like standalone epilogue coursework after the book-loop opening prelude chapter hinge on the capstone path** — "
                "the [preface row 144 When-to-pause opening sentence](../preface.md#skill-navigation-row-144) names the dual reunion before second-pass meta prelude reunion; "
                "read [preface row 144](../preface.md#skill-navigation-row-144), then the "
                "[Row 68 → Row 124 reunion index](../appendix/sources.md#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144), then "
                "[epilogue row 144 closing loop](../epilogue/multiscale.md#row-144-closing-loop) before row 65 second-pass meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 124 closing stitch", stitch + "**Row 124 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 144 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144" not in src:
        idx124 = src.find(
            "## Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 124)"
        )
        idx125 = src.find(
            "## Row 68 → Row 105 Row 68 → Row 65 second-pass meta prelude capstone reunion index (row 125)"
        )
        if idx124 < 0 or idx125 < 0:
            raise SystemExit("row 124/125 sources anchors missing")
        block = src[idx124:idx125]
        block144 = lift_124_to_144(block)
        table_row = (
            "| 144 | Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone (midpoint prelude gate ↔ orchestration meta prelude capstone ↔ row 64 meta) | "
            "[Row 68 → Row 124 book-loop meta prelude capstone reunion index](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144) · "
            "[preface row 144](../preface.md#skill-navigation-row-144) · "
            "[prologue row 144 preview](../prologue/00-many-scales.md#prologue-preview-row-144) · "
            "[prologue row 144 closing stitch](../prologue/00-many-scales.md#row-144-closing-stitch) · "
            "[epilogue row 144 closing loop](../epilogue/multiscale.md#row-144-closing-loop) · "
            "[memory sheet row 144 baby picture](memory-sheet.md#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 64 book-loop meta reunion still feels disconnected from verified orchestration meta prelude capstone on the capstone path** — "
            "read row 68 + row 143 or row 124 gate + epilogue book-loop cross-links + row 64; "
            "[preface row 64](../preface.md#skill-navigation-row-64) |\n"
        )
        src = src.replace(
            "| 143 | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone",
            table_row + "| 143 | Row 68 → Row 123 Row 68 → Row 63 orchestration meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 124)",
            block144
            + "## Row 68 → Row 104 Row 68 → Row 64 book-loop meta prelude capstone reunion index (row 124)",
        )
        extra = (
            "[row 144](#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144) reunites **orchestration meta prelude capstone with the book-loop meta prelude capstone boundary** "
            "when row 143 closed orchestration meta prelude capstone at verified H1→OUT on the capstone path but epilogue book-loop cross-links and row 12 still read like separate courses after verified book-loop meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 143](#row68-row123-orchestration-meta-prelude-capstone-reunion-index-row-143) reunites **Handshake 4b meta prelude capstone with the orchestration meta prelude capstone boundary** "
                "when row 142 closed Handshake 4b meta prelude capstone at verified notch-root stress on the capstone path but epilogue orchestration cross-links and row 16 still read like separate courses after verified orchestration meta prelude meta;"
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 144 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-144-baby-picture" not in mem:
        baby124 = extract_between(mem, "### Row 124 baby picture", "### Row 125 baby picture")
        baby144 = lift_124_to_144(baby124)
        mem = mem.replace("### Row 125 baby picture", baby144 + "### Row 125 baby picture", 1)
        mem_table = (
            "| 144 | Meta | Row 68 → Row 124 Row 68 → Row 64 book-loop meta prelude capstone reunion | "
            "[Row 68 → Row 124 book-loop meta prelude capstone reunion index](sources.md#row68-row124-book-loop-meta-prelude-capstone-reunion-index-row-144) · "
            "[preface row 144 skill checkpoint](../preface.md#skill-navigation-row-144) · "
            "[prologue row 144 preview](../prologue/00-many-scales.md#prologue-preview-row-144) · "
            "[prologue row 144 closing stitch](../prologue/00-many-scales.md#row-144-closing-stitch) · "
            "[epilogue row 144 closing loop](../epilogue/multiscale.md#row-144-closing-loop) | "
            "Row 68 closed but row 64 book-loop meta reunion feels disconnected from verified orchestration meta prelude capstone on the capstone path — "
            "read row 68 + row 143 or row 124 gate + epilogue book-loop cross-links + row 64; "
            "[row 144 baby picture](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 124 | Meta | [Row 68 → Row 104 book-loop meta prelude capstone reunion index]",
            mem_table + "| 124 | Meta | [Row 68 → Row 104 book-loop meta prelude capstone reunion index]",
        )
        if "When row 143 closed but book-loop meta prelude reunion still lags" not in mem:
            mem = mem.replace(
                "When row 142 closed but orchestration meta prelude reunion still lags on the capstone path, switch to [row 143](#row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion).",
                "When row 142 closed but orchestration meta prelude reunion still lags on the capstone path, switch to [row 143](#row-143-baby-picture-row68-row123-orchestration-meta-prelude-capstone-reunion). "
                "When row 143 closed but book-loop meta prelude reunion still lags on the capstone path, switch to [row 144](#row-144-baby-picture-row68-row124-book-loop-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 144")
    else:
        print("memory-sheet: row 144 baby already present")


def main() -> None:
    add_row_144()


if __name__ == "__main__":
    main()
