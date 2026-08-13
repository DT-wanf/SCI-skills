from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def require(path: Path) -> str:
    if not path.exists():
        errors.append(f"Missing: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


skill = require(ROOT / "SKILL.md")
manifest = require(ROOT / "manifest.yaml")

if not skill.startswith("---\nname: sci-skill\n"):
    errors.append("SKILL.md must use name: sci-skill")

for literal in [
    "你好，我是晚风老师打造的「SCI保姆」，你可以叫我“宝宝巴士”,或者山海。我的任务不是一次性替你生成整篇论文，而是根据你的研究方向、现有资源和目标要求，帮助你在实证类、阐释类、方法应用类、理论类和综述类论文中选择合适路线，判断你真正所处的研究阶段，并逐步完成信息收集、任务规划、阶段产出和质量验收。你只需要如实告诉我目前有什么、还不确定什么，我会从你现有的基础开始陪你推进。",
    "把你的研究方向、已有材料或论文草稿发给我，我们就可以开始。",
    "## **下一站已开启：复制下面这段 Prompt**",
    "## **当前阶段还差一点：复制下面这段 Prompt**",
    "## **这一站暂时没有可直接使用的 Prompt：需要先完成真实操作，我会一步一步带你做。**",
    "## Academic web-data acquisition gate",
    "templates/data-acquisition-review-card.md",
    "## **数据已经采集：请先审核，再进入数据清洗**",
    "If status is `SUFFICIENT`, do not load `web-data-acquisition.md`",
    "crawl_necessity` is marked `JUSTIFIED`",
    "## Scientific-figure gate",
    "Never render an experimental result figure without real data",
    "## **这里建议放一张图：请先确认图位和拆图方案**",
    "## **图片初稿已经生成：请审核后再定稿**",
]:
    if literal not in skill:
        errors.append(f"SKILL.md missing required literal: {literal}")

modules = sorted((ROOT / "workflows").glob("*/*.md"))
if len(modules) != 35:
    errors.append(f"Expected 35 stage modules, found {len(modules)}")

expected_ids = {f"{family}{index}" for family in "EIMTR" for index in range(1, 8)}
found_ids: set[str] = set()

required_sections = [
    "## Required fields",
    "## CREATE mode",
    "## REFINE mode",
    "## Source-defined deliverables",
    "### Acceptance criteria",
    "## Next-action card contract",
    "## Transition",
]

for path in modules:
    text = require(path)
    match = re.search(r"^stage_id:\s*([EIMTR][1-7])\s*$", text, re.M)
    if not match:
        errors.append(f"Missing valid stage_id: {path.relative_to(ROOT)}")
        continue
    stage_id = match.group(1)
    found_ids.add(stage_id)
    for key in ["action_type_default:", "capability_candidates:", "external_playbook:"]:
        if key not in text:
            errors.append(f"{stage_id} missing {key}")
    for section in required_sections:
        if section not in text:
            errors.append(f"{stage_id} missing {section}")

if found_ids != expected_ids:
    errors.append(
        "Stage ID mismatch: missing="
        + ",".join(sorted(expected_ids - found_ids))
        + " extra="
        + ",".join(sorted(found_ids - expected_ids))
    )

capabilities = [
    "literature-search",
    "paper-deep-reading",
    "manuscript-writing",
    "academic-polishing",
    "scientific-figures",
    "paper-presentation",
    "statistical-reporting",
    "presubmission-review",
    "reviewer-response",
    "data-availability",
    "web-data-acquisition",
]
for capability in capabilities:
    require(ROOT / "references" / "capabilities" / f"{capability}.md")
    if f"  {capability}: references/capabilities/{capability}.md" not in manifest:
        errors.append(f"Manifest missing capability route: {capability}")

playbooks = [
    "literature-database-export",
    "empirical-data-and-experiment",
    "text-and-archive-collection",
    "prototype-and-validation",
    "submission-platform",
    "web-data-collection",
]
for playbook in playbooks:
    require(ROOT / "references" / "action-playbooks" / f"{playbook}.md")

for template in [
    "beginner-entry.md",
    "next-stage-prompt-card.md",
    "repair-prompt-card.md",
    "manual-action-card.md",
    "hybrid-action-card.md",
    "return-to-agent-prompt.md",
    "stage-review.md",
    "data-source-choice-card.md",
    "data-acquisition-review-card.md",
    "data-cleaning-handoff-card.md",
    "figure-proposal-card.md",
    "figure-review-card.md",
]:
    require(ROOT / "templates" / template)

for schema in [
    "project-state.yaml",
    "stage-module-schema.md",
    "user-style-profile.yaml",
    "web-data-collection-plan.yaml",
    "figure-plan.yaml",
    "figure-qa-report.yaml",
]:
    require(ROOT / "schemas" / schema)

require(ROOT / "references" / "web-source-families.md")
require(ROOT / "references" / "core" / "data-sufficiency-gate.md")
require(ROOT / "scripts" / "test_data_acquisition_gates.py")
require(ROOT / "references" / "core" / "figure-readiness-gate.md")
require(ROOT / "references" / "figure-planning-and-consent.md")
require(ROOT / "references" / "figure-decomposition.md")
require(ROOT / "references" / "reference-figure-adaptation.md")
require(ROOT / "references" / "figure-visual-qa.md")
require(ROOT / "scripts" / "profile_figure_data.py")
require(ROOT / "scripts" / "validate_figure_source.py")
require(ROOT / "scripts" / "inspect_figure_output.py")
require(ROOT / "scripts" / "test_figure_gates.py")
require(ROOT / "scripts" / "test_figure_tools.py")

runtime_files = [
    ROOT / "SKILL.md",
    ROOT / "manifest.yaml",
    *list((ROOT / "templates").glob("*.md")),
    *list((ROOT / "workflows").glob("*/*.md")),
    *list((ROOT / "references" / "capabilities").glob("*.md")),
    *list((ROOT / "references" / "action-playbooks").glob("*.md")),
    ROOT / "references" / "web-source-families.md",
    *list((ROOT / "schemas").glob("*")),
]
for path in runtime_files:
    text = path.read_text(encoding="utf-8")
    if re.search(r"\bnature-", text, re.I):
        errors.append(f"Legacy brand name found in runtime file: {path.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("VALIDATION PASSED")
print(f"Stage modules: {len(modules)}")
print(f"Capabilities: {len(capabilities)}")
print(f"External playbooks: {len(playbooks)}")
