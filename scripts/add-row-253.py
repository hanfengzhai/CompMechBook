#!/usr/bin/env python3
"""Add row 253 meta-stitch (Row 68 → Row 233 ↔ Row 53 dynamics meta prelude capstone reunion, full capstone path)."""
from pathlib import Path
import importlib.util
import re

ROOT = Path(__file__).resolve().parents[1]

PRESERVE_ROW_NUMS = {
    20, 32, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 88, 89, 108,
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
        r"index-row-(\d+)",
    ):
        text = re.sub(pat, repl, text)
    return text


def t233_to_253(text: str) -> str:
    protected = (
        ("row-253-", "__P253__"),
        ("skill-navigation-row-253", "__S253__"),
        ("prologue-preview-row-253", "__prologue-preview-row-253__"),
        ("{#row-253-closing-stitch}", "__{#row-253-closing-stitch}__"),
        ("{#row-253-closing-loop}", "__{#row-253-closing-loop}__"),
        (
            "row68-row233-dynamics-meta-prelude-capstone-reunion-index-row-253",
            "__row68-row233-dynamics-meta-prelude-capstone-reunion-index-row-253__",
        ),
        (
            "row-253-baby-picture-row68-row233-dynamics-meta-prelude-capstone-reunion",
            "__row-253-baby-picture-row68-row233-dynamics-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return out


def _load_add233():
    spec = importlib.util.spec_from_file_location("add233", ROOT / "scripts/add-row-233.py")
    add233 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add233)
    return add233


def _compact_memory_baby() -> str:
    template = (
        "### Row 233 baby picture {#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion}\n\n"
        "**Row 233 baby picture:** when row 68 closed the midpoint prelude and row 232 or row 213 closed "
        "atomistic meta prelude capstone / dynamics meta prelude but **row 53's VIII.1 → VIII.2 audit or the "
        "Bridge → ensembles chain still feel like separate checklists on the full capstone path**, "
        "open the [Row 68 → Row 233 dynamics meta prelude capstone reunion index]"
        "(sources.md#row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233) — read "
        "[preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 232]"
        "(../preface.md#skill-navigation-row-232) or [preface row 213]"
        "(../preface.md#skill-navigation-row-213) atomistic meta prelude capstone / dynamics meta prelude gate → "
        "[VIII.1 Bridge](../part08-md/01-potentials-phase-space.md#bridge) through "
        "[VIII.2 opening hinge from VIII.1](../part08-md/02-ensembles-integrators.md#opening-hinge-viii1-to-viii2) "
        "aloud → [preface row 53](../preface.md#skill-navigation-row-53) five-step audit → confirm EAM Lab act "
        "steps 6–7 before NPT decks on the full capstone path.\n"
    )
    return t233_to_253(template) + "\n"


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 233 skill checkpoint")
    end = preface.index("\n\n### Row 234 skill checkpoint", start)
    row253_preface = t233_to_253(preface[start:end]).strip() + "\n\n"

    b233 = _load_add233()._build_blocks()
    epilogue_loop = t233_to_253(b233["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-233-closing-loop}", "{#row-253-closing-loop}", 1)
    for old_header in (
        "### Row 213 closing loop (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
        "### Row 233 closing loop (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
        "### Row 233 closing loop (Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
    ):
        if old_header in epilogue_loop:
            epilogue_loop = epilogue_loop.replace(
                old_header,
                "### Row 253 closing loop (Row 68 → Row 233 Row 68 → Row 53 dynamics meta prelude capstone reunion)",
                1,
            )
            break
    for spill in ("\n\n\n\n### Row 252 closing loop", "\n\n\n\n### Row 253 closing loop"):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src233_header = (
        "## Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 233)"
    )
    next213_header = (
        "## Row 68 → Row 193 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 213)"
    )
    i = sources.index(src233_header)
    j = sources.index(next213_header, i + len(src233_header))
    sources_index = t233_to_253(sources[i:j])
    sources_index = sources_index.replace(
        "(row 233) {#row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233}",
        "(row 253) {#row68-row233-dynamics-meta-prelude-capstone-reunion-index-row-253}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row213-dynamics-meta-prelude-capstone-reunion-index-row-233",
        "row68-row233-dynamics-meta-prelude-capstone-reunion-index-row-253",
    )

    return {
        "row253_preface": row253_preface,
        "prologue_compass": t233_to_253(b233["prologue_compass"]).replace("(row 233)", "(row 253)", 1),
        "prologue_stitch": t233_to_253(b233["prologue_stitch"].strip()) + "\n\n",
        "prologue_preview": t233_to_253(b233["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "sources_table": t233_to_253(b233["sources_table"]).replace("| 233 | Row 68 → Row 213", "| 253 | Row 68 → Row 233", 1),
        "sources_index": sources_index,
        "memory_table": (
            "| 253 | Meta | [Row 68 → Row 233 dynamics meta prelude capstone reunion index]"
            "(sources.md#row68-row233-dynamics-meta-prelude-capstone-reunion-index-row-253) · "
            "[preface row 253 skill checkpoint](../preface.md#skill-navigation-row-253) · "
            "[prologue row 253 preview](../prologue/00-many-scales.md#prologue-preview-row-253) · "
            "[prologue row 253 closing stitch](../prologue/00-many-scales.md#row-253-closing-stitch) · "
            "[epilogue row 253 closing loop](../epilogue/multiscale.md#row-253-closing-loop) | "
            "Row 68 closed but row 53 dynamics meta reunion feels disconnected from verified "
            "atomistic meta prelude capstone on the full capstone path — read row 68 + row 252 or "
            "row 233 gate + VIII.1 Bridge → VIII.2 + row 53; "
            "[row 253 baby picture](#row-253-baby-picture-row68-row233-dynamics-meta-prelude-capstone-reunion) |\n"
        ),
        "memory_baby": _compact_memory_baby(),
    }


ROW253_EPILOGUE_AFTER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)

ROW253_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)

PROLOGUE_STITCH_ANCHORS = (
    "**Row 252 closing stitch (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-252-closing-stitch}",
    "**Row 232 closing stitch (Row 68 → Row 212 Row 68 → Row 52 atomistic meta prelude capstone reunion).** {#row-232-closing-stitch}",
    "**Row 213 closing stitch (Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion).** {#row-233-closing-stitch}",
)

ROW252_STITCH_OLD = "before row 253 dynamics meta prelude capstone reunion opens on the full capstone path."
ROW252_STITCH_NEW = "before row 254 export meta prelude capstone reunion opens on the full capstone path."

ROW252_EPILOGUE_OLD = (
    "Proceed to [row 233](#row-233-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 232 on the full capstone path,"
)
ROW252_EPILOGUE_NEW = (
    "Proceed to [row 253](#row-253-closing-loop) when row 68 closed but dynamics meta prelude capstone still lags after row 252 on the full capstone path,"
)


def _epilogue_has_row253_after_252(text: str) -> bool:
    if ROW253_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(ROW253_EPILOGUE_AFTER)
    window = text[idx : idx + 20000]
    return (
        "{#row-253-closing-loop}" in window
        and "memory sheet row 253" in window
        and "### Row 253 closing loop" in window
    )


def _replace_epilogue_mid(mid: str, loop: str) -> str:
    """Replace any partial row-253 closing loop block with the canonical loop."""
    if "{#row-253-closing-loop}" in mid:
        start = mid.index("### Row ")
        end = mid.index("{#row-253-closing-loop}")
        end = mid.find("\n\n", end)
        if end == -1:
            end = len(mid)
        else:
            end += 2
        return mid[:start] + loop + mid[end:]
    return mid.rstrip() + "\n\n" + loop


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    before_copper = preface.split(copper, 1)[0]
    if "### Row 253 skill checkpoint" in before_copper:
        print("preface: row 253 capstone already present")
    else:
        if "### Row 252 skill checkpoint" not in before_copper:
            raise SystemExit("row 252 must exist before row 253")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row253_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 253")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "dynamics meta prelude capstone reunion (row 253) |" not in prologue:
        needle = (
            "| Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion (row 252) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 252 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 253 closing stitch" not in prologue:
            for anchor in PROLOGUE_STITCH_ANCHORS:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-252"></span>Row 232 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        if '<span id="prologue-preview-row-253">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW252_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW252_STITCH_OLD, ROW252_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 253")
    else:
        print("prologue: row 253 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW252_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW252_EPILOGUE_OLD, ROW252_EPILOGUE_NEW, 1)
        print("epilogue: updated row 252 proceed link")
    if not _epilogue_has_row253_after_252(epilogue):
        if ROW253_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 252 anchor not found")
        if ROW253_EPILOGUE_BEFORE not in epilogue.split(ROW253_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 252")
        head, tail = epilogue.split(ROW253_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(ROW253_EPILOGUE_BEFORE, 1)
        mid = _replace_epilogue_mid(mid, b["epilogue_loop"])
        epilogue_path.write_text(head + ROW253_EPILOGUE_AFTER + mid + ROW253_EPILOGUE_BEFORE + rest)
        print("epilogue: added row 253")
    else:
        print("epilogue: row 253 closing loop already present after row 252")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row233-dynamics-meta-prelude-capstone-reunion-index-row-253" not in sources:
        needle = "| 213 | Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone"
        if needle not in sources:
            needle = "| 233 | Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone"
        if needle not in sources:
            raise SystemExit("sources dynamics table anchor not found")
        sources = sources.replace(needle, b["sources_table"] + needle, 1)
        src233_header = (
            "## Row 68 → Row 213 Row 68 → Row 53 dynamics meta prelude capstone reunion index (row 233)"
        )
        if src233_header in sources and b["sources_index"].strip()[:80] not in sources:
            sources = sources.replace(src233_header, b["sources_index"] + src233_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 253")
    else:
        print("sources: row 253 index already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-253-baby-picture-row68-row233" not in memory:
        if "| 253 | Meta |" not in memory:
            mem252 = "| 252 | Meta | [Row 68 → Row 232 atomistic meta prelude capstone reunion index]"
            if mem252 in memory:
                memory = memory.replace(mem252, b["memory_table"] + mem252, 1)
        baby_anchors = (
            "### Row 252 baby picture {#row-252-baby-picture-row68-row232-atomistic-meta-prelude-capstone-reunion}",
            "### Row 233 baby picture {#row-233-baby-picture-row68-row213-dynamics-meta-prelude-capstone-reunion}",
        )
        baby_anchor = next((a for a in baby_anchors if a in memory), None)
        if not baby_anchor:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 253")
    else:
        print("memory-sheet: row 253 baby already present")


if __name__ == "__main__":
    main()
