#!/usr/bin/env python3
"""Add row 140 (Row 68 → Row 120 ↔ Row 60 Handshake 3 meta prelude capstone on capstone path)."""
from __future__ import annotations

import re
import sys
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


def lift_120_to_140(s: str) -> str:
    p = [
        ("Row 121 closing loop", "__ROW121_LOOP__"),
        ("Row 120 closing loop", "Row 140 closing loop"),
        ("row-120-closing-loop", "row-140-closing-loop"),
        ("Row 120 closing stitch", "Row 140 closing stitch"),
        ("row-120-closing-stitch", "row-140-closing-stitch"),
        ("prologue-preview-row-120", "prologue-preview-row-140"),
        ("Row 120 preview", "Row 140 preview"),
        ("Row 120 skill checkpoint", "Row 140 skill checkpoint"),
        ("skill-navigation-row-120", "skill-navigation-row-140"),
        ("memory sheet row 120", "memory sheet row 140"),
        ("Row 120 baby picture", "Row 140 baby picture"),
        ("Row 120 three-way audit", "Row 140 three-way audit"),
        (
            "Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            "Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        ),
        (
            "row68-row100-handshake3-meta-prelude-capstone-reunion-index-row-120",
            "row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140",
        ),
        (
            "row-120-baby-picture-row68-row100-handshake3-meta-prelude-capstone-reunion",
            "row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion",
        ),
        ("[row 139]", "__ROW139_REF__"),
        ("[row 119]", "[row 139]"),
        ("row 119", "row 139"),
        ("Row 119", "Row 139"),
        ("__ROW139_REF__", "[row 139]"),
        ("[row 100]", "[row 120]"),
        ("row 100", "row 120"),
        ("Row 100", "Row 120"),
        ("(row 120)", "(row 140)"),
        ("row 120", "row 140"),
        ("Row 120", "Row 140"),
        ("__ROW121_LOOP__", "Row 121 closing loop"),
        (
            "Handshake 3 meta capstone / Handshake 3 meta prelude hinge",
            "Handshake 3 meta capstone / Handshake 3 meta prelude hinge on the capstone path",
        ),
        (
            "after verified load-cell parsing on the capstone path**",
            "after verified load-cell parsing on the capstone path**",
        ),
        (
            "after verified load-cell parsing**",
            "after verified load-cell parsing on the capstone path**",
        ),
        (
            "at the Handshake 3 meta prelude capstone boundary inside the coupling gate",
            "at the Handshake 3 meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 60 reunion |", "Row 68 ↔ Row 60 reunion (capstone path) |"),
        (
            "[Row 68 → Row 80 Handshake 3 meta prelude reunion index (row 100)]",
            "[Row 68 → Row 100 Handshake 3 meta prelude capstone reunion index (row 120)]",
        ),
        (
            "row68-row80-handshake3-meta-prelude-reunion-index-row-100",
            "row68-row100-handshake3-meta-prelude-capstone-reunion-index-row-120",
        ),
        (
            "verified Handshake 3 meta capstone closure (row 119)",
            "verified Handshake 3 meta capstone closure (row 139)",
        ),
        (
            "Row 68 → Row 60 meta (row 120)",
            "Row 68 → Row 60 meta (row 140)",
        ),
        (
            "Row 68 → Row 60 meta (row 100)",
            "Row 68 → Row 60 meta (row 140)",
        ),
        (
            "before Handshake 4a opens in workflow time",
            "before Handshake 4a opens on the capstone path in workflow time",
        ),
        (
            "When row 120 is complete, proceed to [row 121]",
            "When row 140 is complete, proceed to [row 141](preface.md#skill-navigation-row-141) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 121](preface.md#skill-navigation-row-121) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 139](preface.md#skill-navigation-row-139) when Handshake 3 meta capstone still lags after verified DFT workflows meta capstone on the capstone path, to [row 60](preface.md#skill-navigation-row-60) when only Handshake 3 meta stalls, or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_120",
        ),
        (
            "Handshake 3 meta prelude capstone at the ascent-chain boundary in reading time",
            "Handshake 3 meta prelude capstone at the ascent-chain boundary in reading time on the capstone path",
        ),
        (
            "When row 60 feels like epilogue homework after row 119 alone",
            "When row 60 feels like epilogue homework after row 139 alone on the capstone path",
        ),
        (
            "When row 60 feels like epilogue homework after row 139 alone",
            "When row 60 feels like epilogue homework after row 139 alone on the capstone path",
        ),
        ("Recite [preface row 119]", "Recite [preface row 139]"),
        (
            "Do not conflate row 140 (row 68 ↔ row 60 reunion on the capstone path)",
            "Do not conflate row 140 (row 68 ↔ row 60 reunion on the capstone path)",
        ),
        (
            "Do not conflate row 120 (row 68 ↔ row 60 reunion on the capstone path)",
            "Do not conflate row 140 (row 68 ↔ row 60 reunion on the capstone path)",
        ),
        (
            "Do not conflate row 120 (row 68 ↔ row 60 reunion",
            "Do not conflate row 140 (row 68 ↔ row 60 reunion on the capstone path",
        ),
        (
            "row 120 names **why that reunion must follow verified Handshake 3 meta capstone (row 119)",
            "row 140 names **why that reunion must follow verified Handshake 3 meta capstone (row 139)",
        ),
        (
            "Proceed to [row 121](#row-121-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 120",
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 140 on the capstone path, to [row 121](#row-121-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 120 on the opening-hinge path",
        ),
        (
            "Proceed to [row 121](#row-121-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 119",
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 140 on the capstone path, to [row 121](#row-121-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 120 on the opening-hinge path, to [row 120](#row-120-closing-loop) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 139](#row-139-closing-loop) when Handshake 3 meta capstone still lags after row 138 on the capstone path, to [row 60](#row-60-closing-loop) when only Handshake 3 meta stalls",
        ),
        (
            "when opening [row 121](preface.md#skill-navigation-row-121) before row 60 closes",
            "when opening [row 141](preface.md#skill-navigation-row-141) before row 61 closes on the capstone path",
        ),
        (
            "when `alpha_export.yaml` is correct after row 119 but the cross-links audit was skipped",
            "when `alpha_export.yaml` is correct on the capstone path after row 139 but the cross-links audit was skipped",
        ),
        (
            "when row 119 closed but row 60",
            "when row 139 closed but row 60",
        ),
        (
            "When row 119 closed — Handshake 3 meta capstone verified, row 118 or row 99 recited",
            "When row 139 closed — Handshake 3 meta capstone verified, row 138 or row 119 recited on the capstone path",
        ),
        (
            "before row 121 Handshake 4a meta prelude capstone opens",
            "before row 61 Handshake 4a meta prelude opens on the capstone path",
        ),
        (
            "when row 119 and row 60 both verify individually",
            "when row 139 and row 60 both verify individually",
        ),
        (
            "when row 119 closed Handshake 3 meta capstone and row 68 closed the midpoint prelude but **row 60 Handshake 3 meta still opens",
            "when row 139 closed Handshake 3 meta capstone and row 68 closed the midpoint prelude but **row 60 Handshake 3 meta still opens",
        ),
        (
            "rear-view mirror of row 119's foundation archive → quasiharmonic",
            "rear-view mirror of row 139's foundation archive → quasiharmonic",
        ),
        (
            "rear-view mirror of row 119's quasiharmonic turn",
            "rear-view mirror of row 139's quasiharmonic turn",
        ),
        (
            "read row 68 gate + row 119 or row 100 Handshake 3 meta capstone / Handshake 3 meta prelude gate + epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) after verified DFT workflows meta capstone but Handshake 3 still feels disconnected from Parts III–VI",
            "read row 68 gate + row 139 or row 120 Handshake 3 meta capstone / Handshake 3 meta prelude gate + epilogue α cross-links + row 60 meta aloud when load cell parses at \\(T_w\\) on the capstone path after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI",
        ),
        (
            "before row 140 Handshake 3 meta prelude capstone or row 60 workflow reunion opens on the capstone path",
            "before row 141 Handshake 4a meta prelude capstone or row 61 workflow reunion opens on the capstone path",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_120" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_120.*", "", out, flags=re.S)
    return out


def fix_row_139_tail(preface: str) -> str:
    old = (
        "When row 139 is complete, proceed to [row 140](preface.md#skill-navigation-row-140) when load cell parses on the capstone path but Handshake 3 meta prelude still lags, to [row 120](preface.md#skill-navigation-row-120) when Handshake 3 meta capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) when the Handshake 3 meta prelude path (row 119) closed the chapter hinge without row 138 capstone, to [row 99](preface.md#skill-navigation-row-99) for the Row 68 ↔ Row 59 Handshake 3 opening prelude audit alone, to [row 79](preface.md#skill-navigation-row-79) for the Row 68 ↔ Row 59 prelude audit alone, to [row 138](preface.md#skill-navigation-row-138) when DFT workflows meta capstone still lags after verified Kohn–Sham meta capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 139 is complete, proceed to [row 140](preface.md#skill-navigation-row-140) when load cell parses on the capstone path but Handshake 3 meta prelude still lags, to [row 120](preface.md#skill-navigation-row-120) when Handshake 3 meta capstone is clean but Handshake 3 meta prelude still lags on the opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit alone, to [row 119](preface.md#skill-navigation-row-119) for the Row 68 ↔ Row 59 Handshake 3 meta audit on the opening-hinge path alone, to [row 138](preface.md#skill-navigation-row-138) when DFT workflows meta capstone still lags after verified Kohn–Sham meta capstone on the capstone path, to [row 59](preface.md#skill-navigation-row-59) when only IX.3 → Handshake 3 stalls, or extend prose only under `writings/` then sync."
    )
    if old in preface:
        preface = preface.replace(old, new)
    return preface


def fix_row_139_baby(mem: str) -> str:
    return mem.replace(
        "before row 120 Handshake 3 meta prelude capstone opens**",
        "before row 140 Handshake 3 meta prelude capstone opens on the capstone path**",
    )


def add_row_140() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    preface = fix_row_139_tail(preface)
    if "skill-navigation-row-140" in preface and "### Row 140 skill checkpoint" in preface:
        print("preface: row 140 already present")
    else:
        m120 = re.search(
            r"(### Row 120 skill checkpoint.*?)(?=\n### Row 121 skill checkpoint)",
            preface,
            re.S,
        )
        if not m120:
            raise SystemExit("row 120 preface checkpoint missing")
        row140 = lift_120_to_140(m120.group(1))
        anchor = "\n## The copper wire through the book"
        preface = preface.replace(anchor, "\n" + row140 + anchor)
        preface_path.write_text(preface)
        print("preface: added row 140")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-140-closing-loop" not in ep:
        block120 = extract_between(ep, "### Row 120 closing loop", "### Row 121 closing loop")
        block140 = lift_120_to_140(block120)
        ep = ep.replace("### Row 121 closing loop", block140 + "### Row 121 closing loop", 1)
        ep = ep.replace(
            "Proceed to [row 140](#row-140-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 139 on the capstone path, to [row 120](#row-120-closing-loop) when load cell parses at \\(T_w\\) after verified Handshake 3 meta capstone but Handshake 3 still feels disconnected from Parts III–VI on the opening-hinge path",
            "Proceed to [row 140](#row-140-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 139 on the capstone path, to [row 120](#row-120-closing-loop) when row 68 closed but Handshake 3 meta prelude still lags after row 119 on the opening-hinge path, to [row 139](#row-139-closing-loop) when Handshake 3 meta capstone still lags after row 138 on the capstone path",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 140 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 140) |"
    )
    if compass_line not in pro:
        line120 = (
            "| Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 120) |"
        )
        idx120 = pro.find(line120)
        if idx120 < 0:
            raise SystemExit("prologue compass row 120 not found")
        line_end120 = pro.find("\n", idx120)
        compass140 = lift_120_to_140(pro[idx120:line_end120]) + "\n"
        line139 = (
            "| Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone reunion (row 139) |"
        )
        idx139 = pro.find(line139)
        if idx139 < 0:
            raise SystemExit("prologue compass row 139 not found")
        line_end139 = pro.find("\n", idx139)
        pro = pro[: line_end139 + 1] + compass140 + pro[line_end139 + 1 :]
        preview120 = extract_between(
            pro,
            '| <span id="prologue-preview-row-120"></span>',
            '\n| <span id="prologue-preview-row-121">',
        )
        preview140 = lift_120_to_140(preview120)
        pro = pro.replace(
            '| <span id="prologue-preview-row-120"></span>',
            preview140 + '| <span id="prologue-preview-row-120"></span>',
            1,
        )
        if "row-140-closing-stitch" not in pro:
            stitch = (
                "**Row 140 closing stitch (Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion).** {#row-140-closing-stitch} "
                "When row 139 closed — Handshake 3 meta capstone verified, row 138 or row 119 recited on the capstone path, and [`parse_alpha.sh`](../../scripts/parse_alpha.sh) archived `alpha_export.yaml` at \\(T_w\\) — but **row 60 Handshake 3 meta reunion still opens like standalone epilogue coursework after the load-cell chapter hinge on the capstone path** — "
                "the [preface row 140 When-to-pause opening sentence](../preface.md#skill-navigation-row-140) names the dual reunion before Handshake 4a meta prelude reunion; read [preface row 140](../preface.md#skill-navigation-row-140), then the "
                "[Row 68 → Row 120 reunion index](../appendix/sources.md#row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140), then "
                "[epilogue row 140 closing loop](../epilogue/multiscale.md#row-140-closing-loop) before row 61 Handshake 4a meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 121 closing stitch", stitch + "**Row 121 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 140 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140" not in src:
        idx120 = src.find(
            "## Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 120)"
        )
        idx121 = src.find(
            "## Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 121)"
        )
        if idx120 < 0 or idx121 < 0:
            raise SystemExit("row 120/121 sources anchors missing")
        block = src[idx120:idx121]
        block140 = lift_120_to_140(block)
        table_row = (
            "| 140 | Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone (midpoint prelude gate ↔ Handshake 3 meta capstone ↔ row 60 meta) | "
            "[Row 68 → Row 120 Handshake 3 meta prelude capstone reunion index](#row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140) · "
            "[preface row 140](../preface.md#skill-navigation-row-140) · "
            "[prologue row 140 preview](../prologue/00-many-scales.md#prologue-preview-row-140) · "
            "[prologue row 140 closing stitch](../prologue/00-many-scales.md#row-140-closing-stitch) · "
            "[epilogue row 140 closing loop](../epilogue/multiscale.md#row-140-closing-loop) · "
            "[memory sheet row 140 baby picture](memory-sheet.md#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 60 Handshake 3 meta reunion still feels disconnected from verified Handshake 3 meta capstone on the capstone path** — "
            "read row 68 + row 139 or row 120 gate + epilogue α cross-links + row 60; "
            "[preface row 60](../preface.md#skill-navigation-row-60) |\n"
        )
        src = src.replace(
            "| 139 | Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone",
            table_row + "| 139 | Row 68 → Row 119 Row 68 → Row 59 Handshake 3 meta capstone",
        )
        src = src.replace(
            "## Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 120)",
            block140 + "## Row 68 → Row 100 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion index (row 120)",
        )
        extra = (
            "[row 140](#row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140) reunites **Handshake 3 meta capstone with the Handshake 3 meta prelude capstone boundary** "
            "when row 139 closed Handshake 3 meta capstone at verified `alpha_export.yaml` on the capstone path but epilogue α cross-links and Parts III–VI still read like separate courses after verified Handshake 3 meta prelude meta;"
        )
        if extra not in src:
            src = src.replace(
                "when row 138 closed DFT workflows meta capstone at verified foundation archive on the capstone path but `foundation_export.yaml` and IX.3 → Handshake 3 opening hinge still read like separate courses after verified Handshake 3 meta prelude meta;",
                "when row 138 closed DFT workflows meta capstone at verified foundation archive on the capstone path but `foundation_export.yaml` and IX.3 → Handshake 3 opening hinge still read like separate courses after verified Handshake 3 meta prelude meta; "
                + extra,
            )
        src_path.write_text(src)
        print("sources: added row 140 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    mem = fix_row_139_baby(mem)
    if "row-140-baby-picture" not in mem:
        baby120 = extract_between(mem, "### Row 120 baby picture", "### Row 121 baby picture")
        baby140 = lift_120_to_140(baby120)
        mem = mem.replace("### Act VI baby picture", baby140 + "### Act VI baby picture", 1)
        mem_table = (
            "| 140 | Meta | Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion | "
            "[Row 68 → Row 120 Handshake 3 meta prelude capstone reunion index](sources.md#row68-row120-handshake3-meta-prelude-capstone-reunion-index-row-140) · "
            "[preface row 140 skill checkpoint](../preface.md#skill-navigation-row-140) · "
            "[prologue row 140 preview](../prologue/00-many-scales.md#prologue-preview-row-140) · "
            "[prologue row 140 closing stitch](../prologue/00-many-scales.md#row-140-closing-stitch) · "
            "[epilogue row 140 closing loop](../epilogue/multiscale.md#row-140-closing-loop) | "
            "Row 68 closed but row 60 Handshake 3 meta reunion feels disconnected from verified Handshake 3 meta capstone on the capstone path — "
            "read row 68 + row 139 or row 120 gate + epilogue α cross-links + row 60; "
            "[row 140 baby picture](#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "[row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion) |\n| 93 | Meta |",
            "[row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion) |\n" + mem_table + "| 93 | Meta |",
        )
        if "When row 139 closed but Handshake 3 meta prelude reunion still lags" not in mem:
            mem = mem.replace(
                "When row 138 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 139](#row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion).",
                "When row 138 closed but Handshake 3 meta reunion still lags on the capstone path, switch to [row 139](#row-139-baby-picture-row68-row119-handshake3-meta-capstone-reunion). When row 139 closed but Handshake 3 meta prelude reunion still lags on the capstone path, switch to [row 140](#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 140")
    else:
        mem_path.write_text(mem)
        print("memory-sheet: row 140 baby already present")


def main() -> None:
    add_row_140()


if __name__ == "__main__":
    main()
