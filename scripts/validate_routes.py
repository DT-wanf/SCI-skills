from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest = (ROOT / "manifest.yaml").read_text(encoding="utf-8")
errors: list[str] = []

stage_paths = sorted((ROOT / "workflows").glob("*/*.md"))
stage_meta: dict[str, tuple[str, list[str], str | None, list[str]]] = {}

for path in stage_paths:
    text = path.read_text(encoding="utf-8")
    id_match = re.search(r"^stage_id:\s*(\w+)\s*$", text, re.M)
    action_match = re.search(r"^action_type_default:\s*(\S+)\s*$", text, re.M)
    playbook_match = re.search(r"^external_playbook:\s*(\S+)\s*$", text, re.M)
    cap_match = re.search(
        r"^capability_candidates:\s*\n((?:  - .+\n)+)", text, re.M
    )
    if not all([id_match, action_match, playbook_match, cap_match]):
        errors.append(f"Incomplete route metadata: {path.relative_to(ROOT)}")
        continue
    stage_id = id_match.group(1)
    caps = [
        line.removeprefix("  - ").strip()
        for line in cap_match.group(1).splitlines()
    ]
    playbook = playbook_match.group(1)
    alternate_match = re.search(
        r"^external_playbook_candidates:\s*\n((?:  - .+\n)+)", text, re.M
    )
    alternate_playbooks = []
    if alternate_match:
        alternate_playbooks = [
            line.removeprefix("  - ").strip()
            for line in alternate_match.group(1).splitlines()
        ]
    stage_meta[stage_id] = (
        action_match.group(1),
        caps,
        None if playbook == "null" else playbook,
        alternate_playbooks,
    )

for stage_id, (action, caps, playbook, alternate_playbooks) in stage_meta.items():
    if not re.search(rf"^\s{{2}}{stage_id}:\s*\[", manifest, re.M):
        errors.append(f"Manifest missing stage capability candidates: {stage_id}")
    for cap in caps:
        if not (ROOT / "references" / "capabilities" / f"{cap}.md").exists():
            errors.append(f"{stage_id} references missing capability: {cap}")
    if action == "conditional_external":
        if not playbook:
            errors.append(f"{stage_id} is conditional but has no external playbook")
        elif not (
            ROOT / "references" / "action-playbooks" / f"{playbook}.md"
        ).exists():
            errors.append(f"{stage_id} references missing playbook: {playbook}")
    elif action == "prompt" and playbook:
        errors.append(f"{stage_id} is prompt-first but declares playbook: {playbook}")
    elif action not in {"prompt", "conditional_external"}:
        errors.append(f"{stage_id} has invalid action type: {action}")
    if alternate_playbooks and playbook not in alternate_playbooks:
        errors.append(f"{stage_id} default playbook is absent from its candidates")
    for alternate in alternate_playbooks:
        if not (
            ROOT / "references" / "action-playbooks" / f"{alternate}.md"
        ).exists():
            errors.append(f"{stage_id} references missing alternate playbook: {alternate}")

for stage_id in ["E5", "I2"]:
    if not re.search(
        rf"^\s{{2}}{stage_id}:\s*\[[^\]]*web-data-collection[^\]]*\]",
        manifest,
        re.M,
    ):
        errors.append(f"Manifest missing web-data playbook candidate route: {stage_id}")

if errors:
    print("ROUTE VALIDATION FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("ROUTE VALIDATION PASSED")
print(f"Stages checked: {len(stage_meta)}")
