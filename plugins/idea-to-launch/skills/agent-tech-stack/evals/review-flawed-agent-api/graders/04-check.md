---
type: llm
focus: trace
weight: 1
---

review.md 指出模型返回的 JSON 未做结构校验（如用 Pydantic），失败会直接异常
