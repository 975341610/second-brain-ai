<title>Aime X Bits One-Pager</title>
<url>https://bytedance.larkoffice.com/wiki/TIL7wIhVjiqt3MkPbrIcMDw4nig</url>
<content>
最近更新：2026-01-09

# 关于 Aime
## Aime 的定位
Aime 是专为字节同学打造的 AI Agent 工作平台，面向工作场景，集成了字节内部常用工具，帮助大家高效完成各类繁琐重复的任务，包括但不限于：写代码、分析数据、做调研、写文档等。

> 详细介绍：[Aime — 开启字节同学的异步办公新体验](https://bytedance.larkoffice.com/wiki/XxvZwyuyUiTlDEkrEHacSMJKnFe)
> 

## 联系方式
<table header-row="true" col-widths="200,100">
    <tr>
        <td></td>
        <td>PM</td>
    </tr>
    <tr>
        <td>整体 POC</td>
        <td>@(zhujingyan.43@bytedance.com)</td>
    </tr>
    <tr>
        <td>研发场景 POC</td>
        <td>@(maqijun@bytedance.com)</td>
    </tr>
    <tr>
        <td>CodeReview 相关</td>
        <td>@(chenyueyan@bytedance.com)</td>
    </tr>
    <tr>
        <td>DevMind 相关</td>
        <td>@(wzh.albert@bytedance.com)</td>
    </tr>
</table>

# CodeReview
<callout icon="art" bgc="4" bc="4">
- 目前功能已经全量，所以仓库都可以通过邀请 aime 触发任务。
- 如果要开启自动邀请的话，可以选择在 codebase/repo/settings 进行配置。
	- 批量开启需求，请通过 [https://bpm.bytedance.net/apply?cid=16970](https://bpm.bytedance.net/apply?cid=16970) 提交工单，无需审批
</callout>


## 数据看板
https://data.bytedance.net/aeolus/pages/dashboard/1386736?appId=739695&sheetId=1897869

## 历史案例
<table header-row="true" col-widths="200,244,376">
    <tr>
        <td>部门</td>
        <td>回放链接</td>
        <td>用户之声</td>
    </tr>
    <tr>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
</table>

<table col-widths="52,601,376">
    <tr>
        <td colspan="3">**在 Aime 对单次 MR 使用 Aime 做 CodeReview**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>选择一个模板或者直接在任务栏输入 CR 的内容</td>
        <td>![图片](img_SeuJb335eoHxnux8HfvcfsYqnse.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>如果使用模板，填入 MR，发起任务</td>
        <td>![图片](img_FcBZbsSLgo0QNnxKsh0cyyBtnxb.png)</td>
    </tr>
    <tr>
        <td colspan="3">**在 Codebase 对单次 MR 使用 Aime 做 CodeReview**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>邀请 Aime 作为评审人
> 添加后 Aime 就会开始进行 CodeReview
> 
> Aime 任务使用的是添加 Aime 的用户的权限。
> 
> CodeReview 会消耗用户的 Aime 次数。
> </td>
        <td>![图片](img_VKBEbWEMRoEOb7x9bCIc27iIn5Z.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>在检查中可以看到一个 Aime CodeReview，然后在详情中可以看到对应的 Aime 任务链接。
> 新的 MR Version 不会创建新的任务。
> </td>
        <td>![图片](img_Che6bz6uoo16YnxVKjpc28S2n0e.png)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>点击 Re-run 之后会创建一个新的 CodeReview</td>
        <td>![图片](img_Sj1Fbr1PIotPPkxZg7Occirpneh.png)</td>
    </tr>
    <tr>
        <td>4</td>
        <td>CodeReview 运行完毕之后会将结果添加到代码中</td>
        <td>![图片](img_BNhQbxK8HotOQsxdbWOcNEdPnSh.png)</td>
    </tr>
    <tr>
        <td colspan="3">**在 Codebase 每次 MR 都使用 Aime 做 CodeReview**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1. 选择设置 - Code AI features
2. 选择 Aime 作为默认的评审人
> 批量开启默认开关用  [https://bpm.bytedance.net/apply?cid=16970](https://bpm.bytedance.net/apply?cid=16970) 提交工单，无需审批
> </td>
        <td>![图片](img_XXBDbVpZYoklMQx8utYc49Q1n8f.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>后续会默认将 Aime 添加为评审人。</td>
        <td>![图片](img_AdSvbVrtdo0LkBxT48dceQyEnJh.png)</td>
    </tr>
    <tr>
        <td colspan="3">**自定义 CodeReview 规则**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>在业务仓库的 AGENTS.md 里面增加业务规则的说明，或者直接引库内/外部的文档链接。
> [Aime 项目记忆（AGENTS.md）使用指南](https://bytedance.larkoffice.com/docx/VetbdMSMpoXMRMxiQuDcie7inth)
> 
> 注意： 自动发起的任务，由于不依赖用户登陆 Aime，因此可能存在 Lark Token 过期的问题，所以如果有 Lark 文档可能读不到，建议都保存在仓库里面
> </td>
        <td></td>
    </tr>
</table>

## 使用流程
# DevMind
## 历史案例
<table header-row="true" col-widths="200,244,376">
    <tr>
        <td>部门</td>
        <td>回放链接</td>
        <td>用户之声</td>
    </tr>
    <tr>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
</table>

## 使用流程
<table header-row="true" col-widths="52,611,376">
    <tr>
        <td colspan="3">使用 Aime 分析 DevMind 的洞察报告</td>
    </tr>
    <tr>
        <td>1</td>
        <td>打开 DevMind 任一自己有权限的“洞察报告”</td>
        <td>![图片](img_C46ub2xAFoB8TDxQqpJcJn4unUh.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>通过右上角“数据洞察助手”打开数据分析任务抽屉</td>
        <td>![图片](img_TQtcbURcjoktMPxSeExcwZq4ntb.png)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>透过抽屉入口或通过特定指标卡片入口发起数据洞察任务</td>
        <td>![图片](img_AA4XbGtOXoHM5QxoepdcA1S4n0g.png)</td>
    </tr>
    <tr>
        <td>4</td>
        <td>下发任务过程可以精准指定 1-N 个待分析指标，可以复用历史任务和收藏任务</td>
        <td>![图片](img_YzLRbzRXSo1CukxODCQcwOMpndg.png)</td>
    </tr>
    <tr>
        <td>5</td>
        <td>查看 Aime 分析返回的洞察结论</td>
        <td>![图片](img_WOT5bmfhzokCkUxOvhCcZm4SnOd.png)</td>
    </tr>
    <tr>
        <td colspan="3">**使用 Aime 在 DevMind 创建可视化图表**</td>
    </tr>
    <tr>
        <td>1</td>
        <td>打开 DevMind-可视化分析页面，在输入框用自然语言输入可视化图表创建需求</td>
        <td>![图片](img_TVWCbPnwvo3nLnxb2QEcyJR9nFg.png)</td>
    </tr>
    <tr>
        <td>2</td>
        <td>- 通过模板跳转到 Aime 任务页面，在 Aime 返回结果中可获得 DevMind 可视化图表效果预览和链接
- 点击链接进入，查看由 Aime 产生的可视化图表</td>
        <td>![图片](img_RvCWbXu5cofq8Bx1SIqcUEhkn1e.png)
![图片](img_UUP1bVZXCoojrcxynaXcAORqnfb.png)</td>
    </tr>
    <tr>
        <td>3</td>
        <td>通过自然语言指令，向 Aime 下发需求并智能编辑图表</td>
        <td>![图片](img_VOqqbyRYfokm6mxQf4DcfzWNnwd.png)</td>
    </tr>
</table>


</content>
