<title>Aime Skill 开发指南</title>
<url>https://bytedance.larkoffice.com/wiki/MQAnwMcdFiFKrAkCIKQcUTPon8b</url>
<content>
<!-- BLOCK_1 | PF71dGeGmof2B5xzj1fcObUxnte -->
# Skill  开发指南<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | QI6Qd6JErot179xRvTTcWORHnhf -->
## SKILL.md  Aime 实践心得<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | PKWbdhAmsonXfMxXsQ6c1UJAnWw -->
![图片](img_AGHlbk2GNoSVBCxAm9mcPv6pn4c.png)
<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | A9fOdUIuyo73IHxW1wbcRVn7n7b -->
**Name**
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | X1dddVJjvo6iU1xcpQscL7Bnnbg -->
一个英文名称，遵循 Claude Skill 规范
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | Wy0ddontZo1ijfxY0B0cf6TlnMh -->
**Description**
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | Srx5dDZA9ogDTKxr5Qtcy8frn1g -->
是什么，有什么能力，适用场景。 决定被模型主动召回的灵魂，需要写清楚
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | W2tQdPsGNoZjcixXjyCcUuSqnjg -->
```yaml
---
name: feishu-card
description: <font color="purple">生成美观样式的飞书交互式消息卡片</font>，<font color="blue">支持通过邮箱、群组或webhook发送</font>。<font color="red">适用于创建公告、产品发布、系统通知、项目进度、日报、活动通知、庆祝祝贺或任何需要通过飞书分享的结构化内容</font>。
---
```
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | M5KfdyrNFoK3UzxkSUtc7BZvn1e -->
**具体内容 Content**
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | Un58dxtFYoQNClx9FSacqbSHncd -->
<callout icon="pushpin" bgc="4" bc="4">
核心原则： 按需加载，最小化原则
核心建议： 
- 如果是一个功能性 skill， 当模型看到你的 SKILL.md 时，就可以完成大多数任务了（70-80%的活），而不是依赖读取 references 才能干活，更复杂的活，才应该封装到 references 里面去完成。 这样能提升效率，节约 token。 所以 skill.md 的写法 <font color="red">很重要，很重要，</font>他是你这个 skill 的索引，指导干活的总纲。
- 如果模型已经知道的世界知识，不需要过多介绍，增加上下文占用。(**你认为他需要，其实他不需要**)
- 去除所有与该 skill 无关的描述，比如该接口由 xxx 实现，只要教会他怎么用 ，不需要教会他原理，引入无关描述（当然原理排查类的 skill 除外）
</callout>
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | MY9MdgIhoodMRSxPnsgc8V6UnML -->
举个例子： 比如你 skill 中有80个工具或者脚本，而常用的只有10个，那么 skill.md 的写法就应该如下，不止介绍工具，还需要介绍怎么使用，最佳实践
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | TMqsdmNP8oB3rtx7tRjcRQAFntg -->
```markdown
<font background_color="light_green"># 工具介绍</font>
该Skill 主要通过以下工具去完成任务

## 工具1: xxx
```bash
python3 xxxx --prompt xxx --toolset xxx
```
参数说明：
- prompt 必需
- toolset 可选，使用值：files，bash 
....

## 工具10:xxx
xxx

<font background_color="light_green">## 更多工具</font>
如果你需要完成更多更复杂的任务，请参考 /references/tools.md，<font background_color="light_green">多数情况下不需要查看</font>


<font background_color="light_green"># 最佳实践</font>
xxx情况： 应该调用xx工具完成什么事情
xxx情况： 应该xxx完成什么事情

<font background_color="light_green">## 更复杂的实践</font>
如果你需要完成更多更复杂的任务，请参考 /references/best.md
```
<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | HMRjdDP1So9folxItHUcn4q2nyf -->
## Skill-Creator 解读<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | IGSIdIiEXoo395xujIfcb8XNnwg -->
目前官方的 Skill-Creator  对于要开发一个真正可用的 Skill 存在一些问题，如 Aime 实践心得的部分其实包含的不全。但是也有一些很好的思想值得开发者看看。
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | IpzZdBVgRofVm9xlFlkckpmYn2g -->
- 英文版本： https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md 
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | Fpu4dQ414owASDxbgklc8Q8ynFg -->
- 中文阶段： [Skill-Creator 中文解读](https://bytedance.larkoffice.com/wiki/EYE9wl0qZiLwuLkBurKcgiXWnMn)
<!-- END_BLOCK_16 -->



<!-- BLOCK_17 | EQu9dGB9foU3r0x1LceclkDtnZg -->
## 如何在脚本中注入 jwt token<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | Pljhdfj5roeqPCxFo3HcizoPnJg -->
从环境变量 直接直接取 $AIME_USER_CLOUD_JWT
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | RLmjdAlxqoHAE2xWMcSco06LnMh -->
```python
## <你的脚本>
# 从环境变量获取JWT token
jwt_token = os.environ.get('AIME_USER_CLOUD_JWT')
   if not jwt_token:
       print("错误: 未找到环境变量 AIME_USER_CLOUD_JWT，请设置此环境变量后再试")
```
<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | VJmfd096EoCINCxBP4KckhPdn2c -->
其他动态注入的环境变量列表
<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | PFW7dxGnio9QnmxcNMDcmtWtn3e -->
```go
***AimeEnvSessionID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_SESSION_ID"
***AimeEnvSpaceID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_SPACE_ID"
***AimeEnvCurrentUser&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "AIME_CURRENT_USER"
***AimeEnvCurrentUserEmail&nbsp;***AimeShellEnviron = "AIME_CURRENT_USER_EMAIL"

// 当前 workspace 所在路径
***IRIS_WORKSPACE_PATH&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***AimeShellEnviron = "IRIS_WORKSPACE_PATH"
```
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | HD3zdD9acoyTM8xcuQMcDY5pned -->
## 如何检查skill 环境<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | KByYdA4zpoJbKYxb6GDcWGXBnYc -->
```
SkillRootDir/
├── SKILL.md
├── references/
├── script/
└── .aime/
    └── setup/                 # 环境配置脚本
        └── setup.sh           # skill 需要提前安装的依赖 (pip/npm install xxx)
```
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | Emq7dsBEZovr2VxoOyEc4eyWnMg -->
在**&nbsp;setup.sh&nbsp;**   中放入你需要提前安装的依赖，如：**&nbsp;**`pip install xxx`
<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | Sk8dd9aykoajdQxjvoHcFaPUnQg -->
调用skill时，会进行执行与检查
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | WARWdedixo5IqfxRFHFco4Ybnod -->
![图片](img_ErXnbd4cmo3SSUx0Mhzcm98gnXj.png)
<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | doxcn24ZzgvYbvKNM35Oo87GJLg -->
## 动态上下文注入<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | doxcnIyfVUVHrpDpmzw6bZs5l5f -->
在 SKILL.md 中支持 `!`command` `语法，可以在 skill 内容发送给 AI 之前执行 shell 命令，将命令输出动态替换到占位符位置。这对于需要实时数据的场景非常有用。
<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | doxcn7xfafAH7SmtX4PUnBD29jd -->
**语法说明**
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | doxcnVgDu7oJJY59ihkZ9UhlXre -->
<table header-row="true" col-widths="350,350">
    <tr>
        <td>语法</td>
        <td>说明</td>
    </tr>
    <tr>
        <td>`!`command``</td>
        <td>执行命令，输出替换占位符</td>
    </tr>
    <tr>
        <td>`\!`command``</td>
        <td>转义，不执行命令</td>
    </tr>
</table>
<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | doxcnbsqSjU00VdkVOJVrV7jVeb -->
**使用示例**
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | doxcnmfStWeOlZhOsL4KN2fTHjg -->
```markdown
---
name: pr-summary
description: 总结 PR 变更
---

## PR 上下文信息
- PR diff: !`gh pr diff`
- PR 评论: !`gh pr view --comments`
- 变更文件: !`gh pr diff --name-only`
- 当前时间: !`date`

## 你的任务
根据以上 PR 信息，总结这个 Pull Request 的主要变更...
```
<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | doxcnLvDjz7fkOoCSajiOc5BIQg -->
**工作原理**
<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | doxcnIbPvKdGWFPOShwxLwNL79d -->
1. 当 Skill 被加载时，系统会扫描 SKILL.md 中的 `!`command`` 模式
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | doxcnhiBkxV74VCx7pg0nR9eKvg -->
2. 每条命令会在用户workspace下执行
<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | doxcntWLV8Mn37oOUXohOCF72Bb -->
3. 命令输出会替换原始占位符
<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | doxcn8yDGHurV69T8cqpo7gXt1g -->
4. AI 收到的是包含实际数据的完整内容
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | doxcnJpbNaEhr6DZoRpHZxJeKTf -->
大输出处理
<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | doxcnEvFJmh0CDfCRRn2rGnxQUe -->
当命令输出超过 **8000 字符** 时，系统会自动：
<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | doxcnpjTDIx99wBEnfm2mhyarzf -->
1. 将输出保存到 `data/dynamic_output_{hash}.txt` 文件
<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | doxcnAp9o4ssaXr8eziSbHRRXfh -->
2. 在原位置插入提示信息，指引 AI 读取该文件
<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | doxcnBeWaMmgAUO3hlo1RvMO0Ig -->
```markdown
## 处理后效果（大输出场景）
- PR diff: 
[命令输出已保存到文件: data/dynamic_output_abc123.txt，请使用 read 工具读取该文件获取完整内容]
```
<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | doxcnfnQ9inrwVtFHiDbn7XR29b -->
适用场景
<!-- END_BLOCK_43 -->

<!-- BLOCK_44 | doxcnCgE4SJKJYMeu8fvdNMHOsd -->
- 获取 Git/GitHub 实时信息（PR、commit、branch 等）
<!-- END_BLOCK_44 -->

<!-- BLOCK_45 | doxcnG6cOib98zB3rfjrm1gAMOg -->
- 注入当前时间、环境信息
<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | doxcnexY1a3G0e7nyMhZa9TiNLd -->
- 读取动态配置或状态文件
<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | doxcnNMZLIt4uy9CiIHp6042B6g -->
- 任何需要实时数据的 Skill 场景
<!-- END_BLOCK_47 -->



<!-- BLOCK_48 | TTapdvHVJoPtSWx2TpKcc4uenjd -->
## Skill 中模型调用<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | W9Indy5I9oulIex4giOcnll4nie -->
- 目前如果 SKill 脚本中，想调用模型能力，建议自己申请 api_key，直接调用即可 
	- 方舟：https://cloud.bytedance.net/ark/region:ark+cn-beijing/overview
	- gpt 平台：https://gpt.bytedance.net/gpt_openapi/model-square
> 后续可以考虑脚本中直接调用 Aime 内部模型能力，目前安全和风险性还未设计，所以暂不支持
> 
<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | BeIHdeSh3oPNeyx55o0cOePNnfc -->
# Aime 容器环境<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | EBEhds3xOoKsGQxFJTycD6x5nYc -->
- Python: 3.11.9   常见的依赖包不需要安装，如果自己的依赖包，需要安装
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | VMMqdjaVro5EXyxtCtscmeUPnUd -->
- Java: openjdk 17.0.6 2023-01-17
<!-- END_BLOCK_52 -->

<!-- BLOCK_53 | Pa7ZdgoWTo1PlyxwQJlcD34Cn3c -->
```markdown
SKILL.md 内容
步骤一，执行xxxx脚本，获取数据
步骤二，<font background_color="light_green">分析xxx的内容</font>（这个就是agent自己的模型能力）
步骤三，执行xxx脚本
xxxx
```
<!-- END_BLOCK_53 -->

<!-- BLOCK_54 | CZt2d4v8ZoXhSCxxiNGcPy4JnJe -->
- Node v22.21.1    npm: 10.9.4
<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | Efl0dcVQRo1208x1ClAc3OApn5f -->
- Go version go1.24.9 linux/amd64
<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | XMwGd2zWuoBaTcxu4mIcm5JHnUh -->
也可以自己在发起一个任务后，通过任意方式进入 webshell/ssh shell 去查看环境信息
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | XvLFdnBjSo9oprxd3n4cPozanBc -->
<grid cols="2">
<column width="44">
  ![图片](img_XkMWbv4hWoSOR9xypfJc3CFVnfk.png)
</column>
<column width="55">
  ![图片](img_Udaqb8H7ootsQDxhzebcxGEzneh.png)
</column>
</grid>
<!-- END_BLOCK_57 -->




</content>
