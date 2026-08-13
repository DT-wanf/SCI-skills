from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

requirements = {
    "next-stage-prompt-card.md": [
        "## **下一站已开启：复制下面这段 Prompt**",
        "【】中的内容替换成你的真实信息",
        "本阶段验收标准",
    ],
    "repair-prompt-card.md": [
        "## **当前阶段还差一点：复制下面这段 Prompt**",
        "不要进入下一阶段",
        "需要修复的关键缺口",
    ],
    "manual-action-card.md": [
        "## **这一站暂时没有可直接使用的 Prompt：需要先完成真实操作，我会一步一步带你做。**",
        "## 具体操作步骤",
        "## 做到什么算完成",
        "## 完成后带回",
    ],
    "hybrid-action-card.md": [
        "## **操作完成后，复制下面这段 Prompt 发给我**",
        "本次上传的文件",
        "不得把未提供的材料或未完成的操作视为已经完成",
    ],
    "data-source-choice-card.md": [
        "## **先选数据来源：能下载就不爬，确有必要再采集网页**",
        "付费来源必须说明当前价格是否已核实",
        "我选择的方案",
    ],
    "data-acquisition-review-card.md": [
        "## **数据已经采集：请先审核，再进入数据清洗**",
        "宝宝巴士的审核建议",
        "同意进入数据清洗",
        "选择 B 或 C 时保持当前采集环节",
    ],
    "data-cleaning-handoff-card.md": [
        "## **审核通过：下一步进入数据清洗**",
        "复制下面这段 Prompt，开始数据清洗",
        "不得覆盖原始文件",
        "清洗日志",
    ],
    "figure-proposal-card.md": [
        "## **这里建议放一张图：请先确认图位和拆图方案**",
        "为什么建议放",
        "拆图方案",
        "我先上传一张对标图片",
        "用户确认前，不正式生成解释性或视觉增强图",
    ],
    "figure-review-card.md": [
        "## **图片初稿已经生成：请审核后再定稿**",
        "真实输入",
        "实际运行证据",
        "允许插入论文",
        "不使用这张图",
    ],
}

for filename, literals in requirements.items():
    path = ROOT / "templates" / filename
    if not path.exists():
        errors.append(f"Missing template: {filename}")
        continue
    text = path.read_text(encoding="utf-8")
    for literal in literals:
        if literal not in text:
            errors.append(f"{filename} missing: {literal}")

if errors:
    print("PROMPT CARD VALIDATION FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("PROMPT CARD VALIDATION PASSED")
print(f"Templates checked: {len(requirements)}")
