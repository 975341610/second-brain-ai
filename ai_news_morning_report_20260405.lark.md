<callout icon="star" bgc="5">  
**AI 早报｜2026-04-05（周日）**  
  
**关注：** OpenAI / Claude / Cline / AI Agent  
</callout>

## 今日要点

- **OpenAI**：发布多条公司与产品更新（含“融资 1220 亿美元”、Codex 团队按需付费、收购 TBPN 等）。来源：[OpenAI 新闻动态](https://openai.com/zh-Hans-CN/news/)
- **ChatGPT**：CarPlay 语音对话逐步上线；移动端侧边栏改版；Codex 新增“插件目录”并支持打包 MCP 服务器配置。来源：[ChatGPT — 更新日志](https://help.openai.com/zh-hans-cn/articles/6825453-chatgpt-release-notes)
- **Claude 平台**：面向 Opus 4.6 / Sonnet 4.6 提升批处理单次输出上限；并明确部分旧模型的 1M 上下文 beta 退役时间点。来源：[Claude Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview)
- **Claude Code**：4 月初连续发布多个版本，新增 `/powerup` 等交互式学习功能，并强化 MCP、权限与性能。来源：[claude-code Releases](https://github.com/anthropics/claude-code/releases)
- **Cline**：作为 IDE 内自主编程 Agent，强调“可执行命令 + 可改文件 + 可用浏览器 + 可扩展 MCP 工具”，并支持多家模型/接口。来源：[cline README](https://github.com/cline/cline/blob/main/README.md)

---

## OpenAI（公司与产品）

### 1) 官方新闻条目（4 月初）

- **2026-04-02｜公司：**[OpenAI acquires TBPN](https://openai.com/index/openai-acquires-tbpn/)（标题级信息）
- **2026-04-02｜产品：**[Codex 现已面向团队推出按需付费模式](https://openai.com/index/codex-flexible-pricing-for-teams/)（标题级信息）
- **2026-03-31｜公司：**[OpenAI 融资 1220 亿美元，推动 AI 向全新阶段演进](https://openai.com/index/accelerating-the-next-phase-ai/)（标题级信息）

来源：[OpenAI 新闻动态](https://openai.com/zh-Hans-CN/news/)

### 2) ChatGPT / Codex 体验更新（节选）

- **2026-04-02：**Apple CarPlay 中的 ChatGPT（CarPlay 语音对话逐步推出）。
- **2026-03-26：**移动端侧边栏简化；新增“位置共享”（可选、默认关闭）。
- **2026-03-26：**Codex 上线“插件目录”，支持将技能、应用集成与 **MCP 服务器配置**打包为可安装插件。
- **2026-03-23：**ChatGPT 上线“文件资料库”，便于长期检索与复用上传文件。
- **2026-03-24：**Shopping 更新：商品结果更视觉化、可对比；并提及基于 Agentic Commerce Protocol（ACP）的信息检索与呈现改进。

来源：[ChatGPT — 更新日志](https://help.openai.com/zh-hans-cn/articles/6825453-chatgpt-release-notes)

---

## Claude（Anthropic 平台 & Claude Code）

### 1) Claude Platform（API / Console）

- **2026-03-30：**Message Batches API 面向 Opus 4.6 / Sonnet 4.6 将 `max_tokens` 上限提升到 **300k**（需 beta header）。
- **2026-03-30：**Sonnet 4.5 / Sonnet 4 的 **1M 上下文 beta** 将在 **2026-04-30** 退役；建议迁移到 Sonnet 4.6 / Opus 4.6。

来源：[Claude Platform Release Notes](https://platform.claude.com/docs/en/release-notes/overview)

### 2) Claude Code（节选：4 月初版本）

- **v2.1.92（2026-04-04）：**新增更严格的远程设置拉取策略（失败即退出）；新增 Bedrock 交互式配置向导；/cost 增强等。
- **v2.1.90（2026-04-01）：**新增 `/powerup` 交互式功能教学；多项性能与稳定性修复。

来源：[claude-code Releases](https://github.com/anthropics/claude-code/releases)

---

## Cline（自主编程 Agent）

- **定位：**“能用 CLI 和编辑器的 AI 助手”，在用户逐步授权下，可创建/编辑文件、运行终端命令、用浏览器做交互式调试。
- **关键能力：**支持多家 API/模型；支持通过 **MCP** 接入社区工具或“让 Agent 自己创建并安装新工具”。

来源：[cline README](https://github.com/cline/cline/blob/main/README.md)

---

## 行业趋势观察（从“对话”到“可执行的智能体”）

1. **编程智能体竞争白热化：**OpenAI Codex（插件 + MCP 打包）、Anthropic Claude Code（高频迭代）、Cline（IDE 内自治执行）共同指向“任务闭环”的开发方式。
2. **长上下文 / 长输出成为默认军备：**Claude 在平台层提升批处理输出上限并围绕 1M 上下文做迁移引导；面向开发/研究/长文档任务的能力持续上探。
3. **MCP 成为共同语言：**Cline 明确以 MCP 扩展工具；OpenAI Codex 插件亦支持打包 MCP 服务器配置——“工具生态标准化”正在加速。

