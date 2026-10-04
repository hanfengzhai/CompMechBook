#!/usr/bin/env python3
"""Polish row 175 sections after lift_155_to_175."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_175_mod", ROOT / "scripts" / "add-row-175.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_155_to_175 = _mod.lift_155_to_175
export_index_to_electronic_audit_175 = _mod.export_index_to_electronic_audit_175
extract_between = _mod.extract_between


def polish_row_175(s: str) -> str:
    s = s.replace("row 154 closed export", "row 174 closed export")
    s = s.replace("after row 154 alone on the capstone path", "after row 174 alone on the capstone path")
    s = s.replace(
        "verified export meta prelude capstone closure (row 154)",
        "verified export meta prelude capstone closure (row 174)",
    )
    s = s.replace("Row 68 → Row 55 meta (row 115)", "Row 68 → Row 55 meta (row 155)")
    s = s.replace("[prologue row 155 preview]", "[prologue row 175 preview]")
    s = s.replace("prologue row 155 preview", "prologue row 175 preview")
    s = s.replace(
        "Row 68 → Row 155 electronic audit meta prelude capstone reunion index",
        "Row 68 → Row 151 electronic audit meta prelude capstone reunion index",
    )
    s = s.replace("([row 155]", "([row 175]")
    s = s.replace("preface row 155 skill checkpoint", "preface row 175 skill checkpoint")
    s = s.replace("prologue row 155 closing stitch", "prologue row 175 closing stitch")
    s = s.replace("epilogue row 155 closing loop", "epilogue row 175 closing loop")
    s = s.replace("Export meta prelude capstone row 154", "Export meta prelude capstone row 174")
    s = s.replace(
        "When row 175 feels disconnected from row 154",
        "When row 175 feels disconnected from row 174",
    )
    s = s.replace("row 154 when **VIII.2 Bridge", "row 174 when **VIII.2 Bridge")
    s = s.replace("row 155 when **VIII.3 Bridge", "row 175 when **VIII.3 Bridge")
    s = s.replace(
        "When row 154 closed but electronic audit meta reunion still lags",
        "When row 174 closed but electronic audit meta reunion still lags",
    )
    s = s.replace(
        "Row 68 → Row 175 Row 68 → Row 55",
        "Row 68 → Row 151 Row 68 → Row 55",
    )
    s = s.replace("#prologue-preview-row-155", "#prologue-preview-row-175")
    s = s.replace("#row-155-closing-stitch", "#row-175-closing-stitch")
    s = s.replace("#row-155-closing-loop", "#row-175-closing-loop")
    s = s.replace("{#row-155-closing-loop}", "{#row-175-closing-loop}")
    s = s.replace(
        "row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion",
        "row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion",
    )
    s = s.replace("[Preface row 155]", "[Preface row 175]")
    s = re.sub(
        r"\[Preface row 175\]\(\.\./preface\.md#skill-navigation-row-155\)",
        "[Preface row 175](../preface.md#skill-navigation-row-175)",
        s,
    )
    s = re.sub(
        r"\[preface row 175\]\(\.\./preface\.md#skill-navigation-row-155\)",
        "[preface row 175](../preface.md#skill-navigation-row-175)",
        s,
    )
    s = s.replace(
        "[preface row 174](../preface.md#skill-navigation-row-154)",
        "[preface row 174](../preface.md#skill-navigation-row-174)",
    )
    s = s.replace(
        "row68-row135-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
        "row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
    )
    epilogue_175_proceed = (
        "Do not conflate row 175 (row 68 ↔ row 55 reunion on the capstone path) with row 155 "
        "(opening-hinge prelude stitch alone) — row 155 names **Row 68 → Row 135 Row 68 → Row 55 "
        "electronic audit meta prelude capstone reunion**; row 175 names **why that reunion must follow "
        "verified export meta prelude capstone (row 174) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 176](#row-176-closing-loop) when row 68 closed but "
        "Born–Oppenheimer meta prelude capstone still lags after row 175 on the capstone path, to "
        "[row 155](#row-155-closing-loop) when row 68 closed but electronic audit meta prelude still "
        "lags on the opening-hinge path, to "
        "[row 135](#row-135-closing-loop) for the Row 68 ↔ Row 55 electronic audit meta prelude audit on the "
        "opening-hinge path alone, to [row 174](#row-174-closing-loop) when export meta prelude capstone still "
        "lags after verified dynamics meta prelude capstone on the capstone path, to "
        "[row 55](#row-55-closing-loop) when only VIII.3 → IX.0 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 175 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 155 \(row 68 ↔ row 55 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_175_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 175 is complete, proceed to [row 176](preface.md#skill-navigation-row-156) "
        "when row 68 closed but Born–Oppenheimer meta prelude capstone still lags after verified "
        "electronic audit meta prelude capstone on the capstone path, to [row 155](preface.md#skill-navigation-row-155) "
        "when export meta prelude capstone is clean but electronic audit meta prelude still lags on the "
        "opening-hinge path, to [row 135](preface.md#skill-navigation-row-135) for the Row 68 ↔ "
        "Row 55 electronic audit meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 174](preface.md#skill-navigation-row-174) when export meta prelude capstone still "
        "lags after verified dynamics meta prelude capstone on the capstone path, to "
        "[row 55](preface.md#skill-navigation-row-55) for the VIII.3 → IX.0 meta audit alone, to "
        "[row 36](preface.md#skill-navigation-row-36) when only the DFT preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 175 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_175() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 175 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i if i >= 0 else 0)
    m = re.search(
        r"(### Row 155 skill checkpoint.*?)(?=\n### Row 156 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 155 template missing")
    block = polish_row_175(lift_155_to_175(m.group(1)))
    if i >= 0 and j >= 0:
        text = text[:i] + block + text[j:]
    else:
        j = text.find(end)
        text = text[:j] + "\n" + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 175 checkpoint")


def rebuild_epilogue_row_175_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 175 closing loop"
    end = "### Row 174 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 175 loop missing")
    block = polish_row_175(
        lift_155_to_175(
            extract_between(
                text,
                "### Row 155 closing loop",
                "### Row 154 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 175 closing loop")


def fix_prologue_row_175() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 135 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 155) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion (row 175) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_175(lift_155_to_175(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-155"></span>Row 175 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-175"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-155"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_175(lift_155_to_175(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 175 compass/preview")


def rebuild_sources_row_175_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker175 = "## Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 175)"
    i175 = text.find(marker175)
    if i175 < 0:
        print("sources: skip rebuild (row 175 marker missing)")
        return
    start174 = "## Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)"
    i174 = text.find(start174)
    if i174 < 0:
        raise SystemExit("sources row 174 template missing")
    j174_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 53", i175)
    if j174_end < 0:
        j174_end = text.find("\n## Row 68 → Row 132", i175)
    block = polish_row_175(
        export_index_to_electronic_audit_175(
            lift_155_to_175(text[i174 : text.find("\n## Row 68 → Row 151 Row 68 → Row 53", i174)])
        )
    ).strip()
    block = block.replace(
        "(row 175) {#row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175}",
        "(row 175) {#row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175}",
        1,
    )
    text = text[:i175] + block + "\n\n\n" + text[j174_end:]
    path.write_text(text)
    print("sources: rebuilt row 175 index")


def rebuild_memory_row_175_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 175 baby picture"
    if anchor not in text:
        print("memory-sheet: row 175 baby missing — run add-row-175 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 155 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 156 baby picture", start + 1)
    baby155 = extract_between(
        text,
        "### Row 155 baby picture",
        "### Row 156 baby picture",
    )
    baby = polish_row_175(lift_155_to_175(baby155))
    baby = baby.replace(
        "### Row 175 baby picture (Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion) "
        "{#row-155-baby-picture-row68-row135-electronic-audit-meta-prelude-capstone-reunion}",
        "### Row 175 baby picture (Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion) "
        "{#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 175 baby picture")


def patch_row_174_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    new = (
        "When row 174 is complete, proceed to [row 175](preface.md#skill-navigation-row-175) "
        "when row 68 closed but electronic audit meta prelude capstone still lags after verified export meta prelude capstone on the capstone path, "
        "to [row 154](preface.md#skill-navigation-row-154) when dynamics meta prelude capstone is clean but export meta prelude still lags on the opening-hinge path, "
        "to [row 134](preface.md#skill-navigation-row-134) for the Row 68 ↔ Row 54 export meta prelude audit on the opening-hinge prelude path alone, "
        "to [row 173](preface.md#skill-navigation-row-173) when dynamics meta prelude capstone still lags after verified atomistic meta prelude capstone on the capstone path, "
        "to [row 54](preface.md#skill-navigation-row-54) for the VIII.2 → VIII.3 meta audit alone, "
        "to [row 35](preface.md#skill-navigation-row-35) when only the coarse-graining preview stalls, or extend prose only under `writings/` then sync."
    )
    if "When row 174 is complete, proceed to [row 175](preface.md#skill-navigation-row-175)" not in text:
        text = re.sub(
            r"When row 174 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 174 → row 175 proceed")


def remove_duplicate_corrupted_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    marker = "### Row 175 baby picture"
    while text.count(marker) > 1:
        first = text.find(marker)
        second = text.find(marker, first + 1)
        end = text.find("\n### ", second)
        if end < 0:
            end = len(text)
        else:
            end += 1
        text = text[:second] + text[end:]
    if text.count(marker) == 0:
        baby155 = extract_between(
            text,
            "### Row 155 baby picture",
            "### Row 156 baby picture",
        )
        baby = polish_row_175(lift_155_to_175(baby155))
        baby = re.sub(
            r"^### Row 175 baby picture[^\n]*\n",
            "### Row 175 baby picture (Row 68 → Row 151 Row 68 → Row 55 electronic audit meta prelude capstone reunion) "
            "{#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion}\n",
            baby,
            count=1,
        )
        baby = baby.replace(
            "sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
            "sources.md#row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
        )
        baby = baby.replace(
            "[preface row 155](../preface.md#skill-navigation-row-175)",
            "[preface row 155](../preface.md#skill-navigation-row-155)",
        )
        anchor = text.find("### Row 155 baby picture")
        if anchor >= 0:
            text = text[:anchor] + baby + text[anchor:]
    elif text.count(marker) == 1:
        start = text.find(marker)
        end = text.find("\n### ", start + 1)
        block = text[start:end if end >= 0 else len(text)]
        fixed = polish_row_175(block)
        fixed = re.sub(
            r"\{#row-155-baby-picture-row68-row155-electronic-audit-meta-prelude-capstone-reunion\}",
            "{#row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion}",
            fixed,
        )
        fixed = fixed.replace(
            "Row 68 → Row 155 Row 68 → Row 55",
            "Row 68 → Row 151 Row 68 → Row 55",
        )
        fixed = fixed.replace(
            "sources.md#row68-row155-electronic-audit-meta-prelude-capstone-reunion-index-row-155",
            "sources.md#row68-row151-electronic-audit-meta-prelude-capstone-reunion-index-row-175",
        )
        fixed = fixed.replace(
            "[preface row 155](../preface.md#skill-navigation-row-175)",
            "[preface row 155](../preface.md#skill-navigation-row-155)",
        )
        text = text[:start] + fixed + text[end if end >= 0 else len(text) :]
    path.write_text(text)
    print("memory-sheet: deduped row 175 baby picture")


def global_polish_175_links() -> None:
    for rel in (
        "writings/preface/chapters/preface.md",
        "writings/prologue/chapters/00-many-scales.md",
        "writings/epilogue/chapters/multiscale.md",
        "writings/appendix/chapters/sources.md",
    ):
        path = ROOT / rel
        text = path.read_text()
        text = text.replace(
            "Row 68 → Row 155 reunion index",
            "Row 68 → Row 151 reunion index",
        )
        text = text.replace(
            "[Preface: row 155 skill checkpoint](../preface.md#skill-navigation-row-175)",
            "[Preface: row 175 skill checkpoint](../preface.md#skill-navigation-row-175)",
        )
        text = text.replace(
            "row-175-baby-picture-row68-row151-dynamics-meta-prelude-capstone-reunion",
            "row-175-baby-picture-row68-row151-electronic-audit-meta-prelude-capstone-reunion",
        )
        text = text.replace(
            "**why verified export meta prelude capstone demands VIII.3 Bridge to Part IX before any NPT proof on row 55**",
            "**why verified export meta prelude capstone demands VIII.3 Bridge to Part IX before any foundation SCF proof on row 55**",
        )
        text = text.replace(
            "one continuous NPT → export arc",
            "one continuous pedigree → foundation SCF arc",
        )
        path.write_text(text)
    print("writings: global row 175 link polish")


def main() -> None:
    remove_duplicate_corrupted_baby()
    global_polish_175_links()
    rebuild_preface_row_175()
    rebuild_epilogue_row_175_loop()
    fix_prologue_row_175()
    rebuild_sources_row_175_index()
    rebuild_memory_row_175_baby()
    patch_row_174_when_complete()


if __name__ == "__main__":
    main()
