<!-- BLOCK_1 | ZoXOd60JqojugRxXpwDcumFbn2c -->
<callout icon="bulb" bgc="3" bc="3">
不会写脚本？把这个文档发给 Aime 帮忙！
</callout>
<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | HGpCd5BZ2oKSV1x0X80c9SFCnxH -->
可以在 Aime 执行的命令中通过 Agent API 调用由 Agent 提供的能力，实现自动化执行 Agent 内工具等操作。
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | Bgkzd49gDoSc34xZFXScBXwTnGc -->
> 不是 OpenAPI，不能用来触发 Aime 任务，仅限 Aime 执行环境内访问
> 
> OpenAPI 见 [Aime OpenAPI 用户手册](https://bytedance.larkoffice.com/wiki/CmWowLiEdiwOOrkdMRocvnHknSf)
> 
<!-- END_BLOCK_3 -->



<!-- BLOCK_4 | JGUudaRgLoEL1lxvmkPckNXyn6d -->
## 请求格式<!-- 标题序号: 1 --><!-- END_BLOCK_4 -->

<!-- BLOCK_5 | Ou27d9wnWog5q0xgoX8c3PGVnKg -->
**BASE_URL**: 在 Aime 执行命令时会注入到 `$IRIS_AGENT_BASE_URL` 中
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | VP5md5OyEolK3nxAzawcoZOnnPj -->
**Method**: 总是使用 POST，所有接口都是从 JSONRPC 转换出来的
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | HXtMdRZ4ioui8YxpUnVcsY8wnDd -->
**鉴权方式**：携带 header `Authorization: User-Cloud-JWT $AIME_USER_CLOUD_JWT`
<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | HaPwd8LaHofKJ9xHrWFcK4LWnsh -->
**错误响应**：总是以 HTTP 500 + `{"message": "error message"}` 的 JSON 响应返回
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | Z9GadHGmyoPwHrxNnqxcGaasnsD -->
> 通过 python 调用时注意禁用 HTTP_PROXY，见下方[环境变量](https://bytedance.larkoffice.com/wiki/SnSRwt31einNpykFw73c5pVmnEe#NAH4dAE8QojYGFxDfLZcUDPzn0b)小节
> 
<!-- END_BLOCK_9 -->



<!-- BLOCK_10 | WBE1dSG1loAeAUxKLBucdwGenNh -->
## API 列表<!-- 标题序号: 2 --><!-- END_BLOCK_10 -->

<!-- BLOCK_11 | Lnu8dWJ1go0NFwxTcMRcL34lnj7 -->
### 获取 MCP 工具列表<!-- 标题序号: 2.1 --><!-- END_BLOCK_11 -->

<!-- BLOCK_12 | ARaqd0888ovWolxqqrpc3QfRndh -->
`POST /api/v1/tool/list`
<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | TlnWdFlyYownBUxW9VRcqer8nTb -->
获取当前任务添加的**自定义 MCP 服务**提供的工具列表
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | TSsqdsNbkoXtQpxzu0eczW0dnMU -->
**参数**
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | XwpsdgHqOoNZutxTQSPcL0sTnSe -->
`toolset`: MCP 工具集名称，需要在创建任务时添加到拓展中
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | QXamdzuRyoPlocxL7FOc4Tbfn6f -->
**返回值**
<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | MMT5dBGlwokTutxgrekcjOMNnvc -->
```go
type ListToolResponse struct {
  Tools []ToolInfo `json:"**tools**"`
}

type ToolInfo struct {
  Name             **string**           `json:"**name**"`
  Description      **string**           `json:"**description**"`
  ParametersSchema JSONSchema       `json:"**parameters_schema**"`
}
```
<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | Q09Gdtok5o3RvtxSkt6cUk5cnJd -->
**示例**
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | JNNNdPYbSofvdMxIPuEc4V6OnFf -->
```json
<font color="gray">Request:</font>
curl -v "<font background_color="light_green">$IRIS_AGENT_BASE_URL</font>/api/v1/tool/list"\
  -d '{"toolset": "<font color="blue">custom_mcp_name</font>"}'
  -H "Authorization: User-Cloud-JWT <font background_color="light_green">$AIME_USER_CLOUD_JWT</font>"


<font color="gray">Response:</font>
{
  "tools": [
    {
      "name": "mcp:<font color="blue">custom_mcp_name</font>_<font color="purple">tool_name</font>",
      "description": "description",
      "parameter_schema": {
        "type": "object",
        "properties": {},
        "required": []
      }
    }
  ]
}
```
<!-- END_BLOCK_19 -->



<!-- BLOCK_20 | GiumdQRHGobI8wxfHW5cRdyhnHd -->
### 执行 MCP 工具<!-- 标题序号: 2.2 --><!-- END_BLOCK_20 -->

<!-- BLOCK_21 | WnQUdHjJioESttxOoXkcKK2Qnjg -->
`POST /api/v1/tool/execute`
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | LyeHdobugo9cWexLSDdcqOb8nEf -->
**参数**
<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | Ohsodnq4goeUHsx7ffzc8bTmnGf -->
`tool_name`: 工具原始名称，仅支持自定义 MCP 工具，且**需要创建任务时添加到拓展中**
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | Zb9xdYVEfoolG6xsmxrccAsYnOc -->
`parameters`: 调用工具使用的参数 JSON，无需转换为 string
<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | I5Tnd19clouc8PxRLPZcOidwnlg -->
> 由于模型的工具名称只支持数字字母下划线，模型通过 function call 调用的工具 id 和工具名称并不一定相同；
> 
> 通过接口传入的是原始名称，发起任务后可以在 https://aime.bytedance.net/debug 看到 MCP 工具的原始 tool_name 和返回值，或者通过接口查询工具集下的所有工具列表获取到原始名称
> 
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | QvwOdPzGOo12s2xBcUZcatSVnuc -->
**返回值**
<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | DSard3Br7oX0vfxhZfJcO3kCnCf -->
MCP 工具返回的原始 JSON 对象，总是一个 Object。自定义 MCP 工具调用的返回 Schema 如下：
<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | RQtgdxdX8o5sHvxT9u4c42Whnnh -->
```go
type MCPCallResponse struct {
  TextContents  []string `json:"**text_contents**" description:"MCP response text contents"`
  ImageContents []string `json:"**image_contents**" description:"MCP response image contents"`
  Attachments   []string `json:"**attachments**" description:"Raw text/json responses saved to files"`
  LogID         string   `json:"**log_id**,omitempty" description:"MCP request log id"`
}
```
<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | M8uOdbyb8onkXXxrbClcV0bjnLe -->
在 MCP 协议中，MCP 工具返回的原始值是 TextContents 和 ImageContents 的列表，文本内容可能会被截断防止模型上下文超限，因此不能直接解析 TextContents 来获取 JSON 内容。
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | NuNAdTbCAoamHGxayjHcCr2mnEc -->
使用脚本处理时需要单独从 Attachments 中保存的 JSON 文件中解析输出（如果文本内容是合法的 JSON，会保存为 `.json` 文件；否则会保存为 `.txt` 文件），TextContents 返回的每一段对应一个文件。
<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | OzrRdpqMwoKYWaxpoVVcn6ijnof -->
**示例**
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | DOBFd4YR2oRrLpxqqAgcgLbznDh -->
```json
<font color="gray">Request:</font>
curl -v "<font background_color="light_green">$IRIS_AGENT_BASE_URL</font>/api/v1/tool/execute"\
  -d '{"tool_name":"mcp:toolset_tool","parameters":{...}}'
  -H "Authorization: User-Cloud-JWT <font background_color="light_green">$AIME_USER_CLOUD_JWT</font>"

<font color="gray">Response:</font>
{
    "attachments": ["mcp_outputs/xxx.json"],
    "image_contents": [],
    "text_contents": [
        <font background_color="light_green">"{...}"</font>
    ]
}

<font color="gray">Error Response: 500 Internal Server Error</font>
{
    "message": "error message returned when tool execution failed"
}
```
<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | FOmldcWB2o8Ld0xSJtDcYgYJn7b -->
**注意事项**
<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | ZJ04dB0CzoTlDyxkYxpcmlAdn6e -->
同一个任务内，每分钟最多通过此接口执行 120 次工具调用，需要自行处理限流。
<!-- END_BLOCK_34 -->



<!-- BLOCK_35 | O5SsdAciWoXQn0xpgBNcfjHinYg -->
### 更新环境变量<!-- 标题序号: 2.3 --><!-- END_BLOCK_35 -->

<!-- BLOCK_36 | KowhdJ7feoTVs6x6BzIcBHdwn3d -->
`POST /api/v1/terminal/environ/update`
<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | N05kdaYBfodCYyx1iT9cBNSzn9c -->
向 Aime 执行的 bash 命令中注入额外的环境变量，可用于存放 Token 等信息或覆盖 Aime 默认注入的环境变量，本次对话生效。
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | M54fdrgLfoVECtxiiltcAQXsndc -->
**参数**
<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | RfBVd7qzGo35tSxwsHrcyAFSn7c -->
`environ`: `Map<string, string>` 要设置的环境变量 Key: Value
<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | Gr4rdrMeRoICtrxijLdcGaAmnih -->
**返回值**
<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | B8M1dfYGqoaOtvxtc8ncz1cknag -->
`environ`: `Map<string, string>` 更新后的自定义环境变量（不包含默认环境变量的值）
<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | Qoi3diEXmo26GmxKbbKcGUVwnQf -->
**示例**
<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | UVJIdLTEfoqAgwxm8FJcVOvKnRc -->
```json
<font color="gray">Request:</font>
curl -v "<font background_color="light_green">$IRIS_AGENT_BASE_URL</font>/api/v1/terminal/environ/update"\
  -d '{ "environ": { "ENV_KEY": "ENV_VALUE" }}'
  -H "Authorization: User-Cloud-JWT <font background_color="light_green">$AIME_USER_CLOUD_JWT</font>"

<font color="gray">Response:</font>
{
  "environ": {
    "ENV_KEY": "ENV_VALUE"
  }
}
```
<!-- END_BLOCK_43 -->



<!-- BLOCK_44 | Ke6SdPPOIoCxnYxodoNccBNPnve -->
### 重置环境变量<!-- 标题序号: 2.4 --><!-- END_BLOCK_44 -->

<!-- BLOCK_45 | KRledq0hboSvOSxLJbpcOI6snbh -->
`POST /api/v1/terminal/environ/reset`
<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | EcKmdVFXLoP57oxwHrbcHBA0nXb -->
重置之前设置的环境变量回默认状态，本次对话生效。
<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | ITDBdTTpUoQCm5xl8iScl2dDnFe -->
**参数**
<!-- END_BLOCK_47 -->

<!-- BLOCK_48 | A89nd8jwKosBTcxRtJ1cJBbOnVc -->
`keys`: `string[]` 如果传入，则只重置指定的环境变量 key
<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | GaKFd785doUgVNxLnErcAcYvnue -->
**返回值**
<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | LWW8dTCfboPo0QxrTD1cJQsinBh -->
`environ`: `Map<string, string>` 重置后的新环境变量
<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | ICsTdnYQIoMye8xpfVWcZz5Enqb -->
**示例**
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | OIu0d4WD5omPvsxzMS8cPdexn8c -->
```json
<font color="gray">Request:</font>
curl -v "<font background_color="light_green">$IRIS_AGENT_BASE_URL</font>/api/v1/terminal/environ/reset"\
  -d '{"keys": ["KEY1"]}'
  -H "Authorization: User-Cloud-JWT <font background_color="light_green">$AIME_USER_CLOUD_JWT</font>"

<font color="gray">Response:</font>
{
  "environ": {
    "REMAINING_ENV": "REMAINING_ENV_VALUE"
  }
}
```
<!-- END_BLOCK_52 -->



<!-- BLOCK_53 | YRJjdY2EgoLZnUx5F17cwNten0c -->
## 环境变量<!-- 标题序号: 3 --><!-- END_BLOCK_53 -->

<!-- BLOCK_54 | OtGGdw68Do11qLxYuZ6c95AtnTe -->
Aime 执行命令时会注入一些环境变量，可以用于鉴权、判断是否在 Aime 环境等。
<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | RowQdHPsgsThCDbnxROcg295nyh -->
<table col-widths="246,576">
    <tr>
        <td>**环境变量**</td>
        <td>**内容**</td>
    </tr>
    <tr>
        <td>`AIME_SESSION_ID`</td>
        <td>Aime 任务的 Session ID，即任务 url 中
`https://aime.bytedance.net/chat/``<font color="green" background_color="light_green">{id}</font>` 的部分</td>
    </tr>
    <tr>
        <td>`AIME_TEMPLATE_ID`</td>
        <td>Aime 任务的模板 ID，如果该任务由模板创建</td>
    </tr>
    <tr>
        <td>`AIME_SPACE_ID`</td>
        <td>Aime 任务的项目空间 ID，如果该任务在项目空间中创建</td>
    </tr>
    <tr>
        <td>`AIME_WORKSPACE_PATH`</td>
        <td>当前 Aime 任务的工作区根目录</td>
    </tr>
    <tr>
        <td>`AIME_AGENT_BASE_URL`</td>
        <td>Aime Agent API Base URL，详见 [[WIP] Aime Agent 开放能力&高级使用姿势](https://bytedance.larkoffice.com/wiki/Ri4zwejsqigZB6k6Krcca7BJnfd#share-UGeXdrPQYo7IHYx2ddfcRkDJn8f)</td>
    </tr>
    <tr>
        <td>`AIME_CURRENT_USER`</td>
        <td>当前 Aime 任务的发起人邮箱前缀</td>
    </tr>
    <tr>
        <td>`AIME_CURRENT_USER_EMAIL`</td>
        <td>当前 Aime 任务的发起人邮箱，邮箱后缀不一定是 @bytedance.com</td>
    </tr>
    <tr>
        <td>`<font color="orange">AIME_USER_CLOUD_JWT</font>`</td>
        <td>当前用户的字节云 JWT，可用于 TCE/SCM 等平台接口的认证
注意：
- 字节云 JWT 的有效期为 1 小时
- 字节云 JWT 的区域取决于触发 Aime 任务的区域
	- aime.bytedance.net: CN
	- aime.tiktok-row.net: TT-ROW</td>
    </tr>
    <tr>
        <td>`<font color="orange">AIME_USER_CODE_JWT</font>`</td>
        <td>当前用户的 Code User JWT，可用于调用 Codebase API [NextCode OpenAPI 接入指南](https://bytedance.larkoffice.com/wiki/PKoiwOfVniSnO6kEomWcett0nIc)</td>
    </tr>
    <tr>
        <td colspan="2">> 以下环境变量用于声明 terminal 的非交互性，防止启动的命令等待交互直到超时
> </td>
    </tr>
    <tr>
        <td>`DEBIAN_FRONTEND`</td>
        <td>`noninteractive`</td>
    </tr>
    <tr>
        <td>`TERM`</td>
        <td>`xterm`</td>
    </tr>
    <tr>
        <td>`CI`</td>
        <td>`true`</td>
    </tr>
    <tr>
        <td>`PAGER`</td>
        <td>`cat`</td>
    </tr>
    <tr>
        <td>`EDITOR`</td>
        <td>`/bin/true`</td>
    </tr>
    <tr>
        <td>`NO_COLOR`</td>
        <td>`1`</td>
    </tr>
    <tr>
        <td colspan="2">> 其他默认注入的环境变量
> </td>
    </tr>
    <tr>
        <td>`HTTP_PROXY`</td>
        <td>[仅 CN] 用于访问外网；需要访问 Aime Agent API 时需要在脚本中禁用掉</td>
    </tr>
    <tr>
        <td>`HTTPS_PROXY`</td>
        <td>[仅 CN] 用于访问外网；需要访问 Aime Agent API 时需要在脚本中禁用掉</td>
    </tr>
    <tr>
        <td>`BUILD_VERSION`</td>
        <td>`aime` 模拟 SCM 环境，防止部分内部 cli 工具触发扫码登陆</td>
    </tr>
    <tr>
        <td>`BUILD_TYPE`</td>
        <td>`aime` 模拟 SCM 环境，防止部分内部 cli 工具触发扫码登陆</td>
    </tr>
    <tr>
        <td>`BUILD_TOKEN`</td>
        <td>同 `AIME_USER_CLOUD_JWT`</td>
    </tr>
</table>
> 注：在 Remote SSH 或 Web IDE 中的 Terminal 不会注入
> 
> **Aime 在执行命令时会判断是否需要注入密钥类环境变量（标黄的环境变量），防止执行外部脚本/Skill 时误注入导致 token 泄漏**
> 
<!-- END_BLOCK_55 -->



