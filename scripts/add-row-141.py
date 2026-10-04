#!/usr/bin/env python3
"""Add row 141 (Row 68 → Row 121 ↔ Row 61 Handshake 4a meta prelude capstone on capstone path)."""
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


def lift_121_to_141(s: str) -> str:
    p = [
        ("Row 122 closing loop", "__ROW122_LOOP__"),
        ("Row 121 closing loop", "Row 141 closing loop"),
        ("row-121-closing-loop", "row-141-closing-loop"),
        ("Row 121 closing stitch", "Row 141 closing stitch"),
        ("row-121-closing-stitch", "row-141-closing-stitch"),
        ("prologue-preview-row-121", "prologue-preview-row-141"),
        ("Row 121 preview", "Row 141 preview"),
        ("Row 121 skill checkpoint", "Row 141 skill checkpoint"),
        ("skill-navigation-row-121", "skill-navigation-row-141"),
        ("memory sheet row 121", "memory sheet row 141"),
        ("Row 121 baby picture", "Row 141 baby picture"),
        ("Row 121 three-way audit", "Row 141 three-way audit"),
        (
            "Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            "Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        ),
        (
            "row68-row101-handshake4a-meta-prelude-capstone-reunion-index-row-121",
            "row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141",
        ),
        (
            "row-121-baby-picture-row68-row101-handshake4a-meta-prelude-capstone-reunion",
            "row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion",
        ),
        ("[row 122]", "__ROW122_REF__"),
        ("[row 102]", "[row 122]"),
        ("row 102", "row 122"),
        ("Row 102", "Row 122"),
        ("__ROW122_REF__", "[row 122]"),
        ("[row 101]", "[row 121]"),
        ("row 101", "row 121"),
        ("Row 101", "Row 121"),
        ("(row 121)", "(row 141)"),
        ("__ROW122_LOOP__", "Row 122 closing loop"),
        ("row 120", "row 140"),
        ("Row 120", "Row 140"),
        ("preface.md#skill-navigation-row-120)", "preface.md#skill-navigation-row-140)"),
        ("row 121", "row 141"),
        ("Row 121", "Row 141"),
        (
            "Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge",
            "Handshake 3 meta prelude capstone / Handshake 4a meta prelude hinge on the capstone path",
        ),
        (
            "after verified bulk hardening parsing on the capstone path**",
            "after verified bulk hardening parsing on the capstone path**",
        ),
        (
            "after verified bulk hardening parsing**",
            "after verified bulk hardening parsing on the capstone path**",
        ),
        (
            "at the Handshake 4a meta prelude capstone boundary inside the coupling gate",
            "at the Handshake 4a meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 61 reunion |", "Row 68 ↔ Row 61 reunion (capstone path) |"),
        (
            "[Row 68 → Row 81 Handshake 4a meta prelude reunion index (row 101)]",
            "[Row 68 → Row 101 Handshake 4a meta prelude capstone reunion index (row 121)]",
        ),
        (
            "row68-row81-handshake4a-meta-prelude-reunion-index-row-101",
            "row68-row101-handshake4a-meta-prelude-capstone-reunion-index-row-121",
        ),
        (
            "verified Handshake 3 meta prelude capstone closure (row 120)",
            "verified Handshake 3 meta prelude capstone closure (row 140)",
        ),
        (
            "Row 68 → Row 61 meta (row 141)",
            "Row 68 → Row 61 meta (row 141)",
        ),
        (
            "Row 68 → Row 61 meta (row 101)",
            "Row 68 → Row 61 meta (row 141)",
        ),
        (
            "before Handshake 4b opens in workflow time",
            "before Handshake 4b opens on the capstone path in workflow time",
        ),
        (
            "When row 121 is complete, proceed to [row 122]",
            "When row 141 is complete, proceed to [row 142](preface.md#skill-navigation-row-142) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, to [row 122](preface.md#skill-navigation-row-122) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta capstone on the capstone path, to [row 61](preface.md#skill-navigation-row-61) when only Handshake 4a meta stalls, or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_121",
        ),
        (
            "Handshake 4a meta prelude capstone at the descent-chain boundary in reading time",
            "Handshake 4a meta prelude capstone at the descent-chain boundary in reading time on the capstone path",
        ),
        (
            "When row 61 feels like epilogue homework after row 120 alone",
            "When row 61 feels like epilogue homework after row 140 alone on the capstone path",
        ),
        (
            "When row 61 feels like epilogue homework after row 140 alone",
            "When row 61 feels like epilogue homework after row 140 alone on the capstone path",
        ),
        ("Recite [preface row 120]", "Recite [preface row 140]"),
        (
            "Do not conflate row 141 (row 68 ↔ row 61 reunion on the capstone path)",
            "Do not conflate row 141 (row 68 ↔ row 61 reunion on the capstone path)",
        ),
        (
            "Do not conflate row 121 (row 68 ↔ row 61 reunion on the capstone path)",
            "Do not conflate row 141 (row 68 ↔ row 61 reunion on the capstone path)",
        ),
        (
            "Do not conflate row 121 (row 68 ↔ row 61 reunion",
            "Do not conflate row 141 (row 68 ↔ row 61 reunion on the capstone path",
        ),
        (
            "row 121 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 120)",
            "row 141 names **why that reunion must follow verified Handshake 3 meta prelude capstone (row 140)",
        ),
        (
            "Proceed to [row 122](#row-122-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 121",
            "Proceed to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 141 on the capstone path, to [row 122](#row-122-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 121 on the opening-hinge path",
        ),
        (
            "Proceed to [row 122](#row-122-closing-loop) when row 68 closed but Handshake 4b meta still feels disconnected after row 120",
            "Proceed to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 141 on the capstone path, to [row 122](#row-122-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 121 on the opening-hinge path, to [row 121](#row-121-closing-loop) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, to [row 140](#row-140-closing-loop) when Handshake 3 meta prelude capstone still lags after row 139 on the capstone path, to [row 61](#row-61-closing-loop) when only Handshake 4a meta stalls",
        ),
        (
            "when opening [row 122](preface.md#skill-navigation-row-122) before row 61 closes",
            "when opening [row 142](preface.md#skill-navigation-row-142) before row 62 closes on the capstone path",
        ),
        (
            "when `rate_export.yaml` is missing after row 120 but OpenDiS exports already sit in the plasticity deck",
            "when `rate_export.yaml` is missing on the capstone path after row 140 but OpenDiS exports already sit in the plasticity deck",
        ),
        (
            "when row 120 closed but row 61",
            "when row 140 closed but row 61",
        ),
        (
            "When row 120 closed — Handshake 3 meta prelude capstone verified, row 119 or row 100 recited",
            "When row 140 closed — Handshake 3 meta prelude capstone verified, row 139 or row 120 recited on the capstone path",
        ),
        (
            "before row 122 Handshake 4b meta prelude capstone opens",
            "before row 62 Handshake 4b meta prelude opens on the capstone path",
        ),
        (
            "when row 120 and row 61 both verify individually",
            "when row 140 and row 61 both verify individually",
        ),
        (
            "when row 120 closed Handshake 3 meta prelude capstone and row 68 closed the midpoint prelude but **row 61 Handshake 4a meta still opens",
            "when row 140 closed Handshake 3 meta prelude capstone and row 68 closed the midpoint prelude but **row 61 Handshake 4a meta still opens",
        ),
        (
            "rear-view mirror of row 120's Handshake 3 meta → forest → power-law",
            "rear-view mirror of row 140's Handshake 3 meta → forest → power-law",
        ),
        (
            "read row 68 gate + row 120 or row 101 Handshake 3 meta prelude capstone / Handshake 4a meta prelude gate + epilogue rate cross-links + row 61 meta aloud when thermal pre-stress is verified after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation",
            "read row 68 gate + row 140 or row 121 Handshake 3 meta prelude capstone / Handshake 4a meta prelude gate + epilogue rate cross-links + row 61 meta aloud when thermal pre-stress is verified on the capstone path after Handshake 3 meta prelude capstone but OpenDiS exports feed the plasticity deck without power-law extrapolation",
        ),
        (
            "before row 141 Handshake 4a meta prelude capstone or row 61 workflow reunion opens on the capstone path",
            "before row 142 Handshake 4b meta prelude capstone or row 62 workflow reunion opens on the capstone path",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_121" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_121.*", "", out, flags=re.S)
    return out


def fix_row_140_tail(preface: str) -> str:
    old = (
        "When row 140 is complete, proceed to [row 141](preface.md#skill-navigation-row-141) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 121](preface.md#skill-navigation-row-121) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 139](preface.md#skill-navigation-row-139) when Handshake 3 meta capstone still lags after verified DFT workflows meta capstone on the capstone path, to [row 80](preface.md#skill-navigation-row-80) for the Row 68 ↔ Row 60 meta audit alone, to [row 60](preface.md#skill-navigation-row-60) for the Row 59 ↔ Row 40 meta audit alone, to [row 40](preface.md#skill-navigation-row-40) for the full-book \\(lpha(T_w)\\) audit, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 140 is complete, proceed to [row 141](preface.md#skill-navigation-row-141) when row 68 closed but Handshake 4a meta prelude still lags on the capstone path, to [row 121](preface.md#skill-navigation-row-121) when Handshake 3 meta prelude capstone is clean but Handshake 4a meta prelude still lags on the opening-hinge path, to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit alone, to [row 120](preface.md#skill-navigation-row-120) for the Row 68 ↔ Row 60 Handshake 3 meta prelude audit on the opening-hinge path alone, to [row 139](preface.md#skill-navigation-row-139) when Handshake 3 meta capstone still lags after verified DFT workflows meta capstone on the capstone path, to [row 61](preface.md#skill-navigation-row-61) when only Handshake 4a meta stalls, or extend prose only under `writings/` then sync."
    )
    if old in preface:
        preface = preface.replace(old, new)
    return preface


def fix_row_140_baby(mem: str) -> str:
    return mem.replace(
        "before row 141 Handshake 4a meta prelude capstone opens on the capstone path**",
        "before row 141 Handshake 4a meta prelude capstone opens on the capstone path**",
    )


def add_row_141() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    preface = fix_row_140_tail(preface)
    if "skill-navigation-row-141" in preface and "### Row 141 skill checkpoint" in preface:
        print("preface: row 141 already present")
    else:
        m121 = re.search(
            r"(### Row 121 skill checkpoint.*?)(?=\n### Row 122 skill checkpoint)",
            preface,
            re.S,
        )
        if not m121:
            raise SystemExit("row 121 preface checkpoint missing")
        row141 = lift_121_to_141(m121.group(1))
        anchor = "\n## The copper wire through the book"
        preface = preface.replace(anchor, "\n" + row141 + anchor)
        preface_path.write_text(preface)
        print("preface: added row 141")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-141-closing-loop" not in ep:
        block121 = extract_between(ep, "### Row 121 closing loop", "### Row 122 closing loop")
        block141 = lift_121_to_141(block121)
        ep = ep.replace("### Row 122 closing loop", block141 + "### Row 122 closing loop", 1)
        ep = ep.replace(
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 140 on the capstone path, to [row 121](#row-121-closing-loop) when row 68 closed but Handshake 4a meta still feels disconnected after row 120 on the opening-hinge path",
            "Proceed to [row 141](#row-141-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 140 on the capstone path, to [row 121](#row-121-closing-loop) when row 68 closed but Handshake 4a meta prelude still lags after row 120 on the opening-hinge path, to [row 140](#row-140-closing-loop) when Handshake 3 meta prelude capstone still lags after row 139 on the capstone path",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 141 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 141) |"
    )
    if compass_line not in pro:
        line121 = (
            "| Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 121) |"
        )
        idx121 = pro.find(line121)
        if idx121 < 0:
            raise SystemExit("prologue compass row 121 not found")
        line_end121 = pro.find("\n", idx121)
        compass141 = lift_121_to_141(pro[idx121:line_end121]) + "\n"
        line140 = (
            "| Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone reunion (row 140) |"
        )
        idx140 = pro.find(line140)
        if idx140 < 0:
            raise SystemExit("prologue compass row 140 not found")
        line_end140 = pro.find("\n", idx140)
        pro = pro[: line_end140 + 1] + compass141 + pro[line_end140 + 1 :]
        preview121 = extract_between(
            pro,
            '| <span id="prologue-preview-row-121"></span>',
            '\n| <span id="prologue-preview-row-122">',
        )
        preview141 = lift_121_to_141(preview121)
        pro = pro.replace(
            '| <span id="prologue-preview-row-121"></span>',
            preview141 + '| <span id="prologue-preview-row-121"></span>',
            1,
        )
        if "row-141-closing-stitch" not in pro:
            stitch = (
                "**Row 141 closing stitch (Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion).** {#row-141-closing-stitch} "
                "When row 140 closed — Handshake 3 meta prelude capstone verified, row 139 or row 120 recited on the capstone path, and thermal pre-stress at \\(T_w\\) archived in `alpha_export.yaml` — but **row 61 Handshake 4a meta reunion still opens like standalone epilogue coursework after the Handshake 4a opening prelude chapter hinge on the capstone path** — "
                "the [preface row 141 When-to-pause opening sentence](../preface.md#skill-navigation-row-141) names the dual reunion before Handshake 4b meta prelude reunion; read [preface row 141](../preface.md#skill-navigation-row-141), then the "
                "[Row 68 → Row 121 reunion index](../appendix/sources.md#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141), then "
                "[epilogue row 141 closing loop](../epilogue/multiscale.md#row-141-closing-loop) before row 62 Handshake 4b meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 122 closing stitch", stitch + "**Row 122 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 141 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141" not in src:
        idx121 = src.find(
            "## Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 121)"
        )
        idx122 = src.find(
            "## Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 122)"
        )
        if idx121 < 0 or idx122 < 0:
            raise SystemExit("row 121/122 sources anchors missing")
        block = src[idx121:idx122]
        block141 = lift_121_to_141(block)
        table_row = (
            "| 141 | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone (midpoint prelude gate ↔ Handshake 3 meta prelude capstone ↔ row 61 meta) | "
            "[Row 68 → Row 121 Handshake 4a meta prelude capstone reunion index](#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141) · "
            "[preface row 141](../preface.md#skill-navigation-row-141) · "
            "[prologue row 141 preview](../prologue/00-many-scales.md#prologue-preview-row-141) · "
            "[prologue row 141 closing stitch](../prologue/00-many-scales.md#row-141-closing-stitch) · "
            "[epilogue row 141 closing loop](../epilogue/multiscale.md#row-141-closing-loop) · "
            "[memory sheet row 141 baby picture](memory-sheet.md#row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 61 Handshake 4a meta reunion still feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path** — "
            "read row 68 + row 140 or row 121 gate + epilogue rate cross-links + row 61; "
            "[preface row 61](../preface.md#skill-navigation-row-61) |\n"
        )
        src = src.replace(
            "| 140 | Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone",
            table_row + "| 140 | Row 68 → Row 120 Row 68 → Row 60 Handshake 3 meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 121)",
            block141 + "## Row 68 → Row 101 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion index (row 121)",
        )
        extra = (
            "[row 141](#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141) reunites **Handshake 3 meta prelude capstone with the Handshake 4a meta prelude capstone boundary** "
            "when row 140 closed Handshake 3 meta prelude capstone at verified thermal pre-stress on the capstone path but epilogue rate cross-links and Part VII still read like separate courses after verified Handshake 4a meta prelude meta;"
        )
        if extra not in src:
            src = src.replace(
                "when row 139 closed Handshake 3 meta capstone at verified `alpha_export.yaml` on the capstone path but epilogue α cross-links and Parts III–VI still read like separate courses after verified Handshake 3 meta prelude meta;",
                "when row 139 closed Handshake 3 meta capstone at verified `alpha_export.yaml` on the capstone path but epilogue α cross-links and Parts III–VI still read like separate courses after verified Handshake 3 meta prelude meta; "
                + extra,
            )
        src_path.write_text(src)
        print("sources: added row 141 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    mem = fix_row_140_baby(mem)
    if "row-141-baby-picture" not in mem:
        baby121 = extract_between(mem, "### Row 121 baby picture", "### Row 122 baby picture")
        baby141 = lift_121_to_141(baby121)
        mem = mem.replace("### Row 122 baby picture", baby141 + "### Row 122 baby picture", 1)
        mem_table = (
            "| 141 | Meta | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion | "
            "[Row 68 → Row 121 Handshake 4a meta prelude capstone reunion index](sources.md#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141) · "
            "[preface row 141 skill checkpoint](../preface.md#skill-navigation-row-141) · "
            "[prologue row 141 preview](../prologue/00-many-scales.md#prologue-preview-row-141) · "
            "[prologue row 141 closing stitch](../prologue/00-many-scales.md#row-141-closing-stitch) · "
            "[epilogue row 141 closing loop](../epilogue/multiscale.md#row-141-closing-loop) | "
            "Row 68 closed but row 61 Handshake 4a meta reunion feels disconnected from verified Handshake 3 meta prelude capstone on the capstone path — "
            "read row 68 + row 140 or row 121 gate + epilogue rate cross-links + row 61; "
            "[row 141 baby picture](#row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "[row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
            "[row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion) |\n" + mem_table + "| 93 | Meta |",
        )
        if "When row 140 closed but Handshake 4a meta prelude reunion still lags" not in mem:
            mem = mem.replace(
                "When row 139 closed but Handshake 3 meta prelude reunion still lags on the capstone path, switch to [row 140](#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion).",
                "When row 139 closed but Handshake 3 meta prelude reunion still lags on the capstone path, switch to [row 140](#row-140-baby-picture-row68-row120-handshake3-meta-prelude-capstone-reunion). When row 140 closed but Handshake 4a meta prelude reunion still lags on the capstone path, switch to [row 141](#row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 141")
    else:
        mem_path.write_text(mem)
        print("memory-sheet: row 141 baby already present")


def main() -> None:
    add_row_141()


if __name__ == "__main__":
    main()
