#!/usr/bin/env python3
"""Add row 156 (Born–Oppenheimer meta prelude capstone reunion) from row 136 baseline."""
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
    s = s.replace("Row 68 → Row 116", "__ROW68ROW136__")
    s = s.replace("Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta capstone", "__ROW156TITLE__")
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
            "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136",
            "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156",
        ),
        (
            "row-136-baby-picture-row68-row116-born-oppenheimer-meta-capstone-reunion",
            "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion",
        ),
        ("[row 137]", "__ROW137__"),
        ("[row 136]", "[row 156]"),
        ("row 136", "row 156"),
        ("Row 136", "Row 156"),
        ("__ROW137__", "[row 137]"),
        ("[row 135]", "[row 155]"),
        ("row 135", "row 155"),
        ("Row 135", "Row 155"),
        ("[row 116]", "[row 136]"),
        ("row 116", "row 136"),
        ("Row 116", "Row 136"),
        (
            "Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 136)",
            "Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 156)",
        ),
        (
            "verified electronic audit meta prelude capstone closure (row 135)",
            "verified electronic audit meta prelude capstone closure (row 155)",
        ),
        ("when row 135 closed but row 56", "when row 155 closed but row 56"),
        ("when row 135 and row 56", "when row 155 and row 56"),
        (
            "rear-view mirror of row 135's foundation SCF → BO vocabulary turn",
            "rear-view mirror of row 155's foundation SCF → BO vocabulary turn",
        ),
        (
            "when opening [row 117](preface.md#skill-navigation-row-117) before row 57 closes on the capstone path",
            "when opening [row 157](preface.md#skill-navigation-row-157) before row 57 closes on the capstone path",
        ),
        (
            "When row 136 is complete, proceed to [row 137]",
            "When row 156 is complete, proceed to [row 137]",
        ),
        (
            "When row 56 feels like quantum chemistry homework after row 135 alone",
            "When row 56 feels like quantum chemistry homework after row 155 alone on the capstone path",
        ),
        (
            "row 136 (row 68 ↔ row 56 reunion) with row 116",
            "row 156 (row 68 ↔ row 56 reunion on the capstone path) with row 136",
        ),
        (
            "row 136 names **why that reunion must follow verified electronic audit meta prelude capstone (row 135)",
            "row 156 names **why that reunion must follow verified electronic audit meta prelude capstone (row 155)",
        ),
        ("Row 68 → Row 56 meta (row 116)", "Row 68 → Row 56 meta (row 156)"),
        ("Row 68 → Row 116 reunion index", "Row 68 → Row 136 reunion index"),
        (
            "Proceed to [row 117](#row-136-closing-loop) when row 68 closed but Kohn–Sham meta capstone still lags after row 136",
            "Proceed to [row 157](#row-156-closing-loop) when row 68 closed but Kohn–Sham meta prelude capstone still lags after row 156 on the capstone path, "
            "to [row 136](#row-136-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags on the opening-hinge path",
        ),
        ("before the Kohn–Sham meta reunion", "before the Kohn–Sham meta prelude capstone reunion"),
        ("Recite [preface row 135]", "Recite [preface row 155]"),
        (
            "[row 115](preface.md#skill-navigation-row-115) or [Row 68 → Row 116 Born–Oppenheimer meta capstone reunion index (row 116)]",
            "[row 155](preface.md#skill-navigation-row-155) or [Row 68 → Row 136 Born–Oppenheimer meta prelude capstone reunion index (row 136)]",
        ),
        ("Born–Oppenheimer meta capstone reunion", "Born–Oppenheimer meta prelude capstone reunion"),
        ("Born–Oppenheimer meta capstone at the foundation", "Born–Oppenheimer meta prelude capstone at the foundation"),
        ("before Born–Oppenheimer meta capstone", "before Born–Oppenheimer meta prelude capstone"),
        ("Born–Oppenheimer meta capstone for index-card", "Born–Oppenheimer meta prelude capstone for index-card"),
        (
            "it names the dual reunion before the Murnaghan Lab act",
            "it names the dual reunion before the Kohn–Sham meta prelude capstone reunion",
        ),
        (
            "when `cu.relax.out` exists on the capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 135",
            "when `cu.relax.out` exists on the capstone path but \\(V_{\\text{BO}}\\) is unnamed after row 155",
        ),
        (
            "when row 135 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone on the capstone path",
            "when row 155 closed but row 56 IX.0 → IX.1 reunion still feels like quantum chemistry homework disconnected from verified electronic audit meta prelude capstone on the capstone path",
        ),
        (
            "Row 68 → Row 56 meta (row 136) must read as one SCF log",
            "Row 68 → Row 56 meta (row 156) must read as one SCF log",
        ),
        (
            "Do not conflate row 136 (row 68 ↔ row 56 reunion) with row 116",
            "Do not conflate row 156 (row 68 ↔ row 56 reunion on the capstone path) with row 136",
        ),
        (
            "row 116 names **Row 68 → Row 76 Row 68 → Row 56 Born–Oppenheimer meta prelude reunion**; row 136 names",
            "row 136 names **Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion**; row 156 names",
        ),
    ]
    s = tx(s, p)
    s = s.replace("__ROW68ROW136__", "Row 68 → Row 136")
    s = s.replace(
        "__ROW156TITLE__",
        "Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone",
    )
    return s


def dedupe_epilogue_closing_loops() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    seen: set[str] = set()

    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1)
        if anchor in seen:
            return ""
        seen.add(anchor)
        return m.group(0)

    text = re.sub(
        r"(?ms)^### Row \d+ closing loop[^\n]*\{#(row-\d+-closing-loop)\}.*?(?=^### Row |\Z)",
        repl,
        text,
    )
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    path.write_text(text)
    print(f"epilogue: deduped closing loops ({len(seen)} unique anchors kept)")


def insert_preface_row() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    if "### Row 156 skill checkpoint" in text:
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
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    # Fix row 155 proceed tail
    text = text.replace(
        "When row 136 is complete, proceed to [row 137](preface.md#skill-navigation-row-137) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags after verified Murnaghan archive on the capstone path, to [row 117](preface.md#skill-navigation-row-117) when Born–Oppenheimer meta capstone is clean but Kohn–Sham meta capstone still lags on the opening-hinge path, to [row 97](preface.md#skill-navigation-row-117) for the Row 68 ↔ Row 57 Kohn–Sham opening prelude audit alone, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta prelude capstone still lags after verified foundation SCF on the capstone path, to [row 57](preface.md#skill-navigation-row-57) when only IX.1 → IX.2 stalls, or extend prose only under `writings/` then sync.",
        "When row 155 is complete, proceed to [row 156](preface.md#skill-navigation-row-156) when electronic audit meta prelude capstone is clean but Born–Oppenheimer meta prelude capstone still lags after verified foundation SCF archive on the capstone path, to [row 136](preface.md#skill-navigation-row-136) when electronic audit meta capstone is clean but Born–Oppenheimer meta capstone still lags on the opening-hinge path, to [row 96](preface.md#skill-navigation-row-96) for the Row 68 ↔ Row 56 Born–Oppenheimer opening prelude audit alone, to [row 155](preface.md#skill-navigation-row-155) when export meta prelude capstone still lags after verified pedigree checklist on the capstone path, to [row 56](preface.md#skill-navigation-row-56) when only IX.0 → IX.1 stalls, or extend prose only under `writings/` then sync.",
        1,
    )
    path.write_text(text)
    print("preface: added row 156")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "row-156-closing-loop" in text:
        print("epilogue: row 156 loop already present")
        return
    block = lift_136_to_156(
        extract_between(
            text,
            "### Row 136 closing loop",
            "### Row 135 closing loop",
        )
    )
    needle = "### Row 155 closing loop"
    if needle not in text:
        needle = "### Row 135 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 156 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    after = "| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 155) |"
    if "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 156) |" in text:
        print("prologue: row 156 compass already present")
    else:
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 155 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion (row 136) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 136 compass missing")
        new_line = lift_136_to_156(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-136"></span>'
    preview_dst = '| <span id="prologue-preview-row-156"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_136_to_156(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "row-156-closing-stitch" not in text:
        stitch = (
            "**Row 155 closing stitch (Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion).** {#row-156-closing-stitch} "
            "When row 154 closed — export meta prelude capstone verified, row 153 or row 134 recited on the capstone path, and VIII.2 Bridge → VIII.3 pedigree recited with "
            "[EAM-fit audit Lab act](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the foundation SCF Lab act on the capstone path** — "
            "the [preface row 156 When-to-pause opening sentence](../preface.md#skill-navigation-row-156) names the dual reunion before Kohn–Sham meta prelude capstone reunion; "
            "read [preface row 156](../preface.md#skill-navigation-row-156), then the "
            "[Row 68 → Row 136 reunion index](../appendix/sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156), then "
            "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) before row 57 Kohn–Sham meta prelude opens on the capstone path.\n\n"
        )
        # Fix stitch header to row 156 content (born from row 155 electronic stitch template)
        stitch = (
            "**Row 156 closing stitch (Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion).** {#row-156-closing-stitch} "
            "When row 155 closed — electronic audit meta prelude capstone verified, row 154 or row 135 recited on the capstone path, and VIII.3 Bridge → IX.0 SCF recited with "
            "[foundation SCF audit Lab act](../part09-dft/00-opening.md#lab-act-foundation-scf-audit-before-born-oppenheimer-act-vi--foundation) archived `cu.relax.out` — but **row 56 IX.0 → IX.1 opening hinge still opens like standalone quantum chemistry homework after the electronic audit Scene on the capstone path** — "
            "read [preface row 156](../preface.md#skill-navigation-row-156), the "
            "[Row 68 → Row 136 reunion index](../appendix/sources.md#row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156), and "
            "[epilogue row 156 closing loop](../epilogue/multiscale.md#row-156-closing-loop) before row 57 Kohn–Sham meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 155 closing stitch", stitch + "**Row 155 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 156 compass/preview/stitch")


def lift_116_section_to_156(s: str) -> str:
    p = [
        ("row 116", "row 156"),
        ("Row 116", "Row 156"),
        ("row68-row96-born-oppenheimer-meta-capstone-reunion-index-row-116", "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156"),
        ("Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone", "Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone"),
        ("Born–Oppenheimer meta capstone reunion index (row 116)", "Born–Oppenheimer meta prelude capstone reunion index (row 156)"),
        ("Born–Oppenheimer meta capstone reunion**", "Born–Oppenheimer meta prelude capstone reunion**"),
        ("Born–Oppenheimer meta capstone boundary", "Born–Oppenheimer meta prelude capstone boundary"),
        ("electronic audit meta capstone", "electronic audit meta prelude capstone"),
        ("row 115", "row 155"),
        ("Row 115", "Row 155"),
        ("row68-row95-electronic-audit-meta-prelude-reunion-index-row-115", "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155"),
        ("row 96", "row 136"),
        ("Row 96", "Row 136"),
        ("row68-row76-born-oppenheimer-meta-prelude-reunion-index-row-96", "row68-row116-born-oppenheimer-meta-capstone-reunion-index-row-136"),
        ("skill-navigation-row-136", "skill-navigation-row-156"),
        ("row-116-baby-picture", "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion"),
        ("row-116-baby-picture-row68-row96-born-oppenheimer-meta-capstone-reunion", "row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion"),
        ("on the capstone path", "on the capstone path"),
        ("before row 97 Kohn–Sham meta prelude opens", "before row 57 Kohn–Sham meta prelude opens on the capstone path"),
        ("Preface row 116", "Preface row 156"),
        ("memory sheet row 116 baby picture", "memory sheet row 156 baby picture"),
    ]
    return tx(s, p)


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row136-born-oppenheimer-meta-prelude-capstone-reunion-index-row-156"
    if idx_key in text:
        print("sources: row 156 already present")
        return
    block = lift_116_section_to_156(
        extract_between(
            text,
            "## Row 68 → Row 96 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 116)",
            "## Row 68 → Row 137 Row 68 → Row 57 Kohn–Sham meta capstone reunion index (row 137)",
        )
    )
    table_row = (
        "| 156 | Row 68 → Row 136 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone "
        "(midpoint prelude gate ↔ electronic audit meta prelude capstone ↔ row 56 meta) | "
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
    path.write_text(text)
    print("sources: added row 156")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-156-baby-picture" in text:
        print("memory-sheet: row 156 already present")
        return
    baby = lift_136_to_156(
        extract_between(text, "### Row 136 baby picture", "### Row 135 baby picture")
    )
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
        mem_table + "| 155 | Meta | Row 68 → Row 136 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
    )
    # Fix accidental replacement in 155 row if duplicated
    text = text.replace(
        "| 155 | Meta | Row 68 → Row 136 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
        "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion |",
    )
    switch = (
        "When row 155 closed but Born–Oppenheimer meta reunion still lags on the capstone path, switch to [row 156](#row-156-baby-picture-row68-row136-born-oppenheimer-meta-prelude-capstone-reunion)."
    )
    if "When row 155 closed but Born–Oppenheimer meta reunion still lags" not in text:
        text = text.replace(
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion).",
            "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion). "
            + switch,
        )
    path.write_text(text)
    print("memory-sheet: added row 156")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()


if __name__ == "__main__":
    main()
