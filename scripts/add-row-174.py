#!/usr/bin/env python3
"""Add row 174 (Row 68 → Row 151 ↔ Row 54 export meta prelude capstone on capstone path)."""
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


LIFT_154_TO_174_PAIRS: list[tuple[str, str]] = [
    ("Row 155 closing loop", "__PH155_LOOP__"),
    ("Row 154 closing loop", "Row 174 closing loop"),
    ("row-155-closing-loop", "__PH155_LOOP_ANCHOR__"),
    ("row-154-closing-loop", "row-174-closing-loop"),
    ("Row 155 closing stitch", "__PH155_STITCH__"),
    ("Row 154 closing stitch", "Row 174 closing stitch"),
    ("row-155-closing-stitch", "__PH155_STITCH_ANCHOR__"),
    ("row-154-closing-stitch", "row-174-closing-stitch"),
    ("prologue-preview-row-155", "__PH155_PREVIEW__"),
    ("prologue-preview-row-154", "prologue-preview-row-174"),
    ("Row 155 preview", "__PH155_PREVIEW_TEXT__"),
    ("Row 154 preview", "Row 174 preview"),
    ("Row 155 skill checkpoint", "__PH155_SKILL__"),
    ("Row 154 skill checkpoint", "Row 174 skill checkpoint"),
    ("skill-navigation-row-155", "__PH155_SKILL_NAV__"),
    ("skill-navigation-row-154", "skill-navigation-row-174"),
    ("memory sheet row 155", "__PH155_MEM__"),
    ("memory sheet row 154", "memory sheet row 174"),
    ("Row 155 baby picture", "__PH155_BABY__"),
    ("Row 154 baby picture", "Row 174 baby picture"),
    ("Row 155 three-way audit", "__PH155_AUDIT__"),
    ("Row 154 three-way audit", "Row 174 three-way audit"),
    (
        "Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone",
        "Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone",
    ),
    (
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        "row68-row151-export-meta-prelude-capstone-reunion-index-row-174",
    ),
    (
        "row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion",
        "row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion",
    ),
    ("[row 155]", "__ROW155_REF__"),
    ("[row 134]", "[row 154]"),
    ("row 134", "row 154"),
    ("Row 134", "Row 154"),
    ("__ROW155_REF__", "[row 155]"),
    ("[row 153]", "__ROW173_GATE__"),
    ("row 153", "__row173_gate__"),
    ("Row 153", "__ROW173_GATE_CAP__"),
    (
        "Row 68 → Row 114 export meta prelude capstone reunion index (row 134)",
        "Row 68 → Row 134 export meta prelude capstone reunion index (row 154)",
    ),
    (
        "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
        "row68-row151-export-meta-prelude-capstone-reunion-index-row-174",
    ),
    (
        "verified dynamics meta prelude capstone closure (row 153)",
        "verified dynamics meta prelude capstone closure (row 173)",
    ),
    ("when row 153 closed but row 54", "when row 173 closed but row 54"),
    ("after row 153.", "after row 173."),
    ("when row 153 and row 54", "when row 173 and row 54"),
    (
        "rear-view mirror of row 153's finite-\\(T\\) dynamics → yaml handoff turn",
        "rear-view mirror of row 173's finite-\\(T\\) dynamics → yaml handoff turn",
    ),
    (
        "when opening [row 155](preface.md#skill-navigation-row-155) before row 55 closes on the capstone path",
        "when opening [row 174](preface.md#skill-navigation-row-174) before row 55 closes on the capstone path",
    ),
    (
        "When row 154 is complete, proceed to [row 155]",
        "When row 174 is complete, proceed to [row 155]",
    ),
    (
        "Proceed to [row 155](#row-155-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 154 on the capstone path",
        "Proceed to [row 174](#row-174-closing-loop) when row 68 closed but export meta prelude capstone still lags after row 173 on the capstone path, "
        "to [row 154](#row-154-closing-loop) when row 68 closed but export meta prelude still lags on the opening-hinge path",
    ),
    (
        "When row 54 feels like export homework after row 153 alone on the capstone path",
        "When row 54 feels like export homework after row 173 alone on the capstone path",
    ),
    (
        "row 154 (row 68 ↔ row 54 reunion on the capstone path) with row 134",
        "row 174 (row 68 ↔ row 54 reunion on the capstone path) with row 154",
    ),
    (
        "row 154 names **why that reunion must follow verified dynamics meta prelude capstone (row 153)",
        "row 174 names **why that reunion must follow verified dynamics meta prelude capstone (row 173)",
    ),
    ("Row 68 → Row 54 meta (row 134)", "Row 68 → Row 54 meta (row 154)"),
    (
        "Row 68 → Row 134 export meta prelude capstone reunion index (row 154)",
        "Row 68 → Row 151 export meta prelude capstone reunion index (row 174)",
    ),
    ("Row 68 → Row 134 reunion index", "Row 68 → Row 151 reunion index"),
    ("(row 154)", "(row 174)"),
    ("Row 154 closes the", "Row 174 closes the"),
    ("Row 154 does not conflate", "Row 174 does not conflate"),
    ("Row 154 does not replace", "Row 174 does not replace"),
    ("__PH155_LOOP__", "Row 155 closing loop"),
    ("__PH155_LOOP_ANCHOR__", "row-155-closing-loop"),
    ("__PH155_STITCH__", "Row 155 closing stitch"),
    ("__PH155_STITCH_ANCHOR__", "row-155-closing-stitch"),
    ("__PH155_PREVIEW__", "prologue-preview-row-155"),
    ("__PH155_PREVIEW_TEXT__", "Row 155 preview"),
    ("__PH155_SKILL__", "Row 155 skill checkpoint"),
    ("__PH155_SKILL_NAV__", "skill-navigation-row-155"),
    ("__PH155_MEM__", "memory sheet row 155"),
    ("__PH155_BABY__", "Row 155 baby picture"),
    ("__PH155_AUDIT__", "Row 155 three-way audit"),
    ("__ROW173_GATE__", "[row 173]"),
    ("__row173_gate__", "row 173"),
    ("__ROW173_GATE_CAP__", "Row 173"),
]


def lift_154_to_174(s: str) -> str:
    out = tx(s, LIFT_154_TO_174_PAIRS)
    out = out.replace(
        "[row 173](preface.md#skill-navigation-row-153)",
        "[row 173](preface.md#skill-navigation-row-173)",
    )
    out = out.replace(
        "[row 154](preface.md#skill-navigation-row-134)",
        "[row 154](preface.md#skill-navigation-row-154)",
    )
    out = re.sub(
        r"(### Row 174 skill checkpoint[^\n]*)\{#skill-navigation-row-154\}",
        r"\1{#skill-navigation-row-174}",
        out,
        count=1,
    )
    return out


def dynamics_index_to_export_174(block: str) -> str:
    """Turn a lifted dynamics capstone index (173-shaped) into export capstone 174."""
    pairs = [
        ("dynamics meta prelude capstone reunion index (row 173)", "export meta prelude capstone reunion index (row 174)"),
        ("dynamics meta prelude capstone reunion index (row 174)", "export meta prelude capstone reunion index (row 174)"),
        ("Row 68 → Row 53", "Row 68 → Row 54"),
        ("row 53", "row 54"),
        ("atomistic meta prelude capstone", "dynamics meta prelude capstone"),
        ("row 172", "row 173"),
        ("row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152", "row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173"),
        ("VIII.1 Bridge", "VIII.2 Bridge"),
        ("VIII.2 opening hinge from VIII.1", "VIII.3 opening hinge from VIII.2"),
        ("VIII.2 ensembles", "VIII.3 pedigree checklist"),
        ("viii1-viii2-opening-hinge-reunion-index-row-53", "viii2-viii3-opening-hinge-reunion-index-row-54"),
        ("EAM Lab act steps 6–7", "NPT Lab act steps 1–7"),
        ("`cu.foundation/`", "`cu.elastic/`"),
        ("thermostat homework", "export homework"),
        ("screw-core → NPT", "NPT → pedigree"),
        ("static potential → dynamics", "NPT → export"),
        ("skill-navigation-row-173", "skill-navigation-row-174"),
        ("row-173-baby-picture", "row-174-baby-picture"),
        ("dynamics meta prelude capstone reunion", "export meta prelude capstone reunion"),
        ("Row 173", "Row 174"),
        ("row 173", "row 174"),
    ]
    return tx(block, pairs)


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 174 skill checkpoint" in text:
        print("preface: row 174 already present")
        return
    m = re.search(
        r"(### Row 154 skill checkpoint.*?)(?=\n### Row 155 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 154 checkpoint missing")
    block = lift_154_to_174(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 174")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 174 closing loop" in text:
        print("epilogue: row 174 loop already present")
        return
    block = lift_154_to_174(
        extract_between(
            text,
            "### Row 154 closing loop",
            "### Row 153 closing loop",
        )
    )
    needle = "### Row 173 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 174 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion (row 174) |"
    if compass in text:
        print("prologue: row 174 compass already present")
    else:
        after = "| Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 173) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 173 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion (row 154) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 154 compass missing")
        new_line = lift_154_to_174(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-154"></span>'
    preview_dst = '| <span id="prologue-preview-row-174"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_154_to_174(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 174 closing stitch" not in text:
        stitch = (
            "**Row 174 closing stitch (Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-174-closing-stitch} "
            "When row 173 closed — dynamics meta prelude capstone verified, row 173 or row 154 recited on the capstone path, and VIII.2 Bridge → VIII.3 pedigree recited with "
            "[NPT Lab act](../part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) archived `cu.elastic/` — but **row 54 VIII.2 → VIII.3 opening hinge still opens like standalone export homework after the NPT Lab act on the capstone path** — "
            "the [preface row 174 When-to-pause opening sentence](../preface.md#skill-navigation-row-174) names the dual reunion before the electronic audit meta prelude capstone reunion; "
            "read [preface row 174](../preface.md#skill-navigation-row-174), then the "
            "[Row 68 → Row 151 export reunion index](../appendix/sources.md#row68-row151-export-meta-prelude-capstone-reunion-index-row-174), then "
            "[epilogue row 174 closing loop](../epilogue/multiscale.md#row-174-closing-loop) before row 55 electronic audit meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 173 closing stitch", stitch + "**Row 173 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 174 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-export-meta-prelude-capstone-reunion-index-row-174"
    if idx_key in text:
        print("sources: row 174 already present")
        return
    start173 = "## Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)"
    i = text.find(start173)
    if i < 0:
        raise SystemExit("sources row 173 index missing")
    end172 = "## Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion index (row 172)"
    j172 = text.find(end172, i)
    if j172 < 0:
        raise SystemExit("sources row 172 index missing")
    block = dynamics_index_to_export_174(lift_154_to_174(text[i:j172]))
    block = block.replace(
        "## Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)",
        f"## Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion index (row 174) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 174 | Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone (midpoint prelude gate ↔ dynamics meta prelude capstone ↔ row 54 meta) | "
        f"[Row 68 → Row 151 export meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 174](../preface.md#skill-navigation-row-174) · "
        "[prologue row 174 preview](../prologue/00-many-scales.md#prologue-preview-row-174) · "
        "[prologue row 174 closing stitch](../prologue/00-many-scales.md#row-174-closing-stitch) · "
        "[epilogue row 174 closing loop](../epilogue/multiscale.md#row-174-closing-loop) · "
        "[memory sheet row 174 baby picture](memory-sheet.md#row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 54 VIII.2 → VIII.3 opening hinge still feels disconnected from verified dynamics meta prelude capstone on the capstone path** — "
        "read row 68 + row 173 or row 154 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
        "[preface row 54](../preface.md#skill-navigation-row-54) |\n"
    )
    text = text.replace(
        "| 173 | Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone",
        table_row + "| 173 | Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone",
    )
    text = text.replace(start173, block + start173, 1)
    extra = (
        f"[row 174](#{idx_key}) reunites **dynamics meta prelude capstone with the export meta prelude capstone boundary** "
        "when row 173 closed dynamics meta prelude capstone at verified VIII.1 → VIII.2 closure on the capstone path but VIII.2 Bridge and row 54 still read like separate courses;"
    )
    needle = (
        "[row 173](#row68-row151-dynamics-meta-prelude-capstone-reunion-index-row-173) reunites **atomistic meta prelude capstone with the dynamics meta prelude capstone boundary** "
    )
    if extra not in text and needle in text:
        text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 174")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 174 already present")
        return
    baby = lift_154_to_174(
        extract_between(
            text,
            "### Row 154 baby picture",
            "### Row 155 baby picture",
        )
    )
    anchor = "### Row 154 baby picture"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 174 | Meta | Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion | "
        "[Row 68 → Row 151 export meta prelude capstone reunion index](sources.md#row68-row151-export-meta-prelude-capstone-reunion-index-row-174) · "
        "[preface row 174 skill checkpoint](../preface.md#skill-navigation-row-174) · "
        "[prologue row 174 preview](../prologue/00-many-scales.md#prologue-preview-row-174) · "
        "[prologue row 174 closing stitch](../prologue/00-many-scales.md#row-174-closing-stitch) · "
        "[epilogue row 174 closing loop](../epilogue/multiscale.md#row-174-closing-loop) | "
        "Row 68 closed but row 54 VIII.2 → VIII.3 opening hinge feels disconnected from verified dynamics meta prelude capstone on the capstone path — "
        "read row 68 + row 173 or row 154 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
        "[row 174 baby picture](#row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 173 | Meta | Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion |",
        mem_table + "| 173 | Meta | Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion |",
    )
    if "When row 173 closed but export meta reunion still lags" not in text:
        text = text.replace(
            "When row 172 closed but dynamics meta reunion still lags on the capstone path, switch to [row 173](#row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion).",
            "When row 172 closed but dynamics meta reunion still lags on the capstone path, switch to [row 173](#row-173-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion). "
            "When row 173 closed but export meta reunion still lags on the capstone path, switch to [row 174](#row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 174")


def patch_row_173_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    text = text.replace(
        "proceed to [row 174](preface.md#skill-navigation-row-154)",
        "proceed to [row 174](preface.md#skill-navigation-row-174)",
    )
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    ep_text = ep_text.replace(
        "proceed to [row 174](preface.md#skill-navigation-row-154)",
        "proceed to [row 174](preface.md#skill-navigation-row-174)",
    )
    ep.write_text(ep_text)
    print("preface/epilogue: patched row 173 → row 174 proceed links")


def main() -> None:
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_173_proceed_links()


if __name__ == "__main__":
    main()
