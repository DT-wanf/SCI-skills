from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def acquisition_active(status: str, web_appropriate: bool, repairable: bool) -> bool:
    return status in {"ABSENT", "INSUFFICIENT"} and web_appropriate and not repairable


def crawl_active(
    acquisition: bool,
    non_crawl_checked: bool,
    non_crawl_adequate: bool,
    permission_acceptable: bool,
    necessity: str,
) -> bool:
    return all(
        [
            acquisition,
            non_crawl_checked,
            not non_crawl_adequate,
            permission_acceptable,
            necessity == "JUSTIFIED",
        ]
    )


acquisition_cases = [
    ("UNKNOWN", True, False, False),
    ("SUFFICIENT", True, False, False),
    ("INSUFFICIENT", True, True, False),
    ("INSUFFICIENT", False, False, False),
    ("INSUFFICIENT", True, False, True),
    ("ABSENT", True, False, True),
]
for status, web_appropriate, repairable, expected in acquisition_cases:
    actual = acquisition_active(status, web_appropriate, repairable)
    if actual != expected:
        errors.append(f"Acquisition case failed: {status}, expected {expected}, got {actual}")

crawl_cases = [
    (True, True, False, True, "JUSTIFIED", True),
    (False, True, False, True, "JUSTIFIED", False),
    (True, False, False, True, "JUSTIFIED", False),
    (True, True, True, True, "JUSTIFIED", False),
    (True, True, False, False, "JUSTIFIED", False),
    (True, True, False, True, "BLOCKED", False),
]
for acquisition, checked, adequate, permitted, necessity, expected in crawl_cases:
    actual = crawl_active(acquisition, checked, adequate, permitted, necessity)
    if actual != expected:
        errors.append(f"Crawler case failed: expected {expected}, got {actual}")

required_literals = {
    "SKILL.md": [
        "If status is `SUFFICIENT`, do not load `web-data-acquisition.md`",
        "crawl_necessity` is marked `JUSTIFIED`",
    ],
    "references/core/data-sufficiency-gate.md": [
        "`UNKNOWN`",
        "`SUFFICIENT`",
        "`INSUFFICIENT`",
        "`ABSENT`",
        "Otherwise set `crawl_necessity` to `BLOCKED`",
    ],
    "workflows/empirical/E5-data-collection-execution-and-analysis.md": [
        "`DATA_SUFFICIENCY_AUDIT`",
        "skip `ACQUISITION_PLAN`",
        "go directly to `CLEANING_AND_ANALYSIS`",
    ],
    "schemas/project-state.yaml": [
        "data_sufficiency:",
        "crawl_necessity: BLOCKED",
    ],
}
for relative, literals in required_literals.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    for literal in literals:
        if literal not in text:
            errors.append(f"{relative} missing gate literal: {literal}")

if errors:
    print("DATA ACQUISITION GATE TESTS FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("DATA ACQUISITION GATE TESTS PASSED")
print(f"Acquisition cases: {len(acquisition_cases)}")
print(f"Crawler cases: {len(crawl_cases)}")
