#!/usr/bin/env python3
"""Polish row 174 sections after lift_154_to_174."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_174_mod", ROOT / "scripts" / "add-row-174.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_154_to_174 = _mod.lift_154_to_174
dynamics_index_to_export_174 = _mod.dynamics_index_to_export_174
extract_between = _mod.extract_between


def polish_row_174(s: str) -> str:
    s = s.replace("row 153 closed dynamics", "row 173 closed dynamics")
    s = s.replace("after row 153 alone on the capstone path", "after row 173 alone on the capstone path")
    s = s.replace(
        "verified dynamics meta prelude capstone closure (row 153)",
        "verified dynamics meta prelude capstone closure (row 173)",
    )
    s = s.replace("Row 68 → Row 54 meta (row 114)", "Row 68 → Row 54 meta (row 154)")
    s = s.replace("[prologue row 154 preview]", "[prologue row 174 preview]")
    s = s.replace("prologue row 154 preview", "prologue row 174 preview")
    s = s.replace(
        "Row 68 → Row 154 export meta prelude capstone reunion index",
        "Row 68 → Row 151 export meta prelude capstone reunion index",
    )
    s = s.replace("([row 154]", "([row 174]")
    s = s.replace("preface row 154 skill checkpoint", "preface row 174 skill checkpoint")
    s = s.replace("prologue row 154 closing stitch", "prologue row 174 closing stitch")
    s = s.replace("epilogue row 154 closing loop", "epilogue row 174 closing loop")
    s = s.replace("Dynamics meta prelude capstone row 153", "Dynamics meta prelude capstone row 173")
    s = s.replace(
        "When row 174 feels disconnected from row 153",
        "When row 174 feels disconnected from row 173",
    )
    s = s.replace("row 153 when **VIII.1 Bridge", "row 173 when **VIII.1 Bridge")
    s = s.replace("row 154 when **VIII.2 Bridge", "row 174 when **VIII.2 Bridge")
    s = s.replace(
        "When row 153 closed but export meta reunion still lags",
        "When row 173 closed but export meta reunion still lags",
    )
    s = s.replace(
        "Row 68 → Row 174 Row 68 → Row 54",
        "Row 68 → Row 151 Row 68 → Row 54",
    )
    s = s.replace("#prologue-preview-row-154", "#prologue-preview-row-174")
    s = s.replace("#row-154-closing-stitch", "#row-174-closing-stitch")
    s = s.replace("#row-154-closing-loop", "#row-174-closing-loop")
    s = s.replace("{#row-154-closing-loop}", "{#row-174-closing-loop}")
    s = s.replace(
        "row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion",
        "row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion",
    )
    s = s.replace("[Preface row 154]", "[Preface row 174]")
    s = re.sub(
        r"\[Preface row 174\]\(\.\./preface\.md#skill-navigation-row-154\)",
        "[Preface row 174](../preface.md#skill-navigation-row-174)",
        s,
    )
    s = re.sub(
        r"\[preface row 174\]\(\.\./preface\.md#skill-navigation-row-154\)",
        "[preface row 174](../preface.md#skill-navigation-row-174)",
        s,
    )
    s = s.replace(
        "[preface row 173](../preface.md#skill-navigation-row-153)",
        "[preface row 173](../preface.md#skill-navigation-row-173)",
    )
    s = s.replace(
        "row68-row134-export-meta-prelude-capstone-reunion-index-row-154",
        "row68-row151-export-meta-prelude-capstone-reunion-index-row-174",
    )
    epilogue_174_proceed = (
        "Do not conflate row 174 (row 68 ↔ row 54 reunion on the capstone path) with row 154 "
        "(opening-hinge prelude stitch alone) — row 154 names **Row 68 → Row 134 Row 68 → Row 54 "
        "export meta prelude capstone reunion**; row 174 names **why that reunion must follow "
        "verified dynamics meta prelude capstone (row 173) and the outer midpoint prelude "
        "gate (row 68)**. Proceed to [row 175](#row-175-closing-loop) when row 68 closed but "
        "electronic audit meta prelude capstone still lags after row 174 on the capstone path, to "
        "[row 154](#row-154-closing-loop) when row 68 closed but export meta prelude still "
        "lags on the opening-hinge path, to "
        "[row 134](#row-134-closing-loop) for the Row 68 ↔ Row 54 export meta prelude audit on the "
        "opening-hinge path alone, to [row 173](#row-173-closing-loop) when dynamics meta prelude capstone still "
        "lags after verified atomistic meta prelude capstone on the capstone path, to "
        "[row 54](#row-54-closing-loop) when only VIII.2 → VIII.3 stalls, or extend prose only "
        "under `writings/` then sync."
    )
    if "### Row 174 closing loop" in s:
        s = re.sub(
            r"Do not conflate row 154 \(row 68 ↔ row 54 reunion on the capstone path\).*?"
            r"or extend prose only under `writings/` then sync\.\n",
            epilogue_174_proceed + "\n",
            s,
            count=1,
            flags=re.S,
        )
    when_complete = (
        "When row 174 is complete, proceed to [row 175](preface.md#skill-navigation-row-155) "
        "when row 68 closed but electronic audit meta prelude capstone still lags after verified "
        "export meta prelude capstone on the capstone path, to [row 154](preface.md#skill-navigation-row-154) "
        "when dynamics meta prelude capstone is clean but export meta prelude still lags on the "
        "opening-hinge path, to [row 134](preface.md#skill-navigation-row-134) for the Row 68 ↔ "
        "Row 54 export meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 173](preface.md#skill-navigation-row-173) when dynamics meta prelude capstone still "
        "lags after verified atomistic meta prelude capstone on the capstone path, to "
        "[row 54](preface.md#skill-navigation-row-54) for the VIII.2 → VIII.3 meta audit alone, to "
        "[row 35](preface.md#skill-navigation-row-35) when only the coarse-graining preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 174 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_174() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    start = "### Row 174 skill checkpoint"
    end = "\n## The copper wire through the book"
    i = text.find(start)
    j = text.find(end, i if i >= 0 else 0)
    m = re.search(
        r"(### Row 154 skill checkpoint.*?)(?=\n### Row 155 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 154 template missing")
    block = polish_row_174(lift_154_to_174(m.group(1)))
    if i >= 0 and j >= 0:
        text = text[:i] + block + text[j:]
    else:
        j = text.find(end)
        text = text[:j] + "\n" + block + text[j:]
    path.write_text(text)
    print("preface: rebuilt row 174 checkpoint")


def rebuild_epilogue_row_174_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    start = "### Row 174 closing loop"
    end = "### Row 173 closing loop"
    i = text.find(start)
    j = text.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit("epilogue row 174 loop missing")
    block = polish_row_174(
        lift_154_to_174(
            extract_between(
                text,
                "### Row 154 closing loop",
                "### Row 153 closing loop",
            )
        )
    )
    text = text[:i] + block + text[j:]
    path.write_text(text)
    print("epilogue: rebuilt row 174 closing loop")


def fix_prologue_row_174() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 134 Row 68 → Row 54 export meta prelude capstone reunion (row 154) |"
    bad = "| Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion (row 174) |"
    sidx = text.find(src)
    bidx = text.find(bad)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_174(lift_154_to_174(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-154"></span>Row 174 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-174"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-154"></span>'
        pi = text.find(psrc)
        pj = text.find("\n|", pi + 1)
        preview = polish_row_174(lift_154_to_174(text[pi:pj])) + "\n"
        text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 174 compass/preview")


def rebuild_sources_row_174_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker174 = "## Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion index (row 174)"
    i174 = text.find(marker174)
    if i174 < 0:
        print("sources: skip rebuild (row 174 marker missing)")
        return
    start173 = "## Row 68 → Row 151 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 173)"
    i173 = text.find(start173)
    if i173 < 0:
        raise SystemExit("sources row 173 template missing")
    j173_end = text.find("\n## Row 68 → Row 132", i174)
    if j173_end < 0:
        j173_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 52", i174)
    block = polish_row_174(
        dynamics_index_to_export_174(
            lift_154_to_174(text[i173 : text.find("\n## Row 68 → Row 132", i173)])
        )
    ).strip()
    block = block.replace(
        "(row 174) {#row68-row151-export-meta-prelude-capstone-reunion-index-row-174}",
        "(row 174) {#row68-row151-export-meta-prelude-capstone-reunion-index-row-174}",
        1,
    )
    text = text[:i174] + block + "\n\n\n" + text[j173_end:]
    path.write_text(text)
    print("sources: rebuilt row 174 index")


def rebuild_memory_row_174_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 174 baby picture"
    if anchor not in text:
        print("memory-sheet: row 174 baby missing — run add-row-174 first")
        return
    start = text.find(anchor)
    end = text.find("### Row 154 baby picture", start + 1)
    if end < 0:
        end = text.find("### Row 155 baby picture", start + 1)
    baby154 = extract_between(
        text,
        "### Row 154 baby picture",
        "### Row 155 baby picture",
    )
    baby = polish_row_174(lift_154_to_174(baby154))
    baby = baby.replace(
        "### Row 174 baby picture (Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion) "
        "{#row-154-baby-picture-row68-row134-export-meta-prelude-capstone-reunion}",
        "### Row 174 baby picture (Row 68 → Row 151 Row 68 → Row 54 export meta prelude capstone reunion) "
        "{#row-174-baby-picture-row68-row151-export-meta-prelude-capstone-reunion}",
        1,
    )
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 174 baby picture")


def patch_row_173_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    new = (
        "When row 173 is complete, proceed to [row 174](preface.md#skill-navigation-row-174) "
        "when row 68 closed but export meta prelude capstone still lags after verified dynamics meta prelude capstone on the capstone path, "
        "to [row 153](preface.md#skill-navigation-row-153) when atomistic meta prelude capstone is clean but dynamics meta prelude still lags on the opening-hinge path, "
        "to [row 133](preface.md#skill-navigation-row-133) for the Row 68 ↔ Row 53 dynamics meta prelude audit on the opening-hinge prelude path alone, "
        "to [row 172](preface.md#skill-navigation-row-172) when atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the capstone path, "
        "to [row 53](preface.md#skill-navigation-row-53) for the VIII.1 → VIII.2 meta audit alone, "
        "to [row 34](preface.md#skill-navigation-row-34) when only the MD preview stalls, or extend prose only under `writings/` then sync."
    )
    if "When row 173 is complete, proceed to [row 174](preface.md#skill-navigation-row-174)" not in text:
        text = re.sub(
            r"When row 173 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 173 → row 174 proceed")


def remove_duplicate_corrupted_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    bad = (
        "### Row 174 baby picture (Row 68 → Row 114 Row 68 → Row 54 export meta prelude capstone reunion) "
        "{#row-134-baby-picture-row68-row114-export-meta-prelude-capstone-reunion}"
    )
    if bad in text:
        start = text.find(bad)
        end = text.find("### Row 155 baby picture", start)
        text = text[:start] + text[end:]
        path.write_text(text)
        print("memory-sheet: removed duplicate corrupted row 174 baby")


def main() -> None:
    remove_duplicate_corrupted_baby()
    rebuild_preface_row_174()
    rebuild_epilogue_row_174_loop()
    fix_prologue_row_174()
    rebuild_sources_row_174_index()
    rebuild_memory_row_174_baby()
    patch_row_173_when_complete()


if __name__ == "__main__":
    main()
