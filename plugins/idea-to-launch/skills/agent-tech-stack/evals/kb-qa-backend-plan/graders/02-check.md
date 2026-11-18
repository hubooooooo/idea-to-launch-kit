---
type: llm
focus: trace
weight: 1
---

流式问答接口的事件序列以 done 或 error 结束，且模型客户端初始化失败（如缺少 Key）也以 error 事件返回而不是直接断流
