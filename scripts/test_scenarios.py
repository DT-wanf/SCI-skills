from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def stage_meta(stage_id: str) -> tuple[str, set[str], str | None]:
    matches = list((ROOT / "workflows").glob(f"*/*{stage_id[1:]}-*.md"))
    matches = [
        path
        for path in matches
        if re.search(rf"^stage_id:\s*{stage_id}\s*$", path.read_text(encoding="utf-8"), re.M)
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one file for {stage_id}, got {len(matches)}")
    text = matches[0].read_text(encoding="utf-8")
    action = re.search(r"^action_type_default:\s*(\S+)", text, re.M).group(1)
    caps_block = re.search(
        r"^capability_candidates:\s*\n((?:  - .+\n)+)", text, re.M
    ).group(1)
    caps = {line.removeprefix("  - ").strip() for line in caps_block.splitlines()}
    playbook_raw = re.search(r"^external_playbook:\s*(\S+)", text, re.M).group(1)
    playbook = None if playbook_raw == "null" else playbook_raw
    return action, caps, playbook


scenarios = {
    "beginner topic selection": (
        "E1",
        "prompt",
        {"literature-search"},
        None,
    ),
    "review CSV database export": (
        "R2",
        "conditional_external",
        {"literature-search"},
        "literature-database-export",
    ),
    "real experiment and analysis": (
        "E5",
        "conditional_external",
        {"statistical-reporting", "scientific-figures"},
        "empirical-data-and-experiment",
    ),
    "manuscript drafting": (
        "E6",
        "prompt",
        {"manuscript-writing", "academic-polishing"},
        None,
    ),
    "prototype construction": (
        "M4",
        "conditional_external",
        {"scientific-figures", "data-availability"},
        "prototype-and-validation",
    ),
    "source text collection": (
        "I2",
        "conditional_external",
        {"paper-deep-reading"},
        "text-and-archive-collection",
    ),
    "submission and reviewer response": (
        "E7",
        "conditional_external",
        {"presubmission-review", "reviewer-response", "paper-presentation"},
        "submission-platform",
    ),
}

for label, (stage_id, action, required_caps, playbook) in scenarios.items():
    actual_action, caps, actual_playbook = stage_meta(stage_id)
    if actual_action != action:
        errors.append(f"{label}: expected action {action}, got {actual_action}")
    if not required_caps.issubset(caps):
        errors.append(f"{label}: missing capabilities {sorted(required_caps - caps)}")
    if actual_playbook != playbook:
        errors.append(f"{label}: expected playbook {playbook}, got {actual_playbook}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
for alias in ["宝宝巴士", "山海"]:
    if alias not in skill:
        errors.append(f"Missing invocation alias: {alias}")

e4 = next(
    path for path in (ROOT / "workflows" / "empirical").glob("E4-*.md")
).read_text(encoding="utf-8")
e5 = next(
    path for path in (ROOT / "workflows" / "empirical").glob("E5-*.md")
).read_text(encoding="utf-8")
i2 = next(
    path for path in (ROOT / "workflows" / "interpretive").glob("I2-*.md")
).read_text(encoding="utf-8")
m3 = next(
    path for path in (ROOT / "workflows" / "method-application").glob("M3-*.md")
).read_text(encoding="utf-8")
m5 = next(
    path for path in (ROOT / "workflows" / "method-application").glob("M5-*.md")
).read_text(encoding="utf-8")
e6 = next(
    path for path in (ROOT / "workflows" / "empirical").glob("E6-*.md")
).read_text(encoding="utf-8")

scenario_literals = {
    "E4 source-first planning": (e4, ["`SUFFICIENT`", "`INSUFFICIENT`", "`ABSENT`", "crawl_necessity"]),
    "E5 acquisition gates": (e5, ["DATA_SUFFICIENCY_AUDIT", "ACQUISITION_PLAN", "USER_AUDIT", "CLEANING_AND_ANALYSIS"]),
    "E5 web playbook": (e5, ["web-data-collection", "data-acquisition-review-card.md"]),
    "E5 sufficient-data bypass": (e5, ["skip `ACQUISITION_PLAN`", "go directly to `CLEANING_AND_ANALYSIS`"]),
    "I2 web corpus": (i2, ["For `SUFFICIENT`, do not load", "web-data-collection", "crawl_necessity"]),
    "M3 algorithm decomposition": (m3, ["multi-panel overview option", "overview-plus-module-figures", "reference image"]),
    "M5 result figure gate": (m5, ["`RESULT` gate", "Python/R plotting source", "actual execution evidence"]),
    "E6 manuscript figure consent": (e6, ["manuscript-level figure map", "figure proposal card", "decline", "reference image"]),
}
for label, (text, literals) in scenario_literals.items():
    for literal in literals:
        if literal not in text:
            errors.append(f"{label}: missing {literal}")

capability = (
    ROOT / "references" / "capabilities" / "web-data-acquisition.md"
).read_text(encoding="utf-8")
for literal in [
    "Do not activate for `UNKNOWN` or `SUFFICIENT`",
    "official free download",
    "paid licensed dataset",
    "Do not recommend crawling",
    "explicit user approval",
    "crawl_necessity: JUSTIFIED",
]:
    if literal not in capability:
        errors.append(f"web data capability missing: {literal}")

cleaning_handoff = (
    ROOT / "templates" / "data-cleaning-handoff-card.md"
).read_text(encoding="utf-8")
for literal in ["审核通过", "不得覆盖原始文件", "清洗日志", "E5 验收标准"]:
    if literal not in cleaning_handoff:
        errors.append(f"cleaning handoff missing: {literal}")

manifest = (ROOT / "manifest.yaml").read_text(encoding="utf-8")
for literal in [
    "data_sufficiency in [ABSENT, INSUFFICIENT]",
    "data_sufficiency in [UNKNOWN, SUFFICIENT]",
    "non_crawl_routes_adequate is false",
    "crawl_necessity is JUSTIFIED",
]:
    if literal not in manifest:
        errors.append(f"manifest acquisition gate missing: {literal}")

for literal in [
    "figure_activation_conditions:",
    "actual_execution_evidence_available is true",
    "image_generation_model_used_for_result_pixels is true",
    "user_rendering_approval is true",
    "user_final_approval is true",
]:
    if literal not in manifest:
        errors.append(f"manifest figure gate missing: {literal}")

if errors:
    print("SCENARIO TESTS FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("SCENARIO TESTS PASSED")
print(f"Scenarios checked: {len(scenarios)}")
