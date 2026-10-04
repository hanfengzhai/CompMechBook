#!/usr/bin/env python3
"""Add row 170 (Row 68 → Row 150 ↔ Row 50 DDD meta prelude capstone on capstone path)."""
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


LIFT_150_TO_170_PAIRS: list[tuple[str, str]] = [('skill-navigation-row-__N130', 'skill-navigation-row-__N150'), ('Row 68 → Row 130 DDD meta prelude reunion index (row 130)', 'Row 68 → Row 130 DDD meta prelude capstone reunion index (row 150)'), ('Row 150 does not replace', 'Row 170 does not replace'), ('Prologue preview ([row 150]', 'Prologue preview ([row 170]'), ('[preface row 150 skill checkpoint](../preface.md#skill-navigation-row-__N170)', '[preface row 170 skill checkpoint](../preface.md#skill-navigation-row-__N170)'), ('Row 151 closing loop', '__PH0__'), ('Row 150 closing loop', 'Row 170 closing loop'), ('row-__N151-closing-loop', '__PH0__'), ('row-__N150-closing-loop', 'row-__N170-closing-loop'), ('Row 151 closing stitch', '__PH0__'), ('Row 150 closing stitch', 'Row 170 closing stitch'), ('row-__N151-closing-stitch', '__PH0__'), ('row-__N150-closing-stitch', 'row-__N170-closing-stitch'), ('prologue-preview-row-__N151', '__PH0__'), ('prologue-preview-row-__N150', 'prologue-preview-row-__N170'), ('Row 151 preview', '__PH0__'), ('Row 150 preview', 'Row 170 preview'), ('Row 151 skill checkpoint', '__PH0__'), ('Row 150 skill checkpoint', 'Row 170 skill checkpoint'), ('skill-navigation-row-__N151', '__PH0__'), ('skill-navigation-row-__N150', 'skill-navigation-row-__N170'), ('memory sheet row 151', '__PH0__'), ('memory sheet row 150', 'memory sheet row 170'), ('Row 151 baby picture', '__PH0__'), ('Row 150 baby picture', 'Row 170 baby picture'), ('Row 151 three-way audit', '__PH0__'), ('Row 150 three-way audit', 'Row 170 three-way audit'), ('Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone', 'Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone'), ('row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170', 'row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170'), ('row-__N150-baby-picture-row68-row110-ddd-meta-prelude-capstone-reunion', 'row-__N170-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion'), ('[row 151]', '__PH0__'), ('[row 130]', '[row 150]'), ('row 130', 'row 150'), ('Row 130', 'Row 150'), ('__PH0__', '[row 151]'), ('skill-navigation-row-__N149', 'skill-navigation-row-149'), ('[row 149]', '__PH0__'), ('[row 129]', '[row 149]'), ('row 149', 'row 149'), ('Row 149', 'Row 149'), ('__PH0__', '[row 149]'), ('Row 68 → Row 130 DDD meta prelude reunion index (row 130)', 'Row 68 → Row 130 DDD meta prelude capstone reunion index (row 150)'), ('row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150', 'row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170'), ('when Burgers geometry is clear on the capstone path but Peach–Köhler force derivations feel disconnected from the slip-line Lab act after row 149', 'when Burgers geometry is clear on the capstone path but Peach–Köhler force derivations feel disconnected from the slip-line Lab act after row 149'), ('memory sheet row 150 baby picture', 'memory sheet row 170 baby picture'), ('prologue row 150 closing stitch', 'prologue row 170 closing stitch'), ('prologue row 150 preview', 'prologue row 170 preview'), ('Row 150 closes the', 'Row 170 closes the'), ('Row 150 does not conflate', 'Row 170 does not conflate'), ('(row 150)', '(row 170)'), ('__PH0__', 'Row 151 closing loop'), ('__PH0__', 'row-__N151-closing-loop'), ('__PH0__', 'Row 151 closing stitch'), ('__PH0__', 'row-__N151-closing-stitch'), ('__PH0__', 'prologue-preview-row-__N151'), ('__PH0__', 'Row 151 preview'), ('__PH0__', 'Row 151 skill checkpoint'), ('__PH0__', 'skill-navigation-row-__N151'), ('__PH0__', 'memory sheet row 151'), ('__PH0__', 'Row 151 baby picture'), ('__PH0__', 'Row 151 three-way audit'), ('verified taxonomy meta prelude capstone closure (row 149)', 'verified taxonomy meta prelude capstone closure (row 149)'), ('When row 149 closed', 'When row 149 closed'), ('after row 149 alone', 'after row 149 alone'), ('Recite [preface row 149]', 'Recite [preface row 149]'), ('when row 149 closed but row 50 VII.1 → VII.2 reunion still feels like OpenDiS homework disconnected from verified taxonomy meta prelude capstone on the capstone path', 'when row 149 closed but row 50 VII.1 → VII.2 reunion still feels like OpenDiS homework disconnected from verified taxonomy meta prelude capstone on the capstone path'), ('when row 149 and row 50 both verify individually', 'when row 149 and row 50 both verify individually'), ("rear-view mirror of row 149's Burgers → segment-network turn", "rear-view mirror of row 149's Burgers → segment-network turn"), ('read row 68 gate + row 149 or row 130 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud when Burgers taxonomy is clean on the capstone path but OpenDiS decks feel like DDD homework after verified taxonomy meta prelude capstone', 'read row 68 gate + row 149 or row 150 taxonomy meta prelude capstone / DDD meta prelude gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50 meta aloud when taxonomy meta prelude capstone is clean on the capstone path after verified Burgers closure but OpenDiS decks feel like DDD homework at the Peach–Köhler knee'), ('Confirm [row 149](preface.md#skill-navigation-row-__N149) or [Row 68 → Row 130 DDD meta prelude reunion index (row 130)](appendix/sources.md#row68-row130-ddd-meta-prelude-capstone-reunion-index-row-150) recited', 'Confirm [row 149](preface.md#skill-navigation-row-149) or [Row 68 → Row 130 DDD meta prelude capstone reunion index (row 150)](appendix/sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170) recited'), ('Row 150 does not replace row 68, row 50, row 149, row 130, row 90, row 49, or row 32', 'Row 170 does not replace row 68, row 50, row 149, row 150, row 130, row 90, or row 32'), ('[row 149](preface.md#skill-navigation-row-__N149) or [row 130](preface.md#skill-navigation-row-__N130)', '[row 149](preface.md#skill-navigation-row-149) or [row 150](preface.md#skill-navigation-row-__N150)'), ('When row 150 is complete, proceed to [row 151]', 'When row 170 is complete, proceed to [row 151](preface.md#skill-navigation-row-__N151) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path, to [row 150](preface.md#skill-navigation-row-__N150) when taxonomy meta prelude capstone is clean but DDD meta prelude still lags on the opening-hinge path, to [row 130](preface.md#skill-navigation-row-__N130) for the Row 68 ↔ Row 50 DDD meta prelude audit on the opening-hinge prelude path alone, to [row 149](preface.md#skill-navigation-row-149) when taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the capstone path, to [row 149](preface.md#skill-navigation-row-__N149) when midpoint meta prelude capstone is clean but taxonomy meta prelude still lags on the opening-hinge path, to [row 50](preface.md#skill-navigation-row-50) for the VII.1 → VII.2 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_130'), ('Proceed to [row 151](#row-__N151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 150', 'Proceed to [row 151](#row-__N151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 170 on the capstone path, to [row 150](#row-__N150-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the opening-hinge path'), ('when opening [row 151](preface.md#skill-navigation-row-__N151) before row 51 closes on the capstone path', 'when opening [row 151](preface.md#skill-navigation-row-__N151) before row 51 closes on the capstone path'), ('When row 50 feels like OpenDiS homework after row 149 alone on the capstone path', 'When row 50 feels like OpenDiS homework after row 149 alone on the capstone path'), ('row 150 (row 68 ↔ row 50 reunion on the capstone path) with row 130', 'row 170 (row 68 ↔ row 50 reunion on the capstone path) with row 150'), ('row 150 (row 68 ↔ row 50 reunion on the capstone path) with row 130 (opening-hinge prelude stitch alone)', 'row 170 (row 68 ↔ row 50 reunion on the capstone path) with row 150 (opening-hinge prelude stitch alone)'), ('row 150 names **why that reunion must follow verified taxonomy meta prelude capstone (row 149)', 'row 170 names **why that reunion must follow verified taxonomy meta prelude capstone (row 149)'), ('row 149 closed taxonomy', 'row 149 closed taxonomy'), ('Row 68 → Row 50 meta (row 130)', 'Row 68 → Row 50 meta (row 150)'), ('[Preface row 150]', '[Preface row 170]'), ('Row 68 → Row 130 DDD meta prelude capstone reunion index (row 150)', 'Row 68 → Row 150 DDD meta prelude capstone reunion index (row 170)'), ('Row 68 → Row 130 reunion index', 'Row 68 → Row 150 reunion index')]


def lift_150_to_170(s: str) -> str:
    out = tx(s, LIFT_150_TO_170_PAIRS)
    if "DUPLICATE_WHEN_ROW_150" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_150.*", "", out, flags=re.S)
    elif "DUPLICATE_WHEN_ROW_130" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_130.*", "", out, flags=re.S)
    out = out.replace("skill-navigation-row-149", "skill-navigation-row-169")
    out = re.sub(
        r"(### Row 170 skill checkpoint[^\n]*)\{#skill-navigation-row-150\}",
        r"\1{#skill-navigation-row-170}",
        out,
        count=1,
    )
    out = out.replace("{#row-150-closing-loop}", "{#row-170-closing-loop}")
    out = out.replace("{#row-150-closing-stitch}", "{#row-170-closing-stitch}")
    return out


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
    if "### Row 170 skill checkpoint" in text:
        print("preface: row 170 already present")
        return
    m = re.search(
        r"(### Row 150 skill checkpoint.*?)(?=\n### Row 151 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 150 checkpoint missing")
    block = lift_150_to_170(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 170")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 170 closing loop" in text:
        print("epilogue: row 170 loop already present")
        return
    block = lift_150_to_170(
        extract_between(
            text,
            "### Row 150 closing loop",
            "### Row 149 closing loop",
        )
    )
    needle = "### Row 167 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 170 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion (row 170) |"
    if compass in text:
        print("prologue: row 170 compass already present")
    else:
        after = "| Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 169) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 169 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion (row 150) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 150 compass missing")
        new_line = lift_150_to_170(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-150"></span>'
    preview_dst = '| <span id="prologue-preview-row-170"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_150_to_170(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 170 closing stitch" not in text:
        stitch = (
            "**Row 170 closing stitch (Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion).** {#row-170-closing-stitch} "
            "When row 169 closed — taxonomy meta prelude capstone verified, row 168 or row 149 recited on the capstone path, and VII.0 Bridge → VII.1 taxonomy recited with slip-line Lab act classified line defects — "
            "but **row 50 VII.1 → VII.2 opening hinge still opens like standalone OpenDiS homework after the slip-line Lab act on the capstone path** — "
            "the [preface row 170 When-to-pause opening sentence](../preface.md#skill-navigation-row-170) names the dual reunion before homogenization meta prelude reunion; "
            "read [preface row 170](../preface.md#skill-navigation-row-170), then the "
            "[Row 68 → Row 150 reunion index](../appendix/sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170), then "
            "[epilogue row 170 closing loop](../epilogue/multiscale.md#row-170-closing-loop) before row 51 homogenization meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 169 closing stitch", stitch + "**Row 169 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 170 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170"
    if idx_key in text:
        print("sources: row 170 already present")
        return
    start = "## Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 150 index missing")
    block = lift_150_to_170(text[i:])
    block = block.split("## Row 68 → Row 131")[0]
    block = block.replace(
        "## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170)",
        f"## Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 170) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 170 | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone (midpoint prelude gate ↔ taxonomy meta prelude capstone ↔ row 50 meta) | "
        f"[Row 68 → Row 150 DDD meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 170](../preface.md#skill-navigation-row-170) · "
        "[prologue row 170 preview](../prologue/00-many-scales.md#prologue-preview-row-170) · "
        "[prologue row 170 closing stitch](../prologue/00-many-scales.md#row-170-closing-stitch) · "
        "[epilogue row 170 closing loop](../epilogue/multiscale.md#row-170-closing-loop) · "
        "[memory sheet row 170 baby picture](memory-sheet.md#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 50 VII.1 → VII.2 opening hinge still feels disconnected from verified taxonomy meta prelude capstone on the capstone path** — "
        "read row 68 + row 169 or row 150 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
        "[preface row 50](../preface.md#skill-navigation-row-50) |\n"
    )
    text = text.replace(
        "| 169 | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone",
        table_row + "| 169 | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone",
    )
    text = text.replace(
        start,
        block + start,
        1,
    )
    extra = (
        f"[row 169](#{idx_key}) reunites **taxonomy meta prelude capstone with the DDD meta prelude capstone boundary** "
        "when row 169 closed taxonomy meta prelude capstone at verified Burgers closure on the capstone path but VII.1 Bridge and row 50 still read like separate courses after verified DDD meta prelude meta;"
    )
    if extra not in text:
        needle = (
            "[row 168](#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169) reunites **midpoint meta prelude capstone with the taxonomy meta prelude capstone boundary** "
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 170")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 170 already present")
        return
    baby = lift_150_to_170(
        extract_between(
            text,
            "### Row 150 baby picture (Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion) {#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion}",
            "### Row 151 baby picture",
        )
    )
    anchor = "### Row 150 baby picture (Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion) {#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion}"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 170 | Meta | Row 68 → Row 150 Row 68 → Row 50 DDD meta prelude capstone reunion | "
        "[Row 68 → Row 150 DDD meta prelude capstone reunion index](sources.md#row68-row150-ddd-meta-prelude-capstone-reunion-index-row-170) · "
        "[preface row 170 skill checkpoint](../preface.md#skill-navigation-row-170) · "
        "[prologue row 170 preview](../prologue/00-many-scales.md#prologue-preview-row-170) · "
        "[prologue row 170 closing stitch](../prologue/00-many-scales.md#row-170-closing-stitch) · "
        "[epilogue row 170 closing loop](../epilogue/multiscale.md#row-170-closing-loop) | "
        "Row 68 closed but row 50 VII.1 → VII.2 opening hinge feels disconnected from verified taxonomy meta prelude capstone on the capstone path — "
        "read row 68 + row 169 or row 150 gate + VII.1 Bridge → opening hinge → VII.2 Peach–Köhler + row 50; "
        "[row 170 baby picture](#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 169 | Meta | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion |",
        mem_table + "| 169 | Meta | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion |",
    )
    if "When row 169 closed but DDD meta reunion still lags" not in text:
        text = text.replace(
            "When row 149 closed but DDD meta reunion still lags on the capstone path, switch to [row 150](#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion).",
            "When row 149 closed but DDD meta reunion still lags on the capstone path, switch to [row 150](#row-150-baby-picture-row68-row130-ddd-meta-prelude-capstone-reunion). "
            "When row 169 closed but DDD meta reunion still lags on the capstone path, switch to [row 170](#row-170-baby-picture-row68-row150-ddd-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 170")


def patch_row_169_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    old = (
        "Proceed to [row 150](#row-150-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 149 on the capstone path"
    )
    new = (
        "Proceed to [row 170](#row-170-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 169 on the capstone path"
    )
    if old in text:
        text = text.replace(old, new)
    old_p = (
        "When row 169 is complete, proceed to [row 150](preface.md#skill-navigation-row-150) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path"
    )
    new_p = (
        "When row 169 is complete, proceed to [row 170](preface.md#skill-navigation-row-170) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path"
    )
    if old_p in text:
        text = text.replace(old_p, new_p)
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    if old in ep_text:
        ep.write_text(ep_text.replace(old, new))
    print("preface/epilogue: patched row 169 → row 170 proceed links")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_169_proceed_links()


if __name__ == "__main__":
    main()
