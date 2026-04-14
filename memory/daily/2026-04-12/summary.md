
## 01:04:49
- 用户询问项目进度，随后报告了后端服务连接被拒绝（ECONNREFUSED 0.0.0.0:8765）以及前端直接输出原始 SSE 数据流（如 data: {"text": "..."}）的错误。
- 修复了本地 AI (Gemma) 的异步阻塞和 StopIteration 报错问题，梳理了后端调用实例与初始化逻辑，恢复了流畅的流式输出。
- 新增了 Web Search 功能，为 AI 增加了 search 动作，支持通过 DuckDuckGo 搜索并提取网页摘要来辅助回答。
- 修复了后端服务异常退出的问题，在 8765 端口重新启动了后端进程。
- 修复了 DuckDuckGo 的 HTML 结果解析逻辑，确保能够正确抓取文本内容。
- 修复了 AI 输出流的中文编码问题，在后端的 local_ai.py 的 generate_chat_stream 中将 json.dumps 设置为 ensure_ascii=False，以支持中文字符的正确序列化。
- 修复了前端未正确解析 SSE 响应的缺陷，修改了 nova_repo/nova-block/src/lib/api.ts 中的 streamInlineAI 函数，使其能够解析 SSE 响应行并正确提取和渲染 text 字段。
- 重新打包了前端代码并更新至后端的 static 和 frontend_dist 目录，完成了所有修复代码的本地 commit 提交。

## 10:23:04
- 用户提出 AI 深度融合编辑器功能的需求（如自动设置标题、生成标签、插入表格等），期望 AI 能直接调用编辑器原生功能。
- 开发了 AI 编辑器指令系统，修改底层 Prompt，引导 AI 生成特定 XML 动作标签（如 `<Action type="set_title">`、`<Action type="set_tags">`）。
- 在前端新增了流式数据拦截解析器（Stream Command Parser），用于在文本渲染前拦截 `<Action>` 标签，并将其转化为真实的 Tiptap 编辑器 API 调用（自动设置 H1 标题、更新标签状态）。
- 针对用户反馈 AI 依旧只输出普通文本的问题，引入了基于 `【】` 符号（如 `【生成合适的标题】`）的“强指令模式”。后端在匹配到该符号时会向 AI 注入最高优先级系统规则，强制要求其仅输出特定的 XML 动作代码。
- 扩展了编辑器的 AI 动作指令，新增支持插入代码块（`insert_code_block`）、插入待办事项（`insert_todo`）以及精准插入纯文本（`insert_text`）。
- 修复了因 SSE 流式传输分块导致 XML 标签被截断（如 `<Act` 和 `ion>` 分批到达）从而失效漏出的缺陷。
- 重构了前端的 `streamBuffer` 拦截逻辑，当缓冲区存在未闭合的 `<Action` 开头时阻塞文本放行，直到拼凑出完整的 `</Action>` 结尾才触发编辑器操作。
- 优化了前端的指令提取正则表达式，使其兼容换行符，解决了多行文本（如多行代码块）匹配失效的问题。

## 10:56:38
- 用户反馈插入代码块和生成 H1 标题功能仍不可用。
- 排查确认前置流式截断修复存在逻辑缺陷，`<Action>` 标签的半截字符串会被提前作为普通文本渲染，已启动针对 `NovaBlockEditor.tsx` 流式接收池（Buffer）的底层深度重构任务。
- 根据用户提供的 `unsloth/gemma-4-E2B-it-GGUF` 链接，排查发现原模型文件仅 389MB，指令遵循能力不足。
- 下载了完整的 2.9GB `gemma-4-E2B-it-Q4_K_M.gguf` 模型并部署至 `nova_repo/data/models/` 目录，替换了原有的劣质模型。
- 将后端的 `llama-cpp-python` 引擎升级至 `0.3.20` 版本，解决了旧版引擎不支持 Gemma 4 架构导致加载报错的问题，并成功运行了新模型唤醒测试。

## 14:02:18
- 完善了 Tiptap 原生 API 封装逻辑：`set_title` 自动在文档开头插入或覆盖已有 H1 标题；`insert_code_block` 调用 `insertContent({ type: 'codeBlock' })` 生成真正的代码块节点；`set_tags` 在标题下方生成标准格式的标签。
- 修复了更换 Gemma 模型后输出乱码的问题：在 `local_ai.py` 的 `Llama` 实例中强制注入 `chat_format="gemma"` 以匹配其专属对话模板。
- 修复了普通对话文本无法流式输出的问题：调整 `NovaBlockEditor.tsx` 的缓冲器（Buffer）逻辑，当检测到首字符非 `<` 时立即泄洪放行文本上屏。
- 优化了交互体验：在前端新增了 `⏳ AI 思考中...`（`setIsAILoading`）的加载状态提示，填补模型冷启动期间的界面空白。
- 修复了云端网页版更新未生效的问题：排查并使用 `kill -9` 终止了长期占用 `8765` 端口的旧版 `python3 main.py` 僵尸进程，并重新拉起服务。
- 修复了用户输入后无任何响应（请求空转）的严重缺陷：
  - 解决了引入 `setIsAILoading` 时作用域控制不当导致的 `NovaBlockEditor.tsx` TypeScript 编译报错（该报错导致前端 Vite 打包失败，旧代码持续生效）。
  - 排查后台日志发现全局 AI 开关被关闭，将 `backend/api/routes.py` 中的 `ai_enabled` 强制恢复为 `True`。
- 协助用户排查了前端页面版本滞后的问题，指导用户通过强制刷新（硬性重新加载）清除浏览器旧版缓存，以拉取打包更名后的最新 JS 静态文件。

## 19:56:36
- 修复了 AI 流式输出期间因 Nginx 反向代理超时导致的连接中断问题（`ERR_INCOMPLETE_CHUNKED_ENCODING` 报错）：通过在模型返回首字符前发送包含 4096 字节空格的 SSE 注释强制冲刷代理缓冲区；在响应头中添加 `Cache-Control: no-cache, no-transform` 禁用代理缓存；并将 Uvicorn 的 Keep-Alive 存活时间强行延长至 65 秒。
- 在获得用户明确授权后，将流式输出与网关穿透补丁代码成功推送至 `nova` 项目的远程 `main` 分支（Commit ID: `c5984db`）。
- 协助用户排查了本地拉取代码后启动后端闪退及前端提示 `ERR_CONNECTION_REFUSED` 的问题：定位到错误原因是 `backend/api/routes.py` 中的硬件状态监控功能缺少相关库（`ModuleNotFoundError: No module named 'psutil'`）。
- 将缺失的 `psutil` 依赖项补充至代码库的 `requirements.txt` 中并推送到远程 `main` 分支（Commit: `chore: add psutil to requirements.txt`），并指导用户在本地执行 `pip install psutil` 以解决启动报错。

## 20:57:55
- 修复了用户反馈的 `/api/ai/spellcheck` 接口因 500 内部服务器错误引发的跨域（CORS）报错问题：定位到错误根因为后端 Python 代码中构造包含 JSON 示例的 `prompt` 字符串时，使用了未转义大括号 `{}` 的 `f-string`，导致触发 `ValueError: Invalid format specifier` 异常。
- 修改了 `nova_repo/backend/api/routes.py` 代码，将 `prompt` 的构造方式由 `f-string` 替换为普通字符串拼接，成功解决了该报错（接口测试正常返回 `{"errors": []}`），并清理旧进程重新拉起了服务。
- 经用户授权同意，将上述报错修复代码及更新后的 `DEVELOPMENT_LOG.md` 日志文件推送至 GitHub 远程代码库。

## 22:30:19
- 根据用户需求，将原有基于本地小模型的拼写检查接口重构为纯规则引擎：引入 `pyahocorasick` 库实现 Aho-Corasick 自动机极速匹配，结合正则模板处理高频词搭配校验（如“的/地/得”、“在/再”），并增加白名单保护机制以跳过专有名词。
- 采用测试驱动开发（TDD）编写了全套单元测试（`spellcheck_test.py`），同时将前端 Tiptap 插件的请求防抖延迟从 2500ms 缩短至 800ms 以提升输入反馈灵敏度。
- 将重构后的拼写检查代码推送到 `feature/novablock-spellcheck-refactor` 分支后，应用户要求将其直接合并入远程仓库的 `main` 分支并删除了临时特性分支，同时指导用户在本地安装新增的 `pyahocorasick` 依赖（更新了 `requirements.txt`）。
- 针对用户反馈新规则引擎未生效且后端日志中无 `/api/ai/spellcheck` POST 请求的问题，排查定位为前端 `AISpellcheck.ts` 中的触发逻辑失效（`compositionend` 事件未正确绑定至 Tiptap 实例）。
- 修复了前端触发 Bug，将中文输入法监听重构为 Tiptap 原生插件级别，确保中文上屏或键盘正常停顿均能正确唤醒接口请求；同时修复了单句中存在多处相同错词时的红线渲染定位错误，并将相关修复推送至 `main` 分支。
