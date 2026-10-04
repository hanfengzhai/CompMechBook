#!/usr/bin/env python3
"""Polish row 179 Handshake 3 meta prelude capstone sections after lift_159_to_179."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "add_row_179_mod", ROOT / "scripts" / "add-row-179.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
lift_159_to_179 = _mod.lift_159_to_179
export_index_to_handshake3_179 = _mod.export_index_to_handshake3_179
extract_between = _mod.extract_between


def polish_row_179(s: str) -> str:
    s = s.replace("row 158 closed", "row 178 closed")
    s = s.replace("after row 158 alone on the capstone path", "after row 178 alone on the capstone path")
    s = s.replace(
        "verified DFT workflows meta prelude capstone closure (row 178)",
        "verified DFT workflows meta prelude capstone closure (row 178)",
    )
    s = s.replace("Row 68 → Row 59 meta (row 159)", "Row 68 → Row 59 meta (row 179)")
    s = s.replace(
        "Row 68 → Row 139 Handshake 3 meta prelude capstone reunion index",
        "Row 68 → Row 151 Handshake 3 meta prelude capstone reunion index",
    )
    s = s.replace("([row 159]", "([row 179]")
    s = s.replace("preface row 159 skill checkpoint", "preface row 179 skill checkpoint")
    s = s.replace("prologue row 159 preview", "prologue row 179 preview")
    s = s.replace("prologue row 159 closing stitch", "prologue row 179 closing stitch")
    s = s.replace("epilogue row 159 closing loop", "epilogue row 179 closing loop")
    s = s.replace("#prologue-preview-row-159", "#prologue-preview-row-179")
    s = s.replace("#row-159-closing-stitch", "#row-179-closing-stitch")
    s = s.replace("#row-159-closing-loop", "#row-179-closing-loop")
    s = s.replace("{#row-159-closing-loop}", "{#row-179-closing-loop}")
    s = s.replace(
        "row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion",
        "row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion",
    )
    s = s.replace(
        "row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159",
        "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179",
    )
    s = re.sub(
        r"\[Preface row 179\]\(\.\./preface\.md#skill-navigation-row-159\)",
        "[Preface row 179](../preface.md#skill-navigation-row-179)",
        s,
    )
    s = re.sub(
        r"\[preface row 179\]\(\.\./preface\.md#skill-navigation-row-159\)",
        "[preface row 179](../preface.md#skill-navigation-row-179)",
        s,
    )
    s = re.sub(
        r"\[preface row 179\]\(\.\./preface\.md#skill-navigation-row-137\)",
        "[preface row 179](../preface.md#skill-navigation-row-179)",
        s,
    )
    s = s.replace("Kohn–Sham meta capstone reunion", "Handshake 3 meta prelude capstone reunion")
    s = s.replace("verified Kohn–Sham meta capstone", "verified DFT workflows meta prelude capstone")
    when_complete = (
        "When row 179 is complete, proceed to [row 160](preface.md#skill-navigation-row-160) "
        "when row 68 closed but Handshake 4a meta prelude capstone still lags after verified "
        "Handshake 3 meta prelude capstone on the capstone path, to [row 140](preface.md#skill-navigation-row-140) "
        "when Handshake 3 meta prelude capstone is clean but Handshake 3 meta prelude still lags on the "
        "opening-hinge path, to [row 100](preface.md#skill-navigation-row-100) for the Row 68 ↔ "
        "Row 60 Handshake 3 meta prelude audit on the opening-hinge prelude path alone, to "
        "[row 178](preface.md#skill-navigation-row-178) when DFT workflows meta prelude capstone still "
        "lags after verified Kohn–Sham meta prelude capstone on the capstone path, to "
        "[row 59](preface.md#skill-navigation-row-59) for the IX.3 → Handshake 3 meta audit alone, to "
        "[row 40](preface.md#skill-navigation-row-40) when only the Handshake 3 preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    s = re.sub(
        r"When row 179 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
        when_complete,
        s,
        count=1,
        flags=re.S,
    )
    return s


def rebuild_preface_row_179() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    m = re.search(
        r"(### Row 159 skill checkpoint.*?)(?=\n### Row 160 skill checkpoint)",
        text,
        re.S,
    )
    if not m:
        raise SystemExit("preface row 159 template missing")
    block = polish_row_179(lift_159_to_179(m.group(1)))
    start = text.find("### Row 179 skill checkpoint")
    end = text.find("\n### Row 178 skill checkpoint", start if start >= 0 else 0)
    if start >= 0 and end > start:
        text = text[:start] + block + text[end:]
        path.write_text(text)
        print("preface: rebuilt row 179 checkpoint")
    else:
        raise SystemExit("preface row 179 checkpoint missing")


def rebuild_epilogue_row_179_loop() -> None:
    path = ROOT / "writings/epilogue/chapters/multiscale.md"
    text = path.read_text()
    block = polish_row_179(
        lift_159_to_179(
            extract_between(
                text,
                "### Row 159 closing loop",
                "### Row 158 closing loop",
            )
        )
    )
    start = text.find("### Row 179 closing loop")
    end = text.find("\n### Row 178 closing loop", start)
    if start >= 0 and end > start:
        text = text[:start] + block + text[end:]
        path.write_text(text)
        print("epilogue: rebuilt row 179 closing loop")
    else:
        print("epilogue: skip row 179 loop rebuild")


def fix_prologue_row_179() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    text = path.read_text()
    src = "| Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
    bad_prefix = "| Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion (row 159) |"
    sidx = text.find(src)
    bidx = text.find(bad_prefix)
    if sidx >= 0 and bidx >= 0:
        good = polish_row_179(lift_159_to_179(text[sidx : text.find("\n", sidx)]))
        text = text[:bidx] + good + text[text.find("\n", bidx) :]
    text = re.sub(
        r'\| <span id="prologue-preview-row-159"></span>Row 179 preview.*?\|\n',
        "",
        text,
    )
    if '| <span id="prologue-preview-row-179"></span>' not in text:
        psrc = '| <span id="prologue-preview-row-159"></span>'
        pi = text.find(psrc)
        if pi >= 0:
            pj = text.find("\n|", pi + 1)
            preview = polish_row_179(lift_159_to_179(text[pi:pj])) + "\n"
            text = text.replace(psrc, preview + psrc, 1)
    path.write_text(text)
    print("prologue: polished row 179 compass/preview")


def rebuild_sources_row_179_index() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    idx_key = "row68-row151-handshake3-meta-prelude-capstone-reunion-index-row-179"
    i179 = text.find(idx_key)
    if i179 < 0:
        i179 = text.find("handshake3-meta-prelude-capstone-reunion-index-row-179")
    start178 = "## Row 68 → Row 151 Row 68 → Row 58 DFT workflows meta prelude capstone reunion index (row 178)"
    i178 = text.find(start178)
    if i178 < 0:
        i178 = text.find("row68-row151-dft-workflows-meta-prelude-capstone-reunion-index-row-178")
        i178 = text.rfind("\n## ", 0, i178) if i178 >= 0 else -1
    start159 = "## Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 159)"
    i159 = text.find(start159)
    if i159 < 0:
        print("sources: skip row 179 rebuild (templates missing)")
        return
    j159_end = text.find("\n## Row 68 → Row 138", i159)
    if j159_end < 0:
        j159_end = text.find("\n## Row 68 → Row 119", i159)
    if j159_end < 0:
        j159_end = i178 if i178 > i159 else len(text)
    block = polish_row_179(
        export_index_to_handshake3_179(lift_159_to_179(text[i159:j159_end]))
    ).strip()
    block = block.replace(
        "(row 179) {#row68-row139-handshake3-meta-prelude-capstone-reunion-index-row-159}",
        f"(row 179) {{#{idx_key}}}",
        1,
    )
    if f"(row 179) {{#{idx_key}}}" not in block:
        block = re.sub(
            r"## Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index \(row 179\)(?: \{#[^}]+\})?",
            f"## Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion index (row 179) {{#{idx_key}}}",
            block,
            count=1,
        )
    if i179 >= 0:
        i179 = text.rfind("\n## ", 0, i179)
        j179_end = text.find("\n## Row 68 → Row 151 Row 68 → Row 58", i179)
        if j179_end < 0:
            j179_end = text.find("\n## Row 68 → Row 178", i179)
        if j179_end < 0 and i178 > i179:
            j179_end = i178
        text = text[:i179] + block + "\n\n\n" + text[j179_end:]
    elif i178 >= 0:
        text = text[:i178] + block + "\n\n\n" + text[i178:]
    else:
        corrupt_end = text.find("\n## Row 68 → Row 126", 0)
        if corrupt_end < 0:
            corrupt_end = text.find("## Row 68 → Row 157", 0)
        if corrupt_end < 0:
            raise SystemExit("sources: cannot place row 179 index")
        text = text[:corrupt_end] + block + "\n\n\n" + text[corrupt_end:]
    path.write_text(text)
    print("sources: rebuilt row 179 index")


def rebuild_memory_row_179_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    anchor = "### Row 179 baby picture"
    if anchor not in text:
        print("memory-sheet: row 179 baby missing")
        return
    baby159 = extract_between(
        text,
        "### Row 159 baby picture",
        "### Row 158 baby picture",
    )
    baby = polish_row_179(lift_159_to_179(baby159))
    baby = baby.replace(
        "### Row 179 baby picture (Row 68 → Row 139 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) "
        "{#row-159-baby-picture-row68-row139-handshake3-meta-prelude-capstone-reunion}",
        "### Row 179 baby picture (Row 68 → Row 151 Row 68 → Row 59 Handshake 3 meta prelude capstone reunion) "
        "{#row-179-baby-picture-row68-row151-handshake3-meta-prelude-capstone-reunion}",
        1,
    )
    start = text.find(anchor)
    end = text.find("\n### ", start + 1)
    while end >= 0 and text[start:end].count(anchor) == 0:
        end = text.find("\n### ", end + 1)
    if end < 0:
        end = len(text)
    text = text[:start] + baby + text[end:]
    path.write_text(text)
    print("memory-sheet: rebuilt row 179 baby picture")


def remove_duplicate_corrupted_baby() -> None:
    path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    text = path.read_text()
    marker = "### Row 179 baby picture"
    while text.count(marker) > 1:
        first = text.find(marker)
        second = text.find(marker, first + 1)
        end = text.find("\n### ", second)
        if end < 0:
            end = len(text)
        else:
            end += 1
        text = text[:second] + text[end:]
    path.write_text(text)
    print("memory-sheet: deduped row 179 baby picture")


def patch_row_178_when_complete() -> None:
    path = ROOT / "writings/preface/chapters/preface.md"
    text = path.read_text()
    new = (
        "When row 178 is complete, proceed to [row 179](preface.md#skill-navigation-row-179) "
        "when row 68 closed but Handshake 3 meta prelude capstone still lags after verified "
        "DFT workflows meta prelude capstone on the capstone path, to [row 159](preface.md#skill-navigation-row-159) "
        "when DFT workflows meta prelude capstone is clean but Handshake 3 meta prelude still lags on the "
        "opening-hinge path, to [row 139](preface.md#skill-navigation-row-139) for the Row 68 ↔ "
        "Row 59 Handshake 3 meta audit on the opening-hinge prelude path alone, to "
        "[row 177](preface.md#skill-navigation-row-177) when Kohn–Sham meta prelude capstone still "
        "lags after verified Born–Oppenheimer meta prelude capstone on the capstone path, to "
        "[row 59](preface.md#skill-navigation-row-59) for the IX.3 → Handshake 3 meta audit alone, to "
        "[row 40](preface.md#skill-navigation-row-40) when only the Handshake 3 preview stalls, "
        "or extend prose only under `writings/` then sync."
    )
    if "When row 178 is complete, proceed to [row 179]" not in text:
        text = re.sub(
            r"When row 178 is complete, proceed to.*?or extend prose only under `writings/` then sync\.",
            new,
            text,
            count=1,
            flags=re.S,
        )
        path.write_text(text)
        print("preface: patched row 178 → row 179 proceed")


def strip_corrupt_sources_preamble() -> None:
    path = ROOT / "writings/appendix/chapters/sources.md"
    text = path.read_text()
    marker = "That offset is intentional: the wire heats before it yields."
    end_table = text.find(marker)
    if end_table < 0:
        return
    end_table = text.find("\n", end_table) + 1
    bad = text[end_table : text.find("## Row 68 → Row 151 Row 68 → Row 56", end_table)]
    if "Kohn–Sham meta capstone reunion index (row 179)" in bad or "row68-row151-handshake3" in bad:
        text = text[:end_table] + "\n" + text[text.find("## Row 68 → Row 151 Row 68 → Row 56", end_table) :]
        path.write_text(text)
        print("sources: stripped corrupt preamble block")


def main() -> None:
    remove_duplicate_corrupted_baby()
    strip_corrupt_sources_preamble()
    rebuild_preface_row_179()
    rebuild_epilogue_row_179_loop()
    fix_prologue_row_179()
    rebuild_sources_row_179_index()
    rebuild_memory_row_179_baby()
    patch_row_178_when_complete()


if __name__ == "__main__":
    main()
