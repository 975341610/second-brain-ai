<!-- BLOCK_1 | DZsodDG82oEpuHxPuvGcAz11nch -->
> 完整需求 [【WIP】 Aime - 个人助理](https://bytedance.larkoffice.com/wiki/AgkTwIb7Uisf0TkLDLic6kdnnoe?from=from_copylink)
> 
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | Ti5LdWQuoosTayxIE98ceGEDnxz -->
<callout icon="point_right" bgc="3" bc="3">
**开发前共识：**因鉴权和历史存量任务原因，个人助理 bot 用线上 Aime Bot 改造，新起一个 Bot 承载运营消息&任务模式增量通知
- **个人助理 Bot：**原 Aime Bot，承载个人助理对话和所有个人助理模式下的任务状态通知
<!-- comment for text `个人助理 Bot：原 Aime Bot，承载个人助理对话和所有个人助理模式下的任...下单独发起的任务通知`：需要切换机器人链路 1. 批量任务通知 2. 站内信通知 3. 知识冲突检测通知 4. 任务完成通知 5. ackuser通知 6. 浏览器托管通知 7. 二维码登录通知 8. 风神授权通知 9. 任务完成，回放链接发送通知 10. aime上线部署通知 11. 场景检测通知 12. 活动通知 13. 工作流通知  - 完成  - 中间等待  - codebase触发器等待  - 定时任务等待   先不换 14. 创建群组 15. 拉群群组 16. 定时个人任务通知、更新、话题加评论 17. 定时群组任务通知、更新、话题加评论 18. 触发器任务通知、更新、话题加评论 19. 触发器组任务通知、更新、话题加评论 20. openapi 通知卡片 - slardar 21. meego@zhujingyan.43@bytedance.com  @liutianyi.444@bytedance.com -->- **Aime 通知 Bot：**新创建的 Bot，承载运营消息，用户在非个人助理模式下单独发起的任务通知
</callout>
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | RybmddRcSoYe80xTPIUczRN1nOe -->
## <font background_color="light_yellow">❗️ 标黄部分为与🦞飞书插件不同的功能，请研发关注</font><!-- 标题序号: 1 --><!-- END_BLOCK_3 -->

<!-- BLOCK_4 | IWlqdtMEIo9tdhxcrs4cUp6knyg -->
<callout icon="point_right" bgc="3" bc="3">
## 3.9 更新：1. Web 问答都不同步到飞书了
2. 飞书用同一个 bot 发 Web 任务更新提醒
	1. 时机：Web 收到了新 Response，用户 5 分钟未读
	2. 防打扰：若用户一直未读，且期间有新的 Response，不重复提醒
	3. 跳转路径：跳转到 Web 助理，锚定到对应 Response
	4. 提醒文案：不走模型，固定文案随机取 1 
		1. 你在 Web 让我做的任务有新进展啦，去看看吧👉（跳转链接）
		2. 🙋‍♀️之前让我办的事有进展了，去 Web 看看吧（跳转链接）
		3. 👀你给我派的任务有眉目了，点击去 Web 看一眼（跳转链接）
</callout>
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | TsWOdWWCEoow0pxPxEhchr2xnVe -->
## 飞书 bot - 私聊<!-- 标题序号: 2 --><!-- END_BLOCK_5 -->

<!-- BLOCK_6 | CBe7dWGFkoLaHKxfexLcVDZrnDd -->
### Bot 内功能入口<!-- 标题序号: 2.1 --><!-- END_BLOCK_6 -->


<!-- BLOCK_7 | Rnuudee8aoFVbExfWAIcc8FWnDb -->
<font background_color="light_yellow">底部增加</font><font background_color="light_yellow"> 3个快捷入口</font><font background_color="light_yellow">，点击跳 Web 端。</font>
<!-- comment for text ` 4 个快捷入口`：4个过多，保留核心操作就好 --><!-- END_BLOCK_7 -->

<!-- BLOCK_8 | U93cd1qlfoiY7kxBnLUchJ7cnjd -->
<table header-col="true" col-widths="100,100,153,153,144">
    <tr>
        <td>入口名称</td>
        <td>~~个人主端~~</td>
        <td>独立任务
<!-- comment for text `独立任务`：Mark。 叫什么后面再考虑下用户心智，用户怎么理解 --></td>
        <td>定时任务</td>
        <td>助理配置</td>
    </tr>
    <tr>
        <td>入口链接</td>
        <td>~~&nbsp;xxx~~</td>
        <td>xxx</td>
        <td>xxx</td>
        <td>xxx</td>
    </tr>
</table>
<!-- END_BLOCK_8 -->


<!-- BLOCK_9 | QpChdVR7foOhECxwzGZcjd87nfb -->
### 新用户引导<!-- 标题序号: 2.2 --><!-- END_BLOCK_9 -->


<!-- BLOCK_10 | Iv9AdlyLPoJYCSxg2T5cwXWinKd -->
#### <font background_color="light_yellow">首次使用引导对话</font><!-- 标题序号: 2.2.1 --><!-- END_BLOCK_10 -->

<!-- BLOCK_11 | TpExdBR9koeJo8x6vLBceqb4nnF -->
参考 Web 标准文案（后续补充）
<!-- END_BLOCK_11 -->



<!-- BLOCK_12 | EgYMdgHOAo9Vuaxju2dcX1rpnDc -->
#### <font background_color="light_yellow">引导授权链路</font><!-- 标题序号: 2.2.2 --><!-- END_BLOCK_12 -->

<!-- BLOCK_13 | ZdmvdJpBYoOdS3xhyBec01HqnMe -->
引导跳转去 Web 完成授权
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | Tc9kdfQ4NoeHw7xXTtncGYlqngf -->
<table header-row="true" col-widths="273,450">
    <tr>
        <td>场景</td>
        <td>Message 文案示例</td>
    </tr>
    <tr>
        <td>首次引导授权 message</td>
        <td>嗨，朋友！我是你的专属助理🙋‍♀️ 要正式解锁我的全部功能，陪你处理日常、畅聊一切，还需要最后一步小小的授权哦~</td>
    </tr>
    <tr>
        <td>用户未授权，发送其他消息 message</td>
        <td>还没有完成授权，没法帮你做任务🥹 授权仅需 x 步，超简单的，完成后再召唤我吧！</td>
    </tr>
    <tr>
        <td>授权卡片</td>
        <td></td>
    </tr>
</table>
<!-- END_BLOCK_14 -->



<!-- BLOCK_15 | UFJVdlIMxoLne7xBClFciTCSnZd -->
### Agent 链路<!-- 标题序号: 2.3 --><!-- END_BLOCK_15 -->


<!-- BLOCK_16 | REtMdb4kTovaIFxV3p4cLW0Tnec -->
<callout icon="point_right" bgc="3" bc="3">
**开发前共识：无法实现双向完全互通**
1. **web 端&nbsp;**发的消息
	1. 用户发的：无法同步到飞书，生成用户本人发的消息**&nbsp;-- 飞书端只告知 response**
	2. Aime 发的：可同步到飞书，做样式映射
2. **飞书端&nbsp;**发的消息
	1. 用户发的：可同步到 web，做样式映射
	2. Aime 发的：可同步到 web，做样式映射
</callout>
<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | CV0JdYCkio12oYxm5XUcwSXenNa -->
#### Query - 用户发送<!-- 标题序号: 2.3.1 --><!-- END_BLOCK_17 -->

<!-- BLOCK_18 | PiNudtI6focm85xO1M4cZEzDnCd -->
用户发送的消息，可能是各种[飞书消息原子组合](https://bytedance.larkoffice.com/wiki/WOVKwR1TQiQNsGkf0dYcvJFQnUd#share-VQzfdGxDFomlsUxngi4cn9C6nlz)，下面列举几种典型的用户 query 形态：
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | ZIFTdxZiOozFdNxgU7LczOXUn9f -->
##### **飞书端发送：**<!-- 标题序号: 2.3.1.1 --><!-- END_BLOCK_19 -->

<!-- BLOCK_20 | HawsdTbbwoWNy6xLOWXcQQ2tnze -->
<table header-row="true" col-widths="233,191,166,280">
    <tr>
        <td>消息类型</td>
        <td>典型 query 形态</td>
        <td>示意图</td>
        <td>可能的意图</td>
    </tr>
    <tr>
        <td rowspan="4">有文本、表意清晰的单条query</td>
        <td>文本</td>
        <td></td>
        <td rowspan="4">如 query</td>
    </tr>
    <tr>
        <td>文本+代码</td>
        <td></td>
    </tr>
    <tr>
        <td>文本+文档</td>
        <td></td>
    </tr>
    <tr>
        <td>文本+图片/视频</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="3">多个 query 拼接、共同表意</td>
        <td rowspan="3">多条消息组合</td>
        <td></td>
        <td rowspan="3">因文件过多、飞书不支持拼接到单条消息中发送等原因，用户将一个意图拆成多条消息发送。

模型需要理解完整上下文。</td>
    </tr>
    <tr>
        <td></td>
    </tr>
    <tr>
        <td></td>
    </tr>
    <tr>
        <td rowspan="5">无文本、无法推断明确意图的query</td>
        <td>仅文档链接、平台链接</td>
        <td></td>
        <td rowspan="5">无法明确判断。

模型可以根据消息类型初步推断：
- 文档：概括信息、搜索内容、完善文档等
- 代码：代码检查、代码解释等
- 图片：描述/搜索图片信息等
- 本地文件：根据文件类型各不相同，如 logs 可能是检查日志等
- 系统消息/飞书卡片：询问信息等

再要求用户进一步澄清意图。</td>
    </tr>
    <tr>
        <td>仅代码</td>
        <td></td>
    </tr>
    <tr>
        <td>仅图片</td>
        <td></td>
    </tr>
    <tr>
        <td>仅本地文件</td>
        <td></td>
    </tr>
    <tr>
        <td>仅转发系统消息/飞书卡片</td>
        <td></td>
    </tr>
</table>
<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | Sx0KdcX4hoF8MXx3PjpcXfz1nuh -->
##### <font background_color="light_yellow">消息同步到 Web：</font><!-- 标题序号: 2.3.1.2 --><!-- END_BLOCK_21 -->

<!-- BLOCK_22 | OLagdWnO1oiFZ7xV7Z8cUTkjn0t -->
- 飞书/Web 消息同步基本原则：一期不需要额外开发 Web 样式，对标线上 Aime Web 前端能力，不支持的都拉平成纯文本
	- 富文本、at、飞书 emoji ... ：直接拉平
	- 图/视频/文混排：抽取放 query 气泡顶部
	- 话题、聊天记录、系统消息 ...：提取预览态文本信息
<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | S7rPddM3xop6nZxSxxmcVDbQnFd -->
- 详细映射示意：[Aime 个人助理｜飞书 & web 消息映射关系](https://bytedance.larkoffice.com/wiki/FCe2wqXjJimrRskohZhc9hjOnfc?from=from_copylink)
<!-- END_BLOCK_23 -->



<!-- BLOCK_24 | XQK7d1sYooy13Txk13gcDejsnmb -->
#### Response - Bot 回复<!-- 标题序号: 2.3.2 --><!-- END_BLOCK_24 -->

<!-- BLOCK_25 | Bi76dPa4bo9nQbxazbJcf1G5nSe -->
> <font background_color="light_yellow">❓待确认：引用 response 对应的用户 query ，一期是否能支持？ - 3.8 确认不支持</font>
> 
> 必要性：用户可能同时有多个任务在执行，在异步返回结果时，引用树让聊天不混乱
> 
<!-- END_BLOCK_25 -->



<!-- BLOCK_26 | GmUQd7mbQo6KnaxrrnicJtc8nRh -->
##### **飞书端回复****：**<!-- 标题序号: 2.3.2.1 --><!-- END_BLOCK_26 -->

<!-- BLOCK_27 | W5AKd1faroqB1Rx5GrzcgEuMnmh -->
<table header-row="true" header-col="true" col-widths="184,753">
    <tr>
        <td>环节</td>
        <td>Bot 回复消息</td>
    </tr>
    <tr>
        <td>接收 query</td>
        <td>只包含用户在飞书发的 query，接收后同步到 Web
Web 端发的 query 不同步到飞书，只同步任务结果到飞书</td>
    </tr>
    <tr>
        <td><font background_color="light_yellow">执行 query 告知</font></td>
        <td>Aime 回复前，模型执行状态，通过对用户 query 添加 emoji 来展示：

[了解][举手][在做了][敲键盘][击掌][致敬][稍等]

1. **助理 agent：**没有 queue 机制，会打断
	1. 正在执行的 query，thinking 过程中添加`敲键盘emoji`，response 或被打断，就撤回`敲键盘 emoji`

1. **路由到 SubAgent、Worker Agent：**有 queue 机制，不会打断
> 触发频控直接限制发送，不存在无限个 query 排队情况
> 
	1. 用户发送 query，Aime 接收到消息开始思考，在用户本轮意图的 **<font color="red">末条</font>** message 上添加`敲键盘 emoji` （若在进入 b 之前有连续多条 query， 或用户打断补充上下文， 就撤回前面的，保留末条的 emoji ）
	> 路由来的 query 示例：帮我写个 xxxxxxxx 文档
> 
	2. 告知用户已接收到 query，先回复 response，撤回 a 中的`敲键盘 emoji`
	> 告知 response 示例：好的我创建个文档，预计 2-3 分钟回复你
> 
	3. Subagent 或 worker 任务做完以后，回复任务执行结果
	> <font background_color="light_red">任务执行结果 response 示例：天一，这是我帮你梳理的文档，你看看还有啥要补充的，随时找我（文档链接）</font>
> 
> <font background_color="light_red">❓此时能否引用【告知 response 示例：好的我创建个文档，预计 2-3 分钟回复你】- P2 </font>
> </td>
    </tr>
    <tr>
        <td><font background_color="light_yellow">意图澄清</font></td>
        <td>[有些意图](https://bytedance.larkoffice.com/wiki/WOVKwR1TQiQNsGkf0dYcvJFQnUd#share-Eo1gd0ajOopu0LxiIgIcwV4wnyg)无法推测希望执行什么任务，模型可返回澄清 response
1. **<font background_color="light_yellow">&nbsp;</font>**<font background_color="light_yellow">Agent 根据上下文判断是否等待用户补充，如果要补充，等 x 秒 确认用户没有继续发消息</font>
> 用户要补充：“帮我整理下这个文档”；判断要等待；用户在10s 后添加了文档 
> 
> 用户没补充：一个文档+没操作；判断意图需澄清，reponse 要求添加描述；用户 query“帮我整理下这个文档”
> 
2. response 要求澄清：格式（描述已收到的信息）+（提议可能想做的任务）+（询问具体要做什么）
> 澄清示例：
> 
> （仅文档）收到你给我的[【WIP】 Aime - 个人助理](https://bytedance.larkoffice.com/wiki/AgkTwIb7Uisf0TkLDLic6kdnnoe?from=from_copylink)，这看起来是一个做Aime个人助理项目的PRD，请问你需要我做什么，是概括文档信息，还是搜索内容，或者有什么别的可以为你做的？
> 
> （仅图片）这幅巴洛克风格的画挺好看的，你在哪看到的？需要我给你科普一下巴洛克风格吗？
> 
> （仅文件）收到两个文件了，你需要我对它们做什么？比如：看看内容帮你总结；修改或填写；格式转换？
> 
> （仅系统消息）看到了你要在17:00-17:30 和 xx 开会（总结系统消息信息），你需要我帮你做什么操作？
> </td>
    </tr>
    <tr>
        <td>上下文</td>
        <td>1. 助理 Agent 有上下文完整信息，自行推理哪些query 属于当前任务
2. <font background_color="light_yellow">消息同步到 Web 兼容问题</font>
	1. <font background_color="light_yellow">主端此前有些消息类型不支持单独发送（比如首轮不支持发图片、首轮/多轮都不支持单独发文件），但飞书支持。</font>
<!-- comment for text `消息同步到 Web 兼容问题 主端此前有些消息类型不支持单独发送（比如首轮不支持...持单独发送附件消息。`：调通后实际验证下效果 -->	2. <font background_color="light_yellow">在本需求中，需要支持单独发送附件消息。</font></td>
    </tr>
    <tr>
        <td><font background_color="light_yellow">Web 同步</font></td>
        <td>Web 发送 query 获得的所有 response（包含澄清/最终产物），全部发送飞书 bot 通知，不判断用户是否当前开启 web 窗口。
特别的，本次新增的<font background_color="light_yellow">浏览器扫码，要在飞书上出助理 web 的任务链接，让用户去 web 扫码。</font>
> Web - query ---- 飞书 query
> 
> Web - 浏览器扫码在 web 容器打开 --- 飞书 - 浏览器扫码，用户自主点击打开
> 
> Web - 任务完成产物 --- 飞书 - 任务完成产物
> </td>
    </tr>
    <tr>
        <td>回复层级</td>
        <td>私聊 Bot 场景，默认为**独立消息**回复
<font background_color="light_yellow">若用户</font>**<font background_color="light_yellow">主动为对话创建话题</font>**<font background_color="light_yellow">，则 Bot 继续在话题内回复</font>
<!-- comment for text `若用户主动为对话创建话题，则 Bot 继续在话题内回复 若用户离开话题，回到 I...在哪发、我们在哪回）`：pending 本期不做回复层级，那bot的所有回复都是在IM里边吗，包括用户在话题下的消息 --><font background_color="light_yellow">若用户离开话题，回到 IM 发消息，回到 IM 用独立消息回复</font>
<font background_color="light_yellow">（用户上一条在哪发、我们在哪回）</font></td>
    </tr>
</table>
<!-- END_BLOCK_27 -->



<!-- BLOCK_28 | B61dd2LGuoW17cx9RPOcCirhnZf -->
##### **<font background_color="light_yellow">兜底情况：</font>**<!-- 标题序号: 2.3.2.2 --><!-- END_BLOCK_28 -->

<!-- BLOCK_29 | HoDCdepkIoOsKSxo0QscJG9knag -->
不走模型，返回固定文案
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | ZwHedSZNXoGk4cxCiGLcfww5nBC -->
- 进程中断、服务停止、触发违规等其他失败情况，回复Message：遇到了一点问题，稍后再尝试吧
<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | EWXJdUR1doKL92xBiexcahPDn7g -->
-  Aime 频控限制，回复Message：太多任务在排队啦，稍后再召唤我吧
<!-- comment for text ` Aime 频控限制，回复Message：太多任务在排队啦，稍后再召唤我吧`：Cc @dingbo.2020@bytedance.com --><!-- END_BLOCK_31 -->

<!-- BLOCK_32 | BD2hdlnSuo518txTYRgcqrcrnBe -->
- 飞书发消息频控限制，无法返回 message，暂不处理
<!-- END_BLOCK_32 -->



<!-- BLOCK_33 | Xud1dtGMaovGAyx0Am4cdPyjnDf -->
##### **回复形态：**<!-- 标题序号: 2.3.2.3 --><!-- END_BLOCK_33 -->

<!-- BLOCK_34 | By0Od4AmVoZOkGxtwszcozGXnhf -->
基本原则：主要依据时间判断，**<font background_color="light_yellow">耗时长的任务</font>**<font background_color="light_yellow">用飞书卡片承载，异步通知</font>
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | Cx48dHuw4olH6ax9VoGc8MZCnSc -->
- 助理 Agent 只返回消息
<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | Ovf7dTyUGoKhqYxJLCDcONLPnoh -->
- SubAgent 只返回消息（含系统消息）
> Response 1：好的我创建个日程提醒，预计 2-3 分钟回复你
> 
> Response 2：天一，这是我帮你创建的日程提醒，已经发给大家了
> 
> Response 3：（系统消息 - 日程提醒）
> 
<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | XLbFdLWijoZnQdxbeDgcABpBnLg -->
- Worker 可返回消息（含系统消息）~~、~~**飞书消息卡片**
> Response 1：这个任务需要点时间，我去研究下，完成后提醒你
> 
> ~~Response 2：（飞书消息卡片）你交给我的任务完成啦，快去看看吧~ + 任务描述 + 产物文件链接 + {按钮}~~
> 
> <grid cols="2">
> <column width="38">
>   > > 
>   > 
> </column>
> <column width="61">
>   > > 
>   > 
> </column>
> </grid>
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | MBY2dDVDboqRRLxYVchcLQmwnzg -->
##### <font background_color="light_yellow">消息同步到 Web：</font><!-- 标题序号: 2.3.2.4 --><!-- END_BLOCK_38 -->

<!-- BLOCK_39 | IecTdW78foyFBixsDW4cGhJPntc -->
- 飞书/Web 消息同步基本原则：一期不需要额外开发 Web 样式，对标线上 Aime Web 前端能力，不支持的都拉平成纯文本
<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | CD9tdqP7noPYSBxgejychuvRnDg -->
- 详细映射示意：[Aime 个人助理｜飞书 & web 消息映射关系](https://bytedance.larkoffice.com/wiki/FCe2wqXjJimrRskohZhc9hjOnfc?from=from_copylink)
<!-- END_BLOCK_40 -->



<!-- BLOCK_41 | GL3FdRyyyoPOcExgFM9c6cM5nqf -->
## 飞书 bot - 群聊<!-- 标题序号: 3 --><!-- END_BLOCK_41 -->

<!-- BLOCK_42 | N5sNdLmcWoYb6TxjIP7cPFwrnUc -->
<callout icon="point_right" bgc="3" bc="3">
**群聊的 3 个关键点**
1. 群只能@ 机器人发送消息
2. 所有消息转成话题回复，避免刷屏
<!-- comment for text `所有消息转成话题回复，避免刷屏`：pending -->3. 群任务和消息同步到主端，不同步到个人机器人
</callout>
<!-- END_BLOCK_42 -->


<!-- BLOCK_43 | Zp6UdH9YXomQstxTIlCcdDDfnMh -->
### <font background_color="light_yellow">群聊引导授权链路</font><!-- 标题序号: 3.1 --><!-- END_BLOCK_43 -->

<!-- BLOCK_44 | LYCldKOmrodIpIxCkfTczOrKnLb -->
在群聊内，引导跳转去 Web 完成授权，引导消息群内可见。
<!-- END_BLOCK_44 -->

<!-- BLOCK_45 | BlcEdkGfFoCdrMxCYSMceyV8nVi -->
注意：群聊不发卡片，只发消息，避免刷屏。
<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | WoIgdK0s9oaaKrxHPs8co8u5ntc -->
<table header-row="true" col-widths="273,450">
    <tr>
        <td>场景</td>
        <td>Message 文案示例</td>
    </tr>
    <tr>
        <td>首次发 query 引导授权</td>
        <td>嗨，朋友🙋‍♀️ 要正式解锁我的全部功能，帮你总结群消息、发起日程邀请... 还需要最后一步小小的授权哦~
👉点我完成 Aime 个人助理（授权链接）</td>
    </tr>
    <tr>
        <td>用户未授权，发送其他消息</td>
        <td>还没有完成授权，没法帮你做任务🥹 授权仅需 x 步，超简单的，完成后再召唤我吧！
👉点我完成 Aime 个人助理（授权链接）</td>
    </tr>
</table>
<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | HElldBfEFom9ClxVNhRcLYa4nBf -->
### 群聊 Agent 链路<!-- 标题序号: 3.2 --><!-- END_BLOCK_47 -->

<!-- BLOCK_48 | NrUedMCRtoozWxxzYJlclJSUnbd -->
#### Query - 用户发送<!-- 标题序号: 3.2.1 --><!-- END_BLOCK_48 -->

<!-- BLOCK_49 | PvrddKHCCojiilxlULuc59A9nWe -->
用户在群内 @Bot 发送消息
<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | L1dndLggcoptVmxaT7EcGZk7ncC -->
#### Response - Bot 回复<!-- 标题序号: 3.2.2 --><!-- END_BLOCK_50 -->

<!-- BLOCK_51 | A96VdEV95oGRCZxzSmqc1kgfn8b -->
<table header-row="true" header-col="true" col-widths="184,753">
    <tr>
        <td>环节</td>
        <td>Bot 回复消息</td>
    </tr>
    <tr>
        <td>接收 query</td>
        <td>同私聊</td>
    </tr>
    <tr>
        <td>执行 query 告知</td>
        <td>每个用户有自己的队列，在所有 response 前，增加**&nbsp;@ 用户**</td>
    </tr>
    <tr>
        <td>意图澄清</td>
        <td>同私聊</td>
    </tr>
    <tr>
        <td>上下文</td>
        <td>与私聊区别：上下文包含群聊所有聊天记录</td>
    </tr>
    <tr>
        <td>回复层级
<!-- comment for text `回复层级 群聊 bot 场景，默认把消息转成话题回复，话题建在首 query 之...t，不再创建新的话题`：pending --></td>
        <td>群聊 bot 场景，<font background_color="light_yellow">默认把消息转成话题回复，</font>话题建在首 query 之下。
话题内多轮，始终结合话题内完整上下文回答
话题内再 at bot，不再创建新的话题</td>
    </tr>
</table>
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | ElNUdTmjioaBx2x3bescBewinBb -->
兜底情况、回复形态同私聊。
<!-- END_BLOCK_52 -->



<!-- BLOCK_53 | OVhbdU6epoyjCOx28C2csH4AnEg -->
### <font background_color="light_yellow">群聊Web/飞书消息同步</font><!-- 标题序号: 3.3 --><!-- END_BLOCK_53 -->

<!-- BLOCK_54 | NYhxdSp8HofPcYxSuDtcRFkXnJf -->
1. **基本逻辑：**群任务和消息同步到 Web 主端，不同步到个人飞书 bot
<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | TvSBd7KNEoGUqzxAGgecAnjAnOC -->
2. **同步人群：**只有用户自己@ bot 才同步
<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | LZ3hd9YLco0u4Mx5IGocsZkcnCc -->
3. **同步范围：**只同步用户 @bot 的 query 的引用形态（不展示全文，只展示缩略文案，标注来自 xxx 群）、bot 回复用户的 query
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | ZPDBdjq5xolyuDx68HactBtLnwc -->
4. **示例：**
👉飞书
用户 A 在群里 @ bot：query1
bot @并回复用户 A：response1
用户B @ bot：query2
bot @并回复用户 B：response2

👉用户 A 的Web
Aime：
> query1 前 x 字纯文本   **来自 xxx 群**
> 
response1

👉用户 B 的 Web
Aime：
> query2 前 x 字纯文本   **来自 xxx 群**
> 
response2
<!-- END_BLOCK_57 -->





<!-- BLOCK_58 | FZlqdG2tRoJG6Wx4H4JcHJMznld -->
## 附录：飞书消息原子组合<!-- 标题序号: 4 --><!-- END_BLOCK_58 -->

<!-- BLOCK_59 | Ddy3desZboPrPxxvqJMcEwxsnBd -->
> 以下信息供了解飞书消息构造
> 
<!-- END_BLOCK_59 -->

<!-- BLOCK_60 | IK8NdZt67oJ4hAxZes8cL9sNnkd -->
<table header-row="true" header-col="true" col-widths="119,248,138,303">
    <tr>
        <td>一级分类</td>
        <td>二级分类</td>
        <td>示意图</td>
        <td>是否可与其他原子组合</td>
    </tr>
    <tr>
        <td rowspan="8">独立消息</td>
        <td>纯文本</td>
        <td></td>
        <td>允许组合</td>
    </tr>
    <tr>
        <td>富文本</td>
        <td></td>
        <td>允许组合</td>
    </tr>
    <tr>
        <td>图片/视频</td>
        <td><grid cols="2">
<column width="53">
</column>
<column width="46">
</column>
</grid></td>
        <td>允许组合</td>
    </tr>
    <tr>
        <td>艾特</td>
        <td></td>
        <td>允许组合</td>
    </tr>
    <tr>
        <td>飞书 emoji 表情</td>
        <td></td>
        <td>允许组合</td>
    </tr>
    <tr>
        <td>用户添加的图片表情包</td>
        <td></td>
        <td>不允许组合</td>
    </tr>
    <tr>
        <td>文件</td>
        <td></td>
        <td>不支持组合</td>
    </tr>
    <tr>
        <td>文件夹</td>
        <td></td>
        <td>不支持组合</td>
    </tr>
    <tr>
        <td rowspan="2">回复消息</td>
        <td>消息引用</td>
        <td></td>
        <td>必须组合普通消息</td>
    </tr>
    <tr>
        <td>回复 emoji 表情</td>
        <td></td>
        <td>必须组合普通消息</td>
    </tr>
    <tr>
        <td rowspan="2">聚合消息</td>
        <td>话题消息</td>
        <td></td>
        <td>不支持组合</td>
    </tr>
    <tr>
        <td>合并转发聊天记录</td>
        <td></td>
        <td>不支持组合</td>
    </tr>
    <tr>
        <td rowspan="2">飞书结构化消息</td>
        <td>飞书消息卡片</td>
        <td></td>
        <td>不支持组合</td>
    </tr>
    <tr>
        <td>系统消息（会议日程、任务待办等）</td>
        <td></td>
        <td>不支持组合</td>
    </tr>
</table>
<!-- END_BLOCK_60 -->



