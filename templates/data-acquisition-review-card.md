# Data Acquisition Review Card

Use after pilot or full collection and before any destructive cleaning or analysis.

## **数据已经采集：请先审核，再进入数据清洗**

### 采集结果摘要

| 审核项 | 实际结果 | 建议 |
| --- | --- | --- |
| 数据来源与获取方式 | {source_and_route} | {source_advice} |
| 时间、地区与样本范围 | {scope} | {scope_advice} |
| 计划字段与实际字段 | {field_match} | {field_advice} |
| 记录数、缺失与重复 | {quality_profile} | {quality_advice} |
| 失败、排除与已知偏差 | {failures_and_bias} | {bias_advice} |
| 费用、许可、隐私与伦理 | {rights_status} | {rights_advice} |
| 原始文件、日志与数据字典 | {evidence_files} | {evidence_advice} |

### 宝宝巴士的审核建议

{prioritized_review_advice}

在审核通过前，只能进行不改变原始数据的概况检查。不要直接去重、删除、填补、翻译、编码或分析。

请回复一个选项：

```text
A. 我确认数据来源、范围和字段符合研究目标，同意进入数据清洗。
B. 数据暂不通过；请先修改字段、排除规则或采集设置。
C. 数据暂不通过；需要补充样本、更换来源或重新采集。

我的选择：A / B / C
我要求保留的原始字段：
我要求删除或补充的内容：
其他审核意见：
```

选择 A 后，先保留只读原始数据和采集日志，再创建处理副本，并生成项目专用的数据清洗 Prompt。选择 B 或 C 时保持当前采集环节，不得进入清洗。
