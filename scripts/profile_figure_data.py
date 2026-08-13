#!/usr/bin/env python3
"""Profile CSV/TSV inputs before scientific chart selection."""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter
from pathlib import Path
from statistics import fmean


MISSING = {"", "na", "n/a", "nan", "null", "none", "."}


def is_missing(value: str | None) -> bool:
    return value is None or value.strip().lower() in MISSING


def delimiter_for(path: Path, explicit: str | None) -> str:
    if explicit:
        return explicit
    return "\t" if path.suffix.lower() in {".tsv", ".tab"} else ","


def profile(path: Path, delimiter: str | None = None, groups: list[str] | None = None) -> dict:
    if not path.is_file():
        raise ValueError(f"Input is not a file: {path}")
    if path.is_symlink():
        raise ValueError("Symlink inputs are not accepted")

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter_for(path, delimiter))
        if not reader.fieldnames:
            raise ValueError("No header row found")
        rows = list(reader)

    columns: dict[str, dict] = {}
    for name in reader.fieldnames:
        raw = [row.get(name) for row in rows]
        present = [value.strip() for value in raw if not is_missing(value)]
        numeric: list[float] = []
        for value in present:
            try:
                number = float(value)
                if math.isfinite(number):
                    numeric.append(number)
            except ValueError:
                pass

        numeric_fraction = len(numeric) / len(present) if present else 0.0
        summary: dict[str, object] = {
            "missing": len(raw) - len(present),
            "missing_rate": round((len(raw) - len(present)) / len(raw), 6) if raw else 0.0,
            "unique": len(set(present)),
            "inferred_type": "numeric" if present and numeric_fraction >= 0.9 else "categorical_or_text",
        }
        if summary["inferred_type"] == "numeric" and numeric:
            summary.update(
                {
                    "min": min(numeric),
                    "max": max(numeric),
                    "mean": fmean(numeric),
                    "numeric_values": len(numeric),
                }
            )
        else:
            summary["top_values"] = Counter(present).most_common(10)
        columns[name] = summary

    group_counts: dict[str, dict[str, int]] = {}
    for group in groups or []:
        if group not in reader.fieldnames:
            raise ValueError(f"Unknown group column: {group}")
        counts = Counter(
            "<MISSING>" if is_missing(row.get(group)) else row[group].strip()
            for row in rows
        )
        group_counts[group] = dict(sorted(counts.items()))

    return {
        "input": str(path),
        "rows": len(rows),
        "columns": len(reader.fieldnames),
        "column_profiles": columns,
        "group_counts": group_counts,
        "cautions": [
            "Numeric identifiers may be misclassified; verify field semantics manually.",
            "This profile does not decide exclusions, transformations, statistical tests, or chart type by itself.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--delimiter", choices=[",", "\t"])
    parser.add_argument("--group", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        report = profile(args.input, args.delimiter, args.group)
    except (OSError, ValueError, csv.Error) as exc:
        print(json.dumps({"status": "ERROR", "message": str(exc)}, ensure_ascii=False))
        return 2

    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
