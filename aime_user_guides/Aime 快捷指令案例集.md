<title>Aime 快捷指令案例集</title>
<url>https://bytedance.larkoffice.com/wiki/AEpbwGL1si8JMMk6XDEcsI14n8f</url>
<content>
最近更新：2026-01-09

### 群聊总结
1. 功能：支持对**单个**或**多个群**的指定时间范围内的聊天内容进行总结分析
2. 典型场景：
	1. 用户反馈群的问题总结
	2. 稳定性值班群的问题汇总
3. Show case：
	1. 对多个用户反馈群的问题进行日常分析：https://aime.bytedance.net/share/be0d1dfc-79c0-4590-9970-639d3b9fb681
4. 操作流程👇
	1. 打开Aime->https://aime.bytedance.net/chat
	2. 选择“群聊总结”快捷指令
	![图片](img_L7BmbAtjJotXEjxEyJvcM6ADn4e.png)
#### 注意事项：
- 把Aime 机器人拉到你要分析的群聊里（飞书群会有提示，建议提前周知）
- **<font background_color="light_yellow">添加「飞书聊天记录」MCP</font>**，点击「拓展->工具配置」后，搜索关键词后点「+」添加
<grid cols="2">
<column width="41">
  ![图片](img_ZRgrbZfXloKSKrxSgjBcnI7UnNf.png)
</column>
<column width="58">
  ![图片](img_A2Ejbne9bo2jeVx62sxcWzLZn8f.png)
</column>
</grid>


### 风神看板分析
1. 场景：一句话，一个风神看板，一个周报模板文档，Aime帮你写运营周报了！
2. 操作流程👇
	1. 打开Aime->https://aime.bytedance.net/chat
	2. 选择“风神数据分析”快捷指令
	![图片](img_GEBebSrRNo0FZ2xbKaycSCx6ndf.png)
	- 难点1：检查你的风神看板，是否包括你要的核心数据，**指标越精简，分析越准确**
	- 难点2：判断 [运营周报模板-社区产品](https://bytedance.larkoffice.com/wiki/GQg8wd33viMhXak6LmOcQUJQnQh)这个模板是否满足你们团队的周报要求，如果不满足，你也可以让Aime分析你们组之前的周报，提炼框架。【注意：一些基本规则，可以提前给Aime，直接在对应的地方 @aime 让他严格遵守你的要求。】这里就是最大的门槛了，需要一点儿耐心，大家可以随时call我，咱们一起调优～
	![图片](img_LuyPbiP7Qo6qnHxx3oecSC9inBf.png)
3. 高阶玩法：你也可以让Aime直接分析你的群信息（开启群聊功能的具体操作）
4. 效果还是可以的，一次投入，周周受益！
![图片](img_Fe4ObF01loIgYtxVIu3cg7hnntf.png)

### OKR 总结
1. 功能：支持获取个人的OKR内容进行分析；如果是leader，除个人OKR外，还支持获取团队成员（leader-1）的OKR内容进行综合分析
2. 典型场景：
	1. 个人或团队OKR的工作总结
3. Show case：
	1. 某团队的Q3 OKR 总结
	<grid cols="2">
<column width="50">
  Aime 任务描述
  ![图片](img_GwYZbQGTmoWtrSxo2qPcSt9GnBf.png)
</column>
<column width="50">
  报告部分内容的效果呈现
  ![图片](img_BYtAbsMPioFzgTx3VLIcYg41nFh.png)
</column>
</grid>
4. 操作流程👇
	1. 打开Aime->https://aime.bytedance.net/chat
	2. 选择“团队总结”快捷指令
	![图片](img_Kr4LbRtpgoVHVnxT0z1cpNwnn5f.png)

### Oncall总结
1. 功能：支持对团队oncall平台的工单一键总结分析，也支持不同周期的oncall情况数据分析对比，帮你清晰了解用户需求和产品更新方向。
2. 典型场景
	1. 一定周期的oncall总结复盘
	2. 不同周期的oncall情况对比分析
3. Showcase
	1. 一周oncall总结分析
<grid cols="3">
<column width="32">
  ![图片](img_U84tb2KtzoBr7SxsC1JcnjH9nTg.png)
</column>
<column width="40">
  ![图片](img_BVMwbZDJPoQ18TxSkuQcQh3Injf.png)
</column>
<column width="27">
  ![图片](img_SiJFbtLhdo1blxxBG3lc34e8nke.png)
</column>
</grid>
4. 操作流程
	1. 打开Aime->https://aime.bytedance.net/chat
	2. 选择“oncall总结”快捷指令，打开“拓展”里的oncall mcp
<grid cols="2">
<column width="54">
  ![图片](img_Kmj6bpbIjoKrIJxk30FcDO4mnQe.png)
</column>
<column width="45">
  ![图片](img_TzPsb1Ag2ouXpfxqDJjcFM5Sngg.png)
</column>
</grid>
5. 使用技巧
	1. **明确范围**：指定oncall平台的`值班人`和`时间周期`。
	2. **定义标准**：告知Aime清晰的oncall`分类和打标规则`。
	3. **善用模板**：根据交付需求提供`文档模板`，让Aime稳定输出高品质报告。

### Libra实验分析
1. 功能：支持对Libra实验报告一键总结分析，也支持不同周期的Libra实验报告情况数据分析，帮你清晰了解实验组和对照组的正负向差异以及显著性分析
2. 典型场景
	1. 对实验某些指标进行重点分析
	2. 对实验某一周期内容的指标进行分析
3. Showcase
实验分析报告生成（数据脱敏）
![图片](img_YUj9bdK0Zo2JZGxXh0fcHICHnff.png)
4. 操作流程
	1. 打开Aime->https://aime.bytedance.net/chat
	2. 选择“Libra数据分析”快捷指令
![图片](img_ZTiObNI4voacIyxITI7cKio6nge.png)
	1. 填入具体的参数
		1. 粘贴实验报告的链接和PRD文档链接
		2. 指定时间范围（不指定则为实验默认周期）
		3. 指定分析的重点的实验指标（不指定则为全部指标）和分析逻辑

![图片](img_JC7VbSiLEouZkixZHYVc5p40nAd.png)


</content>
