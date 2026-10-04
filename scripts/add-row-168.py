#!/usr/bin/env python3
"""Add row 168 (Row 68 → Row 148 ↔ Row 48 midpoint meta prelude capstone on capstone path)."""
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


def lift_148_to_168(s: str) -> str:
    s = s.replace(
        "[row 148](preface.md#skill-navigation-row-148)",
        "__ROW148_HINGE__",
    )
    s = s.replace(
        "[row 147](preface.md#skill-navigation-row-147)",
        "[row 167](preface.md#skill-navigation-row-167)",
    )
    s = s.replace("skill-navigation-row-128", "__ROW128_NAV__")
    s = s.replace("skill-navigation-row-148", "__ROW168_NAV__")
    s = s.replace(
        "Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone",
        "__ROW168TITLE__",
    )

    p = [
        ("Row 169 closing loop", "__ROW169_LOOP__"),
        ("Row 148 closing loop", "Row 168 closing loop"),
        ("row-169-closing-loop", "__ROW169_LOOP_ANCHOR__"),
        ("row-148-closing-loop", "row-168-closing-loop"),
        ("Row 169 closing stitch", "__ROW169_STITCH__"),
        ("Row 148 closing stitch", "Row 168 closing stitch"),
        ("row-169-closing-stitch", "__ROW169_STITCH_ANCHOR__"),
        ("row-148-closing-stitch", "row-168-closing-stitch"),
        ("prologue-preview-row-169", "__ROW169_PREVIEW__"),
        ("prologue-preview-row-148", "prologue-preview-row-168"),
        ("Row 169 preview", "__ROW169_PREVIEW_TEXT__"),
        ("Row 148 preview", "Row 168 preview"),
        ("Row 169 skill checkpoint", "__ROW169_SKILL__"),
        ("Row 148 skill checkpoint", "Row 168 skill checkpoint"),
        ("skill-navigation-row-169", "__ROW169_SKILL_NAV__"),
        ("memory sheet row 169", "__ROW169_MEM__"),
        ("memory sheet row 148", "memory sheet row 168"),
        ("Row 169 baby picture", "__ROW169_BABY__"),
        ("Row 148 baby picture", "Row 168 baby picture"),
        ("Row 169 three-way audit", "__ROW169_AUDIT__"),
        ("Row 148 three-way audit", "Row 168 three-way audit"),
        (
            "Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone",
            "Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone",
        ),
        (
            "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148",
            "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168",
        ),
        (
            "row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion",
            "row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion",
        ),
        ("[row 169]", "__ROW169_REF__"),
        ("[row 149]", "[row 169]"),
        ("row 149", "row 169"),
        ("Row 149", "Row 169"),
        ("__ROW169_REF__", "[row 169]"),
        ("[row 148]", "__ROW148_REF__"),
        ("[row 128]", "[row 148]"),
        ("row 128", "row 148"),
        ("Row 128", "Row 148"),
        ("__ROW148_REF__", "[row 148]"),
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
        ("(row 148)", "(row 168)"),
        ("__ROW169_LOOP__", "Row 169 closing loop"),
        ("__ROW169_LOOP_ANCHOR__", "row-169-closing-loop"),
        ("__ROW169_STITCH__", "Row 169 closing stitch"),
        ("__ROW169_STITCH_ANCHOR__", "row-169-closing-stitch"),
        ("__ROW169_PREVIEW__", "prologue-preview-row-169"),
        ("__ROW169_PREVIEW_TEXT__", "Row 169 preview"),
        ("__ROW169_SKILL__", "Row 169 skill checkpoint"),
        ("__ROW169_SKILL_NAV__", "skill-navigation-row-169"),
        ("__ROW169_MEM__", "memory sheet row 169"),
        ("__ROW169_BABY__", "Row 169 baby picture"),
        ("__ROW169_AUDIT__", "Row 169 three-way audit"),
        (
            "verified part-boundary meta prelude capstone closure (row 147)",
            "verified part-boundary meta prelude capstone closure (row 167)",
        ),
        ("When row 147 closed", "When row 167 closed"),
        ("after row 147 alone", "after row 167 alone"),
        ("Recite [preface row 147]", "Recite [preface row 167]"),
        (
            "when row 147 closed but row 48 midpoint meta still feels like defect homework disconnected from verified part-boundary meta prelude capstone on the capstone path",
            "when row 167 closed but row 48 midpoint meta still feels like defect homework disconnected from verified part-boundary meta prelude capstone on the capstone path",
        ),
        (
            "when row 147 and row 48 both verify individually",
            "when row 167 and row 48 both verify individually",
        ),
        (
            "rear-view mirror of row 147's twin-ladder → knee → forest turn",
            "rear-view mirror of row 167's twin-ladder → knee → forest turn",
        ),
        (
            "read row 68 gate + row 147 or row 128 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean on the capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion",
            "read row 68 gate + row 167 or row 148 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean on the capstone path after verified twin-ladder reunion but writings/continuum → writings/defects feels like two courses at the knee",
        ),
        (
            "Confirm [row 147](preface.md#skill-navigation-row-147) or [Row 68 → Row 128 midpoint meta prelude capstone reunion index (row 148)](appendix/sources.md#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148) recited",
            "Confirm [row 167](preface.md#skill-navigation-row-167) or [Row 68 → Row 148 midpoint meta prelude capstone reunion index (row 168)](appendix/sources.md#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168) recited",
        ),
        (
            "Row 148 does not replace row 68, row 48, row 147, row 128, row 108, row 88, row 87, row 67, row 32, or row 20",
            "Row 168 does not replace row 68, row 48, row 167, row 148, row 108, row 88, row 87, row 67, row 32, or row 20",
        ),
        (
            "Row 128 does not replace row 68, row 48, row 127, row 128, row 88, row 87, row 67, row 32, or row 20",
            "Row 168 does not replace row 68, row 48, row 167, row 148, row 108, row 88, row 87, row 67, row 32, or row 20",
        ),
        (
            "[row 147](preface.md#skill-navigation-row-147) or [row 128](preface.md#skill-navigation-row-128)",
            "[row 167](preface.md#skill-navigation-row-167) or [row 148](preface.md#skill-navigation-row-148)",
        ),
        (
            "When row 148 is complete, proceed to [row 149]",
            "When row 168 is complete, proceed to [row 169](preface.md#skill-navigation-row-169) when row 68 closed but taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the capstone path, "
            "to [row 148](preface.md#skill-navigation-row-148) when part-boundary meta prelude capstone is clean but midpoint meta prelude still lags on the opening-hinge path, "
            "to [row 128](preface.md#skill-navigation-row-128) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, "
            "to [row 167](preface.md#skill-navigation-row-167) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the capstone path, "
            "to [row 147](preface.md#skill-navigation-row-147) when Writings canonical meta prelude capstone is clean but part-boundary meta prelude still lags on the opening-hinge path, "
            "to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, "
            "to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_148",
        ),
        (
            "Proceed to [row 149](#row-149-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 148 on the capstone path",
            "Proceed to [row 169](#row-169-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 168 on the capstone path, "
            "to [row 148](#row-148-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 149](preface.md#skill-navigation-row-149) before row 49 closes on the capstone path",
            "when opening [row 169](preface.md#skill-navigation-row-169) before row 49 closes on the capstone path",
        ),
        (
            "When row 48 feels like defect homework after row 147 alone on the capstone path",
            "When row 48 feels like defect homework after row 167 alone on the capstone path",
        ),
        (
            "row 148 (row 68 ↔ row 48 reunion on the capstone path) with row 128",
            "row 168 (row 68 ↔ row 48 reunion on the capstone path) with row 148",
        ),
        (
            "row 148 (row 68 ↔ row 48 reunion on the capstone path) with row 128 (opening-hinge prelude stitch alone)",
            "row 168 (row 68 ↔ row 48 reunion on the capstone path) with row 148 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 148 names **why that reunion must follow verified part-boundary meta prelude capstone (row 147)",
            "row 168 names **why that reunion must follow verified part-boundary meta prelude capstone (row 167)",
        ),
        ("row 147 closed part-boundary", "row 167 closed part-boundary"),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_148" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_148.*", "", out, flags=re.S)
    out = out.replace(
        "__ROW168TITLE__",
        "Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone",
    )
    out = out.replace("__ROW168_NAV__", "skill-navigation-row-168")
    out = out.replace("__ROW128_NAV__", "skill-navigation-row-148")
    out = out.replace(
        "__ROW148_HINGE__",
        "[row 148](preface.md#skill-navigation-row-148)",
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
    if "### Row 168 skill checkpoint" in text:
        print("preface: row 168 already present")
        return
    m = re.search(
        r"(### Row 148 skill checkpoint.*?)(?=\n### Row 149 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 148 checkpoint missing")
    block = lift_148_to_168(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 168")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 168 closing loop" in text:
        print("epilogue: row 168 loop already present")
        return
    block = lift_148_to_168(
        extract_between(
            text,
            "### Row 148 closing loop",
            "### Row 147 closing loop",
        )
    )
    needle = "### Row 167 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 168 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 168) |"
    if compass in text:
        print("prologue: row 168 compass already present")
    else:
        after = "| Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 167) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 167 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 148) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 148 compass missing")
        new_line = lift_148_to_168(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-148"></span>'
    preview_dst = '| <span id="prologue-preview-row-168"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_148_to_168(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 168 closing stitch" not in text:
        stitch = (
            "**Row 168 closing stitch (Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-168-closing-stitch} "
            "When row 167 closed — part-boundary meta prelude capstone verified, row 166 or row 147 recited on the capstone path, and twin-ladder Bridge through VI.0 landing recited with `cht_export.yaml` beside both decks — "
            "but **row 48 midpoint opening prelude still opens like standalone defect coursework after VI.4's return-mapping chapter on the capstone path** — "
            "the [preface row 168 When-to-pause opening sentence](../preface.md#skill-navigation-row-168) names the dual reunion before taxonomy meta prelude reunion; "
            "read [preface row 168](../preface.md#skill-navigation-row-168), then the "
            "[Row 68 → Row 148 reunion index](../appendix/sources.md#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168), then "
            "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) before row 49 taxonomy meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 167 closing stitch", stitch + "**Row 167 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 168 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168"
    if idx_key in text:
        print("sources: row 168 already present")
        return
    start = "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 148 index missing")
    block = lift_148_to_168(text[i:])
    block = block.split("## Row 68 → Row 127")[0]
    block = block.replace(
        "## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 168)",
        f"## Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 168) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 168 | Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone "
        "(midpoint prelude gate ↔ part-boundary meta prelude capstone ↔ row 48 meta) | "
        f"[Row 68 → Row 148 midpoint meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 168](../preface.md#skill-navigation-row-168) · "
        "[prologue row 168 preview](../prologue/00-many-scales.md#prologue-preview-row-168) · "
        "[prologue row 168 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch) · "
        "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) · "
        "[memory sheet row 168 baby picture](memory-sheet.md#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 48 midpoint meta reunion still feels disconnected from verified part-boundary meta prelude capstone on the capstone path** — "
        "read row 68 + row 167 or row 148 gate + VI.4 intermission → VII.0 landing + row 48; "
        "[preface row 48](../preface.md#skill-navigation-row-48) |\n"
    )
    text = text.replace(
        "| 167 | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone",
        table_row + "| 167 | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)",
        block + "## Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion index (row 148)",
    )
    extra = (
        f"[row 168](#{idx_key}) reunites **part-boundary meta prelude capstone with the midpoint meta prelude capstone boundary** "
        "when row 167 closed part-boundary meta prelude capstone at verified twin-ladder rhythm on the capstone path but VI.4 intermission and row 48 still read like separate courses after verified fvm → continuum meta;"
    )
    if extra not in text:
        needle = (
            "[row 167](#row68-row147-part-boundary-meta-prelude-capstone-reunion-index-row-167) reunites **Writings canonical meta prelude capstone with the part-boundary meta prelude capstone boundary** "
        )
        if needle in text:
            text = text.replace(needle, needle + " " + extra)
    path.write_text(text)
    print("sources: added row 168")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 168 already present")
        return
    baby = lift_148_to_168(
        extract_between(
            text,
            "### Row 148 baby picture (Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion}",
            "### Row 149 baby picture",
        )
    )
    anchor = "### Row 148 baby picture (Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion}"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 168 | Meta | Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion | "
        "[Row 68 → Row 148 midpoint meta prelude capstone reunion index](sources.md#row68-row148-midpoint-meta-prelude-capstone-reunion-index-row-168) · "
        "[preface row 168 skill checkpoint](../preface.md#skill-navigation-row-168) · "
        "[prologue row 168 preview](../prologue/00-many-scales.md#prologue-preview-row-168) · "
        "[prologue row 168 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch) · "
        "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) | "
        "Row 68 closed but row 48 midpoint meta reunion feels disconnected from verified part-boundary meta prelude capstone on the capstone path — "
        "read row 68 + row 167 or row 148 gate + VI.4 intermission → VII.0 landing + row 48; "
        "[row 168 baby picture](#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 167 | Meta | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion |",
        mem_table + "| 167 | Meta | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion |",
    )
    switch = (
        "When row 167 closed but midpoint meta reunion still lags on the capstone path, switch to [row 168](#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion)."
    )
    if switch not in text:
        text = text.replace(
            "When row 147 closed but midpoint meta reunion still lags on the capstone path, switch to [row 148](#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion).",
            "When row 167 closed but midpoint meta reunion still lags on the capstone path, switch to [row 168](#row-168-baby-picture-row68-row148-midpoint-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 168")


def patch_row_167_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    old = (
        "Proceed to [row 148](#row-148-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 147 on the capstone path"
    )
    new = (
        "Proceed to [row 168](#row-168-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 167 on the capstone path"
    )
    if old in text:
        text = text.replace(old, new)
    fixes = [
        (
            "When row 48 feels like defect homework after row 147 alone on the capstone path",
            "When row 48 feels like defect homework after row 167 alone on the capstone path",
        ),
        (
            "Recite [preface row 147](../preface.md#skill-navigation-row-147) to split part-boundary meta prelude capstone from midpoint reunion",
            "Recite [preface row 167](../preface.md#skill-navigation-row-167) to split part-boundary meta prelude capstone from midpoint reunion",
        ),
    ]
    for a, b in fixes:
        text = text.replace(a, b)
    path.write_text(text)
    ep = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep_text = ep.read_text()
    if old in ep_text:
        ep.write_text(ep_text.replace(old, new))
    print("preface/epilogue: patched row 167 → row 168 proceed links")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_167_proceed_links()


if __name__ == "__main__":
    main()
