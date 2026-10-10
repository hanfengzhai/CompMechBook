#!/usr/bin/env python3
"""Add row 269 meta-stitch (Row 68 → Row 249 ↔ Row 49 taxonomy meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 108,
}


def bump_meta_plus20(text: str) -> str:
    """Shift capstone-path meta row numbers by +20; preserve plot-spine row ids (48, 49, 68, …)."""

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


def t249_to_269(text: str) -> str:
    return bump_meta_plus20(text)


def _load_add249():
    spec = importlib.util.spec_from_file_location("add249", ROOT / "scripts/add-row-249.py")
    add249 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add249)
    return add249


def _build_blocks() -> dict[str, str]:
    add249 = _load_add249()
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 249 skill checkpoint")
    end = preface.index("\n\n## The copper wire through the book", start)
    row269_preface = t249_to_269(preface[start:end]) + "\n\n"

    b249 = add249._build_blocks()
    prologue_stitch = t249_to_269(b249["prologue_stitch"].strip()) + "\n\n"
    prologue_compass = t249_to_269(b249["prologue_compass"])
    prologue_preview = t249_to_269(b249["prologue_preview"])

    epilogue_loop = t249_to_269(b249["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-249-closing-loop}", "{#row-269-closing-loop}", 1)
    epilogue_loop = epilogue_loop.replace(
        "### Row 249 closing loop (Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion)",
        "### Row 269 closing loop (Row 68 → Row 249 Row 68 → Row 49 taxonomy meta prelude capstone reunion)",
        1,
    )

    sources_index = t249_to_269(b249["sources_index"])
    sources_table = t249_to_269(b249["sources_table"]).replace(
        "| 249 | Row 68 → Row 229", "| 269 | Row 68 → Row 249", 1
    )
    memory_table = t249_to_269(b249["memory_table"]).replace("| 249 | Meta |", "| 269 | Meta |", 1)

    memory_baby = t249_to_269(b249["memory_baby"])
    if "{#row-269-baby-picture-row68-row249" not in memory_baby:
        memory_baby = memory_baby.replace(
            "### Row 269 baby picture",
            "### Row 269 baby picture {#row-269-baby-picture-row68-row249-taxonomy-meta-prelude-capstone-reunion}",
            1,
        )

    return {
        "row269_preface": row269_preface,
        "prologue_compass": prologue_compass,
        "prologue_stitch": prologue_stitch,
        "prologue_preview": prologue_preview,
        "epilogue_loop": epilogue_loop,
        "sources_table": sources_table,
        "sources_index": sources_index,
        "memory_baby": memory_baby,
        "memory_table": memory_table,
    }


ROW268_TAIL_OLD = (
    "When row 268 is complete, proceed to [row 269](preface.md#skill-navigation-row-249) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 249](preface.md#skill-navigation-row-229) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 229](preface.md#skill-navigation-row-209) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 148](preface.md#skill-navigation-row-148) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 268](preface.md#skill-navigation-row-268) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 267](preface.md#skill-navigation-row-267) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)
ROW268_TAIL_NEW = (
    "When row 268 is complete, proceed to [row 269](preface.md#skill-navigation-row-269) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the full capstone path, to [row 249](preface.md#skill-navigation-row-249) when midpoint meta prelude capstone is clean but taxonomy meta prelude capstone still lags after verified forest landing on the opening-hinge capstone path alone, to [row 229](preface.md#skill-navigation-row-229) for the Row 68 ↔ Row 49 meta audit on the opening-hinge prelude path alone, to [row 148](preface.md#skill-navigation-row-148) for the Row 68 ↔ Row 48 meta audit on the opening-hinge prelude path alone, to [row 268](preface.md#skill-navigation-row-268) for the Row 68 ↔ Row 48 meta audit on the opening-hinge capstone path alone, to [row 267](preface.md#skill-navigation-row-267) when part-boundary meta prelude capstone still lags after verified Writings canonical meta prelude capstone on the full capstone path, to [row 88](preface.md#skill-navigation-row-88) for the Row 68 ↔ Row 48 opening prelude audit alone, to [row 48](preface.md#skill-navigation-row-48) for the VI.4 → VII.0 meta audit alone, to [row 32](preface.md#skill-navigation-row-32) when only the plasticity preview stalls, or extend prose only under `writings/` then sync."
)

ROW268_EPILOGUE_OLD = (
    "Proceed to [row 269](#row-249-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 268 on the full capstone path,"
)
ROW268_EPILOGUE_NEW = (
    "Proceed to [row 269](#row-269-closing-loop) when row 68 closed but taxonomy meta prelude capstone still lags after row 268 on the full capstone path,"
)

ROW268_STITCH_OLD = (
    "before row 269 taxonomy meta prelude capstone reunion opens on the full capstone path."
)
ROW268_STITCH_NEW = (
    "before row 270 DDD meta prelude capstone reunion opens on the full capstone path."
)


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    if "### Row 269 skill checkpoint" in preface:
        print("preface: row 269 already present")
    else:
        if "### Row 249 skill checkpoint" not in preface:
            raise SystemExit("row 249 must exist before row 269")
        if ROW268_TAIL_OLD in preface:
            preface = preface.replace(ROW268_TAIL_OLD, ROW268_TAIL_NEW, 1)
        elif "skill-navigation-row-249) when midpoint meta prelude capstone is clean but taxonomy" in preface:
            preface = preface.replace(
                "[row 269](preface.md#skill-navigation-row-249)",
                "[row 269](preface.md#skill-navigation-row-269)",
                1,
            )
        preface = preface.replace(copper, "\n" + b["row269_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 269")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "prologue-preview-row-269" not in prologue:
        needle = (
            "| Row 68 → Row 248 Row 68 → Row 48 midpoint meta prelude capstone reunion (row 268) | "
            "[Preface: row 268 skill checkpoint](../preface.md#skill-navigation-row-268)"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 268 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 269 closing stitch" not in prologue:
            prologue = prologue.replace(
                "**Row 268 closing stitch",
                b["prologue_stitch"] + "**Row 268 closing stitch",
                1,
            )
        preview_anchor = '| <span id="prologue-preview-row-268"></span>Row 268 preview'
        if preview_anchor in prologue and '<span id="prologue-preview-row-269">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"].strip() + "\n" + preview_anchor, 1)
        if ROW268_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW268_STITCH_OLD, ROW268_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 269")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if "{#row-269-closing-loop}" not in epilogue or "### Row 269 closing loop" not in epilogue:
        if ROW268_EPILOGUE_OLD in epilogue:
            epilogue = epilogue.replace(ROW268_EPILOGUE_OLD, ROW268_EPILOGUE_NEW, 1)
        marker = (
            "### Row 249 closing loop (Row 68 → Row 229 Row 68 → Row 49 "
            "taxonomy meta prelude capstone reunion) {#row-249-closing-loop}"
        )
        if marker not in epilogue:
            raise SystemExit("epilogue row 249 insert anchor not found")
        if "### Row 269 closing loop" not in epilogue:
            epilogue = epilogue.replace(marker, b["epilogue_loop"] + "\n\n" + marker, 1)
        epilogue_path.write_text(epilogue)
        print("epilogue: added row 269")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row249-taxonomy-meta-prelude-capstone-reunion-index-row-269" not in sources:
        sources = sources.replace(
            "| 249 | Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone",
            b["sources_table"] + "| 249 | Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone",
            1,
        )
        src249_header = (
            "## Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 249) "
            "{#row68-row229-taxonomy-meta-prelude-capstone-reunion-index-row-249}"
        )
        if src249_header not in sources:
            src249_header = (
                "## Row 68 → Row 229 Row 68 → Row 49 taxonomy meta prelude capstone reunion index (row 249)"
            )
        sources = sources.replace(src249_header, b["sources_index"] + src249_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 269")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-269-baby-picture-row68-row249" not in memory:
        memory = memory.replace(
            "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]",
            b["memory_table"] + "| 249 | Meta | [Row 68 → Row 229 taxonomy meta prelude capstone reunion index]",
            1,
        )
        inserted = False
        for baby_anchor in (
            "### Row 247 baby picture {#row-247-baby-picture-row68-row227-part-boundary-meta-prelude-capstone-reunion}",
            "### Row 268 baby picture {#row-268-baby-picture-row68-row228-midpoint-meta-prelude-capstone-reunion}",
            "### Row 249 baby picture {#row-249-baby-picture-row68-row229-taxonomy-meta-prelude-capstone-reunion}",
        ):
            if baby_anchor in memory:
                memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
                inserted = True
                break
        if not inserted:
            raise SystemExit("memory baby picture anchor not found")
        memory_path.write_text(memory)
        print("memory-sheet: added row 269")


if __name__ == "__main__":
    main()
