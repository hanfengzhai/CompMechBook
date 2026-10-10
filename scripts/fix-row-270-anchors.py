#!/usr/bin/env python3
"""Repair row 230/250/270 DDD meta-stitch anchors in prologue from row 130 canonical base."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 108,
}

REUNION_ANCHORS = {
    230: "row68-row210-ddd-meta-prelude-capstone-reunion-index-row-230",
    250: "row68-row230-ddd-meta-prelude-capstone-reunion-index-row-250",
    270: "row68-row250-ddd-meta-prelude-capstone-reunion-index-row-270",
}

REUNION_MIDDLE = {230: 210, 250: 230, 270: 250}
NEXT_ROW = {230: 231, 250: 251, 270: 271}


def bump_meta_plus20(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        n = int(m.group(1))
        if n in PRESERVE_ROW_NUMS:
            return m.group(0)
        return m.group(0).replace(str(n), str(n + 20))

    for pat in (
        r"(?<![0-9])row (\d+)",
        r"(?<![0-9])Row (\d+)",
        r"skill-navigation-row-(\d+)",
        r"prologue-preview-row-(\d+)",
        r"row-(\d+)-closing",
        r"row-(\d+)-baby-picture",
        r"row68-row(\d+)",
        r"reunion-index-row-(\d+)",
    ):
        text = re.sub(pat, repl, text)
    return text


def bump_to_row(text: str, base_row: int, target_row: int) -> str:
    hops = (target_row - base_row) // 20
    for _ in range(hops):
        text = bump_meta_plus20(text)
    return text


def extract_row130_blocks(prologue: str) -> tuple[str, str]:
    m_st = re.search(
        r"(\*\*Row 130 closing stitch \(Row 68 → Row 110 Row 68 → Row 50 DDD meta prelude capstone reunion\)\.\*\* "
        r"\{#row-130-closing-stitch\}[^\n]+)",
        prologue,
    )
    if not m_st:
        raise SystemExit("row 130 closing stitch not found")
    m_pr = re.search(
        r"(\| <span id=\"prologue-preview-row-130\"></span>Row 130 preview[^\n]+\|)",
        prologue,
    )
    if not m_pr:
        raise SystemExit("row 130 preview not found")
    return m_st.group(1), m_pr.group(1)


def canonical_stitch(prologue: str, target: int) -> str:
    base_st, _ = extract_row130_blocks(prologue)
    text = bump_to_row(base_st, 130, target)
    text = re.sub(
        r"\*\*Row \d+ closing stitch \(Row 68 → Row \d+ Row 68 → Row 50 DDD meta prelude capstone reunion\)\.\*\* "
        rf"\{{#row-\d+-closing-stitch\}}",
        f"**Row {target} closing stitch (Row 68 → Row {REUNION_MIDDLE[target]} Row 68 → Row 50 DDD meta prelude capstone reunion).** "
        f"{{#row-{target}-closing-stitch}}",
        text,
        count=1,
    )
    text = re.sub(
        r"before row \d+ homogenization meta prelude capstone opens[^.]*\.",
        f"before row {NEXT_ROW[target]} homogenization meta prelude capstone reunion opens on the full capstone path.",
        text,
        count=1,
    )
    anchor = REUNION_ANCHORS[target]
    text = re.sub(
        r"row68-row\d+-ddd-meta-prelude-capstone-reunion-index-row-\d+",
        anchor,
        text,
    )
    return text.strip()


def canonical_preview(prologue: str, target: int) -> str:
    _, base_pr = extract_row130_blocks(prologue)
    text = bump_to_row(base_pr, 130, target)
    text = re.sub(
        r'<span id="prologue-preview-row-\d+"></span>Row \d+ preview \(Row 68 → Row \d+ Row 68 → Row 50 DDD meta prelude capstone reunion\)',
        f'<span id="prologue-preview-row-{target}"></span>Row {target} preview (Row 68 → Row {REUNION_MIDDLE[target]} Row 68 → Row 50 DDD meta prelude capstone reunion)',
        text,
        count=1,
    )
    anchor = REUNION_ANCHORS[target]
    text = re.sub(
        r"row68-row\d+-ddd-meta-prelude-capstone-reunion-index-row-\d+",
        anchor,
        text,
    )
    return text.strip()


def replace_stitch(prologue: str, target: int, stitch: str) -> str:
    pattern = (
        rf"\*\*Row {target} closing stitch \(Row 68 → Row \d+ Row 68 → Row 50 DDD meta prelude capstone reunion\)\.\*\* "
        rf"(\{{#row-{target}-closing-stitch\}}[^\n]*\n)*"
    )
    m = re.search(pattern, prologue)
    if m:
        return prologue[: m.start()] + stitch + "\n\n" + prologue[m.end() :]
    anchor = f"{{#row-{target}-closing-stitch}}"
    if anchor in prologue:
        idx = prologue.index(anchor)
        start = prologue.rfind("\n\n**", 0, idx)
        end = prologue.find("\n\n**Row ", idx + 10)
        if start != -1 and end != -1:
            return prologue[: start + 2] + stitch + "\n\n" + prologue[end + 2 :]
    return prologue


def replace_preview(prologue: str, target: int, preview: str) -> str:
    pattern = rf"\| <span id=\"prologue-preview-row-{target}\"></span>Row \d+ preview[^\n]+\|"
    m = re.search(pattern, prologue)
    if m:
        return prologue[: m.start()] + preview + prologue[m.end() :]
    return prologue


def main() -> None:
    path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = path.read_text()
    original = prologue
    for target in (230, 250, 270):
        prologue = replace_stitch(prologue, target, canonical_stitch(original, target))
        prologue = replace_preview(prologue, target, canonical_preview(original, target))
    if prologue != original:
        path.write_text(prologue)
        print("prologue: repaired row 230/250/270 DDD stitches and previews")
    else:
        print("prologue: no DDD stitch repair needed")


if __name__ == "__main__":
    main()
