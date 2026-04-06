<title>Aime | 写代码最佳实践</title>
<url>https://bytedance.larkoffice.com/wiki/BTsIwdcZViUMbCkyc68cN2k6nLh</url>
<content>
最近更新：2026-01-09

<callout icon="dizzy" bgc="4" bc="4">
Aime 是什么？ [Aime — 开启字节同学的异步办公新体验](https://bytedance.larkoffice.com/wiki/XxvZwyuyUiTlDEkrEHacSMJKnFe)
Aime 是专为字节同学打造的 AI Agent 工作平台，面向工作场景，集成了字节内部常用工具，帮助大家高效完成各类繁琐重复的任务，包括但不限于：写代码、分析数据、做调研、写文档 等。
这篇文章将教会你如何玩转 Aime **写代码**，助力研发提效！
</callout>

## 使用 Aime 异步研发
**使用Aime 研发与传统 AI 助手不同**

- 对于传统的 IDE 内 AI 助手
你在本地写代码，和 IDE 里的 AI 助手一问一答、实时协作。好处是立刻可用，但你得时刻盯着进度、不断同步上下文，还要手动拆分与追踪任务。

- 使用 Aime 写代码
每个任务都会启动一个“远程智能代理”（agent），在独立、专属且安全的环境中运行，并拥有独立工作空间。你可以在同一个代码库里同时**<font color="blue">开多个任务</font>**，彼此互不干扰，真正做到**<font color="blue">并行推进</font>**。它们能够从一个初始描述出发，一直工作到提交最终的 Merge Request，期间几乎无需人为干预。

换句话说，Aime 不是一个聊天式助手，而是**<font color="blue">“可并行工作的工程师”</font>**。它能**<font color="blue">独立</font>**拉起任务、持续执行、产出可交付成果，并在需要时再把关键结果交还给你。

![board_F7Fdw077yh5zUVbS3meltqCQgdb](board_F7Fdw077yh5zUVbS3meltqCQgdb.drawio)

**Aime 给研发带来的核心价值**

- **<font color="blue">专注高价值工作，减少重复劳动</font>**

把那些规则明确、实现直接的子任务交给 Aime（例如：接口封装、单元测试补齐、简单脚手架搭建）。你可以把精力放在架构设计、关键决策、复杂问题求解等更有创造力的工作上。

- **<font color="blue">清理低优先级的积压需求</font>**

文档补全、类型标注、依赖升级、代码规范化、边角功能修复，往往因为“优先级不高”而无限期延后。Aime 能持续清仓这类任务，稳步提升代码库健康度和产品质量。

- **<font color="blue">作为“弹性人力”，补上人手短板</font>**

把 Aime 当作一支可随时扩容的工程小队。过去因为人手不足而放弃的事情（如老项目重构、引入观测性/细粒度日志、梳理性能瓶颈），现在都可以启动并推进。

- **<font color="blue">加速项目启动</font>**

让 Aime 先搭好地基：初始化仓库、生成项目脚手架、配置 CI/CD、铺好目录结构与基础模块。你接手时即可直接进入关键实现，省去大量重复的准备工作与口头同步。

## 核心能力
要实现上面这些核心价值，Aime 依赖于其背后坚实的技术底座，Aime 深度融合了先进的 **Agent 技术**、**大模型能力**、**研发知识**与**工程平台**，为研发场景带来了以下四大核心能力：

<grid cols="2">
<column width="50">
  **<font color="blue">核心能力一：动态规划</font>**
  - 强大**动态规划能力，**能够根据任务自动生成可执行计划，拆解子任务、明确依赖与验收标准。
  - 在执行中遇到阻塞时，可**自动纠错**、**调整路线**、**改变优先级**或**替换备用方案**，动态适应变化以确保任务达成。
</column>
<column width="50">
  **<font color="blue">核心能力二：研发知识</font>**
  - **内置字节研发知识**，汇集了公司内场的核心基库、技术文档、编码规范与最佳实践，构建了强大的**专属知识库**。
  - 支持知识召回与工具调用，降低找文档的时间成本。
</column>
</grid>

<grid cols="2">
<column width="50">
  **<font color="blue">核心能力三：仓库理解</font>**
  - **强大的代码搜索：**支持精准、高效的代码搜索，快速定位**函数定义**、**变量引用**和**跨文件调用**。
  - **深度结构解析**：自动梳理现有代码库的**结构**、**模块依赖**与**函数调用链**，快速建立上下文。
  - 自动学习并遵循**现有仓库的编码风格**与**设计模式**，确保 Aime 产出的代码在规范上保持一致，无缝集成。
</column>
<column width="50">
  **<font color="blue">核心能力四：研发平台集成</font>**
  - **深度集成 Bits Code，**支持**创建分支**、**推送 Commit** 及**创建 MR** 等日常代码管理操作，简化工作流。
  - **打通构建与发布，**无缝对接 SCM 与 TCE，实现从**代码提交**到**产物构建**及**服务发布**的全流程自动化。
  - **无缝融入WebIDE，**支持集成 **WebIDE** 环境，在浏览器中提供“开箱即用”的开发体验。
</column>
</grid>

<font color="green">Aime 具备了强大的规划、知识、理解和集成能力。然而，一个强大的工具并不等同于能自动产出</font>**<font color="green">高质量的结果</font>**<font color="green">。</font>

这就引出了一个最关键的问题：我们（作为开发者）应该如何“指挥”Aime，才能真正驾驭它的能力，而不是让它“翻车”？

## 最佳实践
<callout icon="bulb" bgc="7" bc="2">
在使用 Aime 时，我们会遇到这种问题：简单的代码改动或者bug修复时表现惊艳，但真正生产级别的代码生成时，却是漏洞百出、无法与现有工程融合的代码。
相比于将问题归咎于“模型能力”不足或者 Aime 有点“菜”，补全**缺失的信息输入**更能帮你在用好 Aime 上**快人一步**。AI 就像一个初级开发者，你没有给他足够的信息（比如代码库规范、API 文档或设计稿），它就只能“猜测”着完成任务，结果自然漏洞百出。
</callout>

### **<font background_color="light_green">让</font>****<font background_color="light_green">Aime 更懂你</font>****<font background_color="light_green">的需求</font>**
<grid cols="2">
<column width="50">
  **✅<font color="green">&nbsp;明确“从哪开始”：提供关键技术上下文</font>**
  - 想一想，如果是你自己处理这个任务，您会先打开哪个代码库、哪个文件或哪篇文档？
  - 主动提供这些“起点”信息（如：**代码仓库**、**关键模块/函数**、相关的 **PRD** 、**错误日志或并必要的代码片段**），可以最大限度地减少 Aime 的无效探索。
  - 分享相关的**技术文档**、**PRD** 或**设计方案**的链接。
  - **示例**：“添加 xxx 模型支持。你应该在 `model_groups` 目录下创建一个新文件，并参考 `[内场文档链接]` 上的最新 API 规范。”
</column>
<column width="50">
  **✅&nbsp;<font color="green">明确“怎么做”，而不只是“做什么”</font>**
  - 把 Aime 想象成一个初级的编码伙伴，其决策可能并不可靠。对于复杂任务，**请从一开始就清楚地概述您首选的方法、架构或逻辑**。
  - 这不仅能提高 Aime 的**成功率**，也能大幅减少您的 Review 时间。
  - **示例**：不要只说“添加单元测试”，而应具体说明：“请为 `GetProfile` 功能添加单元测试，重点覆盖‘用户不存在’和‘DB 连接失败’这两个边界情况，并明确 `Redis` 依赖需要被 mock。”
</column>
</grid>

<grid cols="2">
<column width="50">
  **✅&nbsp;<font color="green">将复杂任务分解为明确的开发步骤</font>**
  - 将大型重构或功能开发拆解为清晰的步骤，将极大提升执行的准确性。
  - **示例**：“1. 在 `UserService` 中添加 `GetProfile` 接口；2. 在 `ProfileService` 中实现该接口的逻辑；3. 为新接口编写单元测试，覆盖xx和xx场景。”
</column>
<column width="50">
  **✅&nbsp;<font color="green">提供代码示例或模板</font>**
  - 分享符合预期的**代码片段**、**函数实现**或**设计模式**作为参考，Aime 会智能适配和遵循。
  - **示例**：“新接口的命名风格请遵循现有的 `GetUser` / `SetUser` 模式”、“请参考这个函数的错误处理方式 [代码片段]”。
</column>
</grid>

<grid cols="2">
<column width="50">
  **✅&nbsp;<font color="green">践行“防御性指令”：预判 Aime 的困惑点</font>**
  - 想象一下您把同一个指令给一个新来的实习生，他们可能会在哪里感到困惑或犯错？
  - **主动在指令中澄清这些潜在的歧义点或“坑”**。
  - **示例**：“请修复搜索模块的 Bug。**注意**：这个模块有很重的缓存逻辑，你在修改后**需要调用 xxx 来清理缓存**才能在测试环境验证结果。”
</column>
<column width="50">
  **✅&nbsp;<font color="green">定义“验收标准”与“反馈闭环”</font>**
  - Aime 的强大之处在于它能**根据明确的标准和工具反馈进行自我修复**。请明确告知它“成功”的定义。
  - **明确规范与格式**：告知 Aime 必须遵循的标准和产出格式。（示例：“代码需符合 Go Lint 规范”、“需要覆盖边界情况的单元测试””、“请为 public 函数添加 TSDoc 注释”。）
  - **引导利用工具**：Aime 已深度集成研发平台，引导它使用这些工具进行自检。（示例：“使用 SCM 进行编译，并自动修复编译错误。”）
</column>
</grid>

---

### **<font background_color="light_orange">避免让</font>****<font background_color="light_orange">&nbsp;Aime “蒙圈”</font>**
<grid cols="2">
<column width="50">
  - **❌ 让 Aime 猜测你的意图**
  	- **Aime 无法通灵👻**。这会迫使它在多个可能性中随意发挥，浪费执行时间。
  	- “帮我看看这个服务。”（看什么？性能？日志？还是代码？）
</column>
<column width="50">
  - **❌ 指令过于简短，缺乏上下文**
  	- **缺少具体的目标和范围，**这会导致 Aime 无法定位问题，甚至无法开始规划任务。
  	- “修复这个 Bug。”（哪个 Bug？复现路径？报错信息？）
  	- “给我写个单测。”（为哪个函数写？需要覆盖哪些 Case？）
</column>
</grid>

<grid cols="2">
<column width="50">
  - **❌ 假设 Aime 知道历史上下文**
  	- **反例**：“给刚才那个函数加个缓存。”（如果会话已中断或过长，Aime 可能已忘记“刚才那个函数”是什么。）
  	- **反例**：“在我的项目里加个新功能。”（Aime 无法直接访问“你的项目”。）
</column>
<column width="50">
  - **❌ 要求模糊，标准主观**
  	- **AI 无法理解主观标准**。“好”、“合格”、“健壮”这类词无法被转化为可执行、可衡量的验收标准。
  	- “让这段代码更‘健壮’一点。”（“健壮”是指错误处理、输入校验还是重试机制？）
  	- “写一个‘好’的重构方案。”（“好”是指性能、可读性还是可维护性？）
</column>
</grid>

- **❌ 缺乏对产出格式的指导**
	- **Aime 会猜测你想要的产出**。它可能会默认生成代码，而您想要的其实是技术文档或序列图。
	- “给我这个模块的设计。”（需要的是技术文档、UML 图还是伪代码？）
	- “分析一下这段代码。”（分析性能、复杂度、安全漏洞还是编码风格？）


### 实践样例
<callout icon="tangerine" bgc="15" bc="2">
Tips: 在 Aime 内通过 **@仓库分支** 功能来精准选择开发分支
</callout>

#### Bugfix
> 当人力不足时，突然有一个插入的 panic，可以使用 Aime 帮你修复简单 bug，补上人手短板。
> 
> 模板分享：https://aime.bytedance.net/chat?autoreg=true&share_id=7011a7b0-c9ed-468c-b274-45c51ec01b29
> 

<callout icon="point_up" bgc="4" bc="2">
帮我修复一个线上 Panic：在 `GetHomepageData` 接口中，如果用户没有 `widgets`，会引发空指针解引用。
1. **<font color="blue" background_color="light_green">(关键上下文)</font>** 这是 Panic 堆栈日志：xxxx.... 
2. **<font color="blue" background_color="light_green">(防御性指令 & 怎么做</font><font color="blue" background_color="light_green">，如果你知道的话可以帮忙缩小范围</font><font color="blue" background_color="light_green">)</font>**<font color="blue" background_color="light_green"> </font>在 `homepage_service.go`里找到 panic 的地方，然后添加一个**空指针检查**。
3. **<font color="blue" background_color="light_green">(验收标准</font><font color="blue" background_color="light_green">，提升结果可用性</font><font color="blue" background_color="light_green">)</font>** 补一个单测来确保你的改动生效
4. <font color="blue" background_color="light_green">(</font>**<font color="blue" background_color="light_green">交付</font><font color="blue" background_color="light_green">，你希望的结果呈现方式</font><font color="blue" background_color="light_green">)</font>** 创建一个 bugfix，然后创建一个 MR  / 总结一份文档
</callout>

#### 后端 API 开发
> 这类规则明确、实现直接，可以参考现有实现的工作交给 Aime，降低重复工作，让自己更聚焦。
> 
> 任务分享：https://aime.bytedance.net/share/eb7c5849-7a15-42c5-ab1a-d73b032f4c22
> 

<callout icon="v" bgc="4" bc="2">
帮我添加一个获取用户配置（`UserProfile`）的新接口。
1. **<font color="blue" background_color="light_green">(从哪开始 & 怎么做)</font>** 你需要先在 `api/idl/user.thrift` 中添加一个 `GetUserProfile(request)` 方法，然后在 `service/user_service.go` 中实现它。
2. **<font color="blue" background_color="light_green">(防御性指令 & 步骤)</font>** 修改 `thrift` 文件后，**运行&nbsp;**`kitex user_service.thrift`
3. **<font color="blue" background_color="light_green">(参考范例)</font>** `user_service.go` 中的 `GetAccountInfo` 方法是你的参考范例，请遵循它的错误处理和 DTO 转换逻辑。
4. **<font color="blue" background_color="light_green">(验收标准)</font>** 你需要为 `GetUserProfile` 添加新的单元测试（Mock 掉 `DAO` 层调用），并确保 `go lint` 和 `go test` 全部通过。
5. **<font color="blue" background_color="light_green">(注意事项)</font>**<font color="blue" background_color="light_green"> </font>确保的 kitex 是 vx.x.x 版本，最新版会有问题
</callout>

#### 前端组件开发
> 优先级不高的需求，使用 Aime 来并行完成，最后统一验收 ！
> 

<callout icon="ok_hand" bgc="4" bc="2">
请在 `src/components/ApiTokenCard.vue` 里添加一个‘复制到剪贴板’功能。
1. **<font color="blue" background_color="light_green">(从哪开始 & 怎么做)</font>**<font color="blue" background_color="light_green"> </font>在 token 字符串旁边添加一个图标按钮（icon-only button）。
2. **<font color="blue" background_color="light_green">(参考范例 & 防御性指令)</font>** 图标请使用我们 `BaseIcon` 库里的 `CopyIcon`。你必须使用 `src/composables/useClipboard.js` 中已有的 `useClipboard` 组合式函数来实现逻辑，不要自己写 `execCommand`。
3. **<font color="blue" background_color="light_green">(验收标准 & 防御性指令)</font>** 复制成功后，按钮需要显示一个 ‘已复制!’ 的 Tooltip 提示，持续 2 秒。同时，确保新按钮的样式和卡片上其他图标按钮的风格完全一致。`npm run lint` 必须通过。
</callout>

#### 项目启动
> 用 2 分钟下达了指令，Aime 帮你完成了所有 Web 服务相关的体力活。您不需要关心 FastAPI 的语法，而是可以立即打开 Aime 生成的 load_intent_model 函数，开始专注于算法模型这一高价值工作。
> 
> 任务分享：https://aime.bytedance.net/share/6081b0b4-96e6-4ae4-b3f8-d636047ddd54
> 

<callout icon="raised_hand_with_fingers_splayed" bgc="4" bc="2">
帮我用 **Python&nbsp;**快速搭一个‘意图识别’的 API 接口。
1. **<font color="blue" background_color="light_green">(怎么做)</font>**
	- 使用 **FastAPI** 框架。
	- 包含 `main.py` 和 `requirements.txt` (包含 `fastapi` 和 `uvicorn`)。
	- `main.py` 中**必须**包含一个 `POST /intent` 接口。
	- **实现基本的接口错误处理逻辑**
	- 接口的输入输出的结构体都是 string
2. **<font color="blue" background_color="light_green">(注意事项&验收标准)</font>**
	- 你需要在 `main.py` 里留一个**空的**、**带注释**的 TODO 给我：
	- 确保 `POST /intent` 接口调用了这个 `load_intent_model` 函数。
	- 最终我能直接运行 `uvicorn` 启动服务，并且能用 `curl` 调通 `/intent` 接口
</callout>

## 使用姿势
> 持续补充中
> 



<table header-row="true" col-widths="165,467,795">
    <tr>
        <td>场景</td>
        <td>使用方式</td>
        <td>分享</td>
    </tr>
    <tr>
        <td>**前后端需求开发**</td>
        <td>1. 提供 PRD，业务上下文
2. 提供 IDL/设计稿 等
3. 注明业务开发规范和注意事项
	1. 在哪个仓库/文件夹开发
	2. 是否要指定开发分支？
	3. 是否要提交 MR?
	4. 是否要写单测？
	5. 能够提供一个开发流程/SOP ？
4. 预期的产出以及验收标准等</td>
        <td>- [从 0 到 1：用 Aime 在 Lark 邮箱后端完成生产级需求的实践复盘](https://bytedance.larkoffice.com/docx/Fl9kdUFDgoI4SVxNg8PchjWLndg)
- [Aime在即梦服务端的最佳实践](https://bytetech.info/articles/7520457489080008744?fromIdType=55&fromId=7516716922617249801#NVNld8IcGoLtO6xF6bKcTOAon1d)
- [告别 Demo，Coding Agent 生产级需求迭代实践](https://bytetech.info/articles/7550195650751643657?to=award_month&from=email#Qxnydan2loRrEqx4YV5c0Y7knUd)
- [后端 AI 提效的关键工作--星图的实践和思考](https://bytetech.info/articles/7565868065272168499?fromIdType=55&fromId=7516716922617249801#WziydcD1Qo2Y3xx10w5cfoilndh)
- [AI Coding 在 后端研发流程 中的探索与实践 - Spec Coding 与  Context Engineering ](https://bytetech.info/articles/7553126165771190313?fromIdType=55&fromId=7516716922617249801)</td>
    </tr>
    <tr>
        <td>**RPC 接入开发**</td>
        <td>1. 开启 Overpass MCP
2. 指定需要接入的 RPC 对应的 PSM 和对应方法
3. 要说明你需要调用的接口要完成的具体业务功能</td>
        <td>- https://aime.bytedance.net/share/d34044fa-637f-42cd-9a18-7c9f7208fa00</td>
    </tr>
    <tr>
        <td>**后端 SDK 替换/升级**</td>
        <td>1. 明确定义被替换的（源）API/SDK/库，以及要迁移到的（目标）API/SDK/库
2. 转换指南，说明每项功能、命令、参数从源到目标的映射关系或者大致指南
3. 提供注意事项</td>
        <td>- https://aime.bytedance.net/chat?autoreg=true&share_id=d6d8c8ce-e7aa-4132-b3b2-26cb8a89969b&spaceId=8f497417-260c-4cdb-8794-e51b7cee31fe
	- https://aime.bytedance.net/share/20b61d0c-412b-4ab9-ad8e-227b6f2de968</td>
    </tr>
    <tr>
        <td>**Panic 修复**</td>
        <td>1. 提供 panic 的堆栈或者堆栈获取方式
2. 说明具体的修复需求</td>
        <td>- https://aime.bytedance.net/chat?autoreg=true&share_id=591c203c-2166-40ef-9657-aadb5efe887b
	- https://aime.bytedance.net/share/6087fd9b-8c92-4b64-8c9d-b85a3bf40407
- https://aime.bytedance.net/chat?autoreg=true&share_id=7011a7b0-c9ed-468c-b274-45c51ec01b29</td>
    </tr>
    <tr>
        <td>**代码排障**</td>
        <td>1. 描述问题，并附上准确的错误信息或日志输出。
2. 提供调用该库的具体代码片段，包括所有传入的参数，是否有可复现的方式
3. 明确说明任务目标，例如在库源码中找到根本原因，或在你的代码中实施修复</td>
        <td>- https://aime.bytedance.net/share/12ffc545-6b00-4a5c-8037-309a08e853ab
- https://aime.bytedance.net/chat?autoreg=true&share_id=d1ca8788-e837-46ea-85b4-0f022e190d53
- https://aime.bytedance.net/chat?autoreg=true&share_id=d3c328b0-1af7-437b-9ef5-e50b71973894</td>
    </tr>
    <tr>
        <td>**代码重构**</td>
        <td>1. 重构的核心目的（如提升性能、改善可维护性、技术栈迁移），并明确界定哪些代码模块、接口或功能在此次重构范围之内
2. 提供待重构代码的准确位置（如分支、关键文件路径）以及任何必要的背景知识（如当前实现的主要逻辑、已知问题）
3. 指明必须使用或替换的技术栈、框架、库，以及处理数据访问、外部依赖和接口调用的新规则</td>
        <td>- https://aime.bytedance.net/chat?autoreg=true&share_id=3b5050f1-e400-4614-904c-b133409c3642&spaceId=cd07dd6b-8847-4abe-b949-d2b877e21ce1</td>
    </tr>
    <tr>
        <td>**代码迁移**</td>
        <td>1. 明确指出源（旧）和目标（新）代码的仓库、分支、文件及函数/方法名称质量要求
2. 明确列出迁移的重点（如：行为一致性、安全性、并发、兼容性）。
3. 简要说明本次迁移的目的（如：重构、功能增强、修复问题）</td>
        <td>- https://aime.bytedance.net/share/15b6b97a-44b3-4b34-bae5-e9c8b65aad11</td>
    </tr>
    <tr>
        <td>**前端依赖升级**</td>
        <td>1. 确定需要升级的具体依赖包
2. 指定要升级到的确切版本号
3. 提供新版本的变更日志（Changelog）或迁移指南，尤其是关于重大变更（Breaking Changes）的说明
4.  说明升级集成后，应如何验证</td>
        <td>- https://aime.bytedance.net/share/b23083ac-6f39-452a-b15a-b0e58ab794b9</td>
    </tr>
    <tr>
        <td>**前端埋点**</td>
        <td>1. 提供描述所有埋点事件、触发时机（如点击、曝光）和业务场景的详细需求
2.  包含每个事件的准确名称（Event Name）和需要上报的参数（Properties）及其格式
3. 说明项目中当前使用的埋点SDK，或者提供一个仓库里的参考示例</td>
        <td>- https://aime.bytedance.net/chat?autoreg=true&share_id=fd73c296-82d5-48d7-8874-5fbec3bfb798</td>
    </tr>
    <tr>
        <td>**静态分析问题修复**</td>
        <td>1. 提供能获取所有待修复问题的访问地址（例如 Bits Analysis 平台链接）
2.  明确修复的目标，修复标准等</td>
        <td>- https://aime.bytedance.net/chat?autoreg=true&share_id=7ee711b3-dbf0-4a1c-86bb-9ded51c6674c</td>
    </tr>
    <tr>
        <td>**单测生成**</td>
        <td>1. 明确指出需要编写单测的具体分支、文件或功能模块
2. 指明项目中现有的测试框架、工具链、Mock 方式和代码风格，确保新单测保持一致</td>
        <td>- https://aime.bytedance.net/chat?autoreg=true&share_id=7c16623c-867d-4b11-a2eb-9fc96680cdf5
- https://aime.bytedance.net/chat?autoreg=true&share_id=822c2b96-62c1-41b5-ae65-919fe9da3a37
- https://aime.bytedance.net/chat?autoreg=true&share_id=8cce632a-662e-4641-8dda-782529f36a5a</td>
    </tr>
</table>

## 案例解析
掌握了最佳实践后，我们来看一个实战。

我们将通过一个 Aime 项目组内真实的研发需求

> **为空间（Space）添加 MCP 数量统计，来对比展示**
> 

这个案例的特殊之处在于，**它所在的仓库高度依赖严格的开发规范**。正确的开发流程是：

1. **修改 IDL**：开发者**必须**先去 `api/idl` 目录修改 `thrift` 文件，定义新的返回字段。

2. **代码生成**：**必须**使用字节内部的 `hertz gen` 工具，根据修改后的 IDL **生成**对应的 Go 结构体。

3. **实现逻辑**：最后才能在 `handler` -> `service` -> `dal` 中编写业务逻辑，填充这些新生成的结构体字段。

**这里的“坑”是：** 如果一个 AI（或初级开发者）不知道这个上下文，它 100% 会**跳过前两步，直接在 Go 代码中（例如&nbsp;entity/mcp.go）手动添加那几个字段**。

这种错误的操作会彻底破坏项目的工程规范，导致 IDL 与实际代码不一致，是绝对无法被合并的。

#### **❌ Query V1：模糊不清的“一句话需求”**
让我们从一个典型的、低效的指令开始。

> **&nbsp;**“帮我给空间加个 MCP 计数功能”
> 

<callout icon="tired_face" bgc="1" bc="1">
**缺乏一切上下文**：
- “MCP”是什么？“空间”是什么？“计数”是什么？
- Aime 完全不知道这是哪个仓库、哪个模块、哪个 API。
**要求极度模糊**：
- 是统计所有 MCP 吗？还是只统计当前空间的？
- Aime 只能“猜”，或者反问你十个问题，这比你自己做还要浪费时间。
</callout>

#### **❌ Query V2：****缺失“工程上下文”的 PRD**
> 帮我开发一个功能，需求描述如下：
> 
> 新增MCP数量统计功能，在列出空间下MCP工具的接口中返回MCP数量信息。
> 
> MCP数量信息字段包括： 1、PublicCount：公司内公开的MCP总数... 2、CustomCount：用户自定义的MCP总数... 3、ActivateCount：已激活的MCP总数... 4、ActivateLimit：激活MCP的上限...
> 
> 仓库在 `https://xxxx/xxx`，帮我实现一下。
> 

<callout icon="sweat_smile" bgc="2" bc="2">
这个指令虽然业务逻辑清晰，但**完全缺失了“How”（如何实现）和“Where”（在哪里实现）**
这会迫使 Aime 去猜所有关键的工程决策：
**猜测 1：在哪里改 (Where)**
Aime 拿到了整个仓库。它不知道这个功能是应该在 api/idl 里改 Thrift 接口，还是在哪里里改 Service。它将花费**巨量时间**去扫描和理解整个仓库，试图定位到正确的文件。
**猜测 2：如何实现 (How)**
Aime 不知道 ActivateLimit 应该是个常量还是应该从 TCC 获取，它可能会试图去查数据库或配置文件，导致实现方式完全错误。
**猜测 3：工程规范**
Aime **完全不知道必须先改 IDL 再用 hertz gen 生成代码**。
它会 100% **直接去修改 Go 结构体文件**，这种做法**从根本上就是错的**，产出的 MR 毫无价值。
</callout>

#### **✅ Query V3：上下文充足的标准指令**
> 任务回放：https://aime.bytedance.net/share/919fb4dc-6a05-4913-a443-3e2e70c0762e
> 

<callout icon="sports_medal" bgc="4" bc="4">
帮我开发一个功能，需求描述如下：
新增MCP数量统计功能... MCP数量信息字段包括：...
> **<font background_color="light_blue">【Where】</font>**
> 
> 你可以主要关注以下目录：
> 
> 1. 接口定义（api/idl）
> 
> 2. 服务层（xxx/next_server） (handler, service, entity)
> 
> 3. 数据库定义（resources/dbschema）
> **<font background_color="light_blue">【 How&nbsp;</font><font background_color="light_blue">(业务逻辑)】</font>**
> 功能开发指引：
> 
> 1. 在 mcp.thrift 的 ListSpaceMCPResponse里添加...
> 
> 2. 在xx/next_server/service/mcp/mcp_space.go进行具体的处理：
> 
> 3. 激活MCP的上线，可以是个常量，固定为20
> **<font background_color="light_blue">【 How&nbsp;</font><font background_color="light_blue">(工程规范)】</font>**
> 其他要求：
> 
> 1. 增量开发需求，你需要先仔细了解现有的存量代码逻辑...
> 
> 2. 提供足够的单元测试，使用Mock方式...
> 
> 3. 所有变更应保持向后兼容...
> 
> 4. 接口定义（api/idl）里，先修改thrift接口定义，再仅执行 hertz gen....
> 
> - ...
> 代码仓是 https://xxxx/xxx
</callout>

对比三个案例可以发现，**从“玩具 Demo”到“生产级代码”的差距，核心在于上下文。**

- **反例 1**：什么都没有，Aime 无法工作。

- **反例 2**：只有“业务上下文”，Aime 会“猜”工程实现，**并 100% 掉入“直接修改结构体”的坑**，导致代码直接不可用。

- **好例子**：提供了**业务 + 技术 + 工程规范** 的完整上下文

<callout icon="sports_medal" bgc="4" bc="2">
最后，强烈推荐大家在仓库里添加一个 `AGENTS.md` ，让 Aime 更懂你的仓库。
详见[Aime 项目记忆（AGENTS.md）使用指南](https://bytedance.larkoffice.com/docx/VetbdMSMpoXMRMxiQuDcie7inth?from=auth_notice)
</callout>

## 业务分享
### Lark 邮箱后端
> [从 0 到 1：用 Aime 在 Lark 邮箱后端完成生产级需求的实践复盘](https://bytedance.larkoffice.com/docx/Fl9kdUFDgoI4SVxNg8PchjWLndg)
> 

作者探索了在 Aime 里，后端需求**全流程交付**中的应用提效能力与边界

![图片](img_KvlebpZJTopLmZxdVSKlYBehgBd.png)

### 即梦服务端
> [Aime在即梦服务端的最佳实践](https://bytetech.info/articles/7520457489080008744?fromIdType=55&fromId=7516716922617249801#NVNld8IcGoLtO6xF6bKcTOAon1d)
> 

作者也分享了他在 Aime 里的使用感受，和本篇文章想要带给大家的最佳实践是一致的。

> **Aime 的能力上限，取决于我们提问的水平**。所谓“Garbage in, garbage out”，只有提供清晰、全面、高质量的输入，我们才能收获精准、有效的输出。
> 

![图片](img_WkyPbemvmoTbn6x7VaslzvKYgp8.png)

### 剪映前端




</content>
