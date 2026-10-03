#!/usr/bin/env python3
"""Add row 142 (Row 68 → Row 122 ↔ Row 62 Handshake 4b meta prelude capstone on capstone path)."""
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


def lift_122_to_142(s: str) -> str:
    p = [
        ("Row 123 closing loop", "__ROW123_LOOP__"),
        ("Row 122 closing loop", "Row 142 closing loop"),
        ("row-122-closing-loop", "row-142-closing-loop"),
        ("Row 122 closing stitch", "Row 142 closing stitch"),
        ("row-122-closing-stitch", "row-142-closing-stitch"),
        ("prologue-preview-row-122", "prologue-preview-row-142"),
        ("Row 122 preview", "Row 142 preview"),
        ("Row 122 skill checkpoint", "Row 142 skill checkpoint"),
        ("skill-navigation-row-122", "skill-navigation-row-142"),
        ("memory sheet row 122", "memory sheet row 142"),
        ("Row 122 baby picture", "Row 142 baby picture"),
        ("Row 122 three-way audit", "Row 142 three-way audit"),
        (
            "Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone",
            "Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone",
        ),
        (
            "row68-row102-handshake4b-meta-prelude-capstone-reunion-index-row-122",
            "row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142",
        ),
        (
            "row-122-baby-picture-row68-row102-handshake4b-meta-prelude-capstone-reunion",
            "row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion",
        ),
        ("[row 123]", "__ROW123_REF__"),
        ("[row 103]", "[row 123]"),
        ("row 103", "row 123"),
        ("Row 103", "Row 123"),
        ("__ROW123_REF__", "[row 123]"),
        ("[row 102]", "[row 122]"),
        ("row 102", "row 122"),
        ("Row 102", "Row 122"),
        ("(row 122)", "(row 142)"),
        ("__ROW123_LOOP__", "Row 123 closing loop"),
        ("row 121", "row 141"),
        ("Row 121", "Row 141"),
        (
            "Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge",
            "Handshake 4a meta prelude capstone / Handshake 4b meta prelude hinge on the capstone path",
        ),
        (
            "at the Handshake 4b meta prelude capstone boundary inside the coupling gate",
            "at the Handshake 4b meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        ("Row 68 ↔ Row 62 reunion |", "Row 68 ↔ Row 62 reunion (capstone path) |"),
        (
            "[Row 68 → Row 82 Handshake 4b meta prelude reunion index (row 102)]",
            "[Row 68 → Row 102 Handshake 4b meta prelude capstone reunion index (row 122)]",
        ),
        (
            "row68-row82-handshake4b-meta-prelude-reunion-index-row-102",
            "row68-row102-handshake4b-meta-prelude-capstone-reunion-index-row-122",
        ),
        (
            "verified Handshake 4a meta prelude capstone closure (row 121)",
            "verified Handshake 4a meta prelude capstone closure (row 141)",
        ),
        (
            "Row 68 → Row 62 meta (row 102)",
            "Row 68 → Row 62 meta (row 142)",
        ),
        (
            "before row 16 orchestration opens in workflow time",
            "before row 16 orchestration opens on the capstone path in workflow time",
        ),
        (
            "When row 122 is complete, proceed to [row 123]",
            "When row 142 is complete, proceed to [row 143](preface.md#skill-navigation-row-143) when row 68 closed but orchestration meta prelude still lags on the capstone path, "
            "to [row 123](preface.md#skill-navigation-row-123) when Handshake 4b meta prelude capstone is clean but orchestration meta prelude still lags on the opening-hinge path, "
            "to [row 103](preface.md#skill-navigation-row-103) for the Row 68 ↔ Row 63 orchestration meta prelude audit alone, "
            "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit on the opening-hinge path alone, "
            "to [row 141](preface.md#skill-navigation-row-141) when Handshake 4a meta prelude capstone still lags after verified Handshake 4a meta capstone on the capstone path, "
            "to [row 62](preface.md#skill-navigation-row-62) when only Handshake 4b meta stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_122",
        ),
        (
            "Handshake 4b meta prelude capstone at the discretization-chain boundary in reading time",
            "Handshake 4b meta prelude capstone at the discretization-chain boundary in reading time on the capstone path",
        ),
        (
            "When row 62 feels like epilogue homework after row 121 alone",
            "When row 62 feels like epilogue homework after row 141 alone on the capstone path",
        ),
        (
            "When row 62 feels like epilogue homework after row 141 alone",
            "When row 62 feels like epilogue homework after row 141 alone on the capstone path",
        ),
        ("Recite [preface row 121]", "Recite [preface row 141]"),
        (
            "Do not conflate row 142 (row 68 ↔ row 62 reunion on the capstone path)",
            "Do not conflate row 142 (row 68 ↔ row 62 reunion on the capstone path)",
        ),
        (
            "Do not conflate row 122 (row 68 ↔ row 62 reunion on the capstone path)",
            "Do not conflate row 142 (row 68 ↔ row 62 reunion on the capstone path)",
        ),
        (
            "Do not conflate row 122 (row 68 ↔ row 62 reunion",
            "Do not conflate row 142 (row 68 ↔ row 62 reunion on the capstone path",
        ),
        (
            "row 122 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 121)",
            "row 142 names **why that reunion must follow verified Handshake 4a meta prelude capstone (row 141)",
        ),
        (
            "Proceed to [row 123](#row-123-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 122",
            "Proceed to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 142 on the capstone path, "
            "to [row 123](#row-123-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 122 on the opening-hinge path",
        ),
        (
            "Proceed to [row 123](#row-123-closing-loop) when row 68 closed but orchestration meta still feels disconnected after row 121",
            "Proceed to [row 143](#row-143-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 142 on the capstone path, "
            "to [row 123](#row-123-closing-loop) when row 68 closed but orchestration meta prelude still lags after row 122 on the opening-hinge path, "
            "to [row 122](#row-122-closing-loop) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit on the opening-hinge path alone, "
            "to [row 141](#row-141-closing-loop) when Handshake 4a meta prelude capstone still lags after row 140 on the capstone path, "
            "to [row 62](#row-62-closing-loop) when only Handshake 4b meta stalls",
        ),
        (
            "when opening [row 123](preface.md#skill-navigation-row-123) before row 62 closes",
            "when opening [row 143](preface.md#skill-navigation-row-143) before row 63 closes on the capstone path",
        ),
        (
            "when `fe2_notch_comparison.dat` exists after row 121 but crystal plasticity is still trusted at the notch root",
            "when `fe2_notch_comparison.dat` exists on the capstone path after row 141 but crystal plasticity is still trusted at the notch root",
        ),
        (
            "when row 121 closed but row 62",
            "when row 141 closed but row 62",
        ),
        (
            "When row 121 closed — Handshake 4a meta prelude capstone verified, row 120 or row 101 recited",
            "When row 141 closed — Handshake 4a meta prelude capstone verified, row 140 or row 121 recited on the capstone path",
        ),
        (
            "before row 123 orchestration meta prelude capstone opens",
            "before row 63 orchestration meta prelude opens on the capstone path",
        ),
        (
            "when row 121 and row 62 both verify individually",
            "when row 141 and row 62 both verify individually",
        ),
        (
            "rear-view mirror of row 121's Handshake 4a meta → bulk",
            "rear-view mirror of row 141's Handshake 4a meta → bulk",
        ),
        (
            "read row 68 gate + row 121 or row 102 Handshake 4a meta prelude capstone / Handshake 4b meta prelude gate + epilogue FE² cross-links + row 62 meta aloud when bulk hardening matches flow stress after Handshake 4a meta prelude capstone but the notch root under-predicts peak stress without FE² audit",
            "read row 68 gate + row 141 or row 122 Handshake 4a meta prelude capstone / Handshake 4b meta prelude gate + epilogue FE² cross-links + row 62 meta aloud when bulk hardening matches flow stress on the capstone path after Handshake 4a meta prelude capstone but the notch root under-predicts peak stress without FE² audit",
        ),
        (
            "before row 142 Handshake 4b meta prelude capstone or row 62 workflow reunion opens on the capstone path",
            "before row 143 orchestration meta prelude capstone or row 63 workflow reunion opens on the capstone path",
        ),
        ("row 122", "row 142"),
        ("Row 122", "Row 142"),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_122" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_122.*", "", out, flags=re.S)
    return out


def fix_row_141_tail(preface: str) -> str:
    bloated = (
        "When row 141 is complete, proceed to [row 142](preface.md#skill-navigation-row-142) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, "
        "to [row 122](preface.md#skill-navigation-row-122) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, "
        "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone, "
        "to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, "
        "to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta capstone on the capstone path, "
        "to [row 81](preface.md#skill-navigation-row-81) for the Row 68 ↔ Row 61 opening prelude audit alone, "
        "to [row 61](preface.md#skill-navigation-row-61) for the Row 60 ↔ Row 41 meta audit alone, "
        "to [row 41](preface.md#skill-navigation-row-41) for the full VII.3 → Handshake 4a meta audit, "
    )
    trimmed = (
        "When row 141 is complete, proceed to [row 142](preface.md#skill-navigation-row-142) when row 68 closed but Handshake 4b meta prelude still lags on the capstone path, "
        "to [row 122](preface.md#skill-navigation-row-122) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, "
        "to [row 102](preface.md#skill-navigation-row-102) for the Row 68 ↔ Row 62 Handshake 4b meta prelude audit alone, "
        "to [row 101](preface.md#skill-navigation-row-101) for the Row 68 ↔ Row 61 Handshake 4a meta prelude audit on the opening-hinge path alone, "
        "to [row 140](preface.md#skill-navigation-row-140) when Handshake 3 meta prelude capstone still lags after verified Handshake 3 meta capstone on the capstone path, "
        "to [row 62](preface.md#skill-navigation-row-62) when only Handshake 4b meta stalls, "
    )
    if bloated in preface:
        preface = preface.replace(bloated, trimmed)
    return preface


def add_row_142() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    preface = fix_row_141_tail(preface)
    if "skill-navigation-row-142" in preface and "### Row 142 skill checkpoint" in preface:
        print("preface: row 142 already present")
    else:
        m122 = re.search(
            r"(### Row 122 skill checkpoint.*?)(?=\n### Row 123 skill checkpoint)",
            preface,
            re.S,
        )
        if not m122:
            raise SystemExit("row 122 preface checkpoint missing")
        row142 = lift_122_to_142(m122.group(1))
        anchor = "\n## The copper wire through the book"
        preface = preface.replace(anchor, "\n" + row142 + anchor)
        preface_path.write_text(preface)
        print("preface: added row 142")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-142-closing-loop" not in ep:
        block122 = extract_between(ep, "### Row 122 closing loop", "### Row 123 closing loop")
        block142 = lift_122_to_142(block122)
        ep = ep.replace("### Row 123 closing loop", block142 + "### Row 123 closing loop", 1)
        ep = ep.replace(
            "Proceed to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 141 on the capstone path, to [row 122](#row-122-closing-loop) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path",
            "Proceed to [row 142](#row-142-closing-loop) when row 68 closed but Handshake 4b meta prelude still lags after row 141 on the capstone path, "
            "to [row 122](#row-122-closing-loop) when Handshake 4a meta prelude capstone is clean but Handshake 4b meta prelude still lags on the opening-hinge path, "
            "to [row 141](#row-141-closing-loop) when Handshake 4a meta prelude capstone still lags after row 140 on the capstone path",
            1,
        )
        ep_path.write_text(ep)
        print("epilogue: added row 142 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 142) |"
    )
    if compass_line not in pro:
        line141 = (
            "| Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 141) |"
        )
        idx141 = pro.find(line141)
        if idx141 < 0:
            raise SystemExit("prologue compass row 141 not found")
        line_end141 = pro.find("\n", idx141)
        compass142 = lift_122_to_142(pro[idx141:line_end141]).replace(
            "Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone reunion (row 141)",
            "Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 142)",
        )
        # Build compass from row 122 line if lift from 141 wrong
        line122 = (
            "| Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion (row 122) |"
        )
        idx122 = pro.find(line122)
        if idx122 >= 0:
            line_end122 = pro.find("\n", idx122)
            compass142 = lift_122_to_142(pro[idx122:line_end122]) + "\n"
        pro = pro[: line_end141 + 1] + compass142 + pro[line_end141 + 1 :]
        preview122 = extract_between(
            pro,
            '| <span id="prologue-preview-row-122"></span>',
            '\n| <span id="prologue-preview-row-123">',
        )
        preview142 = lift_122_to_142(preview122)
        pro = pro.replace(
            '| <span id="prologue-preview-row-122"></span>',
            preview142 + '| <span id="prologue-preview-row-122"></span>',
            1,
        )
        if "row-142-closing-stitch" not in pro:
            stitch = (
                "**Row 142 closing stitch (Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion).** {#row-142-closing-stitch} "
                "When row 141 closed — Handshake 4a meta prelude capstone verified, row 140 or row 121 recited on the capstone path, and "
                "[`parse_rate.sh`](../../scripts/parse_rate.sh) archived `rate_export.yaml` with lab grip rate matching "
                "[`fixtures/cht_export.yaml`](../../fixtures/cht_export.yaml) at \\(T_w\\) after verified Handshake 4a meta prelude capstone — "
                "but **row 62 Handshake 4b meta reunion still opens like standalone epilogue coursework after the Handshake 4b opening prelude chapter hinge on the capstone path** — "
                "the [preface row 142 When-to-pause opening sentence](../preface.md#skill-navigation-row-142) names the dual reunion before orchestration meta prelude reunion; "
                "read [preface row 142](../preface.md#skill-navigation-row-142), then the "
                "[Row 68 → Row 122 reunion index](../appendix/sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142), then "
                "[epilogue row 142 closing loop](../epilogue/multiscale.md#row-142-closing-loop) before row 63 orchestration meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 123 closing stitch", stitch + "**Row 123 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 142 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142" not in src:
        idx122 = src.find(
            "## Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 122)"
        )
        idx123 = src.find(
            "## Row 68 → Row 103 Row 68 → Row 63 orchestration meta prelude capstone reunion index (row 123)"
        )
        if idx122 < 0 or idx123 < 0:
            raise SystemExit("row 122/123 sources anchors missing")
        block = src[idx122:idx123]
        block142 = lift_122_to_142(block)
        table_row = (
            "| 142 | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone (midpoint prelude gate ↔ Handshake 4a meta prelude capstone ↔ row 62 meta) | "
            "[Row 68 → Row 122 Handshake 4b meta prelude capstone reunion index](#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142) · "
            "[preface row 142](../preface.md#skill-navigation-row-142) · "
            "[prologue row 142 preview](../prologue/00-many-scales.md#prologue-preview-row-142) · "
            "[prologue row 142 closing stitch](../prologue/00-many-scales.md#row-142-closing-stitch) · "
            "[epilogue row 142 closing loop](../epilogue/multiscale.md#row-142-closing-loop) · "
            "[memory sheet row 142 baby picture](memory-sheet.md#row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 62 Handshake 4b meta reunion still feels disconnected from verified Handshake 4a meta prelude capstone on the capstone path** — "
            "read row 68 + row 141 or row 122 gate + epilogue FE² cross-links + row 62; "
            "[preface row 62](../preface.md#skill-navigation-row-62) |\n"
        )
        src = src.replace(
            "| 141 | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone",
            table_row + "| 141 | Row 68 → Row 121 Row 68 → Row 61 Handshake 4a meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 122)",
            block142
            + "## Row 68 → Row 102 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion index (row 122)",
        )
        extra = (
            "[row 142](#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142) reunites **Handshake 4a meta prelude capstone with the Handshake 4b meta prelude capstone boundary** "
            "when row 141 closed Handshake 4a meta prelude capstone at verified bulk hardening on the capstone path but epilogue FE² cross-links and Part VII Step 4 still read like separate courses after verified Handshake 4b meta prelude meta;"
        )
        if extra not in src:
            src = src.replace(
                "when row 139 closed Handshake 3 meta capstone at verified `alpha_export.yaml` on the capstone path but epilogue α cross-links and Parts III–VI still read like separate courses after verified Handshake 3 meta prelude meta; "
                + "[row 141](#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141) reunites **Handshake 3 meta prelude capstone with the Handshake 4a meta prelude capstone boundary** "
                "when row 140 closed Handshake 3 meta prelude capstone at verified thermal pre-stress on the capstone path but epilogue rate cross-links and Part VII still read like separate courses after verified Handshake 4a meta prelude meta;",
                "when row 139 closed Handshake 3 meta capstone at verified `alpha_export.yaml` on the capstone path but epilogue α cross-links and Parts III–VI still read like separate courses after verified Handshake 3 meta prelude meta; "
                + "[row 141](#row68-row121-handshake4a-meta-prelude-capstone-reunion-index-row-141) reunites **Handshake 3 meta prelude capstone with the Handshake 4a meta prelude capstone boundary** "
                "when row 140 closed Handshake 3 meta prelude capstone at verified thermal pre-stress on the capstone path but epilogue rate cross-links and Part VII still read like separate courses after verified Handshake 4a meta prelude meta; "
                + extra,
            )
        src_path.write_text(src)
        print("sources: added row 142 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-142-baby-picture" not in mem:
        baby122 = extract_between(mem, "### Row 122 baby picture", "### Row 123 baby picture")
        baby142 = lift_122_to_142(baby122)
        mem = mem.replace("### Row 123 baby picture", baby142 + "### Row 123 baby picture", 1)
        mem_table = (
            "| 142 | Meta | Row 68 → Row 122 Row 68 → Row 62 Handshake 4b meta prelude capstone reunion | "
            "[Row 68 → Row 122 Handshake 4b meta prelude capstone reunion index](sources.md#row68-row122-handshake4b-meta-prelude-capstone-reunion-index-row-142) · "
            "[preface row 142 skill checkpoint](../preface.md#skill-navigation-row-142) · "
            "[prologue row 142 preview](../prologue/00-many-scales.md#prologue-preview-row-142) · "
            "[prologue row 142 closing stitch](../prologue/00-many-scales.md#row-142-closing-stitch) · "
            "[epilogue row 142 closing loop](../epilogue/multiscale.md#row-142-closing-loop) | "
            "Row 68 closed but row 62 Handshake 4b meta reunion feels disconnected from verified Handshake 4a meta prelude capstone on the capstone path — "
            "read row 68 + row 141 or row 122 gate + epilogue FE² cross-links + row 62; "
            "[row 142 baby picture](#row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "[row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion) |\n| 93 | Meta |",
            "[row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion) |\n" + mem_table + "| 93 | Meta |",
        )
        if "When row 141 closed but Handshake 4b meta prelude reunion still lags" not in mem:
            mem = mem.replace(
                "When row 140 closed but Handshake 4a meta prelude reunion still lags on the capstone path, switch to [row 141](#row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion).",
                "When row 140 closed but Handshake 4a meta prelude reunion still lags on the capstone path, switch to [row 141](#row-141-baby-picture-row68-row121-handshake4a-meta-prelude-capstone-reunion). "
                "When row 141 closed but Handshake 4b meta prelude reunion still lags on the capstone path, switch to [row 142](#row-142-baby-picture-row68-row122-handshake4b-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 142")
    else:
        print("memory-sheet: row 142 baby already present")


def main() -> None:
    add_row_142()


if __name__ == "__main__":
    main()
