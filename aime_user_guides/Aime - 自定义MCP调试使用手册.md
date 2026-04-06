<title>Aime - 自定义MCP调试使用手册</title>
<url>https://bytedance.larkoffice.com/wiki/F0znwODSZiA4iJkLbmLcneovnue</url>
<content>
<!-- BLOCK_1 | doxcnWAPQ27cEXyXeJs1VN5t2qh -->
最近更新：2026-01-09
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | At3id5iIboSrDHxjBEucHH6Vnxb -->
<callout icon="sunrise" bgc="2" bc="2">
**文档说明：**
本文档用于说明如何在Aime上添加自定义MCP，并通过调试平台完成对自定义MCP在Aime平台上的效果优化。
</callout>
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | Fp4edUnOIokV2Lxm4FIcDTm2nfg -->
# 前置条件&涉及平台<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | EL3UdTjhUoXusPxFfUHcFoh1nHB -->
- MCP：完成Remote 自定义MCP 开发 ，并支持提供 Steamable Http 或 SSE链接在 Aime上完成注册
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | DsG0dCtkYo1AMFxy5A8copHhn94 -->
- MCP注册&任务发起平台：https://aime.bytedance.net/chat
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | P6a7ditctoG5PzxJto6cll1hnLc -->
- MCP调试平台： [https://aime.bytedance.net/debug/mcp](https://aime.bytedance.net/debug/mcp)
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | TPkqdP4iHoq1X6x7OvOcYfNwnWb -->
# 整体流程<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | doxcnO1TvsPGfzjgmevriclZvkb -->
![board_ZcFpw9GBGhlYZPbLIiYcXapWnHe](board_ZcFpw9GBGhlYZPbLIiYcXapWnHe.drawio)
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | P6CddvOC5osqOHx6zPQcPRGInve -->
![board_BkzYwC3e4h77WvbY3RzcFJmanPe](board_BkzYwC3e4h77WvbY3RzcFJmanPe.drawio)
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | TYCPdqSV1oYaQ6x4G8gcDwPDnkc -->
# 操作指导<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | doxcn9Fz04Zgs2IQwhhUhaM8VAb -->
<table col-widths="160,184,470">
    <tr>
        <td>环节</td>
        <td>平台图示</td>
        <td>操作</td>
    </tr>
    <tr>
        <td>进入MCP配置页</td>
        <td>![图片](img_X5OSb44USoSEZpxls5kcVQ76n7d.png)</td>
        <td>1. 点击输入框左下方 MCP 入口，唤起下拉框
2. 点击MCP配置按钮</td>
    </tr>
    <tr>
        <td>唤起自定义MCP弹窗</td>
        <td>![图片](img_RL8Ob5OZDo33UwxuR8zcYGBonIc.png)</td>
        <td>1. 点击自定义 MCP tab
2. 点击 自定义MCP按钮</td>
    </tr>
    <tr>
        <td>添加MCP信息</td>
        <td>![图片](img_KZrzbfM3MoAyLjx0MBFcVSlknvf.png)</td>
        <td>**MCP名称：**请在50字以内，完成对MCP的命名，命名不影响调用效果
**MCP介绍**：请在200字以内，完成对MCP的功能描述，描述会影响实际调用效果
**添加方式：**可选择 StreamableHttp、SSE、字节云SDK三种方式完成注册
1. 获取SSE URL
> 字节云 MCP Server 平台链接：https://cloud.bytedance.net/faas/mcp_servers?type=own&x-resource-account=public&x-bc-region-id=bytedance
> 
![图片](img_GA1Ob6acHor3WWxIZslcHy8unRb.png)
1. 获取StreamableHttp链接，将 SSE URL的 /sse 替换为 /mcp（或者直接贴到文档使用替换功能）
![图片](img_B85Cbn7t2o1F42xV3TicyB2KnMf.png)
1. 通过字节云 SDK，输入已在字节云Fass 完成注册的MCP PSM链接，发起授权工单，点击完成授权</td>
    </tr>
    <tr>
        <td>添加鉴权信息</td>
        <td>![图片](img_PltFbnvfQoxyS8xlNSUc5Gs0nQd.png)

![图片](img_CffYbELR8oRsLzxGx1DcJkuvnAJ.png)</td>
        <td>1. 通过字节云 SSO登录：默认在登录Aime时自动授权，可直接复用
2. 通过header信息进行登录鉴权：输入header字段和具体参数，调用MCP时将自动完成传参</td>
    </tr>
</table>
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | ThsbdGQ1bo9TnOxlYcRcpzfanIc -->
## 自定义MCP注册<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | QujfdrF61o9MAlxGlGscKf2Xnxg -->
## MCP调试<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | C0ZAdBUxAoZQMNxtTcIcf92rnnb -->
![图片](img_G45mbUJqjoGu9IxsPjTcEFsFnKf.png)
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | DxmLdtaV5oHXCgx8wJ7cTC8FnEf -->
<table header-row="true" col-widths="160,184,470">
    <tr>
        <td>环节</td>
        <td>平台图示</td>
        <td>操作</td>
    </tr>
    <tr>
        <td>发起任务</td>
        <td>![图片](img_N5VrbKe6GoOgpBxQcVlcEMRZndg.png)</td>
        <td>在主输入框发起任务，注意添加新建自定义MCP</td>
    </tr>
    <tr>
        <td>进入 MCP 调试页面</td>
        <td>![图片](img_Dd3FbsTLlojCHkxwF97c8QmVnwc.png)</td>
        <td>点击输入框上方 调试MCP 按钮</td>
    </tr>
    <tr>
        <td>确认工具集列表</td>
        <td>![图片](img_BRh6bccejoEIcrxyqfLcOJhOn4g.png)</td>
        <td>1. 点击左侧的 Plan / Think
2. 点击右侧的工具集列表，确认 Aime 是否使用了这个 MCP。
3. 如果未使用，则需要修改 MCP 介绍。</td>
    </tr>
    <tr>
        <td>确认工具被使用</td>
        <td>![图片](img_QnRYbcGuLos0Dkx1jTtcaOmanCf.png)</td>
        <td>1. 点击左侧的 Execute / Think
2. 点击右侧的思考结果，确认 Aime 是否正确选择了这个 Tool
3. 如果未正确使用，则需要修改 Tool 描述。</td>
    </tr>
    <tr>
        <td>确认工具输入输出无误</td>
        <td>![图片](img_By9nb6tbpoB7bQxUGbecFNhonPc.png)</td>
        <td>1. 点击左侧的 Execute / Tool
2. 查看右侧，确认 Aime 是否正确进行了输出。
3. 如果输出有误，则需要调整工具</td>
    </tr>
    <tr>
        <td>修改信息</td>
        <td>![图片](img_DGL1bV2TeocdOoxapX7cB7uHnad.png)</td>
        <td>调试方式：
1. 点击编辑按钮
2. 在MCP编辑页修改MCP介绍和Tool描述，点击暂存（<font background_color="light_red">仅在调试平台生效，不影响线上效果</font>）
3. 点击单步重试重新运行当前环节。
4. 确认符合预期，复制当前介绍，在对应平台完成修改
	1. MCP 介绍：在[Aime 主站](https://aime.bytedance.net/chat)内完成调整
	2. Tool描述：在MCP 配置环境完成配置更新</td>
    </tr>
</table>
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | FMvBdfOxso2blKxYVjrcfRTCn5j -->
# FAQ<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | STMNdqH4PsBRRHbUofqcTr7Wnih -->
### Q： MCP怎么调试PPE环境？
A：StreamableHTTP和SSE可以通过配置Header鉴权方式配置多环境参数，如图。但需要注意，如果你的MCP依赖x-jwt-token，需要自己显式填写对应KV。因为选了Header鉴权将不会再传递用户字节云Token到MCP。
![图片](img_WcelbXpl8ocFeWxCJL7cSMJSnTh.png)

### Q：为什么我的MCP请求不通？
A：有几种可能：
1. Aime 有CN和I18n控制面。2026.1.5Update：<font background_color="light_yellow">由于公司网络隔离，CN只能访问CN MCP；I18n只能访问I18n MCP</font>（除非做了网络打标）。 因为Aime在CN or I18n Prod，所以无法访问Boe、Devbox、I18n等地域的MCP服务。
	1. cn：https://aime.bytedance.net/chat
	2. i18n: https://aime.tiktok-row.net/chat
2. MCP的配置有问题，比如权限配置。请检查下是否有使用MCP服务的权限（大部分是字节云MCP，可以看看字节云平台上有没有对应MCP的调用权限）。注意：使用StreamHTTP方式接入，需要调用者自行到AI PaaS申请对应MCP的调用者权限。使用SDK方式接入的同学可以点击页面申请授权的给Aime授权，如果还是无效，可以参考2.1
3. 如果是<font background_color="light_red">I18N MCP </font>且使用HTTP or SSE配置。形如``https://xxxx.mcp.tiktok-row.net``。这是因为这是OG域名，需要替换成``https://xxxx.``mcp.byteintl.net````域名Aime才可以在生产网访问

### Q：为什么我本地能通，但是Aime i18n控制面添加MCP失败？
如果你使用的是Streamable HTTP或者SSE接入，请检查你的域名是否为生产网可访问的域名。办公网能使用的域名是OG域名，生产网不可以访问，需要使用生产网域名。 [ROW OG Oncall 自查文档](https://bytedance.larkoffice.com/docx/UD38dOZG3olQbbxdpyEclrRknMS)
![图片](img_YF2BbjLyuoMNSyxUUVvcFlVPnCd.png)

### Q：一直报调用失败 or JsonSchema校验失败
[Json Schema 校验失败案例](https://bytedance.larkoffice.com/wiki/SwgYwR5sRiAXzqkaxaQc8WajnXb)

### Q：MCP如何获取调用者的身份
Aime工具调用时默认会在请求的Header传递调用者的字节云token，key：x-jwt-token。**注意**：如果是用**字节云SDK且在字节云工具配置自定义**接入，由于字节云SDK限制，<font background_color="light_red">header信息被存储在body.params.</font><font background_color="light_red">_mata</font><font background_color="light_red">.headers中，</font><font background_color="light_red">且为大小写敏感</font>，Server端接收时可以参考下。
> 字节云token校验&解析官方文档[https://cloud.bytedance.net/docs/bytecloud/docs/63c4c6df7e9d2a021ec21002/6530ed91edc2c702f6a977cd?x-resource-account=public&x-bc-region-id=bytedance](https://cloud.bytedance.net/docs/bytecloud/docs/63c4c6df7e9d2a021ec21002/6530ed91edc2c702f6a977cd?x-resource-account=public&x-bc-region-id=bytedance)
> 
<grid cols="2">
<column width="50">
  自定义接入的字节云Body 结构如图：
  ![图片](img_Qx54b6KXioXgjqxG5G5cL6LXnHe.png)
</column>
<column width="50">
  具体Headerkv 参考：
  ![图片](img_JCY9bvVrHogPmAxukvKczCjXn7f.png)
</column>
</grid>

<!-- END_BLOCK_17 -->




</content>
