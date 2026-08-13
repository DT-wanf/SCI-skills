#!/usr/bin/env python3
"""Inspect basic metadata for delivered scientific-figure files."""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_svg_length(value: str | None) -> tuple[float | None, str | None]:
    if not value:
        return None, None
    match = re.fullmatch(r"\s*([0-9.]+)\s*([A-Za-z%]*)\s*", value)
    if not match:
        return None, None
    return float(match.group(1)), match.group(2) or "user"


def inspect_svg(path: Path) -> dict:
    root = ET.parse(path).getroot()
    width, width_unit = parse_svg_length(root.attrib.get("width"))
    height, height_unit = parse_svg_length(root.attrib.get("height"))
    text_count = sum(1 for element in root.iter() if element.tag.rsplit("}", 1)[-1] == "text")
    return {
        "format": "SVG",
        "width": width,
        "width_unit": width_unit,
        "height": height,
        "height_unit": height_unit,
        "viewBox": root.attrib.get("viewBox"),
        "editable_text_elements": text_count,
    }


def inspect_raster(path: Path) -> dict:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Pillow is required to inspect PNG/TIFF raster metadata") from exc
    with Image.open(path) as image:
        dpi = image.info.get("dpi")
        return {
            "format": image.format,
            "width_px": image.width,
            "height_px": image.height,
            "mode": image.mode,
            "dpi": list(dpi) if isinstance(dpi, tuple) else dpi,
        }


def inspect_pdf(path: Path) -> dict:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("pypdf is required to inspect PDF metadata") from exc
    reader = PdfReader(str(path))
    first = reader.pages[0]
    box = first.mediabox
    return {
        "format": "PDF",
        "pages": len(reader.pages),
        "width_pt": float(box.width),
        "height_pt": float(box.height),
    }


def inspect(path: Path) -> dict:
    if not path.is_file():
        raise ValueError(f"Output is not a file: {path}")
    if path.is_symlink():
        raise ValueError("Symlink outputs are not accepted")
    if path.stat().st_size == 0:
        raise ValueError("Output file is empty")

    suffix = path.suffix.lower()
    if suffix == ".svg":
        details = inspect_svg(path)
    elif suffix in {".png", ".tif", ".tiff"}:
        details = inspect_raster(path)
    elif suffix == ".pdf":
        details = inspect_pdf(path)
    else:
        raise ValueError("Supported outputs are SVG, PDF, PNG, TIFF, and TIF")

    return {
        "status": "INSPECTED",
        "path": str(path),
        "bytes": path.stat().st_size,
        "details": details,
        "caution": "Metadata inspection does not prove scientific correctness, visual quality, or journal compliance.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        report = inspect(args.output)
    except (OSError, ValueError, RuntimeError, ET.ParseError) as exc:
        print(json.dumps({"status": "ERROR", "message": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
