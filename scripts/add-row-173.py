#!/usr/bin/env python3
"""Add row 173 (Row 68 → Row 151 ↔ Row 53 dynamics meta prelude capstone on capstone path)."""
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


LIFT_153_TO_173_PAIRS: list[tuple[str, str]] = [
    ("Row 154 closing loop", "__PH154_LOOP__"),
    ("Row 153 closing loop", "Row 173 closing loop"),
    ("row-154-closing-loop", "__PH154_LOOP_ANCHOR__"),
    ("row-153-closing-loop", "row-173-closing-loop"),
    ("Row 154 closing stitch", "__PH154_STITCH__"),
    ("Row 153 closing stitch", "Row 173 closing stitch"),
    ("row-154-closing-stitch", "__PH154_STITCH_ANCHOR__"),
    ("row-153-closing-stitch", "row-173-closing-stitch"),
    ("prologue-preview-row-154", "__PH154_PREVIEW__"),
    ("prologue-preview-row-153", "prologue-preview-row-173"),
    ("Row 154 preview", "__PH154_PREVIEW_TEXT__"),
    ("Row 153 preview", "Row 173 preview"),
    ("Row 154 skill checkpoint", "__PH154_SKILL__"),
    ("Row 153 skill checkpoint", "Row 173 skill checkpoint"),
    ("skill-navigation-row-154", "__PH154_SKILL_NAV__"),
    ("skill-navigation-row-153", "skill-navigation-row-173"),
    ("memory sheet row 154", "__PH154_MEM__"),
    ("memory sheet row 153", "memory sheet row 173"),
    ("Row 154 baby picture", "__PH154_BABY__"),
    ("Row 153 baby picture", "Row 173 baby picture"),
    ("Row 154 three-way audit", "__PH154_AUDIT__"),
    ("Row 153 three-way audit", "Row 173 three-way audit"),
    (
        "Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone",
    ),
    (
        "row68-row133-dynamics-meta-prelude-capstone-reunion-index-row-153",
        "row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173",
    ),
    (
        "row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion",
        "row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion",
    ),
    ("[row 154]", "__ROW154_REF__"),
    ("[row 133]", "[row 153]"),
    ("row 133", "row 153"),
    ("Row 133", "Row 153"),
    ("__ROW154_REF__", "[row 154]"),
    ("[row 152]", "__ROW172_GATE__"),
    ("row 152", "__row172_gate__"),
    ("Row 152", "__ROW172_GATE_CAP__"),
    (
        "Row 68 → Row 113 dynamics meta prelude capstone reunion index (row 133)",
        "Row 68 → Row 133 dynamics meta prelude capstone reunion index (row 153)",
    ),
    (
        "row68-row113-dynamics-meta-prelude-capstone-reunion-index-row-133",
        "row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173",
    ),
    (
        "verified atomistic meta prelude capstone closure (row 152)",
        "verified atomistic meta prelude capstone closure (row 172)",
    ),
    ("when row 152 closed but row 53", "when row 172 closed but row 53"),
    ("after row 152.", "after row 172."),
    ("when row 152 and row 53", "when row 172 and row 53"),
    (
        "rear-view mirror of row 152's EAM foundation → NPT thermostat turn",
        "rear-view mirror of row 172's EAM foundation → NPT thermostat turn",
    ),
    (
        "when opening [row 154](preface.md#skill-navigation-row-154) before row 54 closes on the capstone path",
        "when opening [row 173](preface.md#skill-navigation-row-173) before row 54 closes on the capstone path",
    ),
    (
        "When row 153 is complete, proceed to [row 154]",
        "When row 173 is complete, proceed to [row 154]",
    ),
    (
        "Proceed to [row 154](#row-154-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 153 on the capstone path",
        "Proceed to [row 173](#row-173-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 172 on the capstone path, "
        "to [row 153](#row-153-closing-loop) when row 68 closed but dynamics meta prelude still lags on the opening-hinge path",
    ),
    (
        "When row 53 feels like thermostat homework after row 152 alone on the capstone path",
        "When row 53 feels like thermostat homework after row 172 alone on the capstone path",
    ),
    (
        "row 153 (row 68 ↔ row 53 reunion on the capstone path) with row 133",
        "row 173 (row 68 ↔ row 53 reunion on the capstone path) with row 153",
    ),
    (
        "row 153 names **why that reunion must follow verified atomistic meta prelude capstone (row 152)",
        "row 173 names **why that reunion must follow verified atomistic meta prelude capstone (row 172)",
    ),
    ("Row 68 → Row 53 meta (row 133)", "Row 68 → Row 53 meta (row 153)"),
    (
        "Row 68 → Row 133 dynamics meta prelude capstone reunion index (row 153)",
        "Row 68 → Row 151 dynamics meta prelude capstone reunion index (row 173)",
    ),
    ("Row 68 → Row 133 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 153)", "(row 173)"),
    ("Row 153 closes the", "Row 173 closes the"),
    ("Row 153 does not conflate", "Row 173 does not conflate"),
    ("Row 153 does not replace", "Row 173 does not replace"),
    ("__PH154_LOOP__", "Row 154 closing loop"),
    ("__PH154_LOOP_ANCHOR__", "row-154-closing-loop"),
    ("__PH154_STITCH__", "Row 154 closing stitch"),
    ("__PH154_STITCH_ANCHOR__", "row-154-closing-stitch"),
    ("__PH154_PREVIEW__", "prologue-preview-row-154"),
    ("__PH154_PREVIEW_TEXT__", "Row 154 preview"),
    ("__PH154_SKILL__", "Row 154 skill checkpoint"),
    ("__PH154_SKILL_NAV__", "skill-navigation-row-154"),
    ("__PH154_MEM__", "memory sheet row 154"),
    ("__PH154_BABY__", "Row 154 baby picture"),
    ("__PH154_AUDIT__", "Row 154 three-way audit"),
    ("__ROW172_GATE__", "[row 172]"),
    ("__row172_gate__", "row 172"),
    ("__ROW172_GATE_CAP__", "Row 172"),
]


def lift_153_to_173(s: str) -> str:
    out = tx(s, LIFT_153_TO_173_PAIRS)
    out = out.replace(
        "[row 172](preface.md#skill-navigation-row-152)",
        "[row 172](preface.md#skill-navigation-row-172)",
    )
    out = out.replace(
        "[row 153](preface.md#skill-navigation-row-133)",
        "[row 153](preface.md#skill-navigation-row-153)",
    )
    out = re.sub(
        r"(### Row 173 skill checkpoint[^\n]*)\{#skill-navigation-row-153\}",
        r"\1{#skill-navigation-row-173}",
        out,
        count=1,
    )
    return out


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 173 skill checkpoint" in text:
        print("preface: row 173 already present")
        return
    m = re.search(
        r"(### Row 153 skill checkpoint.*?)(?=\n### Row 154 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 153 checkpoint missing")
    block = lift_153_to_173(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 173")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 173 closing loop" in text:
        print("epilogue: row 173 loop already present")
        return
    block = lift_153_to_173(
        extract_between(
            text,
            "### Row 153 closing loop",
            "### Row 152 closing loop",
        )
    )
    needle = "### Row 172 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 173 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 173) |"
    if compass in text:
        print("prologue: row 173 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 172) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 172 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 153 compass missing")
        new_line = lift_153_to_173(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-153"></span>'
    preview_dst = '| <span id="prologue-preview-row-173"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_153_to_173(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 173 closing stitch" not in text:
        stitch = (
            "**Row 173 closing stitch (Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-173-closing-stitch} "
            "When row 172 closed — atomistic meta prelude capstone verified, row 171 or row 152 recited on the capstone path, and VIII.1 Bridge → VIII.2 ensembles recited with "
            "[EAM Lab act](../part08-md/01-potentials-phase-space.md#lab-act-eam-lattice-constant-from-energy-minimization-act-v--notch-prelude) archived `cu_eam_a0.txt` — but **row 53 VIII.1 → VIII.2 opening hinge still opens like standalone thermostat homework after the screw-core Scene on the capstone path** — "
            "the [preface row 173 When-to-pause opening sentence](../preface.md#skill-navigation-row-173) names the dual reunion before the export meta prelude capstone reunion; "
            "read [preface row 173](../preface.md#skill-navigation-row-173), then the "
            "[Row 68 → Row 151 dynamics reunion index](../appendix/sources.md#row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173), then "
            "[epilogue row 173 closing loop](../epilogue/multiscale.md#row-173-closing-loop) before row 54 export meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 172 closing stitch", stitch + "**Row 172 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 173 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173"
    if idx_key in text:
        print("sources: row 173 already present")
        return
    start = "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 153 index missing")
    end172 = "## Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    j172 = text.find(end172, i)
    if j172 < 0:
        raise SystemExit("sources row 172 index missing")
    block = lift_153_to_173(text[i:j172])
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)",
        f"## Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 173 | Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone (midpoint prelude gate ↔ atomistic meta prelude capstone ↔ row 53 meta) | "
        f"[Row 68 → Row 151 dynamics meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 173](../preface.md#skill-navigation-row-173) · "
        "[prologue row 173 preview](../prologue/00-many-scales.md#prologue-preview-row-173) · "
        "[prologue row 173 closing stitch](../prologue/00-many-scales.md#row-173-closing-stitch) · "
        "[epilogue row 173 closing loop](../epilogue/multiscale.md#row-173-closing-loop) · "
        "[memory sheet row 173 baby picture](memory-sheet.md#row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 53 VIII.1 → VIII.2 opening hinge still feels disconnected from verified atomistic meta prelude capstone on the capstone path** — "
        "read row 68 + row 172 or row 153 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
        "[preface row 53](../preface.md#skill-navigation-row-53) |\n"
    )
    text = text.replace(
        "| 172 | Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone",
        table_row + "| 172 | Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone",
    )
    text = text.replace(
        start,
        block + start,
        1,
    )
    extra = (
        f"[row 173](#{idx_key}) reunites **atomistic meta prelude capstone with the dynamics meta prelude capstone boundary** "
        "when row 172 closed atomistic meta prelude capstone at verified VII.3 → VIII.1 closure on the capstone path but VIII.1 Bridge and row 53 still read like separate courses after verified dynamics meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 172](#row68-row151-atomistic-meta-prelude-capstone-reunion-index-row-172) reunites **homogenization meta prelude capstone with the atomistic meta prelude capstone boundary** "
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 173")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 173 already present")
        return
    baby = lift_153_to_173(
        extract_between(
            text,
            "### Row 153 baby picture",
            "### Row 154 baby picture",
        )
    )
    anchor = "### Row 153 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 173 | Meta | Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion | "
        "[Row 68 → Row 151 dynamics meta prelude capstone reunion index](sources.md#row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173) · "
        "[preface row 173 skill checkpoint](../preface.md#skill-navigation-row-173) · "
        "[prologue row 173 preview](../prologue/00-many-scales.md#prologue-preview-row-173) · "
        "[prologue row 173 closing stitch](../prologue/00-many-scales.md#row-173-closing-stitch) · "
        "[epilogue row 173 closing loop](../epilogue/multiscale.md#row-173-closing-loop) | "
        "Row 68 closed but row 53 VIII.1 → VIII.2 opening hinge feels disconnected from verified atomistic meta prelude capstone on the capstone path — "
        "read row 68 + row 172 or row 153 gate + VIII.1 Bridge → opening hinge → VIII.2 ensembles + row 53; "
        "[row 173 baby picture](#row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 172 | Meta | Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion |",
        mem_table + "| 172 | Meta | Row 68 → Row 151 Row 68 → Row 52 atomistic meta prelude capstone reunion |",
    )
    if "When row 172 closed but dynamics meta reunion still lags" not in text:
        text = text.replace(
            "When row 171 closed but atomistic meta reunion still lags on the capstone path, switch to [row 172](#row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion).",
            "When row 171 closed but atomistic meta reunion still lags on the capstone path, switch to [row 172](#row-172-baby-picture-row68-row151-atomistic-meta-prelude-capstone-reunion). "
            "When row 172 closed but dynamics meta reunion still lags on the capstone path, switch to [row 173](#row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 173")


def patch_row_172_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "proceed to [row 173](preface.md#skill-navigation-row-153)",
        "proceed to [row 173](preface.md#skill-navigation-row-173)",
    )
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    ep_text = ep_text.replace(
        "proceed to [row 173](preface.md#skill-navigation-row-153)",
        "proceed to [row 173](preface.md#skill-navigation-row-173)",
    )
    ep.write_text(ep_text)
    print("preface/epilogue: patched row 172 → row 173 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_172_proceed_links()


if __name__ == "__main__":
    main()
