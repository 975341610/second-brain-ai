<title>Aime ArgosMCP使用说明</title>
<url>https://bytedance.larkoffice.com/wiki/J8btwriUdijXCRkjeR4ckPbknTs</url>
<content>
<!-- BLOCK_1 | Wj02dNY5MoMAnOxc7xwcDmd3nSh -->
# 日志<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | RqoKd2LbCoonqOxqgzHcs0ehnoe -->
目前Aime支持关键字搜索日志、Logid搜索日志功能。但由于数据隔离，对应VRegion的数据需要去Aime不同的控制面发起任务才能访问。
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | LDhgdvrUxo2WQmxBbFMcWSplncf -->
- Aime不同控制面链接：
<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | WbnLd870ioIH5Qxvkb0chCl1nAc -->
Aime CN： https://aime.bytedance.net/chat
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | QfVTdGwHqoLt0RxZSsEcn9uvnjb -->
Aime i18n-TT: https://aime.tiktok-row.net/chat
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | Uk6HdFhtkoyhrOxJK7FcEWdFn7c -->
- Aime所在控制面和可访问VRegion关系如下：
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | EipfdWIylousvExS5tKcKS4inOh -->
<table col-widths="118,377">
    <tr>
        <td>**Aime控制面**</td>
        <td>**VRegion**</td>
    </tr>
    <tr>
        <td rowspan="4">CN</td>
        <td>China-BOE </td>
    </tr>
    <tr>
        <td>China-North、China-PPE、China-Aggregation、China-Edge、China-Fintech、China-Enterprise、ChinaSinf-North </td>
    </tr>
    <tr>
        <td>China-East </td>
    </tr>
    <tr>
        <td>China-Pay、China-Pay2 </td>
    </tr>
    <tr>
        <td rowspan="10">i18N 
 </td>
        <td>Singapore-Central、Singapore-PPE、Singapore-Compliance、 
Europe-Central </td>
    </tr>
    <tr>
        <td>US-East、US-PPE </td>
    </tr>
    <tr>
        <td>US-Compliance、US-EE </td>
    </tr>
    <tr>
        <td>MY-Compliance </td>
    </tr>
    <tr>
        <td>ID-Compliance</td>
    </tr>
    <tr>
        <td>ID-Compliance2</td>
    </tr>
    <tr>
        <td>USEASTDT</td>
    </tr>
    <tr>
        <td>SGDdT</td>
    </tr>
    <tr>
        <td>US-SOUTHWEST</td>
    </tr>
    <tr>
        <td>US-BOE </td>
    </tr>
</table>
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | ODzNdJCOyosqnzxkGLicvnahnVg -->
# 其他<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | RNrvdQuP8o8nOhxTTyTcmp0qnYd -->
目前还没支持，后续会持续迭代。目前建议手动给到Argos平台链接让Aime使用浏览器访问。
<!-- END_BLOCK_9 -->



<!-- BLOCK_10 | NNmJd9pqfoehldxjbTWcCrFEnKe -->
# 权限问题<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | DyhSdowVAoQKMlxbiQDcWp9wnMc -->
Aime查询日志使用的是任务发起人的身份访问的，报没权限大概率是psm写错了或者用户确实没权限。
<!-- END_BLOCK_11 -->


</content>
