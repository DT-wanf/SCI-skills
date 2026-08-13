from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def result_render_allowed(
    real_inputs: bool,
    semantics: bool,
    transformations: bool,
    backend: str | None,
    source: bool,
    execution: bool,
    traceability: bool,
    image_generation: bool = False,
    invented_values: bool = False,
) -> bool:
    return all(
        [
            real_inputs,
            semantics,
            transformations,
            backend in {"python", "r"},
            source,
            execution,
            traceability,
            not image_generation,
            not invented_values,
        ]
    )


def explanatory_render_allowed(
    location: bool,
    purpose: bool,
    boundary: bool,
    decomposition: bool,
    route: bool,
    approval: bool,
) -> bool:
    return all([location, purpose, boundary, decomposition, route, approval])


result_cases = [
    ("all result gates pass", (True, True, True, "python", True, True, True), True),
    ("text conclusion only", (False, True, True, "python", True, True, True), False),
    ("no semantics", (True, False, True, "python", True, True, True), False),
    ("no Python/R", (True, True, True, None, True, True, True), False),
    ("script not executed", (True, True, True, "r", True, False, True), False),
    ("no traceability", (True, True, True, "python", True, True, False), False),
]
for label, args, expected in result_cases:
    actual = result_render_allowed(*args)
    if actual != expected:
        errors.append(f"Result gate {label}: expected {expected}, got {actual}")

if result_render_allowed(True, True, True, "python", True, True, True, image_generation=True):
    errors.append("Result gate allowed image generation")
if result_render_allowed(True, True, True, "python", True, True, True, invented_values=True):
    errors.append("Result gate allowed invented values")

explanatory_cases = [
    ("approved proposal", (True, True, True, True, True, True), True),
    ("no manuscript location", (False, True, True, True, True, True), False),
    ("no decomposition", (True, True, True, False, True, True), False),
    ("no user approval", (True, True, True, True, True, False), False),
]
for label, args, expected in explanatory_cases:
    actual = explanatory_render_allowed(*args)
    if actual != expected:
        errors.append(f"Explanatory gate {label}: expected {expected}, got {actual}")

required_literals = {
    "SKILL.md": [
        "Never render an experimental result figure without real data",
        "## Scientific-figure gate",
        "## **这里建议放一张图：请先确认图位和拆图方案**",
        "## **图片初稿已经生成：请审核后再定稿**",
    ],
    "manifest.yaml": [
        "figure_activation_conditions:",
        "actual_execution_evidence_available is true",
        "image_generation_model_used_for_result_pixels is true",
        "user_rendering_approval is true",
        "user_final_approval is true",
    ],
    "references/capabilities/scientific-figures.md": [
        "## Result-figure hard gate",
        "actual execution evidence",
        "## Explanatory and enhancement consent gate",
        "Do not presume one image can explain the entire method",
        "## Reference-figure route",
    ],
    "references/core/figure-readiness-gate.md": [
        "only a textual conclusion is available",
        "backend in [python, r]",
        "user_rendering_approval = true",
        "user_final_approval = true",
    ],
    "templates/figure-proposal-card.md": [
        "只做全览图",
        "我先上传一张对标图片",
        "暂时不制作",
    ],
    "templates/figure-review-card.md": [
        "真实输入",
        "实际运行证据",
        "允许插入论文",
        "不使用这张图",
    ],
}

for relative, literals in required_literals.items():
    path = ROOT / relative
    if not path.exists():
        errors.append(f"Missing figure file: {relative}")
        continue
    text = path.read_text(encoding="utf-8")
    for literal in literals:
        if literal not in text:
            errors.append(f"{relative} missing: {literal}")

if errors:
    print("FIGURE GATE TESTS FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("FIGURE GATE TESTS PASSED")
print(f"Result cases: {len(result_cases) + 2}")
print(f"Explanatory cases: {len(explanatory_cases)}")
