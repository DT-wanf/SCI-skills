from pathlib import Path
import sys

HEADINGS = [
    "## **下一站已开启：复制下面这段 Prompt**",
    "## **当前阶段还差一点：复制下面这段 Prompt**",
    "## **这一站暂时没有可直接使用的 Prompt：需要先完成真实操作，我会一步一步带你做。**",
    "## **先选数据来源：能下载就不爬，确有必要再采集网页**",
    "## **数据已经采集：请先审核，再进入数据清洗**",
    "## **审核通过：下一步进入数据清洗**",
    "## **这里建议放一张图：请先确认图位和拆图方案**",
    "## **图片初稿已经生成：请审核后再定稿**",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python audit_output_contract.py RESPONSE.md")
        return 2
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    found = [heading for heading in HEADINGS if heading in text]
    errors: list[str] = []
    if len(found) != 1:
        errors.append(f"Expected exactly one primary action-card heading, found {len(found)}")
    if found and found[0] == HEADINGS[2]:
        for required in ["具体操作步骤", "做到什么算完成", "完成后带回"]:
            if required not in text:
                errors.append(f"Manual action card missing section: {required}")
    if found and found[0] == HEADINGS[3]:
        for required in ["费用与权限", "我选择的方案"]:
            if required not in text:
                errors.append(f"Data-source choice card missing section: {required}")
    if found and found[0] == HEADINGS[4]:
        for required in ["采集结果摘要", "宝宝巴士的审核建议", "我的选择：A / B / C"]:
            if required not in text:
                errors.append(f"Data-acquisition review card missing section: {required}")
    if found and found[0] == HEADINGS[5]:
        for required in ["不得覆盖原始文件", "清洗日志", "按 E5 验收标准"]:
            if required not in text:
                errors.append(f"Data-cleaning handoff card missing section: {required}")
    if found and found[0] == HEADINGS[6]:
        for required in ["为什么建议放", "拆图方案", "请选择"]:
            if required not in text:
                errors.append(f"Figure proposal card missing section: {required}")
    if found and found[0] == HEADINGS[7]:
        for required in ["证据与运行状态", "宝宝巴士的审核建议", "请选择"]:
            if required not in text:
                errors.append(f"Figure review card missing section: {required}")
    if any(shortcut in text for shortcut in ["自行检索。", "下载CSV后再来。", "完成实验后再来。"]):
        errors.append("Found a forbidden vague external-action shortcut")
    if errors:
        print("OUTPUT CONTRACT FAILED")
        for error in errors:
            print("-", error)
        return 1
    print("OUTPUT CONTRACT PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
