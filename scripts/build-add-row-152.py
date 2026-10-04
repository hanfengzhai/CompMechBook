#!/usr/bin/env python3
"""Generate scripts/add-row-152.py from add-row-151.py (atomistic capstone row 152)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "scripts/add-row-151.py"
DST = ROOT / "scripts/add-row-152.py"

# Reuse atomistic narrative transform from build-add-row-132
from importlib.util import spec_from_loader, module_from_spec
import importlib.machinery

loader = importlib.machinery.SourceFileLoader("b132", str(ROOT / "scripts/build-add-row-132.py"))
mod = module_from_spec(spec_from_loader("b132", loader))
loader.exec_module(mod)
transform = mod.transform


def main() -> None:
    src = SRC.read_text()
    lift_112 = '''def lift_112_to_132(s: str) -> str:
    """Promote opening-hinge row 112 sources index to capstone row 132 wording."""
    p = [
        (
            "Row 68 → Row 92 Row 68 → Row 52 atomistic meta prelude reunion",
            "Row 68 → Row 112 Row 68 → Row 52 atomistic meta prelude capstone reunion",
        ),
        (
            "row68-row92-atomistic-meta-prelude-reunion-index-row-112",
            "row68-row112-atomistic-meta-prelude-capstone-reunion-index-row-132",
        ),
        (
            "row-112-baby-picture-row68-row92-atomistic-meta-prelude-reunion",
            "row-132-baby-picture-row68-row112-atomistic-meta-prelude-capstone-reunion",
        ),
        ("Row 112 names", "Row 132 names"),
        ("(row 112)", "(row 132)"),
        ("skill-navigation-row-112", "skill-navigation-row-132"),
        ("[row 111]", "__R111__"),
        ("row 111", "row 131"),
        ("Row 111", "Row 131"),
        ("__R111__", "[row 131]"),
    ]
    return tx(s, p)
'''

    lift_fn = re.search(
        r"(def lift_131_to_151\(s: str\) -> str:.*?)\n\n\ndef add_row_151",
        src,
        re.S,
    ).group(1)
    lift_fn = transform(lift_fn)
    lift_fn = lift_fn.replace("def lift_131_to_151", "def lift_132_to_152")
    bump = [
        ("skill-navigation-row-151", "skill-navigation-row-152"),
        ("### Row 151 skill checkpoint", "### Row 152 skill checkpoint"),
        ("Row 151 does not replace", "Row 152 does not replace"),
        ("Row 151 three-way audit", "Row 152 three-way audit"),
        ("Row 151 closing loop", "Row 152 closing loop"),
        ("row-151-closing-loop", "row-152-closing-loop"),
        ("Row 151 closing stitch", "Row 152 closing stitch"),
        ("row-151-closing-stitch", "row-152-closing-stitch"),
        ("prologue-preview-row-151", "prologue-preview-row-152"),
        ("Row 151 preview", "Row 152 preview"),
        ("Row 151 skill checkpoint", "Row 152 skill checkpoint"),
        ("memory sheet row 151", "memory sheet row 152"),
        ("Row 151 baby picture", "Row 152 baby picture"),
        (
            "Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone",
            "Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone",
        ),
        (
            "Row 68 → Row 131 Row 68 → Row 52 atomistic meta prelude capstone",
            "Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone",
        ),
        (
            "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
            "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
        ),
        (
            "row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion",
            "row-152-baby-picture-row68-row132-atomistic-meta-prelude-capstone-reunion",
        ),
        ("[row 132]", "__R133__"),
        ("[row 131]", "[row 151]"),
        ("row 131", "row 151"),
        ("Row 131", "Row 151"),
        ("__R133__", "[row 133]"),
        ("[row 111]", "[row 132]"),
        ("row 111", "row 132"),
        ("Row 111", "Row 132"),
        (
            "verified DDD meta prelude capstone closure (row 150)",
            "verified homogenization meta prelude capstone closure (row 151)",
        ),
        ("when row 150 closed but row 51", "when row 151 closed but row 52"),
        ("when row 150 and row 51", "when row 151 and row 52"),
        (
            "rear-view mirror of row 150's Peach–Köhler → spool turn",
            "rear-view mirror of row 151's polycrystal → atomic ink turn",
        ),
        (
            "when opening [row 151](preface.md#skill-navigation-row-151) before row 52 closes",
            "when opening [row 152](preface.md#skill-navigation-row-152) before row 53 closes",
        ),
        (
            "When row 51 feels like DAMASK homework after row 150 alone",
            "When row 52 feels like LAMMPS homework after row 151 alone",
        ),
        (
            "row 151 (row 68 ↔ row 51 reunion on the capstone path) with row 131",
            "row 152 (row 68 ↔ row 52 reunion on the capstone path) with row 132",
        ),
        (
            "row 151 names **why that reunion must follow verified DDD meta prelude capstone (row 150)",
            "row 152 names **why that reunion must follow verified homogenization meta prelude capstone (row 151)",
        ),
        ("Row 68 → Row 51 meta (row 131)", "Row 68 → Row 52 meta (row 132)"),
        ("Row 68 → Row 131 reunion index", "Row 68 → Row 132 reunion index"),
        ("(row 151)", "(row 152)"),
        ("Row 151 closes the", "Row 152 closes the"),
        ("| 151 |", "| 152 |"),
        (
            "Proceed to [row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 150",
            "Proceed to [row 152](#row-152-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 151, "
            "to [row 132](#row-132-closing-loop) when row 68 closed but atomistic meta prelude still lags on the opening-hinge path",
        ),
    ]
    for a, b in bump:
        lift_fn = lift_fn.replace(a, b)

    main_fn = src.split("def add_row_151() -> None:")[1]
    main_fn = "def add_row_152() -> None:" + transform(main_fn)
    main_fn = main_fn.replace("add_row_151()", "add_row_152()")
    main_fn = main_fn.replace("lift_131_to_151", "lift_132_to_152")
    main_fn = main_fn.replace("lift_111_to_131", "lift_112_to_132")
    subs = [
        ("row 151 already present", "row 152 already present"),
        ("added row 151", "added row 152"),
        ("row 131 preface checkpoint missing", "row 132 preface checkpoint missing"),
        (
            r"(### Row 131 skill checkpoint.*?)(?=\n### Row 132 skill checkpoint)",
            r"(### Row 132 skill checkpoint.*?)(?=\n### Row 133 skill checkpoint)",
        ),
        ("m131 = re.search", "m132 = re.search"),
        ("if not m131:", "if not m132:"),
        ("m131.group(1)", "m132.group(1)"),
        ("row151 =", "row152 ="),
        ("+ row151 +", "+ row152 +"),
        ('if "skill-navigation-row-151"', 'if "skill-navigation-row-152"'),
        ('"### Row 151 skill checkpoint"', '"### Row 152 skill checkpoint"'),
        ("row-151-closing-loop", "row-152-closing-loop"),
        ("### Row 131 closing loop", "### Row 132 closing loop"),
        ("block131 =", "block132 ="),
        ("block151 =", "block152 ="),
        ("block151 +", "block152 +"),
        ("### Row 150 closing loop", "### Row 151 closing loop"),
        (
            "| Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion (row 151) |",
            "| Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 152) |",
        ),
        ("prologue compass row 150 not found", "prologue compass row 151 not found"),
        ("line150 =", "line151 ="),
        ("idx150 =", "idx151 ="),
        ("line_end150 =", "line_end151 ="),
        ("line131 =", "line132 ="),
        ("idx131 =", "idx132 ="),
        ("line_end131 =", "line_end132 ="),
        ("compass151 =", "compass152 ="),
        ("compass151 +", "compass152 +"),
        ("preview131 =", "preview132 ="),
        ("preview151 =", "preview152 ="),
        ("preview151 +", "preview152 +"),
        ('prologue-preview-row-131"', 'prologue-preview-row-132"'),
        ('prologue-preview-row-130"', 'prologue-preview-row-151"'),
        ("row-151-closing-stitch", "row-152-closing-stitch"),
        ("Row 151 closing stitch (Row 68 → Row 131", "Row 152 closing stitch (Row 68 → Row 132 Row 68 → Row 52 atomistic"),
        ("**Row 150 closing stitch", "**Row 151 closing stitch"),
        ("row 151 compass", "row 152 compass"),
        (
            "row68-row131-homogenization-meta-prelude-capstone-reunion-index-row-151",
            "row68-row132-atomistic-meta-prelude-capstone-reunion-index-row-152",
        ),
        (
            "## Row 68 → Row 91 Row 68 → Row 51 homogenization meta prelude reunion index (row 111)",
            "## Row 68 → Row 92 Row 68 → Row 52 atomistic meta prelude reunion index (row 112)",
        ),
        ("block111 =", "block112 ="),
        (
            "## Row 68 → Row 130 Row 68 → Row 50 DDD meta prelude capstone reunion index (row 150)",
            "## Row 68 → Row 131 Row 68 → Row 51 homogenization meta prelude capstone reunion index (row 151)",
        ),
        ("| 151 | Row 68 → Row 131", "| 152 | Row 68 → Row 132 Row 68 → Row 52 atomistic meta prelude capstone"),
        ('table_row + "| 150 |', 'table_row + "| 151 |'),
        ("sources: added row 151", "sources: added row 152"),
        ("row-151-baby-picture", "row-152-baby-picture"),
        (
            'baby131 = extract_between(mem, "### Row 131 baby picture", "### Row 132 baby picture")',
            'baby132 = extract_between(mem, "### Row 132 baby picture", "### Row 133 baby picture")',
        ),
        ("baby151 =", "baby152 ="),
        ('baby151 + "### Row 131 baby picture"', 'baby152 + "### Row 132 baby picture"'),
        ("| 151 | Meta |", "| 152 | Meta |"),
        ('mem_table + "| 150 | Meta |', 'mem_table + "| 151 | Meta |'),
        ("memory-sheet: added row 151", "memory-sheet: added row 152"),
        ("row 150 → row 151 proceed", "row 151 → row 152 proceed"),
        (
            "Proceed to [row 151](#row-151-closing-loop) when row 68 closed but homogenization meta prelude capstone still lags after row 150",
            "Proceed to [row 152](#row-152-closing-loop) when row 68 closed but atomistic meta prelude capstone still lags after row 151",
        ),
        ("row 150 → row 151 memory", "row 151 → row 152 memory"),
        ("row-150-baby-picture-row68-row130", "row-151-baby-picture-row68-row131-homogenization-meta-prelude-capstone-reunion"),
        ("skill-navigation-row-151) before row 52", "skill-navigation-row-152) before row 53"),
        ("row 150 proceed → row 151", "row 151 proceed → row 152"),
        (
            "When row 150 is complete, proceed to [row 151]",
            "When row 151 is complete, proceed to [row 152]",
        ),
        (
            "homogenization meta prelude capstone still lags after verified DDD meta prelude capstone on the capstone path",
            "atomistic meta prelude capstone still lags after verified homogenization meta prelude capstone on the capstone path",
        ),
    ]
    for a, b in subs:
        main_fn = main_fn.replace(a, b)

    header = '''#!/usr/bin/env python3
"""Add row 152 (Row 68 → Row 132 ↔ Row 52 atomistic meta prelude capstone on capstone path)."""
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


'''
    helpers = src.split("def lift_111_to_131")[0].split("def extract_between")[1]
    helpers = "def extract_between" + helpers.split("def tx")[0]  # noqa - unused

    out = header + lift_112 + "\n\n" + lift_fn + "\n\n" + main_fn
    if "def main():" not in out:
        out += "\n\ndef main() -> None:\n    add_row_152()\n\n\nif __name__ == \"__main__\":\n    main()\n"
    else:
        out = out.replace("add_row_151()", "add_row_152()")

    DST.write_text(out)
    print(f"Wrote {DST}")


if __name__ == "__main__":
    main()
