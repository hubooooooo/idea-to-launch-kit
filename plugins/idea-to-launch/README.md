# idea-to-launch 插件

把工具包里的两份技术手册剥离流程后，做成两个可以在任何 AI 产品项目里用的 Claude Code 技能。

| 技能 | 来源手册 | 管什么 |
| --- | --- | --- |
| `agent-tech-stack` | `docs/手册/AI产品Vibe Coding通用技术栈手册.md` | 后端技术基线、按需模块、强制工程底线、双层验收、技术适配声明与阶段文档模板 |
| `agent-frontend-stack` | `docs/手册/AI产品Vibe Coding通用前端技术栈手册.md` | Web 前端技术栈、Agent 任务状态模型、流式与恢复、API 与安全、设计与响应式、浏览器检查与交付 |

上线部署手册绑定腾讯云开发的具体操作，不做成技能，只在工具包里用。

## 安装

在 Claude Code 里：

```text
/plugin marketplace add hubooooooo/idea-to-launch-kit
/plugin install idea-to-launch@idea-to-launch-kit
```

## 和工具包、agent-workshop 的关系

- **工具包本身不变**：规则仍在 `AGENTS.md` 和 `docs/手册/`，支持 Claude Code、Codex、Pi 等任何编码工具。插件只是给 Claude Code 用户多一个入口。
- **在工具包工作区里**：两个技能检测到 `AGENTS.md` 和 `docs/手册/` 时，以工具包规则为准，不另起流程。
- **和 agent-workshop 互补**：`agent-prd` 产出 PRD 与方案，`agent-builder` 按方案做出 Agent；本插件提供做的时候用什么栈、守什么底线、怎么验收。

## 剥离了什么

技能里去掉了只在工具包里成立的内容：阶段 0–5 编号、`kit.sh` / `verify.sh`、证据包与是否表、`docs/项目状态.md` 决策台账 D1–D9、"产品经理"角色（改为"用户"）、腾讯云开发的具体部署步骤。工程规则、默认值、模板保留原意。

## 手册更新时的同步清单

技能内容是手册的副本，改手册时顺手核对下面对应的文件，并把技能 `SKILL.md` 开头的"来源"版本号改成新版本：

| 手册章节 | 对应技能文件 |
| --- | --- |
| 通用手册「本手册的三层规则」、第一节、第三节、第八节 | `agent-tech-stack/SKILL.md` |
| 通用手册第九节、第七节 | `agent-tech-stack/references/engineering-rules.md` |
| 通用手册第十节 | `agent-tech-stack/references/validation.md` |
| 通用手册第二节、二之一、第六节、第三部分 | `agent-tech-stack/references/templates.md` |
| 通用手册第三节「Harness 组件 → 产品实现对照表」 | `agent-tech-stack/references/harness-mapping.md` |
| 通用手册第十一节 | `agent-tech-stack/references/production.md` |
| 前端手册第 1–8、22 节要点 | `agent-frontend-stack/SKILL.md` |
| 前端手册第 9–11、14 节 | `agent-frontend-stack/references/agent-interaction.md` |
| 前端手册第 12、13、18、20 节 | `agent-frontend-stack/references/api-and-security.md` |
| 前端手册第 15–17、19 节 | `agent-frontend-stack/references/design-and-responsive.md` |
| 前端手册第 21、22 节 | `agent-frontend-stack/references/testing-and-delivery.md` |
| 前端手册第 23、24 节 | `agent-frontend-stack/references/templates.md` |

改动只涉及工具包流程（阶段、`verify.sh`、证据包）时，技能不用改。
