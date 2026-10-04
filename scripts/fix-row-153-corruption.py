#!/usr/bin/env python3
"""Repair row 153 meta-stitch content and finish prologue/sources/memory inserts."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def bump(s: str) -> str:
    pairs = [
        ("Row 68 → Row 113 Row 68 → Row 53", "Row 68 → Row 133 Row 68 → Row 53"),
        (
            "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
            "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        ),
        (
            "row-133-baby-picture-row68-row113-dynamics-meta-prelude-capstone-reunion",
            "row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion",
        ),
        ("skill-navigation-row-133", "skill-navigation-row-153"),
        ("### Row 133 skill checkpoint", "### Row 153 skill checkpoint"),
        ("Row 133 does not replace", "Row 153 does not replace"),
        ("Row 133 three-way audit", "Row 153 three-way audit"),
        ("Row 133 closing loop", "Row 153 closing loop"),
        ("row-133-closing-loop", "row-153-closing-loop"),
        ("Row 133 closing stitch", "Row 153 closing stitch"),
        ("row-133-closing-stitch", "row-153-closing-stitch"),
        ("prologue-preview-row-133", "prologue-preview-row-153"),
        ("Row 133 preview", "Row 153 preview"),
        ("memory sheet row 133", "memory sheet row 153"),
        ("Row 133 baby picture", "Row 153 baby picture"),
        ("[row 132](preface.md#skill-navigation-row-132)", "[row 152](preface.md#skill-navigation-row-152)"),
        ("[row 152](preface.md#skill-navigation-row-132)", "[row 152](preface.md#skill-navigation-row-152)"),
        (
            "verified atomistic meta prelude capstone closure (row 132)",
            "verified atomistic meta prelude capstone closure (row 152)",
        ),
        ("when row 132 closed but row 53", "when row 152 closed but row 53"),
        ("when row 132 and row 53", "when row 152 and row 53"),
        (
            "rear-view mirror of row 132's static potential → finite-\\(T\\) dynamics turn",
            "rear-view mirror of row 152's EAM foundation → NPT thermostat turn",
        ),
        (
            "when opening [row 114](preface.md#skill-navigation-row-114) before row 54 closes on the capstone path",
            "when opening [row 154](preface.md#skill-navigation-row-153) before row 54 closes on the capstone path",
        ),
        (
            "When row 133 is complete, proceed to [row 134]",
            "When row 153 is complete, proceed to [row 134]",
        ),
        (
            "When row 53 feels like thermostat homework after row 132 alone on the capstone path",
            "When row 53 feels like thermostat homework after row 152 alone on the capstone path",
        ),
        ("Row 133 names", "Row 153 names"),
        ("Row 133 closes the", "Row 153 closes the"),
        ("| 133 |", "| 153 |"),
        ("preface row 133", "preface row 153"),
        ("prologue row 133", "prologue row 153"),
        ("epilogue row 133", "epilogue row 153"),
        ("[Preface row 133]", "[Preface row 153]"),
        ("([row 133]", "([row 153]"),
        (
            "[Row 68 → Row 113 dynamics meta prelude capstone reunion index]",
            "[Row 68 → Row 133 dynamics meta prelude capstone reunion index]",
        ),
        ("Row 68 → Row 113 reunion index", "Row 68 → Row 133 reunion index"),
        (
            "row68-row93-dynamics-meta-prelude-reunion-index-row-113",
            "row68-row113-dynamics-meta-prelude-reunion-index-row-113",
        ),
        (
            "Row 68 → Row 93 dynamics meta prelude reunion index (row 113)",
            "Row 68 → Row 113 dynamics meta prelude reunion index (row 113)",
        ),
        ("Recite [preface row 132]", "Recite [preface row 152]"),
        ("Recite [preface row 151](../preface.md#skill-navigation-row-152)", "Recite [preface row 152](../preface.md#skill-navigation-row-152)"),
        ("Recite [preface row 152](../preface.md#skill-navigation-row-132)", "Recite [preface row 152](../preface.md#skill-navigation-row-152)"),
        ("before the export meta reunion", "before the export meta prelude capstone reunion"),
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
    block133 = extract_between(
        preface,
        "### Row 133 skill checkpoint",
        "\n### Row 134 skill checkpoint",
    )
    block153 = bump(block133)
    anchor = "\n## The copper wire through the book"
    idx = preface.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    head = preface[:idx]
    head = re.sub(
        r"\n### Row 153 skill checkpoint.*?(?=\n## The copper wire through the book|\Z)",
        "",
        head,
        flags=re.S,
    )
    preface = head + "\n" + block153 + preface[idx:]
    preface_path.write_text(preface)
    print("preface: repaired row 153 block")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if ep.count("### Row 153 closing loop") > 1:
        first = ep.find("### Row 153 closing loop")
        second = ep.find("### Row 153 closing loop", first + 1)
        end = ep.find("\n### Row 152 closing loop", second)
        if second > 0 and end > second:
            ep = ep[:second] + ep[end:]
    block133_ep = extract_between(ep, "### Row 133 closing loop", "### Row 132 closing loop")
    block153_ep = bump(block133_ep)
    start153 = ep.find("### Row 153 closing loop")
    end153 = ep.find("\n### Row 152 closing loop", start153)
    if start153 >= 0 and end153 > start153:
        ep = ep[:start153] + block153_ep + ep[end153:]
    ep_path.write_text(bump(ep))
    print("epilogue: repaired row 153 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass153 = (
        "| Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) | "
        "[Preface: row 153 skill checkpoint](../preface.md#skill-navigation-row-153) · "
        "[Row 68 → Row 133 dynamics meta prelude capstone reunion index](../appendix/sources.md#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153) · "
        "[memory sheet row 153 baby picture](../appendix/memory-sheet.md#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion) · "
        "[prologue row 153 preview row](#prologue-preview-row-153); [prologue row 153 closing stitch](#row-153-closing-stitch); "
        "[epilogue row 153 closing loop](../epilogue/multiscale.md#row-153-closing-loop) — "
        "read row 68 gate + row 152 or row 133 atomistic meta prelude capstone / dynamics meta prelude gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53 meta aloud "
        "when EAM foundation is clean on the capstone path but NVT/NPT feels like AtomModel homework after verified atomistic meta prelude capstone |\n"
    )
    if "row 153) |" not in pro.split("compass")[0]:
        line152 = "| Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 152) |"
        idx152 = pro.find(line152)
        if idx152 >= 0:
            line_end = pro.find("\n", idx152)
            pro = pro[: line_end + 1] + compass153 + pro[line_end + 1 :]
    preview133 = extract_between(
        pro,
        '| <span id="prologue-preview-row-133"></span>',
        '\n| <span id="prologue-preview-row-132"></span>',
    )
    preview153 = bump(preview133)
    if "prologue-preview-row-153" not in pro:
        pro = pro.replace(
            '| <span id="prologue-preview-row-133"></span>',
            preview153 + '| <span id="prologue-preview-row-133"></span>',
            1,
        )
    if "row-153-closing-stitch" not in pro:
        stitch = (
            "**Row 152 closing stitch (Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-153-closing-stitch} "
            "When row 151 closed — homogenization meta prelude capstone verified, row 150 or row 132 recited on the capstone path, and VII.3 Bridge → VIII.1 phase space recited with "
            "[EAM Lab act](../part08-md/01-potentials-phase-space.md#lab-act-eam-lattice-constant-from-energy-minimization-act-v--notch-prelude) archived `cu_eam_a0.txt` — but **row 53 VIII.1 → VIII.2 opening hinge still opens like standalone thermostat homework after the screw-core Scene on the capstone path** — "
            "the [preface row 153 When-to-pause opening sentence](../preface.md#skill-navigation-row-153) names the dual reunion before the export meta reunion; "
            "read [preface row 153](../preface.md#skill-navigation-row-153), then the "
            "[Row 68 → Row 133 reunion index](../appendix/sources.md#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153), then "
            "[epilogue row 153 closing loop](../epilogue/multiscale.md#row-153-closing-loop) before row 54 export meta prelude opens on the capstone path.\n\n"
        )
        pro = pro.replace("**Row 152 closing stitch", stitch + "**Row 152 closing stitch", 1)
    pro_path.write_text(pro)
    print("prologue: finished row 153 inserts")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153" not in src:
        block113 = extract_between(
            src,
            "## Row 68 → Row 93 Row 68 → Row 53 dynamics meta prelude reunion index (row 113)",
            "## Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion index (row 114)",
        )
        block153 = bump(block113.replace("reunion index (row 113)", "capstone reunion index (row 133)"))
        block153 = block153.replace("Row 113 names", "Row 153 names").replace("(row 113)", "(row 153)")
        block153 = block153.replace("skill-navigation-row-113", "skill-navigation-row-153")
        block153 = block153.replace("row 112", "row 152").replace("Row 112", "Row 152")
        block153 = block153.replace("dynamics meta capstone", "dynamics meta prelude capstone")
        block153 = block153.replace("atomistic meta capstone", "atomistic meta prelude capstone")
        table_row = (
            "| 153 | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone (midpoint prelude gate ↔ atomistic meta prelude capstone ↔ row 53 meta) | "
            "[Row 68 → Row 133 dynamics meta prelude capstone reunion index](#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153) · "
            "[preface row 153](../preface.md#skill-navigation-row-153) · "
            "[prologue row 153 preview](../prologue/00-many-scales.md#prologue-preview-row-153) · "
            "[prologue row 153 closing stitch](../prologue/00-many-scales.md#row-153-closing-stitch) · "
            "[epilogue row 153 closing loop](../epilogue/multiscale.md#row-153-closing-loop) · "
            "[memory sheet row 153 baby picture](memory-sheet.md#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 53 VIII.1 → VIII.2 opening hinge still feels disconnected from verified atomistic meta prelude capstone on the capstone path** — "
            "read row 68 + row 152 or row 133 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
            "[preface row 53](../preface.md#skill-navigation-row-53) |\n"
        )
        src = src.replace(
            "| 152 | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone",
            table_row + "| 152 | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152)",
            block153 + "## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 152)",
        )
        src_path.write_text(src)
        print("sources: added row 153 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-153-baby-picture" not in mem:
        baby133 = extract_between(mem, "### Row 133 baby picture", "### Row 134 baby picture")
        baby153 = bump(baby133)
        mem = mem.replace("### Row 132 baby picture", baby153 + "### Row 132 baby picture", 1)
        mem_table = (
            "| 153 | Meta | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion | "
            "[Row 68 → Row 133 dynamics meta prelude capstone reunion index](sources.md#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153) · "
            "[preface row 153 skill checkpoint](../preface.md#skill-navigation-row-153) · "
            "[prologue row 153 preview](../prologue/00-many-scales.md#prologue-preview-row-153) · "
            "[prologue row 153 closing stitch](../prologue/00-many-scales.md#row-153-closing-stitch) · "
            "[epilogue row 153 closing loop](../epilogue/multiscale.md#row-153-closing-loop) | "
            "Row 68 closed but row 53 VIII.1 → VIII.2 opening hinge feels disconnected from verified atomistic meta prelude capstone on the capstone path — "
            "read row 68 + row 152 or row 133 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
            "[row 153 baby picture](#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 152 | Meta | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion |",
            mem_table + "| 152 | Meta | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion |",
        )
        if "When row 152 closed but dynamics meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 151 closed but atomistic meta reunion still lags on the capstone path, switch to [row 152](#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion).",
                "When row 151 closed but atomistic meta reunion still lags on the capstone path, switch to [row 152](#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion). "
                "When row 152 closed but dynamics meta reunion still lags on the capstone path, switch to [row 153](#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 153")

    preface = preface_path.read_text()
    preface = preface.replace(
        "When row 152 is complete, proceed to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone is clean but dynamics meta prelude capstone still lags after verified EAM foundation on the capstone path",
        "When row 152 is complete, proceed to [row 153](preface.md#skill-navigation-row-153) when row 68 closed but dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the capstone path",
    )
    preface = preface.replace(
        "Read the [memory sheet row 152 baby picture](appendix/memory-sheet.md#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion) when opening [row 133](preface.md#skill-navigation-row-133) before row 53 closes on the capstone path",
        "Read the [memory sheet row 153 baby picture](appendix/memory-sheet.md#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion) when opening [row 153](preface.md#skill-navigation-row-153) before row 54 closes on the capstone path",
    )
    preface_path.write_text(preface)
    print("preface: updated row 152 → row 153 pointers")


if __name__ == "__main__":
    main()
