#!/usr/bin/env python3
"""Add row 167 (Row 68 → Row 147 ↔ Row 67 part-boundary meta prelude capstone on capstone path)."""
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


def lift_147_to_167(s: str) -> str:
    s = s.replace(
        "[row 147](preface.md#skill-navigation-row-147)",
        "__ROW147_HINGE__",
    )
    s = s.replace(
        "[row 146](preface.md#skill-navigation-row-146)",
        "[row 166](preface.md#skill-navigation-row-166)",
    )
    s = s.replace("skill-navigation-row-127", "__ROW127_NAV__")
    s = s.replace("skill-navigation-row-147", "__ROW167_NAV__")
    s = s.replace(
        "Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone",
        "__ROW167TITLE__",
    )

    p = [
        ("Row 168 closing loop", "__ROW168_LOOP__"),
        ("Row 147 closing loop", "Row 167 closing loop"),
        ("row-168-closing-loop", "__ROW168_LOOP_ANCHOR__"),
        ("row-147-closing-loop", "row-167-closing-loop"),
        ("Row 168 closing stitch", "__ROW168_STITCH__"),
        ("Row 147 closing stitch", "Row 167 closing stitch"),
        ("row-168-closing-stitch", "__ROW168_STITCH_ANCHOR__"),
        ("row-147-closing-stitch", "row-167-closing-stitch"),
        ("prologue-preview-row-168", "__ROW168_PREVIEW__"),
        ("prologue-preview-row-147", "prologue-preview-row-167"),
        ("Row 168 preview", "__ROW168_PREVIEW_TEXT__"),
        ("Row 147 preview", "Row 167 preview"),
        ("Row 168 skill checkpoint", "__ROW168_SKILL__"),
        ("Row 147 skill checkpoint", "Row 167 skill checkpoint"),
        ("skill-navigation-row-168", "__ROW168_SKILL_NAV__"),
        ("memory sheet row 168", "__ROW168_MEM__"),
        ("memory sheet row 147", "memory sheet row 167"),
        ("Row 168 baby picture", "__ROW168_BABY__"),
        ("Row 147 baby picture", "Row 167 baby picture"),
        ("Row 168 three-way audit", "__ROW168_AUDIT__"),
        ("Row 147 three-way audit", "Row 167 three-way audit"),
        (
            "Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone",
            "Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone",
        ),
        (
            "row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147",
            "row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167",
        ),
        (
            "row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion",
            "row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion",
        ),
        ("[row 168]", "__ROW168_REF__"),
        ("[row 148]", "[row 168]"),
        ("row 148", "row 168"),
        ("Row 148", "Row 168"),
        ("__ROW168_REF__", "[row 168]"),
        ("[row 147]", "__ROW147_REF__"),
        ("[row 127]", "[row 147]"),
        ("row 127", "row 147"),
        ("Row 127", "Row 147"),
        ("__ROW147_REF__", "[row 147]"),
        ("[row 146]", "__ROW146_REF__"),
        ("[row 166]", "__ROW166_HINGE__"),
        ("__ROW166_HINGE__", "[row 166](preface.md#skill-navigation-row-166)"),
        ("row 146", "row 166"),
        ("Row 146", "Row 166"),
        ("__ROW146_REF__", "[row 166]"),
        ("(row 147)", "(row 167)"),
        ("__ROW168_LOOP__", "Row 168 closing loop"),
        ("__ROW168_LOOP_ANCHOR__", "row-168-closing-loop"),
        ("__ROW168_STITCH__", "Row 168 closing stitch"),
        ("__ROW168_STITCH_ANCHOR__", "row-168-closing-stitch"),
        ("__ROW168_PREVIEW__", "prologue-preview-row-168"),
        ("__ROW168_PREVIEW_TEXT__", "Row 168 preview"),
        ("__ROW168_SKILL__", "Row 168 skill checkpoint"),
        ("__ROW168_SKILL_NAV__", "skill-navigation-row-168"),
        ("__ROW168_MEM__", "memory sheet row 168"),
        ("__ROW168_BABY__", "Row 168 baby picture"),
        ("__ROW168_AUDIT__", "Row 168 three-way audit"),
        (
            "verified Writings canonical meta prelude capstone closure (row 146)",
            "verified Writings canonical meta prelude capstone closure (row 166)",
        ),
        ("When row 146 closed", "When row 166 closed"),
        ("after row 146 alone", "after row 166 alone"),
        ("Recite [preface row 146]", "Recite [preface row 166]"),
        (
            "when row 146 closed but row 67 part-boundary meta still feels like elasticity homework disconnected from verified Writings canonical meta prelude capstone on the capstone path",
            "when row 166 closed but row 67 part-boundary meta still feels like elasticity homework disconnected from verified Writings canonical meta prelude capstone on the capstone path",
        ),
        (
            "when row 146 and row 67 both verify individually",
            "when row 166 and row 67 both verify individually",
        ),
        (
            "rear-view mirror of row 146's canonical-tree → twin-ladder turn",
            "rear-view mirror of row 166's canonical-tree → twin-ladder turn",
        ),
        (
            "read row 68 gate + row 146 or row 127 Writings meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud when canonical tree is clean on the capstone path but writings/fvm → writings/continuum feels like two courses after verified Writings meta prelude capstone",
            "read row 68 gate + row 166 or row 147 Writings meta prelude capstone / part-boundary meta prelude gate + V.4 Bridge → VI.0 twin-ladder landing + row 67 meta aloud when canonical tree is clean on the capstone path after verified Writings meta prelude capstone but writings/fvm → writings/continuum feels like two courses",
        ),
        (
            "Confirm [row 146](preface.md#skill-navigation-row-146) or [Row 68 → Row 127 part-boundary meta prelude capstone reunion index (row 147)](appendix/sources.md#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147) recited",
            "Confirm [row 166](preface.md#skill-navigation-row-166) or [Row 68 → Row 147 part-boundary meta prelude capstone reunion index (row 167)](appendix/sources.md#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167) recited",
        ),
        (
            "Row 147 does not replace row 68, row 67, row 146, row 127, row 87, row 66, row 47, or row 30",
            "Row 167 does not replace row 68, row 67, row 166, row 147, row 87, row 66, row 47, or row 30",
        ),
        (
            "[row 146](preface.md#skill-navigation-row-146) or [row 127](preface.md#skill-navigation-row-127)",
            "[row 166](preface.md#skill-navigation-row-166) or [row 147](preface.md#skill-navigation-row-147)",
        ),
        (
            "When row 147 is complete, proceed to [row 128]",
            "When row 167 is complete, proceed to [row 168](preface.md#skill-navigation-row-168) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the capstone path, "
            "to [row 147](preface.md#skill-navigation-row-147) when Writings canonical meta prelude capstone is clean but part-boundary meta prelude still lags on the opening-hinge path, "
            "to [row 127](preface.md#skill-navigation-row-127) for the Row 68 ↔ Row 67 meta audit on the opening-hinge prelude path alone, "
            "to [row 166](preface.md#skill-navigation-row-166) when Writings canonical meta prelude capstone still lags after verified second-pass meta prelude capstone on the capstone path, "
            "to [row 87](preface.md#skill-navigation-row-87) for the Row 68 ↔ Row 67 opening prelude audit alone, "
            "to [row 67](preface.md#skill-navigation-row-67) when only part-boundary prelude meta stalls, "
            "to [row 47](preface.md#skill-navigation-row-47) when only the fvm → continuum boundary stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_147",
        ),
        (
            "Proceed to [row 128](#row-128-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 147 on the capstone path",
            "Proceed to [row 168](#row-168-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 167 on the capstone path, "
            "to [row 147](#row-147-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 128](preface.md#skill-navigation-row-128) before row 48 closes on the capstone path",
            "when opening [row 168](preface.md#skill-navigation-row-168) before row 48 closes on the capstone path",
        ),
        (
            "When row 67 feels like elasticity homework after row 146 alone on the capstone path",
            "When row 67 feels like elasticity homework after row 166 alone on the capstone path",
        ),
        (
            "row 147 (row 68 ↔ row 67 reunion on the capstone path) with row 127",
            "row 167 (row 68 ↔ row 67 reunion on the capstone path) with row 147",
        ),
        (
            "row 147 (row 68 ↔ row 67 reunion on the capstone path) with row 127 (opening-hinge prelude stitch alone)",
            "row 167 (row 68 ↔ row 67 reunion on the capstone path) with row 147 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 147 names **why that reunion must follow verified Writings canonical meta prelude capstone (row 146)",
            "row 167 names **why that reunion must follow verified Writings canonical meta prelude capstone (row 166)",
        ),
        (
            "when sync is clean after row 146 but",
            "when sync is clean after row 166 but",
        ),
        (
            "When row 166 is complete, proceed to [row 167](preface.md#skill-navigation-row-167)",
            "When row 166 is complete, proceed to [row 167](preface.md#skill-navigation-row-167)",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_147" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_147.*", "", out, flags=re.S)
    out = out.replace(
        "__ROW167TITLE__",
        "Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone",
    )
    out = out.replace("__ROW167_NAV__", "skill-navigation-row-167")
    out = out.replace("__ROW127_NAV__", "skill-navigation-row-147")
    out = out.replace(
        "__ROW147_HINGE__",
        "[row 147](preface.md#skill-navigation-row-147)",
    )
    out = out.replace("on the capstone path on the capstone path", "on the capstone path")
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
    if "### Row 167 skill checkpoint" in text:
        print("preface: row 167 already present")
        return
    m = re.search(
        r"(### Row 147 skill checkpoint.*?)(?=\n### Row 148 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 147 checkpoint missing")
    block = lift_147_to_167(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 167")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 167 closing loop" in text:
        print("epilogue: row 167 loop already present")
        return
    block = lift_147_to_167(
        extract_between(
            text,
            "### Row 147 closing loop",
            "### Row 146 closing loop",
        )
    )
    needle = "### Row 166 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 167 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 167) |"
    if compass in text:
        print("prologue: row 167 compass already present")
    else:
        after = "| Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion (row 166) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 166 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 147) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 147 compass missing")
        new_line = lift_147_to_167(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-147"></span>'
    preview_dst = '| <span id="prologue-preview-row-167"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_147_to_167(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 167 closing stitch" not in text:
        stitch = (
            "**Row 167 closing stitch (Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion).** {#row-167-closing-stitch} "
            "When row 166 closed — Writings canonical meta prelude capstone verified, row 165 or row 166 recited on the capstone path, and `./scripts/sync-writings.sh --check` green with prose under `writings/` only — "
            "but **row 67 part-boundary meta reunion still opens like standalone elasticity coursework after Navier–Stokes on the capstone path** — "
            "the [preface row 167 When-to-pause opening sentence](../preface.md#skill-navigation-row-167) names the dual reunion before midpoint meta prelude reunion; "
            "read [preface row 167](../preface.md#skill-navigation-row-167), then the "
            "[Row 68 → Row 147 reunion index](../appendix/sources.md#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167), then "
            "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop) before row 48 midpoint meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 166 closing stitch", stitch + "**Row 166 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 167 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167"
    if idx_key in text:
        print("sources: row 167 already present")
        return
    start = "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 147 index missing")
    block = lift_147_to_167(text[i:])
    block = block.replace(
        "## Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 167)",
        f"## Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 167) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 167 | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone "
        "(midpoint prelude gate ↔ Writings meta prelude capstone ↔ row 67 meta) | "
        f"[Row 68 → Row 147 part-boundary meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 167](../preface.md#skill-navigation-row-167) · "
        "[prologue row 167 preview](../prologue/00-many-scales.md#prologue-preview-row-167) · "
        "[prologue row 167 closing stitch](../prologue/00-many-scales.md#row-167-closing-stitch) · "
        "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop) · "
        "[memory sheet row 167 baby picture](memory-sheet.md#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 67 part-boundary meta reunion still feels disconnected from verified Writings canonical meta prelude capstone on the capstone path** — "
        "read row 68 + row 166 or row 147 gate + V.4 Bridge → VI.0 twin-ladder + row 67; "
        "[preface row 67](../preface.md#skill-navigation-row-67) |\n"
    )
    text = text.replace(
        "| 166 | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone",
        table_row + "| 166 | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)",
        block + "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)",
    )
    extra = (
        f"[row 167](#{idx_key}) reunites **Writings canonical meta prelude capstone with the part-boundary meta prelude capstone boundary** "
        "when row 166 closed Writings canonical meta prelude capstone at verified single-manuscript-tree rhythm on the capstone path but twin-ladder Bridge and row 67 still read like separate courses after verified fvm → continuum meta;"
    )
    if extra not in text:
        needle = (
            "[row 166](#row68-row146-writings-meta-prelude-capstone-reunion-index-row-166) reunites **second-pass meta prelude capstone with the Writings canonical meta prelude capstone boundary** "
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 167")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 167 already present")
        return
    baby = lift_147_to_167(
        extract_between(
            text,
            "### Row 147 baby picture (Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion) {#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion}",
            "### Row 148 baby picture",
        )
    )
    anchor = "### Row 147 baby picture (Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion) {#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion}"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 167 | Meta | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion | "
        "[Row 68 → Row 147 part-boundary meta prelude capstone reunion index](sources.md#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167) · "
        "[preface row 167 skill checkpoint](../preface.md#skill-navigation-row-167) · "
        "[prologue row 167 preview](../prologue/00-many-scales.md#prologue-preview-row-167) · "
        "[prologue row 167 closing stitch](../prologue/00-many-scales.md#row-167-closing-stitch) · "
        "[epilogue row 167 closing loop](../epilogue/multiscale.md#row-167-closing-loop) | "
        "Row 68 closed but row 67 part-boundary meta reunion feels disconnected from verified Writings meta prelude capstone on the capstone path — "
        "read row 68 + row 166 or row 147 gate + twin-ladder Bridge + row 67; "
        "[row 167 baby picture](#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 166 | Meta | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion |",
        mem_table + "| 166 | Meta | Row 68 → Row 146 Row 68 → Row 66 Writings canonical meta prelude capstone reunion |",
    )
    switch = (
        "When row 166 closed but twin-ladder reunion still lags on the capstone path, switch to [row 167](#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion)."
    )
    if switch not in text:
        text = text.replace(
            "When row 146 closed but twin-ladder reunion still lags on the capstone path, switch to [row 147](#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion).",
            "When row 166 closed but twin-ladder reunion still lags on the capstone path, switch to [row 167](#row-167-baby-picture-row68-row147-part-boundary-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 167")


def patch_row_166_proceed_links() -> None:
    """Fix row 166 When-to-pause block left by lift_146_to_166 placeholder swaps."""
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    fixes = [
        (
            "when opening [row 167](preface.md#skill-navigation-row-147) before row 67 closes",
            "when opening [row 167](preface.md#skill-navigation-row-167) before row 67 closes",
        ),
        (
            "When row 146 is complete, proceed to [row 167](preface.md#skill-navigation-row-147)",
            "When row 166 is complete, proceed to [row 167](preface.md#skill-navigation-row-167)",
        ),
        (
            "Row 146 does not replace row 68, row 66, row 145, row 146, row 86",
            "Row 166 does not replace row 68, row 66, row 165, row 146, row 86",
        ),
    ]
    for a, b in fixes:
        text = text.replace(a, b)
    path.write_text(text)
    print("preface: patched row 166 proceed links")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_166_proceed_links()


if __name__ == "__main__":
    main()
