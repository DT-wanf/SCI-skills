#!/usr/bin/env python3
"""Static preflight for Python/R scientific-figure source files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


READ_PATTERNS = [
    r"\bread_csv\s*\(", r"\bread_excel\s*\(", r"\bread_table\s*\(",
    r"\bnp\.load(?:txt)?\s*\(", r"\bload\s*\(", r"\bread\.csv\s*\(",
    r"\bread\.table\s*\(", r"\breadRDS\s*\(", r"\bfread\s*\(",
    r"\breadr::read_", r"\bhaven::read_",
]
PLOT_PATTERNS = [
    r"\bplt\.", r"\bsns\.", r"\bmatplotlib\b", r"\bggplot\s*\(",
    r"\bComplexHeatmap::", r"\bHeatmap\s*\(", r"\bsurvminer::",
]
SAVE_PATTERNS = [
    r"\bsavefig\s*\(", r"\bggsave\s*\(", r"\bsvglite\s*\(",
    r"\bcairo_pdf\s*\(", r"\bagg_tiff\s*\(", r"\bpdf\s*\(",
    r"\bpng\s*\(", r"\btiff\s*\(",
]
SIMULATION_PATTERNS = [
    r"\bnp\.random\.", r"\brandom\.", r"\brnorm\s*\(", r"\brunif\s*\(",
    r"\bsimulated?_data\b", r"\bmock_data\b", r"\bexample_data\b",
]
IMAGE_GENERATION_PATTERNS = [
    r"openrouter", r"gpt[-_ ]?image", r"dall[-_ ]?e", r"midjourney",
    r"stable[-_ ]?diffusion", r"image_gen", r"nano banana",
]


def any_pattern(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, re.I) for pattern in patterns)


def validate(path: Path, result_figure: bool) -> dict:
    if not path.is_file():
        return {"status": "FAIL", "failures": [f"Source is not a file: {path}"], "warnings": []}
    if path.is_symlink():
        return {"status": "FAIL", "failures": ["Symlink sources are not accepted"], "warnings": []}
    if path.suffix.lower() not in {".py", ".r"}:
        return {"status": "FAIL", "failures": ["Source must be .py or .R"], "warnings": []}

    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    warnings: list[str] = []

    if not any_pattern(text, PLOT_PATTERNS):
        failures.append("No supported plotting call detected")
    if not any_pattern(text, SAVE_PATTERNS):
        failures.append("No supported figure export call detected")

    reads_input = any_pattern(text, READ_PATTERNS)
    uses_simulation = any_pattern(text, SIMULATION_PATTERNS)
    uses_image_generation = any_pattern(text, IMAGE_GENERATION_PATTERNS)

    if result_figure:
        if not reads_input:
            failures.append("Result figure source does not visibly read a real input file")
        if uses_image_generation:
            failures.append("Image-generation route detected in result-figure source")
        if uses_simulation:
            warnings.append("Random, mock, example, or simulated data pattern detected; verify it is not used as manuscript evidence")
        warnings.append("Static source checks cannot prove execution; require a run command/log and inspect generated outputs")
        warnings.append("Verify that every displayed value traces to the declared real input and transformations")

    return {
        "status": "FAIL" if failures else "PASS_WITH_WARNINGS" if warnings else "PASS",
        "source": str(path),
        "result_figure": result_figure,
        "reads_input": reads_input,
        "uses_simulation_pattern": uses_simulation,
        "uses_image_generation_pattern": uses_image_generation,
        "failures": failures,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--result-figure", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        report = validate(args.source, args.result_figure)
    except (OSError, UnicodeError) as exc:
        report = {"status": "FAIL", "failures": [str(exc)], "warnings": []}

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(report["status"])
        for item in report.get("failures", []):
            print(f"FAIL: {item}")
        for item in report.get("warnings", []):
            print(f"WARN: {item}")
    return 1 if report["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
