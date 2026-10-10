#!/usr/bin/env python3
"""Generate add-row-N taxonomy meta-stitch script from add-row-229 template."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "scripts/add-row-229.py"

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
    88, 89, 108,
}


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


def bump229_to(target: int, text: str) -> str:
    times = (target - 229) // 20
    out = text
    for _ in range(times):
        out = bump_meta_plus20(out)
    return out


def gen(target: int) -> str:
    assert target >= 229 and (target - 229) % 20 == 0
    mid = target - 1
    pair = target - 20
    ddd = target + 1
    ddd_pair = target - 19
    tpl = TEMPLATE.read_text()
    out = tpl
    # Protect target tokens while bumping from 229 baseline
    out = out.replace("add-row-229.py", f"add-row-{target}.py")
    out = re.sub(
        r'"""Add row 229 meta-stitch \(Row 68 → Row 209',
        f'"""Add row {target} meta-stitch (Row 68 → Row {pair}',
        out,
        count=1,
    )
    out = out.replace("t209_to_229", f"t229_to_{target}")
    out = out.replace("def t229_to_229", f"def t229_to_{target}")
    out = out.replace("_load_add209", "_load_add229")
    out = out.replace("add209", "add229")
    out = out.replace("scripts/add-row-209.py", "scripts/add-row-229.py")
    out = out.replace("row229_preface", f"row{target}_preface")
    out = bump229_to(target, out)
    # Fix loader / preface slice to use row 229 block as source (post-bump labels)
    out = out.replace(
        f"start = preface.index(\"### Row {pair} skill checkpoint\")",
        'start = preface.index("### Row 229 skill checkpoint")',
        1,
    )
    out = out.replace(
        f"end = preface.index(\"\\n\\n### Row {ddd} skill checkpoint\", start)",
        'end = preface.index("\\n\\n### Row 230 skill checkpoint", start)',
        1,
    )
    out = out.replace("b209 = add229._build_blocks()", "b229 = add229._build_blocks()", 1)
    out = out.replace('b209["', 'b229["')
    # Epilogue loop anchors (229 template strings after bump should be correct)
    # Main(): predecessor midpoint row checks
    out = out.replace(
        f"if \"### Row {mid} skill checkpoint\" not in preface:",
        'if "### Row 248 skill checkpoint" not in preface:' if target == 249 else (
            'if "### Row 268 skill checkpoint" not in preface:' if target == 269 else
            f'if "### Row {mid} skill checkpoint" not in preface:'
        ),
        1,
    )
    out = out.replace(
        f"raise SystemExit(\"row {mid} must exist before row {target}\")",
        f'raise SystemExit("row {mid} must exist before row {target}")',
        1,
    )
    # Prologue compass needle: insert after midpoint capstone row
    if target == 249:
        needle = (
            '| Row 68 → Row 228 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 248) | '
            '[Preface: row 248 skill checkpoint](../preface.md#skill-navigation-row-248)'
        )
        err = "prologue compass row 248 not found"
        stitch_before = "**Row 248 closing stitch"
    else:
        needle = (
            '| Row 68 → Row 248 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 268) | '
            '[Preface: row 268 skill checkpoint](../preface.md#skill-navigation-row-268)'
        )
        err = "prologue compass row 268 not found"
        stitch_before = "**Row 268 closing stitch"
    out = re.sub(
        r'needle = \(\n            "\| Row 68 → Row 208.*?prologue compass row 228 not found"\n        \)',
        f'needle = (\n            "{needle}"\n        )\n        err_msg = "{err}"',
        out,
        flags=re.DOTALL,
        count=1,
    )
    out = out.replace('raise SystemExit("prologue compass row 248 not found")', "raise SystemExit(err_msg)", 1)
    out = out.replace('raise SystemExit("prologue compass row 268 not found")', "raise SystemExit(err_msg)", 1)
    out = out.replace('"**Row 228 closing stitch"', f'"{stitch_before}"', 1)
    out = out.replace(
        'preview_anchor = \'| <span id="prologue-preview-row-209"></span>Row 209 preview\'',
        f'preview_anchor = \'| <span id="prologue-preview-row-{mid}"></span>Row {mid} preview\'',
        1,
    )
    # ROW228 constants -> ROW{mid}
    out = out.replace("ROW228_TAIL_OLD", f"ROW{mid}_TAIL_OLD")
    out = out.replace("ROW228_TAIL_NEW", f"ROW{mid}_TAIL_NEW")
    out = out.replace("ROW228_EPILOGUE_OLD", f"ROW{mid}_EPILOGUE_OLD")
    out = out.replace("ROW228_EPILOGUE_NEW", f"ROW{mid}_EPILOGUE_NEW")
    out = out.replace("ROW228_STITCH_OLD", f"ROW{mid}_STITCH_OLD")
    out = out.replace("ROW228_STITCH_NEW", f"ROW{mid}_STITCH_NEW")
    # Epilogue proceed line uses row 228 -> row mid
    out = out.replace("after row 228 on the full capstone path", f"after row {mid} on the full capstone path")
    out = out.replace("When row 228 is complete", f"When row {mid} is complete")
    # Sources/memory insert before row 229 / 249
    prev_tax = target - 20
    out = out.replace(
        f"| {prev_tax} | Row 68 → Row {prev_tax - 20} Row 68 → Row 49 taxonomy",
        f"| {prev_tax} | Row 68 → Row {prev_tax - 20} Row 68 → Row 49 taxonomy",
    )
    return out


def main() -> None:
    for target in (249, 269):
        path = ROOT / f"scripts/add-row-{target}.py"
        path.write_text(gen(target))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
