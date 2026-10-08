#!/usr/bin/env python3
"""Add row 156 (Row 68 → Row 136 ↔ Row 56 Born–Oppenheimer meta prelude capstone on capstone path)."""
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


def lift_136_to_156(s: str) -> str:
    p = [
        ("skill-navigation-row-136", "skill-navigation-row-156"),
        ("### Row 136 skill checkpoint", "### Row 156 skill checkpoint"),
        ("Row 136 does not replace", "Row 156 does not replace"),
        ("Row 136 three-way audit", "Row 156 three-way audit"),
        ("Row 136 closing loop", "Row 156 closing loop"),
        ("row-136-closing-loop", "row-156-closing-loop"),
        ("Row 136 closing stitch", "Row 156 closing stitch"),
        ("row-136-closing-stitch", "row-156-closing-stitch"),
        ("prologue-preview-row-136", "prologue-preview-row-156"),
        ("Row 136 preview", "Row 156 preview"),
        ("Row 136 skill checkpoint", "Row 156 skill checkpoint"),
        ("memory sheet row 136", "memory sheet row 156"),
        ("Row 136 baby picture", "Row 156 baby picture"),
        (
            "Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone",
            "Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
        ),
        (
            "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
            "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        ),
        (
            "row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion",
            "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion",
        ),
        ("Born–Oppenheimer meta capstone reunion", "Born–Oppenheimer meta prelude capstone reunion"),
        ("Born–Oppenheimer meta capstone", "Born–Oppenheimer meta prelude capstone"),
        ("born-oppenheimer-meta-capstone-reunion", "born-oppenheimer-meta-prelude-capstone-reunion"),
        ("[row 137]", "__ROW157__"),
        ("[row 135]", "[row 155]"),
        ("row 135", "row 155"),
        ("Row 135", "Row 155"),
        ("__ROW157__", "[row 157]"),
        (
            "Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 136)",
            "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        ),
        (
            "verified electronic audit meta prelude capstone closure with the full-book IX.0 → IX.1 Born–Oppenheimer meta capstone reunion",
            "verified electronic audit meta prelude capstone closure (row 155) with the full-book IX.0 → IX.1 Born–Oppenheimer meta prelude capstone reunion",
        ),
        ("when row 135 closed but row 56", "when row 155 closed but row 56"),
        ("when row 135 and row 56", "when row 155 and row 56"),
        (
            "rear-view mirror of row 135's foundation SCF → BO vocabulary turn at the Born–Oppenheimer meta capstone boundary",
            "rear-view mirror of row 155's foundation SCF → BO vocabulary turn at the Born–Oppenheimer meta prelude capstone boundary",
        ),
        (
            "when opening [row 117](preface.md#skill-navigation-row-117) before row 57 closes on the capstone path",
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes on the capstone path",
        ),
        (
            "When row 136 is complete, proceed to [row 137]",
            "When row 156 is complete, proceed to [row 157]",
        ),
        (
            "when opening [row 117](preface.md#skill-navigation-row-117) before row 57 closes",
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes",
        ),
        (
            "row 136 (row 68 ↔ row 56 reunion on the capstone path) with row 116",
            "row 156 (row 68 ↔ row 56 reunion on the capstone path) with row 136",
        ),
        (
            "row 136 names **why that reunion must follow verified electronic audit meta prelude capstone (row 135)",
            "row 156 names **why that reunion must follow verified electronic audit meta prelude capstone (row 155)",
        ),
        ("Row 68 → Row 56 meta (row 116)", "Row 68 → Row 56 meta (row 156)"),
        ("Row 68 → Row 116 reunion index", "Row 68 → Row 136 reunion index"),
        (
            "Proceed to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 135 on the capstone path",
            "Proceed to [row 156](#row-156-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 155 on the capstone path, "
            "to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags on the opening-hinge path",
        ),
        ("before the Kohn–Sham meta reunion", "before the Kohn–Sham meta prelude capstone reunion"),
        ("before the Murnaghan Lab act", "before the Kohn–Sham meta prelude capstone reunion"),
        ("Recite [preface row 135]", "Recite [preface row 155]"),
        ("[row 115](preface.md#skill-navigation-row-115)", "[row 155](preface.md#skill-navigation-row-155)"),
        (
            "Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 116)",
            "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 136)",
        ),
        ("row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116", "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-136"),
        ("row 135 or row 116", "row 155 or row 136"),
        ("row 96", "row 116"),
        ("row 76", "row 96"),
        ("row 37", "row 57"),
        (
            "[row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path",
            "[row 156](preface.md#skill-navigation-row-156) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path",
        ),
        (
            "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
            "When row 156 is complete, proceed to [row 157](preface.md#skill-navigation-row-157) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude capstone still lags after verified Murnaghan archive on the capstone path, to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta prelude capstone is clean but Kohn–Sham meta prelude capstone still lags on the opening-hinge path, to [row 117](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 155](preface.md#skill-navigation-row-155) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
        ),
    ]
    return tx(s, p)


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "skill-navigation-row-156" in text and "### Row 156 skill checkpoint" in text:
        print("preface: row 156 already present")
        return
    m = re.search(
        r"(### Row 136 skill checkpoint.*?)(?=\n### Row 137 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 136 checkpoint missing")
    block = lift_136_to_156(m.group(1))
    anchor = "\n## The copper wire through the book"
    text = text.replace(anchor, "\n" + block + anchor)
    path.write_text(text)
    print("preface: added row 156")


def patch_row_155_proceed() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    old = (
        "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync."
    )
    new = (
        "When row 155 is complete, proceed to [row 156](preface.md#skill-navigation-row-156) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta prelude capstone still lags after verified foundation SCF archive on the capstone path, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta capstone is clean but Born–Oppenheimer meta capstone still lags on the opening-hinge path, to [row 116](preface.md#skill-navigation-row-116) for the Row 68 ↔ Row 56 Born–Oppenheimer opening prelude audit alone, to [row 155](preface.md#skill-navigation-row-155) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync."
    )
    if old in text:
        text = text.replace(old, new, 1)
        path.write_text(text)
        print("preface: patched row 155 proceed links")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-156-closing-loop" in text:
        print("epilogue: row 156 loop already present")
        return
    block = lift_136_to_156(
        extract_between(
            text,
            "### Row 136 closing loop (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion)",
            "### Row 135 closing loop (Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        )
    )
    needle = "### Row 155 closing loop"
    text = text.replace(needle, block + needle, 1)
    old = (
        "Proceed to [row 156](#row-155-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 155 on the capstone path, "
        "to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude still lags on the opening-hinge path"
    )
    new = (
        "Proceed to [row 156](#row-156-closing-loop) when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after row 155 on the capstone path, "
        "to [row 155](#row-155-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 154 on the capstone path, "
        "to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags on the opening-hinge path"
    )
    if old in text:
        text = text.replace(old, new, 1)
    path.write_text(text)
    print("epilogue: added row 156 loop")


def add_prologue() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    line155 = "| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 155) |"
    if "row 156)" in text and "prologue-preview-row-156" in text:
        print("prologue: row 156 already present")
        return
    idx = text.find(line155)
    if idx < 0:
        raise SystemExit("prologue row 155 compass line missing")
    line_end = text.find("\n", idx)
    new_line = lift_136_to_156(
        text[
            text.find(
                "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 136) |"
            ) : text.find("\n", text.find("| Row 68 → Row 136"))
        ]
    )
    text = text[: line_end + 1] + new_line + "\n" + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-155"></span>'
    if preview_src in text and "prologue-preview-row-156" not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_136_to_156(text[i:j])
        text = text.replace(preview_src, preview_block + preview_src, 1)
    stitch = lift_136_to_156(
        "**Row 136 closing stitch (Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion).** {#row-136-closing-stitch} "
        "When row 135 closed — electronic audit meta prelude capstone verified, row 134 or row 115 recited on the capstone path, and VIII.3 Bridge → IX.0 SCF recited with "
        "[foundation SCF audit Lab act](../part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` and `alpha_export.yaml` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the electronic audit Scene on the capstone path** — "
        "`writings/dft` chapters 00 and 01 build as separate reading acts, Hohenberg–Kohn theorems feel disconnected from [electronic audit export manifest](../part09-dft/00-opening.md#electronic-audit-export-manifest-handoff-to-ix1) and `cu.relax.out`, or row 56's Bridge → BO gate feels disconnected from row 135's foundation SCF → theorem vocabulary turn while the unified HTML reads smoothly — "
        "the [preface row 136 When-to-pause opening sentence](../preface.md#skill-navigation-row-136) names the dual reunion before Kohn–Sham meta reunion; read [preface row 136](../preface.md#skill-navigation-row-136), then the "
        "[Row 68 → Row 116 reunion index](../appendix/sources.md#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136), then "
        "[epilogue row 136 closing loop](../epilogue/multiscale.md#row-136-closing-loop) before row 57 Kohn–Sham meta capstone opens.\n\n"
    ).replace("{#row-136-closing-stitch}", "{#row-156-closing-stitch}").replace(
        "Row 136 closing stitch", "Row 156 closing stitch", 1
    )
    if "row-156-closing-stitch" not in text:
        text = text.replace("**Row 155 closing stitch", stitch + "**Row 155 closing stitch", 1)
    path.write_text(text)
    print("prologue: added row 156")


def add_sources() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156"
    if idx_key in text:
        print("sources: row 156 already present")
        return
    block = lift_136_to_156(
        extract_between(
            text,
            "## Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136)",
            "## Row 68 → Row 117 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 137)",
        )
    )
    block = (
        "## Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion index (row 156) {#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156}"
        + block.split("{#row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136}", 1)[-1]
    )
    table_row = (
        "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone (midpoint prelude gate ↔ electronic audit meta prelude capstone ↔ row 56 meta) | "
        f"[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 156](../preface.md#skill-navigation-row-156) · "
        "[prologue row 156 preview](../prologue/00-many-scales.md#prologue-preview-row-156) · "
        "[prologue row 156 closing stitch](../prologue/00-many-scales.md#row-156-closing-stitch) · "
        "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) · "
        "[memory sheet row 156 baby picture](memory-sheet.md#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 56 IX.0 → IX.1 opening hinge still feels disconnected from verified electronic audit meta prelude capstone on the capstone path** — "
        "read row 68 + row 155 or row 136 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[preface row 56](../preface.md#skill-navigation-row-56) |\n"
    )
    text = text.replace(
        "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
        table_row + "| 155 | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
        block + "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155)",
    )
    extra = (
        "[row 156](#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156) reunites **electronic audit meta prelude capstone with the Born–Oppenheimer meta prelude capstone boundary** "
        "when row 155 closed electronic audit meta prelude capstone at verified foundation SCF on the capstone path but `cu.relax.out` and IX.0 → IX.1 opening hinge still read like separate courses after verified Born–Oppenheimer meta prelude meta;"
    )
    if extra not in text:
        text = text.replace(
            "when row 154 closed export meta prelude capstone at verified pedigree checklist on the capstone path but `pedigree_checklist.yaml` and VIII.3 → IX.0 opening hinge still read like separate courses after verified electronic audit meta prelude meta;",
            "when row 154 closed export meta prelude capstone at verified pedigree checklist on the capstone path but `pedigree_checklist.yaml` and VIII.3 → IX.0 opening hinge still read like separate courses after verified electronic audit meta prelude meta; "
            + extra,
        )
    path.write_text(text)
    print("sources: added row 156")


def add_memory() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-156-baby-picture" in text:
        print("memory-sheet: row 156 already present")
        return
    baby = lift_136_to_156(extract_between(text, "### Row 136 baby picture", "### Row 135 baby picture"))
    text = text.replace("### Row 135 baby picture", baby + "### Row 135 baby picture", 1)
    mem_table = (
        "| 156 | Meta | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion | "
        "[Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index](sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156) · "
        "[preface row 156 skill checkpoint](../preface.md#skill-navigation-row-156) · "
        "[prologue row 156 preview](../prologue/00-many-scales.md#prologue-preview-row-156) · "
        "[prologue row 156 closing stitch](../prologue/00-many-scales.md#row-156-closing-stitch) · "
        "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) | "
        "Row 68 closed but row 56 IX.0 → IX.1 opening hinge feels disconnected from verified electronic audit meta prelude capstone on the capstone path — "
        "read row 68 + row 155 or row 136 gate + IX.0 Bridge → opening hinge → IX.1 BO/HK + row 56; "
        "[row 156 baby picture](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
        mem_table + "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
    )
    if "When row 155 closed but Born–Oppenheimer meta reunion still lags" not in text:
        text = text.replace(
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion).",
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion). "
            "When row 155 closed but Born–Oppenheimer meta prelude capstone reunion still lags on the capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 156")


def main() -> None:
    patch_row_155_proceed()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue()
    add_sources()
    add_memory()


if __name__ == "__main__":
    main()
