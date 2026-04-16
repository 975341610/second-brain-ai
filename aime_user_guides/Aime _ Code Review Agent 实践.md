<title>Aime | Code Review Agent 实践</title>
<url>https://bytedance.larkoffice.com/wiki/Jevqwl4gIixtqUkgh4wcGi10nfb</url>
<content>
<!-- BLOCK_1 | LRGgdIpTBohDmaxU81RcVbhCnEr -->
<callout icon="bulb" bgc="4" bc="4">
## Aime 是什么？Aime 是专为字节同学打造的 AI Agent 工作平台。
Aime 可以使用云端环境，在后台并行甚至主动地帮助大家高效完成各类繁琐重复的任务，包括但不限于：写代码、分析数据、做调研、写文档 等。在代码相关场景中，Aime 可以自主规划仓库探索路径，完成问题分析、修改、运行工作。
</callout>
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | Qtc9dXpAoo9HKpxNI7TcT9M6nMg -->
## 🎡 CR Agent vs. AI Review<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | QOXBdyQyGoK7jExh3mqcE2VNnXf -->
代码评审（Code Review，以下简称 CR）是由代码作者以外的人对所编写的代码进行审查的过程。
<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | Tz96dCEjwoyQWzxsKMEc4HE1nZd -->
Aime Code Review 能力基于 Agent 自主规划能力建设，与传统 AI Review 存在差异：
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | IEoydSQGFonJdCxlUu9cd8URnWh -->
<grid cols="2">
<column width="50">
  **CR Agent**
  - Agent 自主规划，泛化能力较强
  - 关注逻辑、设计、架构问题及缺陷
  - 全链路视角，把好代码合入的最后一道关
</column>
<column width="50">
  **AI Review**
  - 预定义，依赖经验总结及能力沉淀，泛化能力较弱
  - 关注风格检测、常见缺陷识别、安全风险拦截
  - 变更视角，识别潜在的问题
</column>
</grid>
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | SzPOdvkHGoi84Rx16lzcauk2nZX -->
## 📖 Aime CR 方案介绍<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | GagPd7bKvo9zTaxHGyUcLg9kn0f -->
Aime CR Agent 整体工作流程如下：
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | doxcnZsrpBJ7ytyogdgsXnS0kzb -->
![board_E0bKwfUt8hJ4rWb5P97cTzZynpc](board_E0bKwfUt8hJ4rWb5P97cTzZynpc.drawio)
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | AmbIdM1cbo9lvcxARttcbhRinDc -->
1. **Code Review Template**：预定义 Code Review 任务描述，经过多轮调教优化。
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | PC8BdAxg3odbNmxOhsqc52xynmh -->
2. **Aime Agent**：基于 ReAct Agent 核心，自主完成任务规划及执行反馈。
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | HOQ0dlCFxo1Artx4N9gcczPrnMb -->
3. **MCP Tools**：通过默认集成的 Codebase MCP 及其他工具，完成给定的 Merge Request 元信息及变更列表获取。
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | QEXGddIrhoqbzCx7gfic2DulnAb -->
4. **Knowledges**：精心维护的扩展知识，帮助 Agent 更好地完成工作。
<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | X9C6dc69comgtVxrTYyclw3snef -->
5. **TODO List** & **Comments.json**：维护工作记忆，确保对变更文件较多的 MR 也可以较好地完成任务，并记录识别的问题，避免上下文过长导致遗忘。
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | BSQvdYF23ocjABx7T7hc3Pcbnkd -->
6. **Comment Creation Tool**：定制化的评论提交工具，以 Aime 的身份完成评论提交，以便更直观地区分 AI Agent 评论和用户评论，以及后续的数据统计及追踪。
<font color="green">当前，Comment Creation Tool 中包含 Issue 过滤策略，</font><font color="green">仅针对模型打分的 P0 及 P1 问题提交评论</font><font color="green">，后续策略可能调整。</font>
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | XaUmdo0rIoqHrdx6gTdcXM5fnJd -->
### **能力差异详解**<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | BGKddCcZ5ouUQWxcB6PctYRVnbh -->
**1️⃣&nbsp;关注内容：全局上下文&nbsp;vs 局部上下文**
<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | AvH4d5iNGoQDrgxZzyScwk5enJc -->
<grid cols="2">
<column width="50">
  Code Review Agent：具备**全局上下文理解能力**，不仅关注变更行，还会主动上下游代码及项目文档。它能从 “整个系统” 的视角分析变更的影响，例如：
  - 变更是否与其他模块的设计冲突？
  - 是否符合项目的整体架构原则（如分层设计、接口隔离）？
  - 变更是否破坏了历史功能的隐性约束（如某函数的输入输出约定）
</column>
<column width="50">
  基于代码变更行的 AI 审查：核心聚焦于**具体的代码变更行（Diff）**，仅针对提交的增量代码（如新增、修改、删除的行）进行分析。
  它的视角局限于 “变更本身”，即使采用函数片段来代替有限变更行，也无法识别跨函数的问题。
</column>
</grid>
<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | BuNidJM37oNvgoxYfNCcaMjpnff -->
**2️⃣&nbsp;推理能力：动态多步推理 vs 静态匹配**
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | IR7jdPBUhopHjtxBzqIc1ClRntb -->
<grid cols="2">
<column width="50">
  Code Review Agent：基于**智能体（Agent）架构**，具备类似人类的 “多步骤推理” 能力。
  它会模拟开发者的思维过程：先理解变更的目的（如 “修复某功能 bug” 或 “新增接口”），再拆解实现逻辑，然后验证 “实现是否达成目的”“是否引入新风险”“是否有更优方案”。
</column>
<column width="50">
  基于代码变更行的 AI 审查：依赖**预定义规则或简单模型**，推理逻辑是 “触发式” 的 —— 当代码符合某种已知模式（如 “if 条件缺失 else”“未释放资源”）时，触发相应的审查提示。
</column>
</grid>
<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | XDwid9CsOoQrCAxsw0ucVw7EnRf -->
**3️⃣&nbsp;自主性：主动探索 vs 被动处理**
<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | EObHdAHkBoGb0Kx8aVecLwtInVg -->
<grid cols="2">
<column width="50">
  Code Review Agent：**智能体**会**主动**根据审查需求 “主动探索信息”。例如：
  - 自动查询项目文档，确认变更是否符合业务规则；
  - 追溯关联代码（如被调用的函数、父类 / 子类），验证逻辑一致性；
</column>
<column width="50">
  基于代码变更行的 AI 审查：是**被动工具**，仅对输入的 “变更内容” 进行处理，不会主动获取额外信息。
</column>
</grid>
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | QrZGdxplzo0jkOxCuGOcrzyhnqc -->
**4️⃣&nbsp;问题复杂程度：深层系统性问题 vs 表层问题**
<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | TbfqdHIjcokgqUxtsuYc1OOxnVd -->
<grid cols="2">
<column width="50">
  Code Review Agent：更擅长发现**深层、系统性问题**，例如：
  - 架构设计冲突（如在 “低耦合模块” 中新增了强依赖）；
  - 业务逻辑矛盾（如变更与产品需求文档中的核心规则冲突）；
  - 隐性性能瓶颈（如在高频调用链路中新增了耗时操作，单看变更行无法发现）。
</column>
<column width="50">
  基于代码变更行的 AI 审查：擅长发现**表层、显性问题**，如语法错误、代码风格不符、简单逻辑漏洞（基于模式匹配），但无法识别深层问题。
</column>
</grid>
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | JpGidsEsTobc1xxb95bcIWvsnze -->
### 上下文如何扩展<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | Pm1YdOvf6oA1PaxWFrUcQOO6nCh -->
必要的上下文扩展，有助于 Agent 更好理解代码变更的意图，并判断实现与目标的一致性。
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | EhwCd4Y6Jo9WrgxQ7HNcufu3nrc -->
这对 MR 创建者提出了更高的要求，创建者可以通过如下的方式补充上下文信息：
<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | NQxMd1NLIoJSjfxrWBgc991gn0f -->
- MR 描述：描述应涵盖背景信息、修改方案描述等关键信息，填上既有的飞书文档也是个不错的选择。
<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | Kv34dFjNpoyNqWx9XVWc6naRnhe -->
- 关联工作项：关联包含任务描述信息的 Meego 链接，有助于补充修改的背景。当然，如果 Meego 上的信息不足，则不会起到明显的帮助作用。
<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | H95QdwHMNoVQEcxVfKmcXqwqnXd -->
- [AGENTS.md](https://bytedance.larkoffice.com/docx/VetbdMSMpoXMRMxiQuDcie7inth)：还可以通过仓库内的 AGENTS.md 文件，补充代码相关的信息，比如编程规范描述等。
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | WOOYdpp1iofwiox8zTZch9Lrnih -->
- query中飞书文档、项目空间知识、字节编码规范
<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | MYj6dyW4LoIMkTxFC3wcuMhWnbh -->
## 🔆 能力介绍<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | DQiDd2nU1oITfMxu5tpcFbNinCc -->
### 能识别哪些问题<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | YtqjdDvpZoHkeVxitMTcY63SnCc -->
目前通过 Codebase 自动发起的 Aime Code Review 采用预定义模版，涵盖如下六大类问题：
<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | CQr7dDMj2oVqTpxzdzzcaeWWnwc -->
<table col-widths="189,315,573">
    <tr>
        <td>1. 功能完整性</td>
        <td>![图片](img_PIuEbfmqHoWZSnxy5l9cWzgTnhc.png)</td>
        <td>- **目标达成**：代码是否完整、正确地实现了 MR 描述或相关任务中要求的功能？
- **逻辑正确性**：是否存在逻辑错误、边界条件问题（Edge Cases）或计算错误（off-by-one errors）？
- **用户影响**：对于面向用户的改动，是否考虑了不同的用户场景？如果涉及 UI 变更，其交互是否符合预期？</td>
    </tr>
    <tr>
        <td>1. 代码质量与可维护性</td>
        <td>![图片](img_GnnzbPp3Vo2ta7x1FvfcFIuvnYc.png)</td>
        <td>- **可读性**：代码是否清晰易懂？变量、函数、类的命名是否做到见名知意？
- **简洁性**：是否存在冗余、重复或可以被简化的代码（DRY - Don't Repeat Yourself）？
- **代码风格**：是否遵循了团队既定的代码风格指南和编程规范（如命名约定、格式化等）？
- **结构**：代码结构是否合理？函数或方法的长度是否过长？ 一个文件或类是否承担了过多的职责（单一职责原则）？</td>
    </tr>
    <tr>
        <td>1. 性能考量</td>
        <td>![图片](img_Eh7kbGr1yo3BU3x9Cz8cm89Cnof.png)</td>
        <td>- **效率问题**：是否存在明显的性能瓶颈，例如不必要的循环、低效的算法、频繁的 I/O 操作或数据库查询？
- **资源使用**：是否存在资源泄漏（如内存、文件句柄、数据库连接未正确释放）？
- **数据处理**：对于大数据量的处理，方式是否高效，是否会造成过高的内存消耗？</td>
    </tr>
    <tr>
        <td>1. 安全性审查</td>
        <td>![图片](img_KGmQbsUBnopHncxsJK5cHkrLnLr.png)</td>
        <td>- **输入验证**：所有外部输入（如用户输入、API 请求参数）是否都经过了严格的校验和净化，以防止 SQL 注入、跨站脚本（XSS）等攻击？
- **敏感信息**：代码中是否硬编码了密码、密钥、Token 等敏感信息？这些信息是否被安全地存储和管理？
- **依赖安全**：引入的第三方库或依赖是否存在已知的安全漏洞？
- **权限控制**：相关的操作是否进行了恰当的权限检查？</td>
    </tr>
    <tr>
        <td>1. 架构与设计</td>
        <td>![图片](img_Gv8ib447XonwMOxU0mscnAT8nqd.png)</td>
        <td>- **设计模式**：代码是否恰当地运用了常见的设计模式来解决问题？
- **扩展性**：设计是否具备良好的扩展性，便于未来增加新功能或进行修改？
- **解耦**：模块、类或服务之间是否存在不合理的强耦合？
- **代码抽象**：抽象层次是否恰当？有没有将通用逻辑封装成可复用的模块或函数？</td>
    </tr>
    <tr>
        <td>1. 错误处理与健壮性</td>
        <td>![图片](img_BCLobmHeXow4SUxHIw7cwKuonqf.png)</td>
        <td>- **异常处理**：是否对可能发生的异常（如网络请求失败、文件读写错误、空指针等）进行了妥善处理？
- **用户反馈**：当错误发生时，系统是否能优雅地失败，并向用户或日志系统提供清晰的错误信息？
- **事务性**：对于需要多个步骤才能完成的操作，是否保证了其事务性（要么全部成功，要么全部回滚）？</td>
    </tr>
</table>
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | F332delKfoJDjlxzKKgcWKZ7nRg -->
### 支持在 IDE 使用啦  ✨<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | V11sdg4dboS2gSx882ccSZ4Dnbh -->
<callout icon="pushpin" bgc="4" bc="4">
<font background_color="light_yellow">Aime Code Review 支持 IDE 上使用啦 ！！！</font>
Cloud Dev IDE 插件集成 Aime CR 能力，提供 AI 代码评审功能，基于本地代码 diff、文件、函数、圈选代码片段进行评审，无需提交 MR，将发现问题、修复问题的时机前置到 IDE 本地编码环节，减少平台和本地开发的切换。
**一键直达安装/升级 >>>**
</callout>
<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | V2MgdbNi8omOVZxJUpKcHD2hn5g -->
<table col-widths="227,518,276,345">
    <tr>
        <td colspan="2">## **本地发起代码评审**无需发起 MR 即可在本地完成代码评审，丝滑修复。支持四种代码评审范围：
1. 本地代码 diff
2. 选中函数
3. 选中文件
4. 任意圈选代码片段</td>
        <td colspan="2">## **消费评审结果**</td>
    </tr>
    <tr>
        <td>从文件编辑器右键菜单发起评审</td>
        <td>![图片](img_LqQybvl3eo2x1DxLVl6cTzIWnaf.png)
![图片](img_W6zfb9OryohXFvxl4fmcous2nsd.png)</td>
        <td>Aime code review 任务执行结束后，展示评审总结，问题列表，问题的修复代码。
1. 点击问题标题可跳转问题代码行处
2. 点击采纳可以 diff 方式展示修复建议，并应用到本地代码文件中</td>
        <td>![图片](img_O2TjbOQevosKsLxS5zYcadVznth.png)
![图片](img_SrASbTW0loBqOKxd8h6coqfLn6b.png)</td>
    </tr>
    <tr>
        <td>从文件浏览器右键菜单发起评审</td>
        <td>![图片](img_AXi1bOQ3poELZ3xoAUAcEFMrnHc.png)</td>
        <td>问题代码将出现波浪线标记，hover over 展示问题卡片，呈现问题描述和修复代码，点击“应用变更”则将修复代码应用到本地文件中</td>
        <td>![图片](img_DJZgbn9tiozcPMxgGeNcdx1jnsc.png)</td>
    </tr>
    <tr>
        <td>从 CloudDev chat 对话发起评审
1. 点击“代码评审”，则针对本地代码 diff 按照默认规则进行评审
2. 对话框输入 @代码评审 ，通过输入 #指定评审范围，输入评审的要求，点击发送开始评审</td>
        <td>![图片](img_BeCRbX1NkoWhfSxxk8aczqMUnzh.png)
![图片](img_W8QEbAYnAoPdhixkoQyc8NRYnSd.png)</td>
        <td></td>
        <td></td>
    </tr>
</table>
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | XOYsdBzaAooXpXxX6tBcaBu8nYd -->
## ❇️ 线上效果<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | MIssdkgdqoJehJx13pxc9Cennzb -->
### 覆盖情况<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | CVP6dmYmcoMrDlxnYh5cQTWQnuc -->
当前，已有较多仓库已经在使用 Aime 来进行代码评审：
<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | WYkSddSV6ooajPxOKRJckMqsnRh -->
![图片](img_M3Debv23gonvtVxxKCzcfQ6Pnsd.png)
<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | O7lrdE2pKoJKPdxoUK7cEY6Dnog -->
### **效果评价**<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | EUcldoOmsoREiOxUEjvc3ftZnVf -->
#### 离线评测<!-- END_BLOCK_43 -->

<!-- BLOCK_44 | WxPyd5vxdop3OTxplRCcdWTVnFb -->
在构造的离线评测集上，由 Aime Agent 自主探索仓库并识别的问题都具备了相当的可用性，识别问题的范围也常常超出预期：
<!-- END_BLOCK_44 -->

<!-- BLOCK_45 | doxcne0ACvOzGv1RcR1MPkRrqdh -->
<table col-widths="82,100,329">
    <tr>
        <td>**准确率**</td>
        <td>82.71%</td>
        <td>354（正确） / 428（识别）</td>
    </tr>
    <tr>
        <td>**召回率**</td>
        <td>58.42%</td>
        <td>118 （召回） / 202 （Ground Truth）</td>
    </tr>
</table>
<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | RfdRdbJ7UozDshxug35c2F1mnPh -->
> 数据集来源：基于线上真实 MR 数据回流的 35 个 MR 构造的离线评测集
> 
<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | BJAtdH1yJofnjax5QTVcGCpOn3i -->
#### 线上评测<!-- END_BLOCK_47 -->

<!-- BLOCK_48 | doxcnh9uAy6cvtb6A43jK9OfYLb -->
<table col-widths="244,100,198">
    <tr>
        <td>**整体准确率**</td>
        <td>85.51%</td>
        <td>726（正确） / 849（识别）</td>
    </tr>
    <tr>
        <td>代码缺陷</td>
        <td>87.93%</td>
        <td>306（正确） / 348（识别）</td>
    </tr>
    <tr>
        <td>逻辑与健壮</td>
        <td>84.06%</td>
        <td>174（正确） / 207（识别）</td>
    </tr>
    <tr>
        <td>代码安全</td>
        <td>78.05%</td>
        <td>96（正确） / 123（识别）</td>
    </tr>
    <tr>
        <td>代码风格、可读与可维护性</td>
        <td>86.11%</td>
        <td>93（正确） / 108（识别）</td>
    </tr>
    <tr>
        <td>代码性能</td>
        <td>90.00%</td>
        <td>27（正确） / 30（识别）</td>
    </tr>
    <tr>
        <td>架构与设计</td>
        <td>81.82%</td>
        <td>27（正确） / 33（识别）</td>
    </tr>
</table>
<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | NfC7dn5phoXWrJxtw3pcF94Jn3g -->
> 数据来源：基于线上使用 Aime 生成的评论数据，标注时间：10.29
> 
<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | UcFMdH2aAoCoCxxew53cQTk2nYd -->
## 🧑‍🎓 **业务案例**<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | N5kKdG6mOoRsfMxXIr1cRlJgnOg -->
### 国际化电商业务实践<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | PITSdtroEos1VQxFHZHcRPfDnAg -->
- [GEC事故/线上问题 * MR AI ](https://bytedance.sg.larkoffice.com/docx/ISwQdgkUOoO8yZxQRfll17Vdgfd)
国际化电商在 Go、Java、前端、Android 等种语言上都进行了问题回溯：
![图片](img_WdlDbd1vLooeElxXDLbcNBvfnMe.png)
<!-- END_BLOCK_52 -->

<!-- BLOCK_53 | UWOodcn73oZDmKxBJnmcT2M3nbg -->
- [国际化电商CR最佳实践 - Aime CR](https://bytetech.info/articles/7592243660155486249#FpKedFNQeo7MtoxeZKilTf3Pg9c)
![图片](img_H2mPbzPffoKbopxbfn2covfGnSc.png)
<!-- END_BLOCK_53 -->

<!-- BLOCK_54 | B4L1dBiRboylSdxRMoDc0i5HnLg -->
### 生服-服务端业务实践<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | UqlzdDStFoRVVLx7qlIc5RYlnaf -->
- [CR Bug数提升136%，Aime AICR在生服业务最佳实践](https://bytedance.larkoffice.com/wiki/TXQ1wuekxibdhakKp6mcsvFVnIc) 
<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | FYCOdPEAuooQQxx2yhvcGqpYnRh -->
- [上下文穿透+知识注入：Aime 破解Lynx前端CR深层痛点](https://bytedance.larkoffice.com/wiki/HoH6wzoTCi5c4VkZ9Z7cvBwNnng)
![图片](img_PYSJbY7owoJtqaxzz5yctUDsnSf.png)
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | doxcnn6SWrQqtHrsdMJqCgJlXFc -->
<grid cols="2">
<column width="50">
  ![图片](img_SEVSbm4fJoIcRpxnZxVcTorMnxe.png)
</column>
<column width="50">
  **推广后，生服 C 端 <font background_color="light_green">8 月 CR bug 数 提升</font><font background_color="light_green">&nbsp;136%</font>（11 例->26 例）**
  ![图片](img_UEJIbUJCho25V6xEsecccq7bn4f.png)
</column>
</grid>
<!-- END_BLOCK_57 -->

<!-- BLOCK_58 | EmVCdtuSZol3Xkx1JlZcAbxbnjb -->
### Lark Office Engineering-Lark App 业务实践<!-- END_BLOCK_58 -->

<!-- BLOCK_59 | TADGd8GFvowDbhxcbCIclooKnbe -->
- [使用 Aime 辅助 CodeReview](https://bytedance.larkoffice.com/wiki/QFlhwtGsLiBuNNkvQlZceIy8nFe)
<!-- END_BLOCK_59 -->

<!-- BLOCK_60 | Qpgydr8fPoISR4xYLaCc0Lfrnne -->
![图片](img_NjATbisjSowj6Sx1u2icUGG3n7g.png)
<!-- END_BLOCK_60 -->

<!-- BLOCK_61 | VBUcdwJgMo4ovXx1CpbcfEVfn1c -->
### 懂车帝-服务端业务实践<!-- END_BLOCK_61 -->

<!-- BLOCK_62 | Bkc6dJSduoHhGVx8KdKcKRU2nPb -->
- [从 “人肉找茬” 到 “智能扫雷”：Aime 把开发者从重复CR 评审中 “解放”](https://bytedance.larkoffice.com/docx/O1bNd4VhDowKx8xzee9cO8yCnKb?opendoc=1&opendocVersion=0.0.3&hideTemplate=true&onboarding=0&shwm=true&lang=zh)
<!-- END_BLOCK_62 -->

<!-- BLOCK_63 | V814dLfZEozM4uxB398cS1Sdnmg -->
![图片](img_N7trbouO2ogWKLxYFHNcc5DynNd.png)
<!-- END_BLOCK_63 -->

<!-- BLOCK_64 | ZzBHdUfPnoj9KJxQzLScNqoKnWd -->
## 🌪️ 数据看板搭建<!-- END_BLOCK_64 -->

<!-- BLOCK_65 | LMXEdepALolubexPqpGcG2oLnTO -->
！！！！！！p_date是时间分区，用最近一天！！！！！
<!-- END_BLOCK_65 -->

<!-- BLOCK_66 | CBSzdfkbdotLwBxRKNBccx7cnqh -->
### 数据集<!-- END_BLOCK_66 -->

<!-- BLOCK_67 | P6FfdunCuoyaGExASzUcloALnUd -->
<callout icon="pushpin" bgc="4" bc="4">
如果你想搭建一个**平台提供看板&nbsp;相同指标定义的<font background_color="light_yellow">业务版本</font>**，你只需要申请以下数据集
1. Aime CR 生成的全部评论：[aime_cr_comment_detail](https://data.bytedance.net/aeolus/pages/dataManage/detail/4733781?appId=739695&belong=1)
2. 用户对 Aime 的赞踩反馈：[aime_comment_feedback_details](https://data.bytedance.net/aeolus/pages/dataManage/detail/4733385)
3. MR 维度相关统计：[aime_cr_merge_requests_detail](https://data.bytedance.net/aeolus/pages/dataManage/detail/4735807?activeTab=preview&appId=739695&belong=1)
4. ~~仓库开启自动 CR：~~~~aime_repo_penetration_from_settings~~
仅统计 Codebase Setting 开启部分，不包含项目空间触发器；覆盖统计可使用 merge_requests 表。
</callout>
<!-- END_BLOCK_67 -->

<!-- BLOCK_68 | XF6DdaDrBocckSxMSlocqWEsnpe -->
- 平台看板
[preview](https://data.bytedance.net/aeolus/pages/dashboard/1386736?appId=739695&isDefault=1&sheetId=1897869)	- 数据集字段说明
	> <font background_color="light_yellow">PS：特别强调下数据集里「服务树/部门」都是跟仓库关联的信息</font>
> 
		1. Aime CR 生成的全部评论：[aime_cr_comment_detail](https://data.bytedance.net/aeolus/pages/dataManage/detail/4733781?appId=739695&belong=1)
		![preview](RLmTsI2GHhJGoctVCgNcSTYsnlf.xlsx)		2. 用户对 Aime 评论 的赞踩反馈：[aime_comment_feedback_details](https://data.bytedance.net/aeolus/pages/dataManage/detail/4733385)
		> 📌 表格只有有反馈的数据！！
> 
		![preview](RLmTsI2GHhJGoctVCgNcSTYsnlf.xlsx)		3. MR 维度相关统计：[aime_cr_merge_requests_detail](https://data.bytedance.net/aeolus/pages/dataManage/detail/4735807?activeTab=preview&appId=739695&belong=1)
		![preview](RLmTsI2GHhJGoctVCgNcSTYsnlf.xlsx)		4. 仓库开启自动 CR：[aime_repo_penetration_from_settings](https://data.bytedance.net/aeolus/pages/dataManage/detail/4733697?belong=1&appId=739695)
		![preview](RLmTsI2GHhJGoctVCgNcSTYsnlf.xlsx)<!-- END_BLOCK_68 -->

<!-- BLOCK_69 | OVI0dM94iok8xgxXKzQc1BsYnqf -->
### 数据实践<!-- END_BLOCK_69 -->

<!-- BLOCK_70 | SItrd2mLfo3MVOxut8ecvBKzn5c -->
> 该实践基于风神看板！！
> 
<!-- END_BLOCK_70 -->

<!-- BLOCK_71 | QO0sdn5f2oQu9qxFcORcaqzunBd -->
<table col-widths="208,754">
    <tr>
        <td>**目标**</td>
        <td>**如何做**</td>
    </tr>
    <tr>
        <td>如何统计 AI 效果？</td>
        <td>1. 平台对 AI 效果的追踪是周期对线上数据「机评+人评」来判断的，周期非固定，跟随模型/策略变更安排评测任务。
2. 业务如果想要周期判断效果，可以使用以上数据集，并考虑以下定义
	- 规定有效为：对 AI 评论标记「resolved」，可用 `resolved` 字段，为 1 
	- 规定有效为：带来用户修改，可用 `outdated` 字段，为 1
	- 规定有效为：正确的标记「赞」，可用 `feedback` 字段，为 upvote
	- 以上三种定义也可以一并使用，作为非常严格的判定标准。
```
--举例：根据是否修改来作为采纳率

countDistinctIf(`comment_id`, `outdated`!= 0) / COUNT(DISTINCT (`comment_id`))
```</td>
    </tr>
    <tr>
        <td>如何拼接 MR 链接</td>
        <td>```
concat('https://code.byted.org/',`repo_name`,'/merge_requests/',`external_id`)
```</td>
    </tr>
    <tr>
        <td>如何获取问题描述
> 其他的内容也可以尝试用这个方式获取
> </td>
        <td>```sql
-- PS:模型格式化问题，会存在拆不出来的情况，可以参考酌情调整
TRIM(
  regexp_extract(
    [content],
    '(?s)(?:\\*\\*(?:问题描述|Issue\\s+Description)\\*\\*|问题描述|Issue\\s+Description)\\s*[：:]\\s*(.*?)(?:\\r?\\n\\s*\\r?\\n\\s*\\*\\*(?:严重级别|Severity\\s+Level)\\*\\*|$)',
    1
  )
)
```</td>
    </tr>
    <tr>
        <td>服务树、部门关联</td>
        <td>数据来源于 Codebase 仓库配置：
![图片](img_Jy4Qb02PIo19Vhxi3B4cZzR1nfc.png)</td>
    </tr>
</table>
<!-- END_BLOCK_71 -->

<!-- BLOCK_72 | QPHSdXK8IoVS5CxKkDgcFqsTnEb -->
## 相关文章<!-- END_BLOCK_72 -->


<!-- BLOCK_73 | QZsHdfzovosF2uxMEhDc7sEvnLg -->
## 📌 FAQ<!-- END_BLOCK_73 -->

<!-- BLOCK_74 | TmWmdwvwyoPtuBx3VHNc0ZOTnoe -->
### 如何使用 Aime CR<!-- END_BLOCK_74 -->

<!-- BLOCK_75 | XO8GdZipCsxtLAboB5Xc10TgnJf -->
Aime Code Review 包含多种使用方式：
- 方式一（最熟悉的配方）：可以在 [Aime](https://aime.bytedance.net/chat?autoreg=true&share_id=ac374f8d-a679-46c6-89d0-d3e8c0bb7e82) 发起一个对话，填上你希望评审的 MR 链接：
使用[模版](https://aime.bytedance.net/chat?autoreg=true&share_id=90b4410c-116f-4636-b881-c394b04dc148)或者简单的要求，就能让 Aime 帮你干活，如：
```sql
帮我评审合并请求 <mr_link>，识别潜在的技术风险或边界情况，评估对系统其他部分的影响，指出可能的兼容性或性能问题及逻辑缺陷，生成审查报告文档，并将问题评论到合并请求。
```
- 方式二：在 MR 中主动邀请 @aime：
![图片](img_ClZFbMy5koRZEvxu0HdcoA8jnEc.png)
---
如果你希望可以自动评审，可以选择：
- 方式一：使用项目空间触发器，[点击抢先体验](https://bytedance.larkoffice.com/share/base/form/shrcnRXNVIXfJG9TkfbpvwSPKMg)
<grid cols="3">
<column width="33">
  1. 打开 Aime 项目空间“任务触发器”
  ![图片](img_Q5WYbRatJoPjH6x1DrPcx5D5nYf.png)
  ![图片](img_AdvEb24oUow3zyx1RWLc8jpwnwf.png)
</column>
<column width="33">
  1. 新建 Codebase 任务，并选择导入的代码库、触发规则、自定义模版
  ![图片](img_LpWKb9FYkot0qDxsgescX5mfnpe.png)
</column>
<column width="33">
  1. 保存任务，试试在 Codebase 发起 MR 吧
</column>
</grid>
使用项目空间触发器，你可以：
- 多种类型的 CR 触发规则，如：特定命名的分支、标题
- 实现 Aime CR 任务在空间内共享可见
- 绑定自定义模版，并可添加额外的参数
- 自定义多种通知方式

- 方式二：通过 Code 配置自动邀请 Aime
<grid cols="2">
<column width="27">
  1. 找到代码仓库的 “Code AI 设置”（需要仓库 Master 及以上权限）
  ![图片](img_NdvrbQy6uoEX7Sx8mKjcC6Uhnrc.png)
</column>
<column width="72">
  1. 选择默认邀请 Aime 作为评审者
  ![图片](img_RcMabJSZRogUXmxKR14cY415nib.png)
</column>
</grid>
1. 批量开启（无需权限要求）
Bpm 工单无需审批～勾选“开启 Aime CR 自动触发”即可。
[https://bpm.bytedance.net/apply?cid=16970](https://bpm.bytedance.net/apply?cid=16970)
<!-- END_BLOCK_75 -->

<!-- BLOCK_76 | KBdTdZxltooLYvx9gHgcARcRn3d -->
### Aime CR 和 BitsAI CR 有什么关系？<!-- END_BLOCK_76 -->

<!-- BLOCK_77 | M57zdvOeVojRvRxqUQFcXWxDn3c -->
Aime CR 和 BitsAI CR 采用了两种完全不同的技术方案，能力上并不冲突：
<!-- END_BLOCK_77 -->

<!-- BLOCK_78 | doxcn4uxu0JvuDj186ViESZZuof -->
<table col-widths="143,531,553">
    <tr>
        <td>业务场景</td>
        <td>场景描述</td>
        <td>**25.Q4**</td>
    </tr>
    <tr>
        <td>**业务自定义评审**</td>
        <td>1. 代码规范：团队仓库必须遵循的规范或最佳实践（固定）
2. 需求/缺陷一致性：评审「需求/缺陷」与「代码功能实现/变更」的一致性与完备性（动态）</td>
        <td>1. ✅ 自定义代码评审能力建设：用户可通过自定义模版/知识触发任务
	- 自定义过滤配置，路径/分支/....
自定义配置灰度中，很快会全面开放，届时大家可以通过 Aime 项目空间配置评审触发，并实现 CR 任务在 Aime 空间内共享，详见 FAQ；[Aime CR 自定义模板配置 最佳实践](https://bytedance.larkoffice.com/wiki/HPVnwAMWyi8vUPkT2sxclQ98ntg) 仍会作为备选方案支持。
2. 自定义效果评估：支持用户快速验证与调试自定义模板/知识的有效性与收益
3. ✅  提供有效代码评审修复建议
可以通过点击评论中的“一键修复”发起 Aime 任务解决，并验证修复正确性；功能持续改进中。</td>
    </tr>
</table>
<!-- END_BLOCK_78 -->

<!-- BLOCK_79 | QTA3dQvkGoXMKjxKBYScshYPnhf -->
- Aime CR 基于 AI Agent 对仓库深度理解，耗时较 BitsAI 更久，对跨函数、架构、逻辑问题识别有更好的表现
<!-- END_BLOCK_79 -->

<!-- BLOCK_80 | OmuNdB35lodHLSxUjsNcAhWhn4e -->
- BitsAI CR 基于 Diff Patch Review 工作流，效率优于 Aime CR，更关注风格、函数内缺陷
<!-- END_BLOCK_80 -->

<!-- BLOCK_81 | Ioxedy8ZqorB15x52pRc4QoTnlg -->
<font background_color="light_green">两种可以同时开启，</font><font background_color="light_green">Aime CR 的已有评论去重机制</font><font background_color="light_green">，会在</font><font background_color="light_green">一定程度上</font><font background_color="light_green">避免重复评论。</font>
<!-- END_BLOCK_81 -->

<!-- BLOCK_82 | doxcnvkL6kNoCCNJxyuB4LAjnKf -->
### 如何知道 Aime CR 的任务进展？<!-- END_BLOCK_82 -->

<!-- BLOCK_83 | doxcnATSrR3ErUxU5lqK6S7h5hg -->
答：在 MR 中邀请 Aime 后，可以在代码仓库的“检查项（Checks）”中看到 Aime Code Review 的任务状态。点击对应的链接，即可跳转至 Aime 会话页面，实时查看评审的详细进展和思考过程。

<!-- END_BLOCK_83 -->

<!-- BLOCK_84 | V0eYdexelo6n8ExDtcMc2nEinln -->
![图片](img_Ks62bo9TXoCLhQxkMg8cFmWjnUg.png)
<!-- END_BLOCK_84 -->

<!-- BLOCK_85 | doxcncxmt4c1UP4dXUSOqIesnQc -->
### 如何自定义代码评审规则？<!-- END_BLOCK_85 -->

<!-- BLOCK_86 | V2AOdb3exom6Myxd1hUcqOw1noc -->
相关文档： [Aime | CR 自定义规范能力接入指南](https://bytedance.larkoffice.com/wiki/FJQsw75buiUClrkUYCfcORyDnXe?from=from_copylink)
<!-- END_BLOCK_86 -->

<!-- BLOCK_87 | doxcnrlWuNuNJ2aDCBFTfBAF9Jc -->
### 如何联系我们？<!-- END_BLOCK_87 -->

<!-- BLOCK_88 | doxcnkCdXPVPdT2bqPocTuQXrse -->
如果你在使用 Aime CR 的过程中遇到任何问题，或有宝贵的优化建议，欢迎通过以下方式联系我们：
<!-- END_BLOCK_88 -->






</content>
