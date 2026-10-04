#!/usr/bin/env python3
"""Repair row 152 meta-stitch content and finish prologue/sources/memory inserts."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump(s: str) -> str:
    pairs = [
        ("Row 68 → Row 112 Row 68 → Row 52", "Row 68 → Row 132 Row 68 → Row 52"),
        ("row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132", "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152"),
        ("row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion", "row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion"),
        ("skill-navigation-row-132", "skill-navigation-row-152"),
        ("### Row 132 skill checkpoint", "### Row 152 skill checkpoint"),
        ("Row 132 does not replace", "Row 152 does not replace"),
        ("Row 132 three-way audit", "Row 152 three-way audit"),
        ("Row 132 closing loop", "Row 152 closing loop"),
        ("row-132-closing-loop", "row-152-closing-loop"),
        ("Row 132 closing stitch", "Row 152 closing stitch"),
        ("row-132-closing-stitch", "row-152-closing-stitch"),
        ("prologue-preview-row-132", "prologue-preview-row-152"),
        ("Row 132 preview", "Row 152 preview"),
        ("memory sheet row 132", "memory sheet row 152"),
        ("Row 132 baby picture", "Row 152 baby picture"),
        ("[row 131](preface.md#skill-navigation-row-132)", "[row 151](preface.md#skill-navigation-row-152)"),
        ("verified homogenization meta prelude capstone closure (row 131)", "verified homogenization meta prelude capstone closure (row 151)"),
        ("when row 131 closed but row 52", "when row 151 closed but row 52"),
        ("after row 131.", "after row 151."),
        ("when row 131 and row 52", "when row 151 and row 52"),
        ("rear-view mirror of row 131's", "rear-view mirror of row 151's"),
        ("When row 132 is complete, proceed to [row 133]", "When row 152 is complete, proceed to [row 133]"),
        ("When row 132 is complete, proceed", "When row 152 is complete, proceed"),
        ("opening [row 133](preface.md#skill-navigation-row-133) before row 53", "opening [row 133](preface.md#skill-navigation-row-133) before row 53"),
        ("[row 112](preface.md#skill-navigation-row-112) for the Row 68 ↔ Row 52 atomistic meta prelude audit on the opening-hinge path alone, to [row 131]", "[row 132](preface.md#skill-navigation-row-132) for the Row 68 ↔ Row 52 atomistic meta prelude audit on the opening-hinge prelude path alone, to [row 151]"),
        ("Row 68 → Row 111 atomistic meta prelude capstone reunion index", "Row 68 → Row 132 atomistic meta prelude capstone reunion index"),
        ("Row 68 → Row 112 reunion index", "Row 68 → Row 132 reunion index"),
        ("Row 132 names", "Row 152 names"),
        ("Row 132 closes the", "Row 152 closes the"),
        ("| 132 |", "| 152 |"),
        ("preface row 132", "preface row 152"),
        ("prologue row 132", "prologue row 152"),
        ("epilogue row 132", "epilogue row 152"),
        ("[Preface row 132]", "[Preface row 152]"),
        ("([row 132]", "([row 152]"),
        ("Recite [preface row 131](../preface.md#skill-navigation-row-151)", "Recite [preface row 151](../preface.md#skill-navigation-row-151)"),
        ("Recite [preface row 131](../preface.md#skill-navigation-row-132)", "Recite [preface row 151](../preface.md#skill-navigation-row-151)"),
        ("When row 52 feels like LAMMPS homework after row 131 alone", "When row 52 feels like LAMMPS homework after row 151 alone"),
    ]
    for a, b in pairs:
        s = s.replace(a, b)
    return s


def extract_between(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"missing: {start[:60]}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"missing end after: {start[:40]}")
    return text[i:j]


def main() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    block132 = extract_between(
        preface,
        "### Row 132 skill checkpoint",
        "\n### Row 133 skill checkpoint",
    )
    block152 = bump(block132)
    # Replace broken row 152 block before copper wire
    anchor = "\n## The copper wire through the book"
    idx = preface.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    head = preface[:idx]
    head = re.sub(
        r"\n### Row 152 skill checkpoint.*?(?=\n## The copper wire through the book)",
        "\n" + block152.rstrip() + "\n",
        head,
        flags=re.S,
    )
    preface_path.write_text(head + preface[idx:])
    print("preface: repaired row 152")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    # Remove duplicate malformed row-152 loops (keep row 132 canonical loop only once)
    dup_pat = r"\n### Row 151 closing loop \(Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion\) \{#row-152-closing-loop\}.*?(?=\n### Row 1)"
    ep = re.sub(dup_pat, "\n", ep, flags=re.S)
    if "row-152-closing-loop" not in ep:
        loop132 = extract_between(ep, "### Row 132 closing loop", "### Row 150 closing loop")
        loop152 = bump(loop132)
        ep = ep.replace("### Row 151 closing loop", loop152 + "### Row 151 closing loop", 1)
    ep_path.write_text(ep)
    print("epilogue: repaired row 152 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass = "| Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 152) |"
    if compass not in pro:
        needle = "| Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 151) |"
        idx = pro.find(needle)
        if idx < 0:
            raise SystemExit("prologue row 151 compass missing")
        line_end = pro.find("\n", idx)
        src_line = "| Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 132) |"
        sidx = pro.find(src_line)
        compass152 = bump(pro[sidx : pro.find("\n", sidx)]) + "\n"
        pro = pro[: line_end + 1] + compass152 + pro[line_end + 1 :]
    if "prologue-preview-row-152" not in pro:
        prev132 = extract_between(
            pro,
            '| <span id="prologue-preview-row-132"></span>',
            '\n| <span id="prologue-preview-row-151"></span>',
        )
        pro = pro.replace(
            '| <span id="prologue-preview-row-132"></span>',
            bump(prev132) + '| <span id="prologue-preview-row-132"></span>',
            1,
        )
    if "row-152-closing-stitch" not in pro:
        stitch132 = "**Row 132 closing stitch"
        if stitch132 in pro:
            # insert row 152 stitch before row 151 stitch
            snippet = (
                "**Row 152 closing stitch (Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-152-closing-stitch} "
                "When row 151 closed — homogenization meta prelude capstone verified, row 150 or row 132 recited on the capstone path, and VII.2 Bridge → VII.3 polycrystal recited with handoff Lab act archived `mobility.yaml` — "
                "but **row 52 VII.3 → VIII.1 opening hinge still opens like standalone LAMMPS homework after the mesoscale export Scene on the capstone path** — "
                "read [preface row 152](../preface.md#skill-navigation-row-152), then the "
                "[Row 68 → Row 132 reunion index](../appendix/sources.md#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152), then "
                "[epilogue row 152 closing loop](../epilogue/multiscale.md#row-152-closing-loop) before row 53 dynamics meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 151 closing stitch", snippet + "**Row 151 closing stitch", 1)
    pro_path.write_text(pro)
    print("prologue: row 152 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152" not in src:
        idx_block = extract_between(
            src,
            "## Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 132)",
            "## Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 133)",
        )
        idx152 = bump(idx_block)
        table_row = (
            "| 152 | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone (midpoint prelude gate ↔ homogenization meta prelude capstone ↔ row 52 meta) | "
            "[Row 68 → Row 132 atomistic meta prelude capstone reunion index](#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152) · "
            "[preface row 152](../preface.md#skill-navigation-row-152) · "
            "[prologue row 152 preview](../prologue/00-many-scales.md#prologue-preview-row-152) · "
            "[prologue row 152 closing stitch](../prologue/00-many-scales.md#row-152-closing-stitch) · "
            "[epilogue row 152 closing loop](../epilogue/multiscale.md#row-152-closing-loop) · "
            "[memory sheet row 152 baby picture](memory-sheet.md#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 52 VII.3 → VIII.1 opening hinge still feels disconnected from verified homogenization meta prelude capstone on the capstone path** — "
            "read row 68 + row 151 or row 132 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
            "[preface row 52](../preface.md#skill-navigation-row-52) |\n"
        )
        src = src.replace(
            "| 151 | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone",
            table_row + "| 151 | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)",
            idx152 + "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)",
        )
        extra = (
            " [row 152](#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152) reunites **homogenization meta prelude capstone with the atomistic meta prelude capstone boundary** "
            "when row 151 closed homogenization meta prelude capstone at verified polycrystal closure on the capstone path but `mobility.yaml` and VII.3 → VIII.1 opening hinge still read like separate courses after verified atomistic meta prelude meta;"
        )
        needle = "[row 132](#row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132) reunites **homogenization meta prelude capstone with the atomistic meta prelude capstone boundary**"
        if needle in src and extra.strip() not in src:
            src = src.replace(needle, needle + extra, 1)
        src_path.write_text(src)
    print("sources: row 152 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-152-baby-picture-row68-row132" not in mem:
        baby132 = extract_between(mem, "### Row 132 baby picture", "### Row 133 baby picture")
        baby152 = bump(baby132)
        mem = mem.replace("### Row 132 baby picture", baby152 + "### Row 132 baby picture", 1)
        mem_table = (
            "| 152 | Meta | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion | "
            "[Row 68 → Row 132 atomistic meta prelude capstone reunion index](sources.md#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152) · "
            "[preface row 152 skill checkpoint](../preface.md#skill-navigation-row-152) · "
            "[prologue row 152 preview](../prologue/00-many-scales.md#prologue-preview-row-152) · "
            "[prologue row 152 closing stitch](../prologue/00-many-scales.md#row-152-closing-stitch) · "
            "[epilogue row 152 closing loop](../epilogue/multiscale.md#row-152-closing-loop) | "
            "Row 68 closed but row 52 VII.3 → VIII.1 opening hinge feels disconnected from verified homogenization meta prelude capstone on the capstone path — "
            "read row 68 + row 151 or row 132 gate + VII.3 Bridge → opening hinge → VIII.1 phase space + row 52; "
            "[row 152 baby picture](#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 151 | Meta | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion |",
            mem_table + "| 151 | Meta | Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion |",
        )
        if "When row 151 closed but atomistic meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 131 closed but atomistic meta reunion still lags on the capstone path, switch to [row 132](#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion).",
                "When row 131 closed but atomistic meta reunion still lags on the capstone path, switch to [row 132](#row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion). "
                "When row 151 closed but atomistic meta reunion still lags on the capstone path, switch to [row 152](#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
    print("memory-sheet: row 152")


if __name__ == "__main__":
    main()
