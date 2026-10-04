#!/usr/bin/env python3
"""Add row 169 (Row 68 → Row 149 ↔ Row 49 taxonomy meta prelude capstone on capstone path)."""
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


def lift_149_to_169(s: str) -> str:
    p = [
        ("Row 150 closing loop", "__ROW130_LOOP__"),
        ("Row 149 closing loop", "Row 169 closing loop"),
        ("row-150-closing-loop", "__ROW130_LOOP_ANCHOR__"),
        ("row-149-closing-loop", "row-169-closing-loop"),
        ("Row 150 closing stitch", "__ROW130_STITCH__"),
        ("Row 149 closing stitch", "Row 169 closing stitch"),
        ("row-150-closing-stitch", "__ROW130_STITCH_ANCHOR__"),
        ("row-149-closing-stitch", "row-169-closing-stitch"),
        ("prologue-preview-row-150", "__ROW130_PREVIEW__"),
        ("prologue-preview-row-149", "prologue-preview-row-169"),
        ("Row 150 preview", "__ROW130_PREVIEW_TEXT__"),
        ("Row 149 preview", "Row 169 preview"),
        ("Row 150 skill checkpoint", "__ROW130_SKILL__"),
        ("Row 149 skill checkpoint", "Row 169 skill checkpoint"),
        ("skill-navigation-row-150", "__ROW130_SKILL_NAV__"),
        ("skill-navigation-row-149", "skill-navigation-row-169"),
        ("memory sheet row 150", "__ROW130_MEM__"),
        ("memory sheet row 149", "memory sheet row 169"),
        ("Row 150 baby picture", "__ROW130_BABY__"),
        ("Row 149 baby picture", "Row 169 baby picture"),
        ("Row 150 three-way audit", "__ROW130_AUDIT__"),
        ("Row 149 three-way audit", "Row 169 three-way audit"),
        (
            "Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone",
            "Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone",
        ),
        (
            "row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-129",
            "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-149",
        ),
        (
            "row-129-baby-picture-row68-row129-taxonomy-meta-prelude-capstone-reunion",
            "row-149-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion",
        ),
        ("[row 150]", "__ROW130_REF__"),
        ("[row 130]", "[row 150]"),
        ("row 110", "row 130"),
        ("Row 110", "Row 130"),
        ("__ROW130_REF__", "[row 150]"),
        ("skill-navigation-row-129", "skill-navigation-row-149"),
        ("[row 149]", "__ROW129_REF__"),
        ("[row 129]", "[row 149]"),
        ("row 109", "row 129"),
        ("Row 109", "Row 129"),
        ("__ROW129_REF__", "[row 149]"),
        ("skill-navigation-row-148", "skill-navigation-row-168"),
        ("[row 148]", "__ROW128_REF__"),
        ("[row 128]", "[row 168]"),
        ("row 128", "row 148"),
        ("Row 128", "Row 148"),
        ("__ROW128_REF__", "[row 168]"),
        (
            "Row 68 → Row 89 taxonomy meta prelude reunion index (row 129)",
            "Row 68 → Row 129 taxonomy meta prelude capstone reunion index (row 149)",
        ),
        (
            "row68-row89-taxonomy-meta-prelude-reunion-index-row-109",
            "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-149",
        ),
        (
            "when forest landing is clean on the capstone path but Burgers circuits feel disconnected from return-mapping after row 128",
            "when forest landing is clean on the capstone path but Burgers circuits feel disconnected from return-mapping after row 148",
        ),
        ("memory sheet row 149 baby picture", "memory sheet row 169 baby picture"),
        ("prologue row 149 closing stitch", "prologue row 169 closing stitch"),
        ("prologue row 149 preview", "prologue row 169 preview"),
        ("Row 149 closes the", "Row 169 closes the"),
        ("Row 149 does not conflate", "Row 169 does not conflate"),
        ("(row 149)", "(row 169)"),
        ("__ROW130_LOOP__", "Row 150 closing loop"),
        ("__ROW130_LOOP_ANCHOR__", "row-150-closing-loop"),
        ("__ROW130_STITCH__", "Row 150 closing stitch"),
        ("__ROW130_STITCH_ANCHOR__", "row-150-closing-stitch"),
        ("__ROW130_PREVIEW__", "prologue-preview-row-150"),
        ("__ROW130_PREVIEW_TEXT__", "Row 150 preview"),
        ("__ROW130_SKILL__", "Row 150 skill checkpoint"),
        ("__ROW130_SKILL_NAV__", "skill-navigation-row-150"),
        ("__ROW130_MEM__", "memory sheet row 150"),
        ("__ROW130_BABY__", "Row 150 baby picture"),
        ("__ROW130_AUDIT__", "Row 150 three-way audit"),
        (
            "verified midpoint meta prelude capstone closure (row 148)",
            "verified midpoint meta prelude capstone closure (row 168)",
        ),
        ("When row 148 closed", "When row 168 closed"),
        ("after row 148 alone", "after row 168 alone"),
        ("Recite [preface row 148]", "Recite [preface row 168]"),
        (
            "when row 148 closed but row 49 VII.0 → VII.1 reunion still feels like Defects Notes homework disconnected from verified midpoint meta prelude capstone on the capstone path",
            "when row 168 closed but row 49 VII.0 → VII.1 reunion still feels like Defects Notes homework disconnected from verified midpoint meta prelude capstone on the capstone path",
        ),
        (
            "when row 148 and row 49 both verify individually",
            "when row 168 and row 49 both verify individually",
        ),
        (
            "rear-view mirror of row 128's forest landing → Burgers turn",
            "rear-view mirror of row 148's forest landing → Burgers turn",
        ),
        (
            "read row 68 gate + row 148 or row 129 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when forest landing is clean on the capstone path but Burgers circuits feel like Defects Notes homework after verified midpoint meta prelude capstone",
            "read row 68 gate + row 168 or row 149 midpoint meta prelude capstone / taxonomy meta prelude gate + VII.0 Bridge → opening hinge → VII.1 taxonomy + row 49 meta aloud when midpoint meta prelude capstone is clean on the capstone path after verified forest landing but Burgers circuits feel like Defects Notes homework at the taxonomy knee",
        ),
        (
            "Confirm [row 148](preface.md#skill-navigation-row-148) or [Row 68 → Row 89 taxonomy meta prelude reunion index (row 129)](appendix/sources.md#row68-row89-taxonomy-meta-prelude-reunion-index-row-109) recited",
            "Confirm [row 168](preface.md#skill-navigation-row-168) or [Row 68 → Row 129 taxonomy meta prelude capstone reunion index (row 149)](appendix/sources.md#row68-row129-taxonomy-meta-prelude-capstone-reunion-index-row-129) recited",
        ),
        (
            "Row 149 does not replace row 68, row 49, row 148, row 129, row 89, row 88, row 48, or row 32",
            "Row 169 does not replace row 68, row 49, row 168, row 149, row 129, row 89, row 88, row 48, or row 32",
        ),
        (
            "[row 148](preface.md#skill-navigation-row-148) or [row 129](preface.md#skill-navigation-row-129)",
            "[row 168](preface.md#skill-navigation-row-168) or [row 149](preface.md#skill-navigation-row-149)",
        ),
        (
            "When row 149 is complete, proceed to [row 150]",
            "When row 169 is complete, proceed to [row 150](preface.md#skill-navigation-row-150) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the capstone path, "
            "to [row 149](preface.md#skill-navigation-row-149) when midpoint meta prelude capstone is clean but taxonomy meta prelude still lags on the opening-hinge path, "
            "to [row 129](preface.md#skill-navigation-row-129) for the Row 68 ↔ Row 49 taxonomy meta prelude audit on the opening-hinge prelude path alone, "
            "to [row 168](preface.md#skill-navigation-row-168) when midpoint meta prelude capstone still lags after verified part-boundary meta prelude capstone on the capstone path, "
            "to [row 148](preface.md#skill-navigation-row-148) when part-boundary meta prelude capstone is clean but midpoint meta prelude still lags on the opening-hinge path, "
            "to [row 49](preface.md#skill-navigation-row-49) for the VII.0 → VII.1 meta audit alone, "
            "to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_149",
        ),
        (
            "Proceed to [row 150](#row-150-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 129",
            "Proceed to [row 150](#row-150-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after row 169 on the capstone path, "
            "to [row 149](#row-149-closing-loop) when row 68 closed but DDD meta prelude capstone still lags after verified taxonomy meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 150](preface.md#skill-navigation-row-150) before row 50 closes on the capstone path",
            "when opening [row 150](preface.md#skill-navigation-row-150) before row 50 closes on the capstone path",
        ),
        (
            "When row 49 feels like Defects Notes homework after row 148 alone on the capstone path",
            "When row 49 feels like Defects Notes homework after row 168 alone on the capstone path",
        ),
        (
            "row 149 (row 68 ↔ row 49 reunion on the capstone path) with row 109",
            "row 169 (row 68 ↔ row 49 reunion on the capstone path) with row 129",
        ),
        (
            "row 149 (row 68 ↔ row 49 reunion on the capstone path) with row 129 (opening-hinge prelude stitch alone)",
            "row 169 (row 68 ↔ row 49 reunion on the capstone path) with row 149 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 149 names **why that reunion must follow verified midpoint meta prelude capstone (row 148)",
            "row 169 names **why that reunion must follow verified midpoint meta prelude capstone (row 168)",
        ),
        ("row 148 closed midpoint", "row 168 closed midpoint"),
        ("Row 68 → Row 49 meta (row 129)", "Row 68 → Row 49 meta (row 149)"),
        ("[Preface row 149]", "[Preface row 169]"),
        (
            "Row 68 → Row 89 Row 68 → Row 49 taxonomy meta prelude reunion index (row 129)",
            "Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169)",
        ),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_149" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_149.*", "", out, flags=re.S)
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
    if "### Row 169 skill checkpoint" in text:
        print("preface: row 169 already present")
        return
    m = re.search(
        r"(### Row 149 skill checkpoint.*?)(?=\n### Row 150 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 149 checkpoint missing")
    block = lift_149_to_169(m.group(1))
    anchor = "\n## The copper wire through the book"
    idx = text.find(anchor)
    if idx < 0:
        raise SystemExit("copper wire anchor missing")
    text = text[:idx] + "\n" + block + text[idx:]
    path.write_text(text)
    print("preface: added row 169")


def insert_epilogue_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    if "### Row 168 closing loop" in text:
        print("epilogue: row 169 loop already present")
        return
    block = lift_149_to_169(
        extract_between(
            text,
            "### Row 149 closing loop",
            "### Row 148 closing loop",
        )
    )
    needle = "### Row 167 closing loop"
    text = text.replace(needle, block + needle, 1)
    path.write_text(text)
    print("epilogue: added row 169 loop")


def add_prologue_compass() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    compass = "| Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 169) |"
    if compass in text:
        print("prologue: row 168 compass already present")
    else:
        after = "| Row 68 → Row 148 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 168) |"
        idx = text.find(after)
        if idx < 0:
            raise SystemExit("prologue row 167 compass missing")
        line_end = text.find("\n", idx)
        src = "| Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion (row 149) |"
        sidx = text.find(src)
        if sidx < 0:
            raise SystemExit("prologue row 149 compass missing")
        new_line = lift_149_to_169(text[sidx : text.find("\n", sidx)]) + "\n"
        text = text[: line_end + 1] + new_line + text[line_end + 1 :]
    preview_src = '| <span id="prologue-preview-row-149"></span>'
    preview_dst = '| <span id="prologue-preview-row-169"></span>'
    if preview_src in text and preview_dst not in text:
        i = text.find(preview_src)
        j = text.find("\n|", i + 1)
        preview_block = lift_149_to_169(text[i:j]) + "\n"
        text = text.replace(preview_src, preview_block + preview_src, 1)
    if "**Row 169 closing stitch" not in text:
        stitch = (
            "**Row 169 closing stitch (Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion).** {#row-169-closing-stitch} "
            "When row 168 closed — midpoint meta prelude capstone verified, row 167 or row 148 recited on the capstone path, and intermission → VII.0 landing recited with `hardening.yaml` beside Act IV — "
            "but **row 49 VII.0 → VII.1 opening hinge still opens like standalone Defects Notes homework after the forest Scene on the capstone path** — "
            "the [preface row 168 When-to-pause opening sentence](../preface.md#skill-navigation-row-168) names the dual reunion before taxonomy meta prelude reunion; "
            "read [preface row 169](../preface.md#skill-navigation-row-169), then the "
            "[Row 68 → Row 148 reunion index](../appendix/sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169), then "
            "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) before row 50 DDD meta prelude opens on the capstone path.\n\n"
        )
        text = text.replace("**Row 168 closing stitch", stitch + "**Row 168 closing stitch", 1)
    path.write_text(text)
    print("prologue: row 169 compass/preview/stitch")


def add_sources_row() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169"
    if idx_key in text:
        print("sources: row 169 already present")
        return
    start = "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)"
    i = text.find(start)
    if i < 0:
        raise SystemExit("sources row 149 index missing")
    block = lift_149_to_169(text[i:])
    block = block.split("## Row 68 → Row 127")[0]
    block = block.replace(
        "## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169)",
        f"## Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 169) {{#{idx_key}}}",
        1,
    )
    table_row = (
        "| 169 | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone Row 68 → Row 48 midpoint meta prelude capstone "
        "(midpoint prelude gate ↔ part-boundary meta prelude capstone ↔ row 48 meta) | "
        f"[Row 68 → Row 148 midpoint meta prelude capstone reunion index](#{idx_key}) · "
        "[preface row 168](../preface.md#skill-navigation-row-168) · "
        "[prologue row 168 preview](../prologue/00-many-scales.md#prologue-preview-row-169) · "
        "[prologue row 168 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch) · "
        "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) · "
        "[memory sheet row 168 baby picture](memory-sheet.md#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion) | "
        "Row 68 closed but **row 48 midpoint meta reunion still feels disconnected from verified part-boundary meta prelude capstone on the capstone path** — "
        "read row 68 + row 167 or row 148 gate + VI.4 intermission → VII.0 landing + row 48; "
        "[preface row 48](../preface.md#skill-navigation-row-48) |\n"
    )
    text = text.replace(
        "| 168 | Row 68 → Row 148 Row 68 → Row 67 part-boundary meta prelude capstone",
        table_row + "| 168 | Row 68 → Row 148 Row 68 → Row 67 part-boundary meta prelude capstone",
    )
    text = text.replace(
        "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)",
        block + "## Row 68 → Row 129 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 149)",
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
    print("sources: added row 169")


def add_memory_row() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    if "row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion" in text:
        print("memory-sheet: row 169 already present")
        return
    baby = lift_149_to_169(
        extract_between(
            text,
            "### Row 150 baby picture (Row 68 → Row 129 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion}",
            "### Row 150 baby picture",
        )
    )
    anchor = "### Row 150 baby picture (Row 68 → Row 129 Row 68 → Row 48 midpoint meta prelude capstone reunion) {#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion}"
    text = text.replace(anchor, baby + anchor, 1)
    mem_table = (
        "| 169 | Meta | Row 68 → Row 149 Row 68 → Row 49 taxonomy meta prelude capstone reunion | Row 68 → Row 48 midpoint meta prelude capstone reunion | "
        "[Row 68 → Row 148 midpoint meta prelude capstone reunion index](sources.md#row68-row149-taxonomy-meta-prelude-capstone-reunion-index-row-169) · "
        "[preface row 168 skill checkpoint](../preface.md#skill-navigation-row-168) · "
        "[prologue row 168 preview](../prologue/00-many-scales.md#prologue-preview-row-169) · "
        "[prologue row 168 closing stitch](../prologue/00-many-scales.md#row-168-closing-stitch) · "
        "[epilogue row 168 closing loop](../epilogue/multiscale.md#row-168-closing-loop) | "
        "Row 68 closed but row 48 midpoint meta reunion feels disconnected from verified part-boundary meta prelude capstone on the capstone path — "
        "read row 68 + row 167 or row 148 gate + VI.4 intermission → VII.0 landing + row 48; "
        "[row 168 baby picture](#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion) |\n"
    )
    text = text.replace(
        "| 167 | Meta | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion |",
        mem_table + "| 167 | Meta | Row 68 → Row 147 Row 68 → Row 67 part-boundary meta prelude capstone reunion |",
    )
    switch = (
        "When row 167 closed but midpoint meta reunion still lags on the capstone path, switch to [row 168](#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion)."
    )
    if switch not in text:
        text = text.replace(
            "When row 147 closed but midpoint meta reunion still lags on the capstone path, switch to [row 148](#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion).",
            "When row 167 closed but midpoint meta reunion still lags on the capstone path, switch to [row 168](#row-169-baby-picture-row68-row149-taxonomy-meta-prelude-capstone-reunion).",
        )
    path.write_text(text)
    print("memory-sheet: added row 169")


def patch_row_168_proceed_links() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    old = (
        "Proceed to [row 148](#row-148-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 147 on the capstone path"
    )
    new = (
        "Proceed to [row 169](#row-169-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 168 on the capstone path"
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
    print("preface/epilogue: patched row 168 → row 169 proceed links")


def main() -> None:
    dedupe_epilogue_closing_loops()
    insert_preface_row()
    insert_epilogue_loop()
    add_prologue_compass()
    add_sources_row()
    add_memory_row()
    patch_row_168_proceed_links()


if __name__ == "__main__":
    main()
