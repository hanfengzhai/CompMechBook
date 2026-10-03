#!/usr/bin/env python3
"""Add row 149 (Row 68 → Row 129 ↔ Row 49 taxonomy meta prelude capstone on capstone path)."""
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


def lift_89_to_109(s: str) -> str:
    """Promote opening-hinge row 109 sources index to capstone row 129 wording."""
    p = [
        (
            "Row 68 → Row 89 Row 68 → Row 49 taxonomy meta prelude reunion",
            "Row 68 → Row 109 Row 68 → Row 49 taxonomy meta prelude capstone reunion",
        ),
        (
            "row68-row89-taxonomy-meta-prelude-reunion-index-row-109",
            "row68-row109-taxonomy-meta-prelude-capstone-reunion-index-row-129",
        ),
        (
            "row-109-baby-picture-row68-row89-taxonomy-meta-prelude-reunion",
            "row-129-baby-picture-row68-row109-taxonomy-meta-prelude-capstone-reunion",
        ),
        ("Row 109 names", "Row 129 names"),
        ("Row 109 does not replace", "Row 129 does not replace"),
        ("(row 109)", "(row 129)"),
        ("skill-navigation-row-109", "skill-navigation-row-129"),
        ("preface row 109", "preface row 129"),
        ("Preface row 109", "Preface row 129"),
        ("memory sheet row 109", "memory sheet row 129"),
        ("Row 109 baby picture", "Row 129 baby picture"),
        ("row 108 verified", "row 128 verified"),
        ("[row 108]", "__ROW108_REF__"),
        ("row 108", "row 128"),
        ("Row 108", "Row 128"),
        ("__ROW108_REF__", "[row 128]"),
        ("[row 107]", "__ROW107_REF__"),
        ("row 107", "row 127"),
        ("Row 107", "Row 127"),
        ("__ROW107_REF__", "[row 127]"),
        (
            "midpoint meta capstone / taxonomy opening prelude",
            "midpoint meta prelude capstone / taxonomy meta prelude",
        ),
        ("midpoint meta capstone", "midpoint meta prelude capstone"),
        ("taxonomy meta capstone", "taxonomy meta prelude capstone"),
        (
            "taxonomy meta capstone boundary",
            "taxonomy meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        (
            "taxonomy meta reunion",
            "taxonomy meta prelude capstone reunion",
        ),
        ("row 107 verified fvm", "row 127 verified twin-ladder"),
        ("on Cauchy stress", "on the capstone path"),
    ]
    return tx(s, p)


def lift_129_to_149(s: str) -> str:
    p = [
        ("Row 130 closing loop", "__ROW130_LOOP__"),
        ("Row 129 closing loop", "Row 149 closing loop"),
        ("row-130-closing-loop", "__ROW130_LOOP_ANCHOR__"),
        ("row-129-closing-loop", "row-149-closing-loop"),
        ("Row 130 closing stitch", "__ROW130_STITCH__"),
        ("Row 129 closing stitch", "Row 149 closing stitch"),
        ("row-130-closing-stitch", "__ROW130_STITCH_ANCHOR__"),
        ("row-129-closing-stitch", "row-149-closing-stitch"),
        ("prologue-preview-row-130", "__ROW130_PREVIEW__"),
        ("prologue-preview-row-129", "prologue-preview-row-149"),
        ("Row 130 preview", "__ROW130_PREVIEW_TEXT__"),
        ("Row 129 preview", "Row 149 preview"),
        ("Row 130 skill checkpoint", "__ROW130_SKILL__"),
        ("Row 129 skill checkpoint", "Row 149 skill checkpoint"),
        ("skill-navigation-row-130", "__ROW130_SKILL_NAV__"),
        ("skill-navigation-row-129", "skill-navigation-row-149"),
        ("memory sheet row 130", "__ROW130_MEM__"),
        ("memory sheet row 129", "memory sheet row 149"),
        ("Row 130 baby picture", "__ROW130_BABY__"),
        ("Row 129 baby picture", "Row 149 baby picture"),
        ("Row 130 three-way audit", "__ROW130_AUDIT__"),
        ("Row 129 three-way audit", "Row 149 three-way audit"),
        (
            "Row 68 → Row 109 Row 68 → Row 49 taxonomy meta prelude capstone",
            "Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone",
        ),
        (
            "row68-row109-taxonomy-meta-prelude-capstone-reunion-index-row-129",
            "row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149",
        ),
        (
            "row-129-baby-picture-row68-row109-taxonomy-meta-prelude-capstone-reunion",
            "row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion",
        ),
        ("[row 130]", "__ROW130_REF__"),
        ("[row 110]", "[row 130]"),
        ("row 110", "row 130"),
        ("Row 110", "Row 130"),
        ("__ROW130_REF__", "[row 130]"),
        ("skill-navigation-row-109", "skill-navigation-row-129"),
        ("[row 129]", "__ROW129_REF__"),
        ("[row 109]", "[row 129]"),
        ("row 109", "row 129"),
        ("Row 109", "Row 129"),
        ("__ROW129_REF__", "[row 129]"),
        ("skill-navigation-row-128", "skill-navigation-row-148"),
        ("[row 128]", "__ROW128_REF__"),
        ("[row 108]", "[row 148]"),
        ("row 128", "row 148"),
        ("Row 128", "Row 148"),
        ("__ROW128_REF__", "[row 148]"),
        (
            "Row 68 → Row 89 taxonomy meta prelude reunion index (row 109)",
            "Row 68 → Row 109 taxonomy meta prelude capstone reunion index (row 129)",
        ),
        (
            "row68-row89-taxonomy-meta-prelude-reunion-index-row-109",
            "row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149",
        ),
        (
            "when forest landing is clean on the capstone path but Burgers circuits feel disconnected from return-mapping after row 128",
            "when forest landing is clean on the capstone path but Burgers circuits feel disconnected from return-mapping after row 148",
        ),
        ("memory sheet row 129 baby picture", "memory sheet row 149 baby picture"),
        ("prologue row 129 closing stitch", "prologue row 149 closing stitch"),
        ("prologue row 129 preview", "prologue row 149 preview"),
        ("Row 129 closes the", "Row 149 closes the"),
        ("Row 129 does not conflate", "Row 149 does not conflate"),
        ("(row 129)", "(row 149)"),
        ("__ROW130_LOOP__", "Row 130 closing loop"),
        ("__ROW130_LOOP_ANCHOR__", "row-130-closing-loop"),
        ("__ROW130_STITCH__", "Row 130 closing stitch"),
        ("__ROW130_STITCH_ANCHOR__", "row-130-closing-stitch"),
        ("__ROW130_PREVIEW__", "prologue-preview-row-130"),
        ("__ROW130_PREVIEW_TEXT__", "Row 130 preview"),
        ("__ROW130_SKILL__", "Row 130 skill checkpoint"),
        ("__ROW130_SKILL_NAV__", "skill-navigation-row-130"),
        ("__ROW130_MEM__", "memory sheet row 130"),
        ("__ROW130_BABY__", "Row 130 baby picture"),
        ("__ROW130_AUDIT__", "Row 130 three-way audit"),
        (
            "verified midpoint meta prelude capstone closure (row 128)",
            "verified midpoint meta prelude capstone closure (row 148)",
        ),
        ("When row 128 closed", "When row 148 closed"),
        ("after row 128 alone", "after row 148 alone"),
        ("Recite [preface row 128]", "Recite [preface row 148]"),
        (
            "when row 128 closed but row 49 VII.0 → VII.1 reunion still feels like Defects Notes homework disconnected from verified midpoint meta prelude capstone on the capstone path",
            "when row 148 closed but row 49 VII.0 → VII.1 reunion still feels like Defects Notes homework disconnected from verified midpoint meta prelude capstone on the capstone path",
        ),
        (
            "when row 128 and row 49 both verify individually",
            "when row 148 and row 49 both verify individually",
        ),
        (
            "rear-view mirror of row 128's forest landing → Burgers turn",
            "rear-view mirror of row 148's forest landing → Burgers turn",
        ),
        (
            "read row 68 gate + row 128 or row 109 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when forest landing is clean on the capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone",
            "read row 68 gate + row 148 or row 129 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when midpoint meta prelude capstone is clean on the capstone path after verified forest landing but Burgers circuits feel like Defects Notes homework at the taxonomy knee",
        ),
        (
            "Confirm [row 128](preface.md#skill-navigation-row-128) or [Row 68 → Row 89 taxonomy meta prelude reunion index (row 109)](appendix/sources.md#row68-row89-taxonomy-meta-prelude-reunion-index-row-109) recited",
            "Confirm [row 148](preface.md#skill-navigation-row-148) or [Row 68 → Row 109 taxonomy meta prelude capstone reunion index (row 129)](appendix/sources.md#row68-row109-taxonomy-meta-prelude-capstone-reunion-index-row-129) recited",
        ),
        (
            "Row 129 does not replace row 68, row 49, row 128, row 109, row 89, row 88, row 48, or row 32",
            "Row 149 does not replace row 68, row 49, row 148, row 129, row 109, row 89, row 88, row 48, or row 32",
        ),
        (
            "[row 128](preface.md#skill-navigation-row-128) or [row 109](preface.md#skill-navigation-row-109)",
            "[row 148](preface.md#skill-navigation-row-148) or [row 129](preface.md#skill-navigation-row-129)",
        ),
        (
            "When row 129 is complete, proceed to [row 130]",
            "When row 149 is complete, proceed to [row 130](preface.md#skill-navigation-row-130) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, "
            "to [row 129](preface.md#skill-navigation-row-129) when midpoint meta prelude capstone is clean but taxonomy meta prelude still lags on the opening-hinge path, "
            "to [row 109](preface.md#skill-navigation-row-109) for the Row 68 ↔ Row 49 taxonomy meta prelude audit on the opening-hinge prelude path alone, "
            "to [row 148](preface.md#skill-navigation-row-148) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the capstone path, "
            "to [row 128](preface.md#skill-navigation-row-128) when part-boundary meta prelude capstone is clean but midpoint meta prelude still lags on the opening-hinge path, "
            "to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, "
            "to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_129",
        ),
        (
            "Proceed to [row 130](#row-130-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 129",
            "Proceed to [row 130](#row-130-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 149 on the capstone path, "
            "to [row 129](#row-129-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 130](preface.md#skill-navigation-row-130) before row 50 closes on the capstone path",
            "when opening [row 130](preface.md#skill-navigation-row-130) before row 50 closes on the capstone path",
        ),
        (
            "When row 49 feels like Defects Notes homework after row 128 alone on the capstone path",
            "When row 49 feels like Defects Notes homework after row 148 alone on the capstone path",
        ),
        (
            "row 129 (row 68 ↔ row 49 reunion on the capstone path) with row 109",
            "row 149 (row 68 ↔ row 49 reunion on the capstone path) with row 129",
        ),
        (
            "row 129 (row 68 ↔ row 49 reunion on the capstone path) with row 109 (opening-hinge prelude stitch alone)",
            "row 149 (row 68 ↔ row 49 reunion on the capstone path) with row 129 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 129 names **why that reunion must follow verified midpoint meta prelude capstone (row 128)",
            "row 149 names **why that reunion must follow verified midpoint meta prelude capstone (row 148)",
        ),
        ("row 128 closed midpoint", "row 148 closed midpoint"),
        ("Row 68 → Row 49 meta (row 109)", "Row 68 → Row 49 meta (row 129)"),
        ("[Preface row 129]", "[Preface row 149]"),
        (
            "Row 68 → Row 89 Row 68 → Row 49 taxonomy meta prelude reunion index (row 109)",
            "Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_129" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_129.*", "", out, flags=re.S)
    return out


def add_row_149() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-149" in preface and "### Row 149 skill checkpoint" in preface:
        print("preface: row 149 already present")
    else:
        m129 = re.search(
            r"(### Row 129 skill checkpoint.*?)(?=\n### Row 130 skill checkpoint)",
            preface,
            re.S,
        )
        if not m129:
            raise SystemExit("row 129 preface checkpoint missing")
        row149 = lift_129_to_149(m129.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row149 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 149")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-149-closing-loop" not in ep:
        block129 = extract_between(ep, "### Row 129 closing loop", "### Row 128 closing loop")
        block149 = lift_129_to_149(block129)
        ep = ep.replace("### Row 148 closing loop", block149 + "### Row 148 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 149 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 149) |"
    )
    if compass_line not in pro:
        line148 = (
            "| Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 148) |"
        )
        idx148 = pro.find(line148)
        if idx148 < 0:
            raise SystemExit("prologue compass row 148 not found")
        line_end148 = pro.find("\n", idx148)
        line129 = (
            "| Row 68 → Row 109 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 129) |"
        )
        idx129 = pro.find(line129)
        if idx129 < 0:
            raise SystemExit("prologue compass row 129 not found")
        line_end129 = pro.find("\n", idx129)
        compass149 = lift_129_to_149(pro[idx129:line_end129]) + "\n"
        pro = pro[: line_end148 + 1] + compass149 + pro[line_end148 + 1 :]
        preview129 = extract_between(
            pro,
            '| <span id="prologue-preview-row-129"></span>',
            '\n| <span id="prologue-preview-row-130"></span>',
        )
        preview149 = lift_129_to_149(preview129)
        pro = pro.replace(
            '| <span id="prologue-preview-row-129"></span>',
            preview149 + '| <span id="prologue-preview-row-129"></span>',
            1,
        )
        if "row-149-closing-stitch" not in pro:
            stitch = (
                "**Row 149 closing stitch (Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-149-closing-stitch} "
                "When row 148 closed — midpoint meta prelude capstone verified, row 147 or row 128 recited on the capstone path, and intermission → VII.0 landing recited with `hardening.yaml` beside Act IV — "
                "but **row 49 VII.0 → VII.1 opening hinge still opens like standalone Defects Notes homework after the forest Scene on the capstone path** — "
                "the [preface row 149 When-to-pause opening sentence](../preface.md#skill-navigation-row-149) names the dual reunion before DDD meta prelude reunion; "
                "read [preface row 149](../preface.md#skill-navigation-row-149), then the "
                "[Row 68 → Row 129 reunion index](../appendix/sources.md#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149), then "
                "[epilogue row 149 closing loop](../epilogue/multiscale.md#row-149-closing-loop) before row 50 DDD meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 129 closing stitch", stitch + "**Row 129 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 149 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149" not in src:
        block109 = extract_between(
            src,
            "## Row 68 → Row 89 Row 68 → Row 49 taxonomy meta prelude reunion index (row 109)",
            "## Row 68 → Row 90 Row 68 → Row 50 DDD meta prelude reunion index (row 110)",
        )
        block149 = lift_129_to_149(lift_89_to_109(block109))
        table_row = (
            "| 149 | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone (midpoint prelude gate ↔ midpoint meta prelude capstone ↔ row 49 meta) | "
            "[Row 68 → Row 129 taxonomy meta prelude capstone reunion index](#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149) · "
            "[preface row 149](../preface.md#skill-navigation-row-149) · "
            "[prologue row 149 preview](../prologue/00-many-scales.md#prologue-preview-row-149) · "
            "[prologue row 149 closing stitch](../prologue/00-many-scales.md#row-149-closing-stitch) · "
            "[epilogue row 149 closing loop](../epilogue/multiscale.md#row-149-closing-loop) · "
            "[memory sheet row 149 baby picture](memory-sheet.md#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 49 VII.0 → VII.1 opening hinge still feels disconnected from verified midpoint meta prelude capstone on the capstone path** — "
            "read row 68 + row 148 or row 129 gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
            "[preface row 49](../preface.md#skill-navigation-row-49) |\n"
        )
        src = src.replace(
            "| 148 | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone",
            table_row + "| 148 | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)",
            block149 + "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)",
        )
        extra = (
            "[row 148](#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149) reunites **midpoint meta prelude capstone with the taxonomy meta prelude capstone boundary** "
            "when row 148 closed midpoint meta prelude capstone at verified forest landing on the capstone path but VII.0 Bridge and row 49 still read like separate courses after verified taxonomy meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 147](#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148) reunites **part-boundary meta prelude capstone with the midpoint meta prelude capstone boundary** "
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 149 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-149-baby-picture" not in mem:
        baby129 = extract_between(mem, "### Row 129 baby picture", "### Row 130 baby picture")
        baby149 = lift_129_to_149(baby129)
        mem = mem.replace("### Row 129 baby picture", baby149 + "### Row 129 baby picture", 1)
        mem_table = (
            "| 149 | Meta | Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion | "
            "[Row 68 → Row 129 taxonomy meta prelude capstone reunion index](sources.md#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-149) · "
            "[preface row 149 skill checkpoint](../preface.md#skill-navigation-row-149) · "
            "[prologue row 149 preview](../prologue/00-many-scales.md#prologue-preview-row-149) · "
            "[prologue row 149 closing stitch](../prologue/00-many-scales.md#row-149-closing-stitch) · "
            "[epilogue row 149 closing loop](../epilogue/multiscale.md#row-149-closing-loop) | "
            "Row 68 closed but row 49 VII.0 → VII.1 opening hinge feels disconnected from verified midpoint meta prelude capstone on the capstone path — "
            "read row 68 + row 148 or row 129 gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49; "
            "[row 149 baby picture](#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 148 | Meta | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion |",
            mem_table + "| 148 | Meta | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion |",
        )
        if "When row 148 closed but taxonomy meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 147 closed but midpoint meta reunion still lags on the capstone path, switch to [row 148](#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion).",
                "When row 147 closed but midpoint meta reunion still lags on the capstone path, switch to [row 148](#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion). "
                "When row 148 closed but taxonomy meta reunion still lags on the capstone path, switch to [row 149](#row-149-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 149")
    else:
        print("memory-sheet: row 149 baby already present")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    old = (
        "Proceed to [row 129](#row-129-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 148 on the capstone path"
    )
    new = (
        "Proceed to [row 149](#row-149-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 148 on the capstone path"
    )
    if old in ep:
        ep = ep.replace(old, new)
        ep_path.write_text(ep)
        print("epilogue: row 148 → row 149 proceed link")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    old_p = (
        "Read the [memory sheet row 148 baby picture](appendix/memory-sheet.md#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion) when opening [row 129](preface.md#skill-navigation-row-129) before row 49 closes on the capstone path"
    )
    new_p = (
        "Read the [memory sheet row 148 baby picture](appendix/memory-sheet.md#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion) when opening [row 149](preface.md#skill-navigation-row-149) before row 49 closes on the capstone path"
    )
    if old_p in preface:
        preface = preface.replace(old_p, new_p)
        preface_path.write_text(preface)
        print("preface: row 148 → row 149 memory sheet pointer")


def main() -> None:
    add_row_149()


if __name__ == "__main__":
    main()
