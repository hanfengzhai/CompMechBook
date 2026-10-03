#!/usr/bin/env python3
"""Add row 150 (Row 68 → Row 130 ↔ Row 50 DDD meta prelude capstone on capstone path)."""
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


def lift_110_to_130(s: str) -> str:
    """Promote opening-hinge row 110 sources index to capstone row 130 wording."""
    p = [
        (
            "Row 68 → Row 90 Row 68 → Row 50 DDD meta prelude reunion",
            "Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion",
        ),
        (
            "row68-row90-ddd-meta-prelude-reunion-index-row-110",
            "row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130",
        ),
        (
            "row-110-baby-picture-row68-row90-ddd-meta-prelude-reunion",
            "row-130-baby-picture-row68-row110-ddd-meta-prelude-capstone-reunion",
        ),
        ("Row 110 names", "Row 130 names"),
        ("Row 110 does not replace", "Row 130 does not replace"),
        ("(row 110)", "(row 130)"),
        ("skill-navigation-row-110", "skill-navigation-row-130"),
        ("preface row 110", "preface row 130"),
        ("Preface row 110", "Preface row 130"),
        ("memory sheet row 110", "memory sheet row 130"),
        ("Row 110 baby picture", "Row 130 baby picture"),
        ("[row 109]", "__ROW109_REF__"),
        ("row 109", "row 129"),
        ("Row 109", "Row 129"),
        ("__ROW109_REF__", "[row 129]"),
        (
            "taxonomy meta capstone / DDD opening prelude",
            "taxonomy meta prelude capstone / DDD meta prelude",
        ),
        ("taxonomy meta capstone", "taxonomy meta prelude capstone"),
        ("DDD meta capstone boundary", "DDD meta prelude capstone boundary inside the coupling gate on the capstone path"),
        ("DDD meta reunion", "DDD meta prelude capstone reunion"),
        ("DDD meta capstone", "DDD meta prelude capstone"),
        ("row 109 verified", "row 129 verified"),
        ("inside the coupling gate", "inside the coupling gate on the capstone path"),
    ]
    return tx(s, p)


def lift_130_to_150(s: str) -> str:
    p = [
        ("skill-navigation-row-110", "skill-navigation-row-130"),
        (
            "Row 68 → Row 90 DDD meta prelude reunion index (row 110)",
            "Row 68 → Row 110 DDD meta prelude capstone reunion index (row 130)",
        ),
        ("Row 130 does not replace", "Row 150 does not replace"),
        (
            "Prologue preview ([row 130]",
            "Prologue preview ([row 150]",
        ),
        (
            "[preface row 130 skill checkpoint](../preface.md#skill-navigation-row-150)",
            "[preface row 150 skill checkpoint](../preface.md#skill-navigation-row-150)",
        ),
        ("Row 131 closing loop", "__ROW131_LOOP__"),
        ("Row 130 closing loop", "Row 150 closing loop"),
        ("row-131-closing-loop", "__ROW131_LOOP_ANCHOR__"),
        ("row-130-closing-loop", "row-150-closing-loop"),
        ("Row 131 closing stitch", "__ROW131_STITCH__"),
        ("Row 130 closing stitch", "Row 150 closing stitch"),
        ("row-131-closing-stitch", "__ROW131_STITCH_ANCHOR__"),
        ("row-130-closing-stitch", "row-150-closing-stitch"),
        ("prologue-preview-row-131", "__ROW131_PREVIEW__"),
        ("prologue-preview-row-130", "prologue-preview-row-150"),
        ("Row 131 preview", "__ROW131_PREVIEW_TEXT__"),
        ("Row 130 preview", "Row 150 preview"),
        ("Row 131 skill checkpoint", "__ROW131_SKILL__"),
        ("Row 130 skill checkpoint", "Row 150 skill checkpoint"),
        ("skill-navigation-row-131", "__ROW131_SKILL_NAV__"),
        ("skill-navigation-row-130", "skill-navigation-row-150"),
        ("memory sheet row 131", "__ROW131_MEM__"),
        ("memory sheet row 130", "memory sheet row 150"),
        ("Row 131 baby picture", "__ROW131_BABY__"),
        ("Row 130 baby picture", "Row 150 baby picture"),
        ("Row 131 three-way audit", "__ROW131_AUDIT__"),
        ("Row 130 three-way audit", "Row 150 three-way audit"),
        (
            "Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone",
            "Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone",
        ),
        (
            "row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130",
            "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150",
        ),
        (
            "row-130-baby-picture-row68-row110-ddd-meta-prelude-capstone-reunion",
            "row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion",
        ),
        ("[row 131]", "__ROW131_REF__"),
        ("[row 110]", "[row 130]"),
        ("row 110", "row 130"),
        ("Row 110", "Row 130"),
        ("__ROW131_REF__", "[row 131]"),
        ("skill-navigation-row-129", "skill-navigation-row-149"),
        ("[row 129]", "__ROW129_REF__"),
        ("[row 109]", "[row 129]"),
        ("row 129", "row 149"),
        ("Row 129", "Row 149"),
        ("__ROW129_REF__", "[row 149]"),
        (
            "Row 68 → Row 90 DDD meta prelude reunion index (row 110)",
            "Row 68 → Row 110 DDD meta prelude capstone reunion index (row 130)",
        ),
        (
            "row68-row90-ddd-meta-prelude-reunion-index-row-110",
            "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150",
        ),
        (
            "when Burgers geometry is clear on the capstone path but Peach–Köhler force derivations feel disconnected from the slip-line Lab act after row 129",
            "when Burgers geometry is clear on the capstone path but Peach–Köhler force derivations feel disconnected from the slip-line Lab act after row 149",
        ),
        ("memory sheet row 130 baby picture", "memory sheet row 150 baby picture"),
        ("prologue row 130 closing stitch", "prologue row 150 closing stitch"),
        ("prologue row 130 preview", "prologue row 150 preview"),
        ("Row 130 closes the", "Row 150 closes the"),
        ("Row 130 does not conflate", "Row 150 does not conflate"),
        ("(row 130)", "(row 150)"),
        ("__ROW131_LOOP__", "Row 131 closing loop"),
        ("__ROW131_LOOP_ANCHOR__", "row-131-closing-loop"),
        ("__ROW131_STITCH__", "Row 131 closing stitch"),
        ("__ROW131_STITCH_ANCHOR__", "row-131-closing-stitch"),
        ("__ROW131_PREVIEW__", "prologue-preview-row-131"),
        ("__ROW131_PREVIEW_TEXT__", "Row 131 preview"),
        ("__ROW131_SKILL__", "Row 131 skill checkpoint"),
        ("__ROW131_SKILL_NAV__", "skill-navigation-row-131"),
        ("__ROW131_MEM__", "memory sheet row 131"),
        ("__ROW131_BABY__", "Row 131 baby picture"),
        ("__ROW131_AUDIT__", "Row 131 three-way audit"),
        (
            "verified taxonomy meta prelude capstone closure (row 129)",
            "verified taxonomy meta prelude capstone closure (row 149)",
        ),
        ("When row 129 closed", "When row 149 closed"),
        ("after row 129 alone", "after row 149 alone"),
        ("Recite [preface row 129]", "Recite [preface row 149]"),
        (
            "when row 129 closed but row 50 VII.1 → VII.2 reunion still feels like OpenDiS homework disconnected from verified taxonomy meta prelude capstone on the capstone path",
            "when row 149 closed but row 50 VII.1 → VII.2 reunion still feels like OpenDiS homework disconnected from verified taxonomy meta prelude capstone on the capstone path",
        ),
        (
            "when row 129 and row 50 both verify individually",
            "when row 149 and row 50 both verify individually",
        ),
        (
            "rear-view mirror of row 129's Burgers → segment-network turn",
            "rear-view mirror of row 149's Burgers → segment-network turn",
        ),
        (
            "read row 68 gate + row 129 or row 110 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud when Burgers taxonomy is clean on the capstone path but OpenDiS decks feel like DDD homework after verified taxonomy meta prelude capstone",
            "read row 68 gate + row 149 or row 130 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud when taxonomy meta prelude capstone is clean on the capstone path after verified Burgers closure but OpenDiS decks feel like DDD homework at the Peach–Köhler knee",
        ),
        (
            "Confirm [row 129](preface.md#skill-navigation-row-129) or [Row 68 → Row 90 DDD meta prelude reunion index (row 110)](appendix/sources.md#row68-row90-ddd-meta-prelude-reunion-index-row-110) recited",
            "Confirm [row 149](preface.md#skill-navigation-row-149) or [Row 68 → Row 110 DDD meta prelude capstone reunion index (row 130)](appendix/sources.md#row68-row110-ddd-meta-prelude-capstone-reunion-index-row-130) recited",
        ),
        (
            "Row 130 does not replace row 68, row 50, row 129, row 110, row 90, row 49, or row 32",
            "Row 150 does not replace row 68, row 50, row 149, row 130, row 110, row 90, or row 32",
        ),
        (
            "[row 129](preface.md#skill-navigation-row-129) or [row 110](preface.md#skill-navigation-row-110)",
            "[row 149](preface.md#skill-navigation-row-149) or [row 130](preface.md#skill-navigation-row-130)",
        ),
        (
            "When row 130 is complete, proceed to [row 131]",
            "When row 150 is complete, proceed to [row 131](preface.md#skill-navigation-row-131) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path, "
            "to [row 130](preface.md#skill-navigation-row-130) when taxonomy meta prelude capstone is clean but DDD meta prelude still lags on the opening-hinge path, "
            "to [row 110](preface.md#skill-navigation-row-110) for the Row 68 ↔ Row 50 DDD meta prelude audit on the opening-hinge prelude path alone, "
            "to [row 149](preface.md#skill-navigation-row-149) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the capstone path, "
            "to [row 129](preface.md#skill-navigation-row-129) when midpoint meta prelude capstone is clean but taxonomy meta prelude still lags on the opening-hinge path, "
            "to [row 50](preface.md#skill-navigation-row-50) for the VII.1 → VII.2 meta audit alone, "
            "to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_130",
        ),
        (
            "Proceed to [row 131](#row-131-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 130",
            "Proceed to [row 131](#row-131-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 150 on the capstone path, "
            "to [row 130](#row-130-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 131](preface.md#skill-navigation-row-131) before row 51 closes on the capstone path",
            "when opening [row 131](preface.md#skill-navigation-row-131) before row 51 closes on the capstone path",
        ),
        (
            "When row 50 feels like OpenDiS homework after row 129 alone on the capstone path",
            "When row 50 feels like OpenDiS homework after row 149 alone on the capstone path",
        ),
        (
            "row 130 (row 68 ↔ row 50 reunion on the capstone path) with row 110",
            "row 150 (row 68 ↔ row 50 reunion on the capstone path) with row 130",
        ),
        (
            "row 130 (row 68 ↔ row 50 reunion on the capstone path) with row 110 (opening-hinge prelude stitch alone)",
            "row 150 (row 68 ↔ row 50 reunion on the capstone path) with row 130 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 130 names **why that reunion must follow verified taxonomy meta prelude capstone (row 129)",
            "row 150 names **why that reunion must follow verified taxonomy meta prelude capstone (row 149)",
        ),
        ("row 129 closed taxonomy", "row 149 closed taxonomy"),
        ("Row 68 → Row 50 meta (row 110)", "Row 68 → Row 50 meta (row 130)"),
        ("[Preface row 130]", "[Preface row 150]"),
        (
            "Row 68 → Row 110 DDD meta prelude capstone reunion index (row 130)",
            "Row 68 → Row 130 DDD meta prelude capstone reunion index (row 150)",
        ),
        (
            "Row 68 → Row 110 reunion index",
            "Row 68 → Row 130 reunion index",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_130" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_130.*", "", out, flags=re.S)
    return out


def add_row_150() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-150" in preface and "### Row 150 skill checkpoint" in preface:
        print("preface: row 150 already present")
    else:
        m130 = re.search(
            r"(### Row 130 skill checkpoint.*?)(?=\n### Row 131 skill checkpoint)",
            preface,
            re.S,
        )
        if not m130:
            raise SystemExit("row 130 preface checkpoint missing")
        row150 = lift_130_to_150(m130.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row150 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 150")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-150-closing-loop" not in ep:
        block130 = extract_between(ep, "### Row 130 closing loop", "### Row 129 closing loop")
        block150 = lift_130_to_150(block130)
        ep = ep.replace("### Row 149 closing loop", block150 + "### Row 149 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 150 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion (row 150) |"
    )
    if compass_line not in pro:
        line149 = (
            "| Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 149) |"
        )
        idx149 = pro.find(line149)
        if idx149 < 0:
            raise SystemExit("prologue compass row 149 not found")
        line_end149 = pro.find("\n", idx149)
        line130 = (
            "| Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion (row 130) |"
        )
        idx130 = pro.find(line130)
        if idx130 < 0:
            raise SystemExit("prologue compass row 130 not found")
        line_end130 = pro.find("\n", idx130)
        compass150 = lift_130_to_150(pro[idx130:line_end130]) + "\n"
        pro = pro[: line_end149 + 1] + compass150 + pro[line_end149 + 1 :]
        preview130 = extract_between(
            pro,
            '| <span id="prologue-preview-row-130"></span>',
            '\n| <span id="prologue-preview-row-129"></span>',
        )
        preview150 = lift_130_to_150(preview130)
        pro = pro.replace(
            '| <span id="prologue-preview-row-130"></span>',
            preview150 + '| <span id="prologue-preview-row-130"></span>',
            1,
        )
        if "row-150-closing-stitch" not in pro:
            stitch = (
                "**Row 150 closing stitch (Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion).** {#row-150-closing-stitch} "
                "When row 149 closed — taxonomy meta prelude capstone verified, row 148 or row 129 recited on the capstone path, and VII.0 Bridge → VII.1 taxonomy recited with slip-line Lab act classified line defects — "
                "but **row 50 VII.1 → VII.2 opening hinge still opens like standalone OpenDiS homework after the slip-line Lab act on the capstone path** — "
                "the [preface row 150 When-to-pause opening sentence](../preface.md#skill-navigation-row-150) names the dual reunion before homogenization meta prelude reunion; "
                "read [preface row 150](../preface.md#skill-navigation-row-150), then the "
                "[Row 68 → Row 130 reunion index](../appendix/sources.md#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150), then "
                "[epilogue row 150 closing loop](../epilogue/multiscale.md#row-150-closing-loop) before row 51 homogenization meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 149 closing stitch", stitch + "**Row 149 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 150 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150" not in src:
        block110 = extract_between(
            src,
            "## Row 68 → Row 90 Row 68 → Row 50 DDD meta prelude reunion index (row 110)",
            "## Row 68 → Row 91 Row 68 → Row 51 homogenization meta prelude reunion index (row 111)",
        )
        block150 = lift_130_to_150(lift_110_to_130(block110))
        table_row = (
            "| 150 | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone (midpoint prelude gate ↔ taxonomy meta prelude capstone ↔ row 50 meta) | "
            "[Row 68 → Row 130 DDD meta prelude capstone reunion index](#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150) · "
            "[preface row 150](../preface.md#skill-navigation-row-150) · "
            "[prologue row 150 preview](../prologue/00-many-scales.md#prologue-preview-row-150) · "
            "[prologue row 150 closing stitch](../prologue/00-many-scales.md#row-150-closing-stitch) · "
            "[epilogue row 150 closing loop](../epilogue/multiscale.md#row-150-closing-loop) · "
            "[memory sheet row 150 baby picture](memory-sheet.md#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 50 VII.1 → VII.2 opening hinge still feels disconnected from verified taxonomy meta prelude capstone on the capstone path** — "
            "read row 68 + row 149 or row 130 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
            "[preface row 50](../preface.md#skill-navigation-row-50) |\n"
        )
        src = src.replace(
            "| 149 | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone",
            table_row + "| 149 | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)",
            block150 + "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)",
        )
        extra = (
            "[row 149](#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150) reunites **taxonomy meta prelude capstone with the DDD meta prelude capstone boundary** "
            "when row 149 closed taxonomy meta prelude capstone at verified Burgers closure on the capstone path but VII.1 Bridge and row 50 still read like separate courses after verified DDD meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 148](#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149) reunites **midpoint meta prelude capstone with the taxonomy meta prelude capstone boundary** "
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 150 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-150-baby-picture" not in mem:
        baby130 = extract_between(mem, "### Row 130 baby picture", "### Row 131 baby picture")
        baby150 = lift_130_to_150(baby130)
        mem = mem.replace("### Row 130 baby picture", baby150 + "### Row 130 baby picture", 1)
        mem_table = (
            "| 150 | Meta | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion | "
            "[Row 68 → Row 130 DDD meta prelude capstone reunion index](sources.md#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150) · "
            "[preface row 150 skill checkpoint](../preface.md#skill-navigation-row-150) · "
            "[prologue row 150 preview](../prologue/00-many-scales.md#prologue-preview-row-150) · "
            "[prologue row 150 closing stitch](../prologue/00-many-scales.md#row-150-closing-stitch) · "
            "[epilogue row 150 closing loop](../epilogue/multiscale.md#row-150-closing-loop) | "
            "Row 68 closed but row 50 VII.1 → VII.2 opening hinge feels disconnected from verified taxonomy meta prelude capstone on the capstone path — "
            "read row 68 + row 149 or row 130 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
            "[row 150 baby picture](#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 149 | Meta | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion |",
            mem_table + "| 149 | Meta | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion |",
        )
        if "When row 149 closed but DDD meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 148 closed but taxonomy meta reunion still lags on the capstone path, switch to [row 149](#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion).",
                "When row 148 closed but taxonomy meta reunion still lags on the capstone path, switch to [row 149](#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion). "
                "When row 149 closed but DDD meta reunion still lags on the capstone path, switch to [row 150](#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 150")
    else:
        print("memory-sheet: row 150 baby already present")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    old = (
        "Proceed to [row 130](#row-130-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 149 on the capstone path"
    )
    new = (
        "Proceed to [row 150](#row-150-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 149 on the capstone path"
    )
    if old in ep:
        ep = ep.replace(old, new)
        ep_path.write_text(ep)
        print("epilogue: row 149 → row 150 proceed link")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    old_p = (
        "Read the [memory sheet row 149 baby picture](appendix/memory-sheet.md#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion) when opening [row 130](preface.md#skill-navigation-row-130) before row 50 closes on the capstone path"
    )
    new_p = (
        "Read the [memory sheet row 149 baby picture](appendix/memory-sheet.md#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion) when opening [row 150](preface.md#skill-navigation-row-150) before row 51 closes on the capstone path"
    )
    if old_p in preface:
        preface = preface.replace(old_p, new_p)
        preface_path.write_text(preface)
        print("preface: row 149 → row 150 memory sheet pointer")

    old_p2 = (
        "When row 149 is complete, proceed to [row 130](preface.md#skill-navigation-row-130) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path"
    )
    new_p2 = (
        "When row 149 is complete, proceed to [row 150](preface.md#skill-navigation-row-150) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path"
    )
    if old_p2 in preface:
        preface = preface.replace(old_p2, new_p2)
        preface_path.write_text(preface)
        print("preface: row 149 proceed → row 150")


def main() -> None:
    add_row_150()


if __name__ == "__main__":
    main()
