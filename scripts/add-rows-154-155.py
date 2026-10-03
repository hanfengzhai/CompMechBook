#!/usr/bin/env python3
"""Add row 154 (export meta prelude capstone reunion) and row 155 (electronic audit meta prelude capstone reunion)."""
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


def lift_134_to_154(s: str) -> str:
    p = [
        ("skill-navigation-row-134", "skill-navigation-row-154"),
        ("### Row 134 skill checkpoint", "### Row 154 skill checkpoint"),
        ("Row 134 does not replace", "Row 154 does not replace"),
        ("Row 134 three-way audit", "Row 154 three-way audit"),
        ("Row 134 closing loop", "Row 154 closing loop"),
        ("row-134-closing-loop", "row-154-closing-loop"),
        ("Row 134 closing stitch", "Row 154 closing stitch"),
        ("row-134-closing-stitch", "row-154-closing-stitch"),
        ("prologue-preview-row-134", "prologue-preview-row-154"),
        ("Row 134 preview", "Row 154 preview"),
        ("Row 134 skill checkpoint", "Row 154 skill checkpoint"),
        ("memory sheet row 134", "memory sheet row 154"),
        ("Row 134 baby picture", "Row 154 baby picture"),
        (
            "Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone",
            "Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone",
        ),
        (
            "row68-row114-export-meta-prelude-capstone-reunion-index-row-134",
            "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        ),
        (
            "row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion",
            "row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion",
        ),
        ("[row 135]", "__ROW135__"),
        ("[row 133]", "[row 153]"),
        ("row 133", "row 153"),
        ("Row 133", "Row 153"),
        ("__ROW135__", "[row 135]"),
        (
            "Row 68 → Row 114 export meta prelude capstone reunion index (row 134)",
            "Row 68 → Row 134 export meta prelude capstone reunion index (row 154)",
        ),
        (
            "verified dynamics meta prelude capstone closure (row 133)",
            "verified dynamics meta prelude capstone closure (row 153)",
        ),
        ("when row 133 closed but row 54", "when row 153 closed but row 54"),
        ("when row 133 and row 54", "when row 153 and row 54"),
        (
            "rear-view mirror of row 133's finite-\\(T\\) dynamics → yaml handoff turn",
            "rear-view mirror of row 153's NPT archive → pedigree checklist turn",
        ),
        (
            "when opening [row 115](preface.md#skill-navigation-row-115) before row 55 closes on the capstone path",
            "when opening [row 155](preface.md#skill-navigation-row-155) before row 55 closes on the capstone path",
        ),
        (
            "When row 134 is complete, proceed to [row 135]",
            "When row 154 is complete, proceed to [row 155]",
        ),
        (
            "When row 54 feels like export homework after row 133 alone on the capstone path",
            "When row 54 feels like export homework after row 153 alone on the capstone path",
        ),
        (
            "row 134 (row 68 ↔ row 54 reunion on the capstone path) with row 114",
            "row 154 (row 68 ↔ row 54 reunion on the capstone path) with row 134",
        ),
        (
            "row 134 names **why that reunion must follow verified dynamics meta prelude capstone (row 133)",
            "row 154 names **why that reunion must follow verified dynamics meta prelude capstone (row 153)",
        ),
        ("Row 68 → Row 54 meta (row 114)", "Row 68 → Row 54 meta (row 154)"),
        ("Row 68 → Row 114 reunion index", "Row 68 → Row 134 reunion index"),
        (
            "Proceed to [row 115](#row-134-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 134 on the capstone path",
            "Proceed to [row 155](#row-154-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 154 on the capstone path, "
            "to [row 134](#row-134-closing-loop) when row 68 closed but export meta prelude still lags on the opening-hinge path",
        ),
        ("before the electronic audit meta reunion", "before the electronic audit meta prelude capstone reunion"),
        ("Recite [preface row 133]", "Recite [preface row 153]"),
        ("[row 115](preface.md#skill-navigation-row-115)", "[row 135](preface.md#skill-navigation-row-135)"),
        (
            "[Row 68 → Row 95 electronic audit meta prelude reunion index (row 115)]",
            "[Row 68 → Row 115 electronic audit meta prelude reunion index (row 135)]",
        ),
        ("[row 134](preface.md#skill-navigation-row-134) or [row 115]", "[row 154](preface.md#skill-navigation-row-154) or [row 135]"),
    ]
    return tx(s, p)


def lift_135_to_155(s: str) -> str:
    p = [
        ("skill-navigation-row-135", "skill-navigation-row-155"),
        ("### Row 135 skill checkpoint", "### Row 155 skill checkpoint"),
        ("Row 135 does not replace", "Row 155 does not replace"),
        ("Row 135 three-way audit", "Row 155 three-way audit"),
        ("Row 135 closing loop", "Row 155 closing loop"),
        ("row-135-closing-loop", "row-155-closing-loop"),
        ("Row 135 closing stitch", "Row 155 closing stitch"),
        ("row-135-closing-stitch", "row-155-closing-stitch"),
        ("prologue-preview-row-135", "prologue-preview-row-155"),
        ("Row 135 preview", "Row 155 preview"),
        ("Row 135 skill checkpoint", "Row 155 skill checkpoint"),
        ("memory sheet row 135", "memory sheet row 155"),
        ("Row 135 baby picture", "Row 155 baby picture"),
        (
            "Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone",
            "Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone",
        ),
        (
            "row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135",
            "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
        ),
        (
            "row-135-baby-picture-row68-row115-electronic-audit-meta-prelude-capstone-reunion",
            "row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion",
        ),
        ("[row 136]", "__ROW136__"),
        ("[row 134]", "[row 154]"),
        ("row 134", "row 154"),
        ("Row 134", "Row 154"),
        ("__ROW136__", "[row 136]"),
        (
            "Row 68 → Row 115 electronic audit meta prelude capstone reunion index (row 135)",
            "Row 68 → Row 135 electronic audit meta prelude capstone reunion index (row 155)",
        ),
        (
            "verified export meta prelude capstone closure (row 134)",
            "verified export meta prelude capstone closure (row 154)",
        ),
        ("when row 134 closed but row 55", "when row 154 closed but row 55"),
        ("when row 134 and row 55", "when row 154 and row 55"),
        (
            "rear-view mirror of row 134's yaml pedigree → foundation SCF turn",
            "rear-view mirror of row 154's pedigree checklist → IX.0 SCF audit turn",
        ),
        (
            "when opening [row 116](preface.md#skill-navigation-row-136) before row 56 closes on the capstone path",
            "when opening [row 156](preface.md#skill-navigation-row-156) before row 56 closes on the capstone path",
        ),
        (
            "When row 135 is complete, proceed to [row 136]",
            "When row 155 is complete, proceed to [row 156]",
        ),
        (
            "When row 55 feels like DFT homework after row 134 alone on the capstone path",
            "When row 55 feels like DFT homework after row 154 alone on the capstone path",
        ),
        (
            "row 135 (row 68 ↔ row 55 reunion on the capstone path) with row 115",
            "row 155 (row 68 ↔ row 55 reunion on the capstone path) with row 135",
        ),
        (
            "row 135 names **why that reunion must follow verified export meta prelude capstone (row 134)",
            "row 155 names **why that reunion must follow verified export meta prelude capstone (row 154)",
        ),
        ("Row 68 → Row 55 meta (row 115)", "Row 68 → Row 55 meta (row 155)"),
        ("Row 68 → Row 115 reunion index", "Row 68 → Row 135 reunion index"),
        (
            "Proceed to [row 116](#row-135-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 135 on the capstone path",
            "Proceed to [row 156](#row-155-closing-loop) when row 68 closed but Born–Oppenheimer meta capstone still lags after row 155 on the capstone path, "
            "to [row 135](#row-135-closing-loop) when row 68 closed but electronic audit meta prelude still lags on the opening-hinge path",
        ),
        ("before the Born–Oppenheimer meta reunion", "before the Born–Oppenheimer meta prelude capstone reunion"),
        ("Recite [preface row 134]", "Recite [preface row 154]"),
        ("[row 115](preface.md#skill-navigation-row-115)", "[row 135](preface.md#skill-navigation-row-135)"),
    ]
    return tx(s, p)


def insert_preface_row(row_num: int, lift_fn, src_anchor: str, dst_anchor: str) -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    skill = f"skill-navigation-row-{row_num}"
    if skill in text and f"### Row {row_num} skill checkpoint" in text:
        print(f"preface: row {row_num} already present")
        return
    m = re.search(
        rf"(### Row {src_anchor} skill checkpoint.*?)(?=\n### Row {dst_anchor} skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit(f"preface row {src_anchor} checkpoint missing")
    block = lift_fn(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    # Insert after row 153 if adding 154/155
    insert_at = idx
    if row_num > 153:
        r153 = text.find("### Row 153 skill checkpoint")
        if r153 >= 0 and r153 < idx:
            insert_at = idx
    text = text[:insert_at] + "\n" + block + text[insert_at:]
    path.write_text(text)
    print(f"preface: added row {row_num}")


def insert_epilogue_loop(row_num: int, lift_fn, src_num: int, before_num: int) -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if f"row-{row_num}-closing-loop" in text:
        print(f"epilogue: row {row_num} loop already present")
        return
    block = lift_fn(
        extract_between(
            text,
            f"### Row {src_num} closing loop",
            f"### Row {before_num} closing loop",
        )
    )
    needle = f"### Row {before_num} closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print(f"epilogue: added row {row_num} loop")


def add_prologue_compass(row_num: int, lift_fn, after_line: str, src_line: str) -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    lifted_src = lift_fn(src_line)
    if lifted_src.strip() in text:
        print(f"prologue: row {row_num} compass already present")
        return
    idx = text.find(after_line)
    if idx < 0:
        raise SystemExit(f"prologue line not found: {after_line[:60]}")
    line_end = text.find("\n", idx)
    new_line = lift_fn(text[idx:line_end]) + "\n"
    text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = f'| <span id="prologue-preview-row-{row_num - 20}"></span>'
    if row_num == 154:
        preview_src = '| <span id="prologue-preview-row-134"></span>'
    if row_num == 155:
        preview_src = '| <span id="prologue-preview-row-135"></span>'
    preview_dst = f'| <span id="prologue-preview-row-{row_num}"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_fn(text[i:j])
        text = text.replace(preview_src, preview_block + preview_src, 1)
    stitch_key = f"row-{row_num}-closing-stitch"
    if stitch_key not in text:
        if row_num == 154:
            stitch = (
                "**Row 153 closing stitch (Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-154-closing-stitch} "
                "When row 153 closed — dynamics meta prelude capstone verified, row 152 or row 133 recited on the capstone path, and VIII.1 Bridge → VIII.2 NPT recited with "
                "[NPT Lab act](../part08-md/02-ensembles-integrators.md#lab-act-npt-tension-on-a-copper-nanowire-segment) archived `cu.elastic/` — but **row 54 VIII.2 → VIII.3 opening hinge still opens like standalone coarse-graining homework after the thermostat Scene on the capstone path** — "
                "the [preface row 154 When-to-pause opening sentence](../preface.md#skill-navigation-row-154) names the dual reunion before the electronic audit meta prelude capstone reunion; "
                "read [preface row 154](../preface.md#skill-navigation-row-154), then the "
                "[Row 68 → Row 134 reunion index](../appendix/sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154), then "
                "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) before row 55 electronic audit meta prelude opens on the capstone path.\n\n"
            )
            text = text.replace("**Row 153 closing stitch", stitch + "**Row 153 closing stitch", 1)
        elif row_num == 155:
            stitch = (
                "**Row 154 closing stitch (Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-155-closing-stitch} "
                "When row 154 closed — export meta prelude capstone verified, row 153 or row 134 recited on the capstone path, and VIII.2 Bridge → VIII.3 pedigree recited with "
                "[EAM-fit audit Lab act](../part08-md/03-ab-initio-and-coarse-graining.md#lab-act-eam-fit-audit-before-the-notch-md-run-act-v--notch) archived `pedigree_checklist.yaml` — but **row 55 VIII.3 → IX.0 opening hinge still opens like standalone DFT homework after the export Scene on the capstone path** — "
                "the [preface row 155 When-to-pause opening sentence](../preface.md#skill-navigation-row-155) names the dual reunion before Born–Oppenheimer meta prelude capstone reunion; "
                "read [preface row 155](../preface.md#skill-navigation-row-155), then the "
                "[Row 68 → Row 135 reunion index](../appendix/sources.md#row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155), then "
                "[epilogue row 155 closing loop](../epilogue/multiscale.md#row-155-closing-loop) before row 56 Born–Oppenheimer meta prelude opens on the capstone path.\n\n"
            )
            text = text.replace("**Row 154 closing stitch", stitch + "**Row 154 closing stitch", 1)
    path.write_text(text)
    print(f"prologue: added row {row_num} compass/preview/stitch")


def add_sources_row(row_num: int, lift_fn, src_section: int, table_src: int) -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = {
        154: "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        155: "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
    }[row_num]
    if idx_key in text:
        print(f"sources: row {row_num} already present")
        return
    block = lift_fn(
        extract_between(
            text,
            f"## Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion index (row {src_section})",
            f"## Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 135)",
        )
        if row_num == 154
        else extract_between(
            text,
            "## Row 68 → Row 115 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 135)",
            "## Row 68 → Row 116 Row 68 → Row 56 Born–Oppenheimer meta capstone reunion index (row 136)",
        )
    )
    if row_num == 154:
        block = "## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154) {#row68-row134-export-meta-prelude-capstone-reunion-index-row-154}" + block.split("{#row68-row114-export-meta-prelude-capstone-reunion-index-row-134}", 1)[-1]
        table_row = (
            f"| {row_num} | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone (midpoint prelude gate ↔ dynamics meta prelude capstone ↔ row 54 meta) | "
            f"[Row 68 → Row 134 export meta prelude capstone reunion index](#{idx_key}) · "
            f"[preface row {row_num}](../preface.md#skill-navigation-row-{row_num}) · "
            f"[prologue row {row_num} preview](../prologue/00-many-scales.md#prologue-preview-row-{row_num}) · "
            f"[prologue row {row_num} closing stitch](../prologue/00-many-scales.md#row-{row_num}-closing-stitch) · "
            f"[epilogue row {row_num} closing loop](../epilogue/multiscale.md#row-{row_num}-closing-loop) · "
            f"[memory sheet row {row_num} baby picture](memory-sheet.md#row-{row_num}-baby-picture-row68-row134-export-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 54 VIII.2 → VIII.3 opening hinge still feels disconnected from verified dynamics meta prelude capstone on the capstone path** — "
            "read row 68 + row 153 or row 134 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
            f"[preface row 54](../preface.md#skill-navigation-row-54) |\n"
        )
        text = text.replace(
            "| 153 | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
            table_row + "| 153 | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone",
        )
        text = text.replace(
            "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)",
            block + "## Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 153)",
        )
    else:
        block = "## Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 155) {#row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155}" + block.split("{#row68-row115-electronic-audit-meta-prelude-capstone-reunion-index-row-135}", 1)[-1]
        table_row = (
            f"| {row_num} | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone (midpoint prelude gate ↔ export meta prelude capstone ↔ row 55 meta) | "
            f"[Row 68 → Row 135 electronic audit meta prelude capstone reunion index](#{idx_key}) · "
            f"[preface row {row_num}](../preface.md#skill-navigation-row-{row_num}) · "
            f"[prologue row {row_num} preview](../prologue/00-many-scales.md#prologue-preview-row-{row_num}) · "
            f"[prologue row {row_num} closing stitch](../prologue/00-many-scales.md#row-{row_num}-closing-stitch) · "
            f"[epilogue row {row_num} closing loop](../epilogue/multiscale.md#row-{row_num}-closing-loop) · "
            f"[memory sheet row {row_num} baby picture](memory-sheet.md#row-{row_num}-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 55 VIII.3 → IX.0 opening hinge still feels disconnected from verified export meta prelude capstone on the capstone path** — "
            "read row 68 + row 154 or row 135 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; "
            f"[preface row 55](../preface.md#skill-navigation-row-55) |\n"
        )
        text = text.replace(
            "| 154 | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone",
            table_row + "| 154 | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone",
        )
        text = text.replace(
            "## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154)",
            block + "## Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion index (row 154)",
        )
    path.write_text(text)
    print(f"sources: added row {row_num}")


def add_memory_row(row_num: int, lift_fn, src_baby: int, before_baby: str) -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if f"row-{row_num}-baby-picture" in text:
        print(f"memory-sheet: row {row_num} already present")
        return
    baby = lift_fn(extract_between(text, f"### Row {src_baby} baby picture", f"### {before_baby}"))
    text = text.replace(f"### {before_baby}", baby + f"### {before_baby}", 1)
    prev = row_num - 1
    mem_table = lift_fn(
        f"| {prev} | Meta | Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion | placeholder |\n"
    )
    if row_num == 154:
        mem_table = (
            "| 154 | Meta | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion | "
            "[Row 68 → Row 134 export meta prelude capstone reunion index](sources.md#row68-row134-export-meta-prelude-capstone-reunion-index-row-154) · "
            "[preface row 154 skill checkpoint](../preface.md#skill-navigation-row-154) · "
            "[prologue row 154 preview](../prologue/00-many-scales.md#prologue-preview-row-154) · "
            "[prologue row 154 closing stitch](../prologue/00-many-scales.md#row-154-closing-stitch) · "
            "[epilogue row 154 closing loop](../epilogue/multiscale.md#row-154-closing-loop) | "
            "Row 68 closed but row 54 VIII.2 → VIII.3 opening hinge feels disconnected from verified dynamics meta prelude capstone on the capstone path — "
            "read row 68 + row 153 or row 134 gate + VIII.2 Bridge → opening hinge → VIII.3 pedigree + row 54; "
            "[row 154 baby picture](#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion) |\n"
        )
        text = text.replace(
            "| 153 | Meta | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion |",
            mem_table + "| 153 | Meta | Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion |",
        )
        old = "When row 152 closed but dynamics meta reunion still lags"
        new = (
            "When row 152 closed but dynamics meta reunion still lags on the capstone path, switch to [row 153](#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion). "
            "When row 153 closed but export meta reunion still lags on the capstone path, switch to [row 154](#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion)."
        )
        if "When row 153 closed but export meta reunion still lags" not in text and old in text:
            text = text.replace(
                "When row 152 closed but dynamics meta reunion still lags on the capstone path, switch to [row 153](#row-153-baby-picture-row68-row133-dynamics-meta-prelude-capstone-reunion).",
                new,
            )
    else:
        mem_table = (
            "| 155 | Meta | Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion | "
            "[Row 68 → Row 135 electronic audit meta prelude capstone reunion index](sources.md#row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155) · "
            "[preface row 155 skill checkpoint](../preface.md#skill-navigation-row-155) · "
            "[prologue row 155 preview](../prologue/00-many-scales.md#prologue-preview-row-155) · "
            "[prologue row 155 closing stitch](../prologue/00-many-scales.md#row-155-closing-stitch) · "
            "[epilogue row 155 closing loop](../epilogue/multiscale.md#row-155-closing-loop) | "
            "Row 68 closed but row 55 VIII.3 → IX.0 opening hinge feels disconnected from verified export meta prelude capstone on the capstone path — "
            "read row 68 + row 154 or row 135 gate + VIII.3 Bridge → opening hinge → IX.0 SCF audit + row 55; "
            "[row 155 baby picture](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion) |\n"
        )
        text = text.replace(
            "| 154 | Meta | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion |",
            mem_table + "| 154 | Meta | Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion |",
        )
        if "When row 154 closed but electronic audit meta reunion still lags" not in text:
            text = text.replace(
                "When row 153 closed but export meta reunion still lags on the capstone path, switch to [row 154](#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion).",
                "When row 153 closed but export meta reunion still lags on the capstone path, switch to [row 154](#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion). "
                "When row 154 closed but electronic audit meta reunion still lags on the capstone path, switch to [row 155](#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion).",
            )
    path.write_text(text)
    print(f"memory-sheet: added row {row_num}")


def patch_row_153_proceed_links() -> None:
    preface = ROOT / "writings/preface/chapters/preface.md"
    text = preface.read_text()
    text = text.replace(
        "when opening [row 154](preface.md#skill-navigation-row-153) before row 54 closes",
        "when opening [row 154](preface.md#skill-navigation-row-154) before row 54 closes",
    )
    preface.write_text(text)


def main() -> None:
    insert_preface_row(154, lift_134_to_154, "134", "135")
    insert_preface_row(155, lift_135_to_155, "135", "136")
    insert_epilogue_loop(154, lift_134_to_154, 134, 153)
    insert_epilogue_loop(155, lift_135_to_155, 135, 154)
    line153 = "| Row 68 → Row 133 Row 68 → Row 53 dynamics meta prelude capstone reunion (row 153) |"
    add_prologue_compass(154, lift_134_to_154, line153, line153)
    line154 = "| Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion (row 154) |"
    add_prologue_compass(155, lift_135_to_155, line154, line154)
    add_sources_row(154, lift_134_to_154, 134, 153)
    add_sources_row(155, lift_135_to_155, 135, 154)
    add_memory_row(154, lift_134_to_154, 134, "Row 133 baby picture")
    add_memory_row(155, lift_135_to_155, 135, "Row 134 baby picture")
    patch_row_153_proceed_links()


if __name__ == "__main__":
    main()
