#!/usr/bin/env python3
"""Add row 153 (Row 68 → Row 133 ↔ Row 53 dynamics meta prelude capstone on capstone path)."""
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


def lift_113_to_133(s: str) -> str:
    """Promote opening-hinge row 113 sources index to capstone row 133 wording."""
    p = [
        (
            "Row 68 → Row 93 Row 68 → Row 53 dynamics meta prelude reunion",
            "Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion",
        ),
        (
            "row68-row93-dynamics-meta-prelude-reunion-index-row-113",
            "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
        ),
        (
            "row-113-baby-picture-row68-row93-dynamics-meta-prelude-reunion",
            "row-133-baby-picture-row68-row113-dynamics-meta-prelude-capstone-reunion",
        ),
        ("Row 113 names", "Row 133 names"),
        ("(row 113)", "(row 133)"),
        ("skill-navigation-row-113", "skill-navigation-row-133"),
        ("[row 112]", "__R112__"),
        ("row 112", "row 132"),
        ("Row 112", "Row 132"),
        ("__R112__", "[row 132]"),
        ("dynamics meta capstone boundary", "dynamics meta prelude capstone boundary"),
        ("dynamics meta capstone path", "dynamics meta prelude capstone path"),
        ("Dynamics meta capstone", "Dynamics meta prelude capstone"),
        ("dynamics meta capstone", "dynamics meta prelude capstone"),
        ("atomistic meta capstone", "atomistic meta prelude capstone"),
        ("Atomistic meta capstone", "Atomistic meta prelude capstone"),
        ("Preface row 113", "Preface row 133"),
        ("preface row 113", "preface row 133"),
        ("memory sheet row 113", "memory sheet row 133"),
        ("Row 113 baby picture", "Row 133 baby picture"),
    ]
    return tx(s, p)


def lift_133_to_153(s: str) -> str:
    p = [
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
        ("Row 133 skill checkpoint", "Row 153 skill checkpoint"),
        ("memory sheet row 133", "memory sheet row 153"),
        ("Row 133 baby picture", "Row 153 baby picture"),
        (
            "Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone",
            "Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
        ),
        (
            "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
            "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        ),
        (
            "row-133-baby-picture-row68-row113-dynamics-meta-prelude-capstone-reunion",
            "row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion",
        ),
        ("[row 134]", "__ROW134__"),
        ("[row 132]", "[row 152]"),
        ("row 132", "row 152"),
        ("Row 132", "Row 152"),
        ("__ROW134__", "[row 134]"),
        (
            "Row 68 → Row 113 dynamics meta prelude capstone reunion index (row 133)",
            "Row 68 → Row 133 dynamics meta prelude capstone reunion index (row 153)",
        ),
        (
            "row68-row93-dynamics-meta-prelude-reunion-index-row-113",
            "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        ),
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
            "When row 133 is complete, proceed to [row 134](preface.md#skill-navigation-row-134) when dynamics meta prelude capstone is clean but export meta prelude capstone still lags after verified NPT archive on the capstone path, to [row 114](preface.md#skill-navigation-row-114) when dynamics meta capstone is clean but export meta capstone still lags on the opening-hinge path, to [row 113](preface.md#skill-navigation-row-113) for the Row 68 ↔ Row 53 dynamics meta audit on the opening-hinge path alone, to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone still lags after verified EAM foundation on the capstone path, to [row 54](preface.md#skill-navigation-row-54) when only VIII.2 → VIII.3 stalls, or extend prose only under `writings/` then sync.",
            "When row 153 is complete, proceed to [row 134](preface.md#skill-navigation-row-134) when row 68 closed but export meta prelude capstone still lags after verified dynamics meta prelude capstone on the capstone path, to [row 153](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone is clean but dynamics meta prelude still lags on the opening-hinge path, to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta prelude audit on the opening-hinge prelude path alone, to [row 152](preface.md#skill-navigation-row-152) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the capstone path, to [row 54](preface.md#skill-navigation-row-54) when only VIII.2 → VIII.3 stalls, or extend prose only under `writings/` then sync.",
        ),
        (
            "When row 53 feels like thermostat homework after row 132 alone on the capstone path",
            "When row 53 feels like thermostat homework after row 152 alone on the capstone path",
        ),
        (
            "row 133 (row 68 ↔ row 53 reunion on the capstone path) with row 113",
            "row 153 (row 68 ↔ row 53 reunion on the capstone path) with row 133",
        ),
        (
            "row 133 names **why that reunion must follow verified atomistic meta prelude capstone (row 132)",
            "row 153 names **why that reunion must follow verified atomistic meta prelude capstone (row 152)",
        ),
        ("Row 68 → Row 53 meta (row 113)", "Row 68 → Row 53 meta (row 153)"),
        ("Row 68 → Row 113 reunion index", "Row 68 → Row 133 reunion index"),
        ("(row 153)", "(row 153)"),
        ("Row 153 closes the", "Row 153 closes the"),
        ("Row 153 does not conflate", "Row 153 does not conflate"),
        (
            "Proceed to [row 114](#row-133-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 133 on the capstone path",
            "Proceed to [row 154](#row-153-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 153 on the capstone path, "
            "to [row 133](#row-133-closing-loop) when row 68 closed but dynamics meta prelude still lags on the opening-hinge path",
        ),
        ("before the export meta reunion", "before the export meta prelude capstone reunion"),
        ("row 151 closed atomistic meta prelude capstone", "row 152 closed atomistic meta prelude capstone"),
        ("Recite [preface row 132]", "Recite [preface row 152]"),
    ]
    return tx(s, p)


def add_row_153() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-153" in preface and "### Row 153 skill checkpoint" in preface:
        print("preface: row 153 already present")
    else:
        m133 = re.search(
            r"(### Row 133 skill checkpoint.*?)(?=\n### Row 134 skill checkpoint)",
            preface,
            re.S,
        )
        if not m133:
            raise SystemExit("row 133 preface checkpoint missing")
        row153 = lift_133_to_153(m133.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row153 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 153")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-153-closing-loop" not in ep:
        block133 = extract_between(ep, "### Row 133 closing loop", "### Row 132 closing loop")
        block153 = lift_133_to_153(block133)
        ep = ep.replace("### Row 152 closing loop", block153 + "### Row 152 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 153 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) |"
    )
    if compass_line not in pro:
        line152 = (
            "| Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 152) |"
        )
        idx152 = pro.find(line152)
        if idx152 < 0:
            raise SystemExit("prologue compass row 152 not found")
        line_end152 = pro.find("\n", idx152)
        line133 = (
            "| Row 68 → Row 113 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 133) |"
        )
        idx133 = pro.find(line133)
        if idx133 < 0:
            raise SystemExit("prologue compass row 133 not found")
        line_end133 = pro.find("\n", idx133)
        compass153 = lift_133_to_153(pro[idx133:line_end133]) + "\n"
        pro = pro[: line_end152 + 1] + compass153 + pro[line_end152 + 1 :]
        preview133 = extract_between(
            pro,
            '| <span id="prologue-preview-row-133"></span>',
            '\n| <span id="prologue-preview-row-152"></span>',
        )
        preview153 = lift_133_to_153(preview133)
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
        print("prologue: added row 153 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153" not in src:
        block113 = extract_between(
            src,
            "## Row 68 → Row 93 Row 68 → Row 53 dynamics meta prelude reunion index (row 113)",
            "## Row 68 → Row 94 Row 68 → Row 54 export meta prelude reunion index (row 114)",
        )
        block153 = lift_133_to_153(lift_113_to_133(block113))
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
        extra = (
            "[row 152](#row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153) reunites **atomistic meta prelude capstone with the dynamics meta prelude capstone boundary** "
            "when row 152 closed atomistic meta prelude capstone at verified VII.3 → VIII.1 closure on the capstone path but VIII.1 Bridge and row 53 still read like separate courses after verified dynamics meta prelude meta;"
        )
        if extra not in src:
            needle = (
                "[row 151](#row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152) reunites **homogenization meta prelude capstone with the atomistic meta prelude capstone boundary** "
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 153 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-153-baby-picture" not in mem:
        baby133 = extract_between(mem, "### Row 133 baby picture", "### Row 134 baby picture")
        baby153 = lift_133_to_153(baby133)
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
    else:
        print("memory-sheet: row 153 baby already present")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    old = (
        "Proceed to [row 133](#row-133-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 152 on the capstone path"
    )
    new = (
        "Proceed to [row 153](#row-153-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 152 on the capstone path"
    )
    if old in ep:
        ep = ep.replace(old, new)
        ep_path.write_text(ep)
        print("epilogue: row 133 → row 153 proceed link")

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    old_p = (
        "Read the [memory sheet row 152 baby picture](appendix/memory-sheet.md#row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion) when opening [row 133](preface.md#skill-navigation-row-133) before row 53 closes on the capstone path"
    )
    new_p = (
        "Read the [memory sheet row 153 baby picture](appendix/memory-sheet.md#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion) when opening [row 153](preface.md#skill-navigation-row-153) before row 54 closes on the capstone path"
    )
    if old_p in preface:
        preface = preface.replace(old_p, new_p)
        preface_path.write_text(preface)
        print("preface: row 133 → row 153 memory sheet pointer")

    old_p2 = (
        "When row 152 is complete, proceed to [row 133](preface.md#skill-navigation-row-133) when atomistic meta prelude capstone is clean but dynamics meta prelude capstone still lags after verified EAM foundation on the capstone path"
    )
    new_p2 = (
        "When row 152 is complete, proceed to [row 153](preface.md#skill-navigation-row-153) when row 68 closed but dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the capstone path"
    )
    if old_p2 in preface:
        preface = preface.replace(old_p2, new_p2)
        preface_path.write_text(preface)
        print("preface: row 152 proceed → row 153")


def main() -> None:
    add_row_153()


if __name__ == "__main__":
    main()
