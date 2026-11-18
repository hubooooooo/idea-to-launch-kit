---
tags: [idea-to-launch]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

后端已经好了（FastAPI）：POST /api/v1/tasks 提交一个"写周报"任务，返回 {task_id}；GET /api/v1/tasks/{id} 查状态，status 有 pending/running/need_confirm/done/error；GET /api/v1/tasks/{id}/stream 是 SSE，事件有 chunk、done、error。帮我用 Next.js 写这个生成页的前端：输入框、提交、流式显示结果、中间需要我确认时能点确认。把代码写在当前目录的 weekly-web/ 下，不需要 npm install，代码和一份简短说明就行。
