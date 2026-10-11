#!/usr/bin/env python3
"""Add row 255 meta-stitch (Row 68 → Row 235 ↔ Row 55 electronic audit meta prelude capstone reunion, full capstone path)."""
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


def fix_capstone_anchor_overbump(text: str) -> str:
    """Undo accidental +20 on capstone reunion anchors (255/256 → 275/276)."""
    return (
        text.replace("reunion-index-row-276", "reunion-index-row-256")
        .replace("reunion-index-row-275", "reunion-index-row-255")
        .replace("skill-navigation-row-275", "skill-navigation-row-255")
        .replace("prologue-preview-row-275", "prologue-preview-row-255")
        .replace("row-275-closing-stitch", "row-255-closing-stitch")
        .replace("row-275-closing-loop", "row-255-closing-loop")
        .replace("prologue-preview-row-276", "prologue-preview-row-256")
        .replace("row-276-closing-stitch", "row-256-closing-stitch")
        .replace("row-276-closing-loop", "row-256-closing-loop")
        .replace("skill-navigation-row-276", "skill-navigation-row-256")
    )


def t235_to_255(text: str) -> str:
    protected = (
        ("row-255-", "__P255__"),
        ("skill-navigation-row-255", "__S255__"),
        ("prologue-preview-row-255", "__prologue-preview-row-255__"),
        ("{#row-255-closing-stitch}", "__{#row-255-closing-stitch}__"),
        ("{#row-255-closing-loop}", "__{#row-255-closing-loop}__"),
        (
            "row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255",
            "__row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255__",
        ),
        (
            "row-255-baby-picture-row68-row235-electronic-audit-meta-prelude-capstone-reunion",
            "__row-255-baby-picture-row68-row235-electronic-audit-meta-prelude-capstone-reunion__",
        ),
    )
    out = text
    for old, new in protected:
        out = out.replace(old, new)
    out = bump_meta_plus20(out)
    for old, new in protected:
        out = out.replace(new, old)
    return fix_capstone_anchor_overbump(out)


def _load_add235():
    spec = importlib.util.spec_from_file_location("add235", ROOT / "scripts/add-row-235.py")
    add235 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add235)
    return add235


def _load_add253():
    spec = importlib.util.spec_from_file_location("add253", ROOT / "scripts/add-row-253.py")
    add253 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add253)
    return add253


def _load_add254():
    spec = importlib.util.spec_from_file_location("add254", ROOT / "scripts/add-row-254.py")
    add254 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add254)
    return add254


def _compact_memory_baby() -> str:
    template = (
        "### Row 235 baby picture {#row-235-baby-picture-row68-row215-electronic-audit-meta-prelude-capstone-reunion}\n\n"
        "**Row 235 baby picture:** when row 68 closed the midpoint prelude and row 254 or row 215 closed "
        "export meta prelude capstone / electronic audit meta prelude but **row 55's VIII.3 → IX.0 audit or the "
        "Bridge → SCF chain still feel like separate checklists on the full capstone path**, "
        "open the [Row 68 → Row 235 electronic audit meta prelude capstone reunion index]"
        "(sources.md#row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235) — read "
        "[preface row 68](../preface.md#skill-navigation-row-68) gate → [preface row 254]"
        "(../preface.md#skill-navigation-row-254) or [preface row 215]"
        "(../preface.md#skill-navigation-row-215) export meta prelude capstone / electronic audit meta prelude gate → "
        "[VIII.3 Bridge → opening hinge → IX.0 SCF audit](../part08-md/03-ab-initio-and-coarse-graining.md#bridge-to-part-ix) through "
        "[IX.0 opening hinge from VIII.3](../part09-dft/00-opening.md#opening-hinge-viii3-to-ix) "
        "aloud → [preface row 55](../preface.md#skill-navigation-row-55) five-step audit → confirm EAM-fit audit Lab act "
        "steps 1–6 before foundation SCF on the full capstone path.\n"
    )
    return t235_to_255(template) + "\n"


def _build_blocks() -> dict[str, str]:
    preface = (ROOT / "writings/preface/chapters/preface.md").read_text()
    start = preface.index("### Row 235 skill checkpoint")
    end = preface.index("\n\n### Row 236 skill checkpoint", start)
    row255_preface = t235_to_255(preface[start:end]).strip() + "\n\n"

    b235 = _load_add235()._build_blocks()
    epilogue_loop = t235_to_255(b235["epilogue_loop"])
    epilogue_loop = epilogue_loop.replace("{#row-235-closing-loop}", "{#row-255-closing-loop}", 1)
    for old_header in (
        "### Row 215 closing loop (Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        "### Row 235 closing loop (Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
        "### Row 235 closing loop (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
    ):
        if old_header in epilogue_loop:
            epilogue_loop = epilogue_loop.replace(
                old_header,
                "### Row 255 closing loop (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
                1,
            )
            break
    for spill in (
        "\n\n\n\n### Row 256 closing loop",
        "\n\n\n\n### Row 236 closing loop",
        "\n\n\n\n### Row 255 closing loop",
    ):
        if spill in epilogue_loop:
            epilogue_loop = epilogue_loop.split(spill, 1)[0].rstrip() + "\n\n"
            break

    sources = (ROOT / "writings/appendix/chapters/sources.md").read_text()
    src235_header = (
        "## Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 235)"
    )
    next215_header = (
        "## Row 68 → Row 195 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 215)"
    )
    i = sources.index(src235_header)
    j = sources.index(next215_header, i + len(src235_header))
    sources_index = t235_to_255(sources[i:j])
    sources_index = sources_index.replace(
        "(row 235) {#row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235}",
        "(row 255) {#row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255}",
        1,
    )
    sources_index = sources_index.replace(
        "row68-row215-electronic-audit-meta-prelude-capstone-reunion-index-row-235",
        "row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255",
    )
    sources_index = re.sub(
        r"\s*\{#row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255\}\s*"
        r"\{#row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255\}",
        " {#row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255}",
        sources_index,
        count=1,
    )

    return {
        "row255_preface": row255_preface,
        "prologue_compass": t235_to_255(b235["prologue_compass"]).replace("(row 235)", "(row 255)", 1),
        "prologue_stitch": t235_to_255(b235["prologue_stitch"].strip()) + "\n\n",
        "prologue_preview": t235_to_255(b235["prologue_preview"]),
        "epilogue_loop": epilogue_loop.rstrip() + "\n\n",
        "epilogue_loop253": _load_add253()._build_blocks()["epilogue_loop"].rstrip() + "\n\n",
        "epilogue_loop254": _load_add254()._build_blocks()["epilogue_loop"].rstrip() + "\n\n",
        "sources_table": t235_to_255(b235["sources_table"]).replace("| 235 | Row 68 → Row 215", "| 255 | Row 68 → Row 235", 1),
        "sources_index": sources_index,
        "memory_table": (
            "| 255 | Meta | [Row 68 → Row 235 electronic audit meta prelude capstone reunion index]"
            "(sources.md#row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255) · "
            "[preface row 255 skill checkpoint](../preface.md#skill-navigation-row-255) · "
            "[prologue row 255 preview](../prologue/00-many-scales.md#prologue-preview-row-255) · "
            "[prologue row 255 closing stitch](../prologue/00-many-scales.md#row-255-closing-stitch) · "
            "[epilogue row 255 closing loop](../epilogue/multiscale.md#row-255-closing-loop) | "
            "Row 68 closed but row 55 electronic audit reunion feels disconnected from verified "
            "export meta prelude capstone on the full capstone path — read row 68 + row 254 or "
            "row 235 gate + VIII.3 Bridge → IX.0 + row 55; "
            "[row 255 baby picture](#row-255-baby-picture-row68-row235-electronic-audit-meta-prelude-capstone-reunion) |\n"
        ),
        "memory_baby": _compact_memory_baby(),
    }


ROW255_EPILOGUE_AFTER = (
    "### Row 252 closing loop (Row 68 → Row 232 Row 68 → Row 52 atomistic meta prelude capstone reunion) "
    "{#row-252-closing-loop}"
)

ROW255_EPILOGUE_BEFORE = (
    "### Row 227 closing loop (Row 68 → Row 227 Row 68 → Row 67 part-boundary meta prelude capstone reunion) "
    "{#row-247-closing-loop}"
)

PROLOGUE_STITCH_ANCHORS = (
    "**Row 254 closing stitch (Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-254-closing-stitch}",
    "**Row 234 closing stitch (Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion).** {#row-254-closing-stitch}",
)

ROW254_STITCH_OLD = "before row 255 electronic audit meta prelude capstone reunion opens on the full capstone path."
ROW254_STITCH_NEW = "before row 256 Born–Oppenheimer meta prelude capstone reunion opens on the full capstone path."

ROW254_EPILOGUE_OLD = (
    "Proceed to [row 215](#row-215-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 234 on the full capstone path,"
)
ROW254_EPILOGUE_NEW = (
    "Proceed to [row 255](#row-255-closing-loop) when row 68 closed but electronic audit meta prelude capstone still lags after row 254 on the full capstone path,"
)

CAPSTONE_ROW255_TITLE = (
    "### Row 255 skill checkpoint — Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion audit"
)


def _epilogue_has_row255_in_capstone_chain(text: str) -> bool:
    if ROW255_EPILOGUE_AFTER not in text:
        return False
    idx = text.index(ROW255_EPILOGUE_AFTER)
    window = text[idx : idx + 35000]
    return (
        "{#row-255-closing-loop}" in window
        and "memory sheet row 235" in window
        and "### Row 255 closing loop" in window
        and "after row 254 alone" in window
    )


def _trim_loop_spill(loop: str, spill_header: str) -> str:
    if spill_header in loop:
        loop = loop.split(spill_header, 1)[0].rstrip() + "\n\n"
    return loop


def _canonical_capstone_loops(b: dict[str, str]) -> tuple[str, str, str]:
    loop253 = _trim_loop_spill(
        b["epilogue_loop253"],
        "### Row 234 closing loop (Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion)",
    )
    loop254 = _trim_loop_spill(
        b["epilogue_loop254"],
        "### Row 235 closing loop (Row 68 → Row 235 Row 68 → Row 55 electronic audit meta prelude capstone reunion)",
    )
    loop254 = loop254.replace(ROW254_EPILOGUE_OLD, ROW254_EPILOGUE_NEW, 1)
    loop255 = b["epilogue_loop"]
    if loop255.count("{#row-255-closing-loop}") > 1:
        loop255 = loop255.split("{#row-255-closing-loop}", 1)[0] + "{#row-255-closing-loop}" + loop255.split(
            "{#row-255-closing-loop}", 1
        )[1].split("\n\n### Row", 1)[0]
        if not loop255.endswith("\n\n"):
            loop255 = loop255.rstrip() + "\n\n"
    loop255 = loop255.replace(
        "When row 55 feels like DFT homework after row 214 alone on the full capstone path",
        "When row 55 feels like DFT homework after row 254 alone on the full capstone path",
        1,
    ).replace(
        "when row 214 closed export meta prelude capstone",
        "when row 254 closed export meta prelude capstone",
        1,
    ).replace(
        "Recite [preface row 214](../preface.md#skill-navigation-row-194)",
        "Recite [preface row 254](../preface.md#skill-navigation-row-254)",
        1,
    ).replace(
        "verified export meta prelude capstone (row 214)",
        "verified export meta prelude capstone (row 254)",
        1,
    )
    return loop253, loop254, loop255


def _rebuild_capstone_mid(mid: str, loop253: str, loop254: str, loop255: str) -> str:
    marker = "### Row 253 closing loop"
    if marker not in mid:
        raise SystemExit("row 253 closing loop header missing in capstone mid")
    start = mid.index(marker)
    return mid[:start] + loop253 + loop254 + loop255


def main() -> None:
    b = _build_blocks()
    copper = "\n## The copper wire through the book"

    preface_path = ROOT / "writings/preface/chapters/preface.md"
    preface = preface_path.read_text()
    before_copper = preface.split(copper, 1)[0]
    if CAPSTONE_ROW255_TITLE in before_copper:
        print("preface: row 255 capstone already present")
    else:
        if "### Row 254 skill checkpoint" not in before_copper:
            raise SystemExit("row 254 must exist before row 255")
        if copper not in preface:
            raise SystemExit("copper wire anchor not found")
        preface = preface.replace(copper, "\n" + b["row255_preface"] + copper, 1)
        preface_path.write_text(preface)
        print("preface: added row 255")

    prologue_path = ROOT / "writings/prologue/chapters/00-many-scales.md"
    prologue = prologue_path.read_text()
    if "electronic audit meta prelude capstone reunion (row 255) |" not in prologue:
        needle = (
            "| Row 68 → Row 234 Row 68 → Row 54 export meta prelude capstone reunion (row 254) |"
        )
        if needle not in prologue:
            raise SystemExit("prologue compass row 254 not found")
        idx = prologue.find(needle)
        line_end = prologue.find("\n", idx)
        prologue = prologue[: line_end + 1] + b["prologue_compass"] + prologue[line_end + 1 :]
        if "**Row 255 closing stitch" not in prologue:
            for anchor in PROLOGUE_STITCH_ANCHORS:
                if anchor in prologue:
                    prologue = prologue.replace(anchor, b["prologue_stitch"] + anchor, 1)
                    break
        preview_anchor = '| <span id="prologue-preview-row-254"></span>Row 234 preview'
        if preview_anchor not in prologue:
            raise SystemExit("prologue preview insert anchor not found")
        if '<span id="prologue-preview-row-255">' not in prologue:
            prologue = prologue.replace(preview_anchor, b["prologue_preview"] + preview_anchor)
        if ROW254_STITCH_OLD in prologue:
            prologue = prologue.replace(ROW254_STITCH_OLD, ROW254_STITCH_NEW)
        prologue_path.write_text(prologue)
        print("prologue: added row 255")
    else:
        print("prologue: row 255 already present")

    epilogue_path = ROOT / "writings/epilogue/chapters/multiscale.md"
    epilogue = epilogue_path.read_text()
    if ROW254_EPILOGUE_OLD in epilogue:
        epilogue = epilogue.replace(ROW254_EPILOGUE_OLD, ROW254_EPILOGUE_NEW, 1)
        print("epilogue: updated row 254 proceed link")
    force_rebuild = epilogue.count("{#row-255-closing-loop}") > 1
    if force_rebuild or not _epilogue_has_row255_in_capstone_chain(epilogue):
        if ROW255_EPILOGUE_AFTER not in epilogue:
            raise SystemExit("epilogue row 252 anchor not found")
        if ROW255_EPILOGUE_BEFORE not in epilogue.split(ROW255_EPILOGUE_AFTER, 1)[1]:
            raise SystemExit("epilogue row 247 marker not found after row 252")
        head, tail = epilogue.split(ROW255_EPILOGUE_AFTER, 1)
        mid, rest = tail.split(ROW255_EPILOGUE_BEFORE, 1)
        l253, l254, l255 = _canonical_capstone_loops(b)
        mid = _rebuild_capstone_mid(mid, l253, l254, l255)
        epilogue_path.write_text(head + ROW255_EPILOGUE_AFTER + mid + ROW255_EPILOGUE_BEFORE + rest)
        print("epilogue: rebuilt capstone chain through row 255")
    else:
        print("epilogue: row 255 closing loop already present in capstone chain")

    sources_path = ROOT / "writings/appendix/chapters/sources.md"
    sources = sources_path.read_text()
    if "row68-row235-electronic-audit-meta-prelude-capstone-reunion-index-row-255" not in sources:
        needle = "| 235 | Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone"
        if needle not in sources:
            raise SystemExit("sources electronic audit table anchor not found")
        sources = sources.replace(needle, b["sources_table"] + needle, 1)
        src235_header = (
            "## Row 68 → Row 215 Row 68 → Row 55 electronic audit meta prelude capstone reunion index (row 235)"
        )
        if src235_header in sources and b["sources_index"].strip()[:80] not in sources:
            sources = sources.replace(src235_header, b["sources_index"] + src235_header, 1)
        sources_path.write_text(sources)
        print("sources: added row 255")
    else:
        print("sources: row 255 index already present")

    memory_path = ROOT / "writings/appendix/chapters/memory-sheet.md"
    memory = memory_path.read_text()
    if "row-255-baby-picture-row68-row235" not in memory:
        if "| 255 | Meta |" not in memory:
            mem254 = "| 254 | Meta | [Row 68 → Row 234 export meta prelude capstone reunion index]"
            if mem254 in memory:
                memory = memory.replace(mem254, b["memory_table"] + mem254, 1)
        baby_anchors = (
            "### Row 254 baby picture {#row-254-baby-picture-row68-row234-export-meta-prelude-capstone-reunion}",
            "### Row 235 baby picture {#row-235-baby-picture-row68-row215-electronic-audit-meta-prelude-capstone-reunion}",
        )
        baby_anchor = next((a for a in baby_anchors if a in memory), None)
        if not baby_anchor:
            raise SystemExit("memory baby picture anchor not found")
        memory = memory.replace(baby_anchor, b["memory_baby"] + baby_anchor, 1)
        memory_path.write_text(memory)
        print("memory-sheet: added row 255")
    else:
        print("memory-sheet: row 255 baby already present")


if __name__ == "__main__":
    main()
