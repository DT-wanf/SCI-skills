# Data Source Choice Card

Use only after data status is `ABSENT` or `INSUFFICIENT`, web evidence is appropriate, and the research question, unit, and scope are sufficiently clear. Never use for `UNKNOWN` or `SUFFICIENT`. Provide two or three topic-specific options; do not force the user to know database or crawler terminology.

## **先选数据来源：能下载就不爬，确有必要再采集网页**

| 方案 | 数据来源与能回答的问题 | 建议字段 | 获取方式 | 费用与权限 | 优点、偏差与难度 |
| --- | --- | --- | --- | --- | --- |
| 1（推荐） | {source_and_fit} | {fields} | {route} | {cost_and_rights} | {tradeoffs} |
| 2 | {source_and_fit} | {fields} | {route} | {cost_and_rights} | {tradeoffs} |
| 3（可选） | {source_and_fit} | {fields} | {route} | {cost_and_rights} | {tradeoffs} |

付费来源必须说明当前价格是否已核实、购买后能够获得什么、研究使用和导出限制，以及免费替代方案。没有核实的价格或权限标记为 `待核实`。

请回复：

```text
我选择的方案：1 / 2 / 3 / 需要重新推荐
预算或机构访问条件：
我希望保留或删去的字段：
其他限制：
```
