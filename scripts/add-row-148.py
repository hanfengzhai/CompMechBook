#!/usr/bin/env python3
"""Add row 148 (Row 68 → Row 128 ↔ Row 48 midpoint meta prelude capstone on capstone path)."""
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


def lift_88_to_128(s: str) -> str:
    """Promote opening-hinge row 108 sources index to capstone row 128 wording."""
    p = [
        (
            "Row 68 → Row 88 Row 68 → Row 48 midpoint meta prelude reunion",
            "Row 68 → Row 108 Row 68 → Row 48 midpoint meta prelude capstone reunion",
        ),
        (
            "row68-row88-midpoint-meta-prelude-reunion-index-row-108",
            "row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128",
        ),
        (
            "row-108-baby-picture-row68-row88-midpoint-meta-prelude-reunion",
            "row-128-baby-picture-row68-row108-midpoint-meta-prelude-capstone-reunion",
        ),
        ("Row 108 names", "Row 128 names"),
        ("Row 108 does not replace", "Row 128 does not replace"),
        ("(row 108)", "(row 128)"),
        ("skill-navigation-row-108", "skill-navigation-row-128"),
        ("preface row 108", "preface row 128"),
        ("Preface row 108", "Preface row 128"),
        ("memory sheet row 108", "memory sheet row 128"),
        ("Row 108 baby picture", "Row 128 baby picture"),
        ("row 106 verified", "row 126 verified"),
        ("[row 106]", "__ROW106_REF__"),
        ("row 106", "row 126"),
        ("Row 106", "Row 126"),
        ("__ROW106_REF__", "[row 126]"),
        ("[row 107]", "__ROW107_REF__"),
        ("row 107", "row 127"),
        ("Row 107", "Row 127"),
        ("__ROW107_REF__", "[row 127]"),
        (
            "part-boundary meta capstone / midpoint opening prelude",
            "part-boundary meta prelude capstone / midpoint meta prelude",
        ),
        ("part-boundary meta capstone", "part-boundary meta prelude capstone"),
        ("midpoint meta capstone", "midpoint meta prelude capstone"),
        (
            "midpoint meta capstone boundary",
            "midpoint meta prelude capstone boundary inside the coupling gate on the capstone path",
        ),
        (
            "midpoint meta reunion",
            "midpoint meta prelude capstone reunion",
        ),
        ("row 107 verified fvm", "row 127 verified twin-ladder"),
        ("on Cauchy stress", "on the capstone path"),
    ]
    return tx(s, p)


def lift_128_to_148(s: str) -> str:
    p = [
        ("Row 129 closing loop", "__ROW129_LOOP__"),
        ("Row 128 closing loop", "Row 148 closing loop"),
        ("row-129-closing-loop", "__ROW129_LOOP_ANCHOR__"),
        ("row-128-closing-loop", "row-148-closing-loop"),
        ("Row 129 closing stitch", "__ROW129_STITCH__"),
        ("Row 128 closing stitch", "Row 148 closing stitch"),
        ("row-129-closing-stitch", "__ROW129_STITCH_ANCHOR__"),
        ("row-128-closing-stitch", "row-148-closing-stitch"),
        ("prologue-preview-row-129", "__ROW129_PREVIEW__"),
        ("prologue-preview-row-128", "prologue-preview-row-148"),
        ("Row 129 preview", "__ROW129_PREVIEW_TEXT__"),
        ("Row 128 preview", "Row 148 preview"),
        ("Row 129 skill checkpoint", "__ROW129_SKILL__"),
        ("Row 128 skill checkpoint", "Row 148 skill checkpoint"),
        ("skill-navigation-row-129", "__ROW129_SKILL_NAV__"),
        ("skill-navigation-row-128", "skill-navigation-row-148"),
        ("memory sheet row 129", "__ROW129_MEM__"),
        ("memory sheet row 128", "memory sheet row 148"),
        ("Row 129 baby picture", "__ROW129_BABY__"),
        ("Row 128 baby picture", "Row 148 baby picture"),
        ("Row 129 three-way audit", "__ROW129_AUDIT__"),
        ("Row 128 three-way audit", "Row 148 three-way audit"),
        (
            "Row 68 → Row 108 Row 68 → Row 48 midpoint meta prelude capstone",
            "Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone",
        ),
        (
            "row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128",
            "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148",
        ),
        (
            "row-128-baby-picture-row68-row108-midpoint-meta-prelude-capstone-reunion",
            "row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion",
        ),
        ("[row 129]", "__ROW129_REF__"),
        ("[row 109]", "[row 129]"),
        ("row 109", "row 129"),
        ("Row 109", "Row 129"),
        ("__ROW129_REF__", "[row 129]"),
        ("skill-navigation-row-108", "skill-navigation-row-128"),
        ("[row 128]", "__ROW128_REF__"),
        ("[row 108]", "[row 128]"),
        ("row 108", "row 128"),
        ("Row 108", "Row 128"),
        ("__ROW128_REF__", "[row 128]"),
        ("[row 127]", "__ROW127_REF__"),
        ("__ROW127_REF__", "[row 147]"),
        ("skill-navigation-row-127", "skill-navigation-row-147"),
        (
            "Row 68 → Row 88 midpoint meta prelude reunion index (row 108)",
            "Row 68 → Row 128 midpoint meta prelude capstone reunion index (row 148)",
        ),
        (
            "row68-row88-midpoint-meta-prelude-reunion-index-row-108",
            "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148",
        ),
        ("when twin-ladder reunion is clean after row 127 but", "when twin-ladder reunion is clean after row 147 but"),
        ("memory sheet row 128 baby picture", "memory sheet row 148 baby picture"),
        ("prologue row 128 closing stitch", "prologue row 148 closing stitch"),
        ("prologue row 128 preview", "prologue row 148 preview"),
        ("Row 128 three-way audit", "Row 148 three-way audit"),
        ("Row 128 closes the", "Row 148 closes the"),
        ("Row 128 does not conflate", "Row 148 does not conflate"),
        ("(row 128)", "(row 148)"),
        ("__ROW129_LOOP__", "Row 129 closing loop"),
        ("__ROW129_LOOP_ANCHOR__", "row-129-closing-loop"),
        ("__ROW129_STITCH__", "Row 129 closing stitch"),
        ("__ROW129_STITCH_ANCHOR__", "row-129-closing-stitch"),
        ("__ROW129_PREVIEW__", "prologue-preview-row-129"),
        ("__ROW129_PREVIEW_TEXT__", "Row 129 preview"),
        ("__ROW129_SKILL__", "Row 129 skill checkpoint"),
        ("__ROW129_SKILL_NAV__", "skill-navigation-row-129"),
        ("__ROW129_MEM__", "memory sheet row 129"),
        ("__ROW129_BABY__", "Row 129 baby picture"),
        ("__ROW129_AUDIT__", "Row 129 three-way audit"),
        (
            "verified part-boundary meta prelude capstone closure (row 127)",
            "verified part-boundary meta prelude capstone closure (row 147)",
        ),
        ("When row 127 closed", "When row 147 closed"),
        ("after row 127 alone", "after row 147 alone"),
        ("Recite [preface row 127]", "Recite [preface row 147]"),
        (
            "when row 127 closed but row 48 midpoint meta still feels like defect homework disconnected from verified part-boundary meta prelude capstone on the capstone path",
            "when row 147 closed but row 48 midpoint meta still feels like defect homework disconnected from verified part-boundary meta prelude capstone on the capstone path",
        ),
        (
            "when row 127 and row 48 both verify individually",
            "when row 147 and row 48 both verify individually",
        ),
        (
            "rear-view mirror of row 127's twin-ladder → knee → forest turn",
            "rear-view mirror of row 147's twin-ladder → knee → forest turn",
        ),
        (
            "read row 68 gate + row 127 or row 108 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean on the capstone path but writings/continuum → writings/defects feels like two courses at the knee after verified twin-ladder reunion",
            "read row 68 gate + row 147 or row 128 part-boundary meta prelude capstone / midpoint meta prelude gate + VI.4 intermission → Bridge → VII.0 landing + row 48 meta aloud when part-boundary meta prelude capstone is clean on the capstone path after verified twin-ladder reunion but writings/continuum → writings/defects feels like two courses at the knee",
        ),
        (
            "Confirm [row 127](preface.md#skill-navigation-row-127) or [Row 68 → Row 88 midpoint meta prelude reunion index (row 108)](appendix/sources.md#row68-row88-midpoint-meta-prelude-reunion-index-row-108) recited",
            "Confirm [row 147](preface.md#skill-navigation-row-147) or [Row 68 → Row 108 midpoint meta prelude capstone reunion index (row 128)](appendix/sources.md#row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128) recited",
        ),
        (
            "Row 128 does not replace row 68, row 48, row 127, row 108, row 88, row 87, row 67, row 32, or row 20",
            "Row 148 does not replace row 68, row 48, row 147, row 128, row 108, row 88, row 87, row 67, row 32, or row 20",
        ),
        (
            "[row 127](preface.md#skill-navigation-row-127) or [row 108](preface.md#skill-navigation-row-108)",
            "[row 147](preface.md#skill-navigation-row-147) or [row 128](preface.md#skill-navigation-row-128)",
        ),
        (
            "When row 128 is complete, proceed to [row 129]",
            "When row 148 is complete, proceed to [row 129](preface.md#skill-navigation-row-129) when row 68 closed but taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the capstone path, "
            "to [row 128](preface.md#skill-navigation-row-128) when part-boundary meta prelude capstone is clean but midpoint meta prelude still lags on the opening-hinge path, "
            "to [row 108](preface.md#skill-navigation-row-108) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, "
            "to [row 147](preface.md#skill-navigation-row-147) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the capstone path, "
            "to [row 127](preface.md#skill-navigation-row-127) when Writings canonical meta prelude capstone is clean but part-boundary meta prelude still lags on the opening-hinge path, "
            "to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, "
            "to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, "
            "or extend prose only under `writings/` then sync.\n\nDUPLICATE_WHEN_ROW_128",
        ),
        (
            "Proceed to [row 129](#row-129-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 128",
            "Proceed to [row 129](#row-129-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 148 on the capstone path, "
            "to [row 128](#row-128-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after verified midpoint meta prelude capstone on the opening-hinge path",
        ),
        (
            "when opening [row 129](preface.md#skill-navigation-row-129) before row 49 closes on the capstone path",
            "when opening [row 129](preface.md#skill-navigation-row-129) before row 49 closes on the capstone path",
        ),
        (
            "When row 48 feels like defect homework after row 127 alone on the capstone path",
            "When row 48 feels like defect homework after row 147 alone on the capstone path",
        ),
        (
            "row 128 (row 68 ↔ row 48 reunion on the capstone path) with row 108",
            "row 148 (row 68 ↔ row 48 reunion on the capstone path) with row 128",
        ),
        (
            "row 128 (row 68 ↔ row 48 reunion on the capstone path) with row 108 (opening-hinge prelude stitch alone)",
            "row 148 (row 68 ↔ row 48 reunion on the capstone path) with row 128 (opening-hinge prelude stitch alone)",
        ),
        (
            "row 128 names **why that reunion must follow verified part-boundary meta prelude capstone (row 127)",
            "row 148 names **why that reunion must follow verified part-boundary meta prelude capstone (row 147)",
        ),
        ("row 127 closed part-boundary", "row 147 closed part-boundary"),
        ("Row 68 → Row 48 meta (row 108)", "Row 68 → Row 48 meta (row 128)"),
        ("[Preface row 128]", "[Preface row 148]"),
    ]
    out = tx(s, p)
    if "DUPLICATE_WHEN_ROW_128" in out:
        out = re.sub(r"\n\nDUPLICATE_WHEN_ROW_128.*", "", out, flags=re.S)
    return out


def add_row_148() -> None:
    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "skill-navigation-row-148" in preface and "### Row 148 skill checkpoint" in preface:
        print("preface: row 148 already present")
    else:
        m128 = re.search(
            r"(### Row 128 skill checkpoint.*?)(?=\n### Row 129 skill checkpoint)",
            preface,
            re.S,
        )
        if not m128:
            raise SystemExit("row 128 preface checkpoint missing")
        row148 = lift_128_to_148(m128.group(1))
        anchor = "\n## The copper wire through the book"
        idx = preface.find(anchor)
        if idx < 0:
            raise SystemExit("copper wire anchor missing")
        preface = preface[:idx] + "\n" + row148 + preface[idx:]
        preface_path.write_text(preface)
        print("preface: added row 148")

    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    if "row-148-closing-loop" not in ep:
        block128 = extract_between(ep, "### Row 128 closing loop", "### Row 109 closing loop")
        block148 = lift_128_to_148(block128)
        ep = ep.replace("### Row 147 closing loop", block148 + "### Row 147 closing loop", 1)
        ep_path.write_text(ep)
        print("epilogue: added row 148 loop")

    pro_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    pro = pro_path.read_text()
    compass_line = (
        "| Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 148) |"
    )
    if compass_line not in pro:
        line147 = (
            "| Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion (row 147) |"
        )
        idx147 = pro.find(line147)
        if idx147 < 0:
            raise SystemExit("prologue compass row 147 not found")
        line_end147 = pro.find("\n", idx147)
        line128 = (
            "| Row 68 → Row 108 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 128) |"
        )
        idx128 = pro.find(line128)
        if idx128 < 0:
            raise SystemExit("prologue compass row 128 not found")
        line_end128 = pro.find("\n", idx128)
        compass148 = lift_128_to_148(pro[idx128:line_end128]) + "\n"
        pro = pro[: line_end147 + 1] + compass148 + pro[line_end147 + 1 :]
        preview128 = extract_between(
            pro,
            '| <span id="prologue-preview-row-128"></span>',
            '\n| <span id="prologue-preview-row-108"></span>',
        )
        preview148 = lift_128_to_148(preview128)
        pro = pro.replace(
            '| <span id="prologue-preview-row-128"></span>',
            preview148 + '| <span id="prologue-preview-row-128"></span>',
            1,
        )
        if "row-148-closing-stitch" not in pro:
            stitch = (
                "**Row 148 closing stitch (Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion).** {#row-148-closing-stitch} "
                "When row 147 closed — part-boundary meta prelude capstone verified, row 146 or row 127 recited on the capstone path, and twin-ladder Bridge through VI.0 landing recited with `cht_export.yaml` beside both decks — "
                "but **row 48 midpoint opening prelude still opens like standalone defect coursework after VI.4's return-mapping chapter on the capstone path** — "
                "the [preface row 148 When-to-pause opening sentence](../preface.md#skill-navigation-row-148) names the dual reunion before taxonomy meta prelude reunion; "
                "read [preface row 148](../preface.md#skill-navigation-row-148), then the "
                "[Row 68 → Row 128 reunion index](../appendix/sources.md#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148), then "
                "[epilogue row 148 closing loop](../epilogue/multiscale.md#row-148-closing-loop) before row 49 taxonomy meta prelude opens on the capstone path.\n\n"
            )
            pro = pro.replace("**Row 128 closing stitch", stitch + "**Row 128 closing stitch", 1)
        pro_path.write_text(pro)
        print("prologue: added row 148 compass/preview/stitch")

    src_path = ROOT / "writings/appendix/chapters/sources.md"
    src = src_path.read_text()
    if "row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148" not in src:
        block108 = extract_between(
            src,
            "## Row 68 → Row 88 Row 68 → Row 48 midpoint meta prelude reunion index (row 108)",
            "## Row 68 → Row 89 Row 68 → Row 49 taxonomy meta prelude reunion index (row 109)",
        )
        block148 = lift_128_to_148(lift_88_to_128(block108))
        table_row = (
            "| 148 | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone (midpoint prelude gate ↔ part-boundary meta prelude capstone ↔ row 48 meta) | "
            "[Row 68 → Row 128 midpoint meta prelude capstone reunion index](#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148) · "
            "[preface row 148](../preface.md#skill-navigation-row-148) · "
            "[prologue row 148 preview](../prologue/00-many-scales.md#prologue-preview-row-148) · "
            "[prologue row 148 closing stitch](../prologue/00-many-scales.md#row-148-closing-stitch) · "
            "[epilogue row 148 closing loop](../epilogue/multiscale.md#row-148-closing-loop) · "
            "[memory sheet row 148 baby picture](memory-sheet.md#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion) | "
            "Row 68 closed but **row 48 midpoint meta reunion still feels disconnected from verified part-boundary meta prelude capstone on the capstone path** — "
            "read row 68 + row 147 or row 128 gate + VI.4 intermission → VII.0 landing + row 48; "
            "[preface row 48](../preface.md#skill-navigation-row-48) |\n"
        )
        src = src.replace(
            "| 147 | Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone",
            table_row + "| 147 | Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone",
        )
        src = src.replace(
            "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)",
            block148 + "## Row 68 → Row 127 Row 68 → Row 67 part-boundary meta prelude capstone reunion index (row 147)",
        )
        extra = (
            "[row 147](#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148) reunites **part-boundary meta prelude capstone with the midpoint meta prelude capstone boundary** "
            "when row 147 closed part-boundary meta prelude capstone at verified twin-ladder rhythm on the capstone path but VI.4 intermission and row 48 still read like separate courses after verified fvm → continuum meta;"
        )
        if extra not in src:
            needle = (
                "[row 146](#row68-row127-part-boundary-meta-prelude-capstone-reunion-index-row-147) reunites **Writings canonical meta prelude capstone with the part-boundary meta prelude capstone boundary** "
            )
            if needle in src:
                src = src.replace(needle, needle + " " + extra)
        src_path.write_text(src)
        print("sources: added row 148 index")

    mem_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    mem = mem_path.read_text()
    if "row-148-baby-picture" not in mem:
        baby128 = extract_between(mem, "### Row 128 baby picture", "### Row 129 baby picture")
        baby148 = lift_128_to_148(baby128)
        mem = mem.replace("### Row 128 baby picture", baby148 + "### Row 128 baby picture", 1)
        mem_table = (
            "| 148 | Meta | Row 68 → Row 128 Row 68 → Row 48 midpoint meta prelude capstone reunion | "
            "[Row 68 → Row 128 midpoint meta prelude capstone reunion index](sources.md#row68-row128-midpoint-meta-prelude-capstone-reunion-index-row-148) · "
            "[preface row 148 skill checkpoint](../preface.md#skill-navigation-row-148) · "
            "[prologue row 148 preview](../prologue/00-many-scales.md#prologue-preview-row-148) · "
            "[prologue row 148 closing stitch](../prologue/00-many-scales.md#row-148-closing-stitch) · "
            "[epilogue row 148 closing loop](../epilogue/multiscale.md#row-148-closing-loop) | "
            "Row 68 closed but row 48 midpoint meta reunion feels disconnected from verified part-boundary meta prelude capstone on the capstone path — "
            "read row 68 + row 147 or row 128 gate + VI.4 intermission → VII.0 landing + row 48; "
            "[row 148 baby picture](#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion) |\n"
        )
        mem = mem.replace(
            "| 128 | Meta | [Row 68 → Row 108 midpoint meta prelude capstone reunion index](sources.md#row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128) ·",
            mem_table + "| 128 | Meta | [Row 68 → Row 108 midpoint meta prelude capstone reunion index](sources.md#row68-row108-midpoint-meta-prelude-capstone-reunion-index-row-128) ·",
        )
        if "When row 147 closed but midpoint meta reunion still lags" not in mem:
            mem = mem.replace(
                "When row 146 closed but twin-ladder reunion still lags on the capstone path, switch to [row 147](#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion).",
                "When row 146 closed but twin-ladder reunion still lags on the capstone path, switch to [row 147](#row-147-baby-picture-row68-row127-part-boundary-meta-prelude-capstone-reunion). "
                "When row 147 closed but midpoint meta reunion still lags on the capstone path, switch to [row 148](#row-148-baby-picture-row68-row128-midpoint-meta-prelude-capstone-reunion).",
            )
        mem_path.write_text(mem)
        print("memory-sheet: added row 148")
    else:
        print("memory-sheet: row 148 baby already present")

    # Point row 147 capstone epilogue at row 148 on the capstone path.
    ep_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    ep = ep_path.read_text()
    old = (
        "Proceed to [row 128](#row-128-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 147 on the capstone path"
    )
    new = (
        "Proceed to [row 148](#row-148-closing-loop) when row 68 closed but midpoint meta prelude capstone still lags after row 147 on the capstone path"
    )
    if old in ep:
        ep = ep.replace(old, new)
        ep_path.write_text(ep)
        print("epilogue: row 147 → row 148 proceed link")


def main() -> None:
    add_row_148()


if __name__ == "__main__":
    main()
