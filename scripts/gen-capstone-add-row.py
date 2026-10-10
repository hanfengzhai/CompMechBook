#!/usr/bin/env python3
"""Generate add-row-(base+20).py from add-row-{base}.py capstone template (add-row-248 style)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def gen_from_248_style(base: int) -> str:
    cap = base + 20
    src = (ROOT / "scripts/add-row-248.py").read_text()
    # 248 template bumps 228 -> 248; generalize to base -> cap
    pairs = [
        ("248", str(cap)),
        ("228", str(base)),
        ("247", str(cap - 1)),
        ("227", str(base - 1)),
        ("249", str(cap + 1)),
        ("229", str(base + 1)),
        ("midpoint meta prelude capstone", "__THEME__"),
    ]
    out = src
    for a, b in pairs:
        out = out.replace(a, b)
    # Fix theme: row 258 uses DFT from 238; 256 BO from 236; etc.
    return out


def gen_from_247_style(base: int) -> str:
    cap = base + 20
    src = (ROOT / "scripts/add-row-247.py").read_text()
    pairs = [
        ("247", str(cap)),
        ("227", str(base)),
        ("246", str(cap - 1)),
        ("226", str(base - 1)),
        ("248", str(cap + 1)),
        ("228", str(base + 1)),
    ]
    out = src
    for a, b in pairs:
        out = out.replace(a, b)
    return out


def gen_from_237_style() -> str:
    """Row 257 from add-row-237 (Kohn-Sham capstone)."""
    src = (ROOT / "scripts/add-row-237.py").read_text()
    repl = [
        ("237", "257"),
        ("217", "237"),
        ("236", "256"),
        ("216", "236"),
        ("238", "258"),
        ("218", "238"),
        ("bump217_to_237", "bump237_to_257"),
        ("_load_add217", "_load_add237"),
        ("add217", "add237"),
        ("add-row-217.py", "add-row-237.py"),
        ("row237_preface", "row257_preface"),
        ("Row 217 skill checkpoint", "Row 237 skill checkpoint"),
        ("Row 218 skill checkpoint", "Row 238 skill checkpoint"),
        ("Kohn–Sham meta prelude capstone reunion (row 237)", "Kohn–Sham meta prelude capstone reunion (row 257)"),
        ("row68-row217-kohn-sham-meta-prelude-capstone-reunion-index-row-237", "row68-row237-kohn-sham-meta-prelude-capstone-reunion-index-row-257"),
        ("row-237-baby-picture-row68-row217", "row-257-baby-picture-row68-row237"),
        ("Row 68 → Row 217 Row 68 → Row 57", "Row 68 → Row 237 Row 68 → Row 57"),
        ("Row 68 → Row 197", "Row 68 → Row 217"),
        ("row 197", "row 217"),
        ("Row 197", "Row 217"),
        ("row 178 DFT", "row 258 DFT"),
        ("row 239 Handshake", "row 259 Handshake"),
        ("before row 238 DFT", "before row 258 DFT"),
        ("prologue-preview-row-236", "prologue-preview-row-256"),
        ("Row 236 preview", "Row 256 preview"),
        ("Row 236 closing stitch", "Row 256 closing stitch"),
        ("row-236-closing-stitch", "row-256-closing-stitch"),
        ("Row 68 → Row 216 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 236)", "Row 68 → Row 236 Row 68 → Row 56 Born–Oppenheimer meta prelude capstone reunion (row 256)"),
        ("row-236-closing-loop", "row-256-closing-loop"),
        ("Row 216 closing loop", "Row 236 closing loop"),
        ("row 236 on the full", "row 256 on the full"),
        ("row 217 on the full", "row 237 on the full"),
        ("#row-217-closing-loop", "#row-237-closing-loop"),
        ("#row-238-closing-loop", "#row-258-closing-loop"),
        ("row 218 on the full", "row 238 on the full"),
        ("Add row 237 meta-stitch", "Add row 257 meta-stitch"),
        ("Row 68 → Row 217 ↔ Row 57", "Row 68 → Row 237 ↔ Row 57"),
    ]
    out = src
    for a, b in repl:
        out = out.replace(a, b)
    # Protected bump tags
    out = out.replace("__P257__", "__P257__").replace(
        '("row-257-", "__P257__")',
        '("row-257-", "__P257__")',
    )
    out = re.sub(
        r'def bump237_to_257\(text: str\) -> str:\n    protected = \(\n        \("row-237-"',
        'def bump237_to_257(text: str) -> str:\n    protected = (\n        ("row-257-"',
        out,
        count=1,
    )
    # Fix protected block in bump function - replace 237 with 257 in protected tuple
    out = out.replace('("row-237-", "__P237__")', '("row-257-", "__P257__")')
    out = out.replace('("skill-navigation-row-237", "__S237__")', '("skill-navigation-row-257", "__S257__")')
    out = out.replace('("prologue-preview-row-237", "__PR237__")', '("prologue-preview-row-257", "__PR257__")')
    out = out.replace('("{#row-237-closing-stitch}", "__ST237__")', '("{#row-257-closing-stitch}", "__ST257__")')
    out = out.replace('("{#row-237-closing-loop}", "__LP237__")', '("{#row-257-closing-loop}", "__LP257__")')
    out = out.replace("### Row 237 skill checkpoint", "### Row 257 skill checkpoint", 1)
    out = out.replace("### Row 237 skill checkpoint", "### Row 237 skill checkpoint")  # keep source read
    # main() checks
    out = out.replace('if "### Row 237 skill checkpoint" in preface:', 'if "### Row 257 skill checkpoint" in preface:')
    out = out.replace('if "### Row 236 skill checkpoint" not in preface:', 'if "### Row 256 skill checkpoint" not in preface:')
    out = out.replace('raise SystemExit("row 236 must exist before row 237")', 'raise SystemExit("row 256 must exist before row 257")')
    out = out.replace('print("preface: added row 237")', 'print("preface: added row 257")')
    out = out.replace('print("preface: row 237 already present")', 'print("preface: row 257 already present")')
    out = out.replace('"row237_preface"', '"row257_preface"')
    out = out.replace('b["row237_preface"]', 'b["row257_preface"]')
    out = out.replace('if "### Row 237 closing loop" in epilogue:', 'if "### Row 257 closing loop" in epilogue:')
    out = out.replace("_insert_row237_epilogue", "_insert_row257_epilogue")
    out = out.replace("epilogue: added row 237", "epilogue: added row 257")
    out = out.replace('print("prologue: added row 237")', 'print("prologue: added row 257")')
    out = out.replace('Kohn–Sham meta prelude capstone reunion (row 237) |', 'Kohn–Sham meta prelude capstone reunion (row 257) |')
    out = out.replace('PROLOGUE_STITCH_ANCHOR = (\n    "**Row 236 closing stitch', 'PROLOGUE_STITCH_ANCHOR = (\n    "**Row 256 closing stitch')
    out = out.replace('{#row-236-closing-stitch}', '{#row-256-closing-stitch}')
    out = out.replace("_insert_row237_epilogue(epilogue, b[\"epilogue_loop\"])", "_insert_row257_epilogue(epilogue, b[\"epilogue_loop\"])")
    return out


def gen_from_238_style() -> str:
    """Row 258 from add-row-238 (DFT workflows capstone)."""
    src = (ROOT / "scripts/add-row-238.py").read_text()
    repl = [
        ("238", "258"),
        ("218", "238"),
        ("237", "257"),
        ("217", "237"),
        ("239", "259"),
        ("219", "239"),
        ("bump218_to_238", "bump238_to_258"),
        ("_load_add218", "_load_add238"),
        ("add218", "add238"),
        ("add-row-218.py", "add-row-238.py"),
        ("row238_preface", "row258_preface"),
        ("Row 218 skill checkpoint", "Row 238 skill checkpoint"),
        ("Row 219 skill checkpoint", "Row 239 skill checkpoint"),
        ("DFT workflows meta prelude capstone reunion (row 238)", "DFT workflows meta prelude capstone reunion (row 258)"),
        ("row68-row218-dft-workflows-meta-prelude-capstone-reunion-index-row-238", "row68-row238-dft-workflows-meta-prelude-capstone-reunion-index-row-258"),
        ("row-238-baby-picture-row68-row218", "row-258-baby-picture-row68-row238"),
        ("Row 68 → Row 218 Row 68 → Row 58", "Row 68 → Row 238 Row 68 → Row 58"),
        ("Row 68 → Row 198", "Row 68 → Row 218"),
        ("Add row 238 meta-stitch", "Add row 258 meta-stitch"),
        ("Row 68 → Row 218 ↔ Row 58", "Row 68 → Row 238 ↔ Row 58"),
        ("before row 239 Handshake", "before row 259 Handshake"),
        ("Row 68 → Row 217 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 237)", "Row 68 → Row 237 Row 68 → Row 57 Kohn–Sham meta prelude capstone reunion (row 257)"),
        ("row-237-closing-stitch", "row-257-closing-stitch"),
        ("Row 237 closing stitch", "Row 257 closing stitch"),
        ("Row 237 preview", "Row 257 preview"),
        ("prologue-preview-row-237", "prologue-preview-row-257"),
        ("Row 217 closing loop", "Row 237 closing loop"),
        ("row-237-closing-loop", "row-257-closing-loop"),
        ("row 237 on the full", "row 257 on the full"),
        ("row 217 on the full", "row 237 on the full"),
    ]
    out = src
    for a, b in repl:
        out = out.replace(a, b)
    out = out.replace('("row-258-", "__P258__")', '("row-258-", "__P258__")')
    out = out.replace('if "### Row 238 skill checkpoint" in preface:', 'if "### Row 258 skill checkpoint" in preface:')
    out = out.replace('if "### Row 237 skill checkpoint" not in preface:', 'if "### Row 257 skill checkpoint" not in preface:')
    out = out.replace('raise SystemExit("row 237 must exist before row 238")', 'raise SystemExit("row 257 must exist before row 258")')
    out = out.replace('print("preface: added row 238")', 'print("preface: added row 258")')
    out = out.replace('b["row238_preface"]', 'b["row258_preface"]')
    out = out.replace("_insert_row238_epilogue", "_insert_row258_epilogue")
    out = out.replace('if "### Row 238 closing loop" in epilogue:', 'if "### Row 258 closing loop" in epilogue:')
    # bump protected
    out = out.replace('("row-238-", "__P238__")', '("row-258-", "__P258__")')
    out = out.replace('("skill-navigation-row-238", "__S238__")', '("skill-navigation-row-258", "__S258__")')
    out = out.replace('("prologue-preview-row-238", "__PR238__")', '("prologue-preview-row-258", "__PR258__")')
    out = out.replace('("{#row-238-closing-stitch}", "__ST238__")', '("{#row-258-closing-stitch}", "__ST258__")')
    out = out.replace('("{#row-238-closing-loop}", "__LP238__")', '("{#row-258-closing-loop}", "__LP258__")')
    return out


def main() -> None:
    targets = sys.argv[1:] or ["255", "256", "257", "258"]
    for t in targets:
        n = int(t)
        base = n - 20
        if n == 257:
            text = gen_from_237_style()
        elif n == 258:
            text = gen_from_238_style()
        elif n % 20 == 0 and (ROOT / f"scripts/add-row-{base}.py").exists():
            # Use 247-style for odd capstones in 245-248 band; 248-style for even
            if n in (246, 248, 256, 258):
                text = gen_from_248_style(base)
            else:
                text = gen_from_247_style(base)
        else:
            raise SystemExit(f"unsupported target row {n}")
        path = ROOT / f"scripts/add-row-{n}.py"
        path.write_text(text)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
