#!/usr/bin/env python3
"""Add row 151 (Row 68 → Row 131 ↔ Row 51 homogenization meta prelude capstone on capstone path)."""
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


def lift_111_to_131(s: str) -> str:
    """Promote opening-hinge row 111 sources index to capstone row 131 wording."""
    p = [
        (
            "Row 68 → Row 91 Row 68 → Row 51 homogenization meta prelude reunion",
            "Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion",
        ),
        (
            "row68-row91-homogenization-meta-prelude-reunion-index-row-111",
            "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131",
        ),
        (
            "row-111-baby-picture-row68-row91-homogenization-meta-prelude-reunion",
            "row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion",
        ),
        ("Row 111 names", "Row 131 names"),
        ("Row 111 does not replace", "Row 131 does not replace"),
        ("(row 111)", "(row 131)"),
        ("skill-navigation-row-111", "skill-navigation-row-131"),
        ("preface row 111", "preface row 131"),
        ("Preface row 111", "Preface row 131"),
        ("memory sheet row 111", "memory sheet row 131"),
        ("Row 111 baby picture", "Row 131 baby picture"),
        ("[row 110]", "__ROW110_REF__"),
        ("row 110", "row 130"),
        ("Row 110", "Row 130"),
        ("__ROW110_REF__", "[row 130]"),
        (
            "DDD meta capstone / homogenization opening prelude",
            "DDD meta prelude capstone / homogenization meta prelude",
        ),
        ("DDD meta capstone", "DDD meta prelude capstone"),
        (
            "homogenization meta capstone boundary",
            "homogenization meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        ("homogenization meta reunion", "homogenization meta prelude capstone reunion"),
        ("homogenization meta capstone", "homogenization meta prelude capstone"),
        ("inside the coupling gate", "inside the coupling gate on the capstone path"),
    ]
    return tx(s, p)


def lift_131_to_151(s: str) -> str:
    p = [
        ("skill-navigation-row-131", "skill-navigation-row-151"),
        ("### Row 131 skill checkpoint", "### Row 151 skill checkpoint"),
        ("Row 131 does not replace", "Row 151 does not replace"),
        ("Row 131 three-way audit", "Row 151 three-way audit"),
        ("Row 131 closing loop", "Row 151 closing loop"),
        ("row-131-closing-loop", "row-151-closing-loop"),
        ("Row 131 closing stitch", "Row 151 closing stitch"),
        ("row-131-closing-stitch", "row-151-closing-stitch"),
        ("prologue-preview-row-131", "prologue-preview-row-151"),
        ("Row 131 preview", "Row 151 preview"),
        ("Row 131 skill checkpoint", "Row 151 skill checkpoint"),
        ("memory sheet row 131", "memory sheet row 151"),
        ("Row 131 baby picture", "Row 151 baby picture"),
        (
            "Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone",
            "Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone",
        ),
        (
            "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131",
            "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        ),
        (
            "row-131-baby-picture-row68-row111-homogenization-meta-prelude-capstone-reunion",
            "row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion",
        ),
        ("[row 132]", "__ROW132_REF__"),
        ("[row 111]", "[row 131]"),
        ("row 111", "row 131"),
        ("Row 111", "Row 131"),
        ("__ROW132_REF__", "[row 132]"),
        ("[row 130]", "[row 150]"),
        ("row 130", "row 150"),
        ("Row 130", "Row 150"),
        (
            "Row 68 → Row 91 homogenization meta prelude reunion index (row 111)",
            "Row 68 → Row 111 homogenization meta prelude capstone reunion index (row 131)",
        ),
        (
            "row68-row91-homogenization-meta-prelude-reunion-index-row-111",
            "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
        ),
        (
            "verified DDD meta prelude capstone closure (row 130)",
            "verified DDD meta prelude capstone closure (row 150)",
        ),
        ("when row 130 closed but row 51", "when row 150 closed but row 51"),
        ("after row 130.", "after row 150."),
        ("when row 130 and row 51", "when row 150 and row 51"),
        (
            "rear-view mirror of row 130's Peach–Köhler → spool turn",
            "rear-view mirror of row 150's Peach–Köhler → spool turn",
        ),
        (
            "when opening [row 132](preface.md#skill-navigation-row-132) before row 52 closes on the capstone path",
            "when opening [row 151](preface.md#skill-navigation-row-151) before row 52 closes on the capstone path",
        ),
        (
            "When row 131 is complete, proceed to [row 132](preface.md#skill-navigation-row-132) when homogenization meta prelude capstone is clean but atomistic meta prelude capstone still lags after verified polycrystal closure on the capstone path, to [row 112](preface.md#skill-navigation-row-112) when homogenization meta prelude capstone is clean but atomistic meta capstone still lags after verified polycrystal closure on the opening-hinge path, to [row 111](preface.md#skill-navigation-row-111) for the Row 68 ↔ Row 51 homogenization meta prelude audit on the opening-hinge path alone, to [row 130](preface.md#skill-navigation-row-130) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, to [row 51](preface.md#skill-navigation-row-51) for the VII.2 → VII.3 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
            "When row 151 is complete, proceed to [row 132](preface.md#skill-navigation-row-132) when row 68 closed but atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the capstone path, to [row 131](preface.md#skill-navigation-row-131) when DDD meta prelude capstone is clean but homogenization meta prelude still lags on the opening-hinge path, to [row 111](preface.md#skill-navigation-row-111) for the Row 68 ↔ Row 51 homogenization meta prelude audit on the opening-hinge prelude path alone, to [row 150](preface.md#skill-navigation-row-150) when DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, to [row 130](preface.md#skill-navigation-row-130) when taxonomy meta prelude capstone is clean but DDD meta prelude still lags on the opening-hinge path, to [row 51](preface.md#skill-navigation-row-51) for the VII.2 → VII.3 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "Proceed to [row 132](#row-132-closing-loop) when row 68 closed but atomistic meta capstone still lags after row 131 on the capstone path",
            "Proceed to [row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 150 on the capstone path, "
            "to [row 131](#row-131-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge path",
        ),
        (
            "When row 51 feels like DAMASK homework after row 130 alone on the capstone path",
            "When row 51 feels like DAMASK homework after row 150 alone on the capstone path",
        ),
        (
            "row 131 (row 68 ↔ row 51 reunion on the capstone path) with row 111",
            "row 151 (row 68 ↔ row 51 reunion on the capstone path) with row 131",
        ),
        (
            "row 131 names **why that reunion must follow verified DDD meta prelude capstone (row 130)",
            "row 151 names **why that reunion must follow verified DDD meta prelude capstone (row 150)",
        ),
        ("Row 68 → Row 51 meta (row 111)", "Row 68 → Row 51 meta (row 131)"),
        (
            "Row 68 → Row 111 homogenization meta prelude capstone reunion index (row 131)",
            "Row 68 → Row 131 homogenization meta prelude capstone reunion index (row 151)",
        ),
        ("Row 68 → Row 111 reunion index", "Row 68 → Row 131 reunion index"),
        (
            "row68-row91-homogenization-meta-prelude-reunion-index-row-111",
            "row68-row111-homogenization-meta-prelude-capstone-reunion-index-row-131",
        ),
        ("(row 131)", "(row 151)"),
        ("Row 131 closes the", "Row 151 closes the"),
        ("Row 131 does not conflate", "Row 151 does not conflate"),
    ]
    return tx(s, p)


def add_row_151() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-151" in preface and "### Row 151 skill checkpoint" in preface:
        print("preface: row 151 already present")
    else:
        m131 = re.search(
            r"(### Row 131 skill checkpoint.*?)(?=\n### Row 132 skill checkpoint)",
            preface,
            re.S,
        )
        if not m131:
            raise SystemExit("row 131 preface checkpoint missing")
        row151 = lift_131_to_151(m131.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row151 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 151")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-151-closing-loop" not in ep:
        block131 = extract_between(ep, "### Row 131 closing loop", "### Row 130 closing loop")
        block151 = lift_131_to_151(block131)
        ep = ep.replace("### Row 150 closing loop", block151 + "### Row 150 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 151 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 151) |"
    )
    if compass_line not in pro:
        line150 = (
            "| Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion (row 150) |"
        )
        idx150 = pro.find(line150)
        if idx150 < 0:
            raise SystemExit("prologue compass row 150 not found")
        line_end150 = pro.find("\n", idx150)
        line131 = (
            "| Row 68 → Row 111 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 131) |"
        )
        idx131 = pro.find(line131)
        if idx131 < 0:
            raise SystemExit("prologue compass row 131 not found")
        line_end131 = pro.find("\n", idx131)
        compass151 = lift_131_to_151(pro[idx131:line_end131]) + "\n"
        pro = pro[: line_end150 + 1] + compass151 + pro[line_end150 + 1 :]
        preview131 = extract_between(
            pro,
            '| <span id="prologue-preview-row-131"></span>',
            '\n| <span id="prologue-preview-row-130"></span>',
        )
        preview151 = lift_131_to_151(preview131)
        pro = pro.replace(
            '| <span id="prologue-preview-row-131"></span>',
            preview151 + '| <span id="prologue-preview-row-131"></span>',
            1,
        )
        if "row-151-closing-stitch" not in pro:
            stitch = (
                "**Row 151 closing stitch (Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion).** {#row-151-closing-stitch} "
                "When row 150 closed — DDD meta prelude capstone verified, row 149 or row 130 recited on the capstone path, and VII.1 Bridge → VII.2 Peach–Köhler recited with forest-density Lab act linked \\(\\tau(\\gamma)\\) to Taylor hardening — "
                "but **row 51 VII.2 → VII.3 opening hinge still opens like standalone DAMASK homework after the post-yield forest Scene on the capstone path** — "
                "the [preface row 151 When-to-pause opening sentence](../preface.md#skill-navigation-row-151) names the dual reunion before the atomistic meta reunion; "
                "read [preface row 151](../preface.md#skill-navigation-row-151), then the "
                "[Row 68 → Row 131 reunion index](../appendix/sources.md#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151), then "
                "[epilogue row 151 closing loop](../epilogue/multiscale.md#row-151-closing-loop) before row 52 atomistic meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 150 closing stitch", stitch + "**Row 150 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 151 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151" not in src:
        block111 = extract_between(
            src,
            "## Row 68 → Row 91 Row 68 → Row 51 homogenization meta prelude reunion index (row 111)",
            "## Row 68 → Row 92 Row 68 → Row 52 atomistic meta prelude reunion index (row 112)",
        )
        block151 = lift_131_to_151(lift_111_to_131(block111))
        table_row = (
            "| 151 | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone (midpoint prelude gate ↔ DDD meta prelude capstone ↔ row 51 meta) | "
            "[Row 68 → Row 131 homogenization meta prelude capstone reunion index](#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151) · "
            "[preface row 151](../preface.md#skill-navigation-row-151) · "
            "[prologue row 151 preview](../prologue/00-many-scales.md#prologue-preview-row-151) · "
            "[prologue row 151 closing stitch](../prologue/00-many-scales.md#row-151-closing-stitch) · "
            "[epilogue row 151 closing loop](../epilogue/multiscale.md#row-151-closing-loop) · "
            "[memory sheet row 151 baby picture](memory-sheet.md#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 51 VII.2 → VII.3 opening hinge still feels disconnected from verified DDD meta prelude capstone on the capstone path** — "
            "read row 68 + row 150 or row 131 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
            "[preface row 51](../preface.md#skill-navigation-row-51) |\n"
        )
        src = src.replace(
            "| 150 | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone",
            table_row + "| 150 | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)",
            block151 + "## Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)",
        )
        extra = (
            "[row 150](#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151) reunites **DDD meta prelude capstone with the homogenization meta prelude capstone boundary** "
            "when row 150 closed DDD meta prelude capstone at verified Peach–Köhler closure on the capstone path but VII.2 Bridge and row 51 still read like separate courses after verified homogenization meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 149](#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150) reunites **taxonomy meta prelude capstone with the DDD meta prelude capstone boundary** "
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 151 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-151-baby-picture" not in mem:
        baby131 = extract_between(mem, "### Row 131 baby picture", "### Row 132 baby picture")
        baby151 = lift_131_to_151(baby131)
        mem = mem.replace("### Row 131 baby picture", baby151 + "### Row 131 baby picture", 1)
        mem_table = (
            "| 151 | Meta | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion | "
            "[Row 68 → Row 131 homogenization meta prelude capstone reunion index](sources.md#row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151) · "
            "[preface row 151 skill checkpoint](../preface.md#skill-navigation-row-151) · "
            "[prologue row 151 preview](../prologue/00-many-scales.md#prologue-preview-row-151) · "
            "[prologue row 151 closing stitch](../prologue/00-many-scales.md#row-151-closing-stitch) · "
            "[epilogue row 151 closing loop](../epilogue/multiscale.md#row-151-closing-loop) | "
            "Row 68 closed but row 51 VII.2 → VII.3 opening hinge feels disconnected from verified DDD meta prelude capstone on the capstone path — "
            "read row 68 + row 150 or row 131 gate + VII.2 Bridge → opening hinge → VII.3 homogenization + row 51; "
            "[row 151 baby picture](#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 150 | Meta | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion |",
            mem_table + "| 150 | Meta | Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion |",
        )
        if "When row 150 closed but homogenization meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 149 closed but DDD meta reunion still lags on the capstone path, switch to [row 150](#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion).",
                "When row 149 closed but DDD meta reunion still lags on the capstone path, switch to [row 150](#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion). "
                "When row 150 closed but homogenization meta reunion still lags on the capstone path, switch to [row 151](#row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 151")
    else:
        print("memory-sheet: row 151 baby already present")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    old = (
        "Proceed to [row 131](#row-131-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 150 on the capstone path"
    )
    new = (
        "Proceed to [row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 150 on the capstone path"
    )
    if old in ep:
        ep = ep.replace(old, new)
        ep_path.write_text(ep)
        print("epilogue: row 150 → row 151 proceed link")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    old_p = (
        "Read the [memory sheet row 150 baby picture](appendix/memory-sheet.md#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion) when opening [row 131](preface.md#skill-navigation-row-131) before row 51 closes on the capstone path"
    )
    new_p = (
        "Read the [memory sheet row 150 baby picture](appendix/memory-sheet.md#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion) when opening [row 151](preface.md#skill-navigation-row-151) before row 52 closes on the capstone path"
    )
    if old_p in preface:
        preface = preface.replace(old_p, new_p)
        preface_path.write_text(preface)
        print("preface: row 150 → row 151 memory sheet pointer")

    old_p2 = (
        "When row 150 is complete, proceed to [row 131](preface.md#skill-navigation-row-131) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path"
    )
    new_p2 = (
        "When row 150 is complete, proceed to [row 151](preface.md#skill-navigation-row-151) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path"
    )
    if old_p2 in preface:
        preface = preface.replace(old_p2, new_p2)
        preface_path.write_text(preface)
        print("preface: row 150 proceed → row 151")


def main() -> None:
    add_row_151()


if __name__ == "__main__":
    main()
