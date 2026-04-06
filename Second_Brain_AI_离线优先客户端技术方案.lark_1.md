<!-- BLOCK_1 | doxcnVjGk0LvBUFnsdkiM5UCJMg -->
## 1. 架构总览与选型<!-- END_BLOCK_1 -->

<!-- BLOCK_2 | doxcnr6CWjUitYtWZOLpdBL1Llc -->
本章节旨在为 Second Brain AI Windows 客户端的实现提供一个全面的架构蓝图和技术选型决策。我们将探讨两条核心实施路线，并针对数据持久化、本地搜索等关键模块给出具体方案。
<!-- END_BLOCK_2 -->

<!-- BLOCK_3 | doxcnWRQz2OI6GDnFB6Kvl1sKag -->
### 1.1. 实施路线对比与建议<!-- END_BLOCK_3 -->

<!-- BLOCK_4 | doxcnWTfmlYKzVMfRpzJZwEwTRf -->
为了实现离线优先的核心目标，我们评估了两种主流的实施路线：**A. Electron + 本地后端** 和 **B. 纯前端离线方案**。
<!-- END_BLOCK_4 -->

<!-- BLOCK_5 | doxcnvBvPc26NCKwyzNYSqub4Eg -->
![board_Gfi5wCeuVhkFYebHEFAc5tL0nYd](board_Gfi5wCeuVhkFYebHEFAc5tL0nYd_1.drawio)
<!-- END_BLOCK_5 -->

<!-- BLOCK_6 | doxcnts9pvDElNHT9xLOObhRUJc -->
<callout icon="bulb" bgc="3" bc="3">
**核心建议：**
我们建议采用 **混合路线**：
- **内容创作与编辑 (文档型数据)**：采用 **路线 B** 的 `Tiptap + Yjs + y-indexeddb` 方案。这套组合为富文本编辑提供了原生的 CRDT 支持，能实现高效的离线编辑和无冲突的自动合并，是处理文档型数据的业界最佳实践。
- **元数据管理、搜索与附件 (关系型/向量数据)**：采用 **路线 A** 的 `Electron + 本地后端` 方案。利用 Python 后端的强大生态处理文件 I/O、数据库操作和向量计算，能更好地保留现有后端的逻辑，并为未来功能扩展（如集成更复杂的本地 AI 模型）提供灵活性。
这种混合方案兼顾了富文本离线编辑的最佳体验和后端逻辑的稳定与可扩展性。
</callout>
<!-- END_BLOCK_6 -->

<!-- BLOCK_7 | doxcn4wlz8AVP8e41hNP4d5KS0g -->
#### 1.1.1. 路线 A: Electron + 本地后端 (Python/FastAPI)<!-- END_BLOCK_7 -->

<!-- BLOCK_8 | doxcnqC3b3KsNQa6T3uEPWLMKQd -->
此路线将现有的 FastAPI 后端直接打包到 Electron 应用中，作为本地服务运行。
<!-- END_BLOCK_8 -->

<!-- BLOCK_9 | doxcn9RdmsgybrLCaHJmEkz3CVd -->
- **架构**：
	- **前端**：React + Tiptap 编辑器，作为纯粹的 UI 层。
	- **中间层**：Electron 主进程负责管理窗口生命周期，并作为“后端管理器”，启动、监控和终止本地的 Python 服务。
	- **后端**：将 FastAPI, ChromaDB, SQLite 等 Python 依赖打包成一个或多个可执行文件，随 Electron 应用一同分发。
	- **通信**：前端通过 IPC 调用 Electron 主进程暴露的安全接口，主进程再通过 HTTP 请求与本地 FastAPI 服务通信。
<!-- END_BLOCK_9 -->

<!-- BLOCK_10 | doxcniXgWzrkM5KIAf6unkoKxTc -->
- **优点**：
	- **逻辑复用**：最大限度地复用现有后端代码和业务逻辑。
	- **生态强大**：可利用 Python 丰富的库处理复杂任务，如文件解析、数据分析、本地 AI 模型集成等。
	- **计算密集型任务友好**：适合在后台运行独立的计算进程，避免阻塞 UI。
<!-- END_BLOCK_10 -->

<!-- BLOCK_11 | doxcnoBwmKZICNqkeu5MJ7Baosf -->
- **缺点**：
	- **打包复杂**：将 Python 环境（尤其是包含 C/C++ 依赖的库）打包为单一可执行文件，挑战较大，体积也更庞大。
	- **进程管理开销**：需要精细管理后端子进程的生命周期，确保与主应用同步启动和退出，并处理僵尸进程等问题。
	- **端到端延迟**：`渲染进程 -> 主进程 -> 本地后端` 的通信链路较长，不适合高频、低延迟的交互。
<!-- END_BLOCK_11 -->

<!-- BLOCK_12 | doxcnDyhwRx6Yvx1Y2BBo0z5Vnf -->
#### 1.1.2. 路线 B: 纯前端离线方案 (IndexedDB + Yjs)<!-- END_BLOCK_12 -->

<!-- BLOCK_13 | doxcnwAKw7ArJhYvOPGN0ehfbre -->
此路线将所有核心逻辑前移，利用浏览器技术栈在渲染进程中实现完整的离线功能。
<!-- END_BLOCK_13 -->

<!-- BLOCK_14 | doxcnYR2Sfg0LxThuD1kPvpXxbe -->
- **架构**：
	- **数据持久化**：
		- **文档内容**：使用 `y-indexeddb` 将 Tiptap 的 Yjs 文档状态直接持久化到 IndexedDB。
		- **元数据/附件**：使用 `SQLite` 的 WebAssembly 版本（如 `sql.js`）在浏览器中运行，管理笔记元数据、标签、关系等。
	- **数据同步**：
		- **文档内容**：Yjs 的 CRDT 结构天然支持增量同步。未来可通过 `y-websocket` 或 `Hocuspocus` 等 Provider 连接云端，实现自动合并。
		- **元数据**：通过自定义的增量同步协议（Delta Sync）与云端 API 对账。
	- **搜索**：向量搜索可在 Web Worker 中运行轻量级嵌入模型和相似度计算，或降级为基于 `tantivy` (Rust to WASM) 的全文索引。
<!-- END_BLOCK_14 -->

<!-- BLOCK_15 | doxcnunWpXcMBSOslt92hOtilkf -->
- **优点**：
	- **极致的离线体验**：所有操作均在本地完成，响应速度快，无需等待后端。
	- **打包简单**：纯前端项目，打包流程成熟，体积相对可控。
	- **现代协同基础**：基于 CRDT 的架构为未来实现多人实时协作奠定了坚实基础。
<!-- END_BLOCK_15 -->

<!-- BLOCK_16 | doxcnpVicDeZDbMsPU8jdvLnN9e -->
- **缺点**：
	- **浏览器环境限制**：文件系统访问、系统级操作受限。大文件处理、数据库备份等操作不如本地后端方便。
	- **重构成本高**：需要将现有后端的数据库逻辑（如基于 SQLite 的查询）用 JavaScript 或 WASM 重写。
	- **本地 AI 能力受限**：在浏览器中运行大型嵌入模型或 AI 服务存在性能瓶颈和内存限制。
<!-- END_BLOCK_16 -->

<!-- BLOCK_17 | doxcn54fmVk3sjIC3WEhUEscDJc -->
### 1.2. 数据持久化方案<!-- END_BLOCK_17 -->

<!-- BLOCK_18 | doxcnJ2eEFXesCgzomRFjYd3NBd -->
根据混合路线的建议，我们对不同类型的数据采用不同的持久化策略。
<!-- END_BLOCK_18 -->

<!-- BLOCK_19 | doxcnV0MSAEvCEzAIC1qgkzPHBh -->
#### 1.2.1. 笔记主数据与附件 (SQLite)<!-- END_BLOCK_19 -->

<!-- BLOCK_20 | doxcncPHO1oZD0c9BhXqqq5UVbc -->
笔记的元数据（标题、标签、创建/修改日期）、附件信息、版本历史等关系型数据，由本地 Python 后端管理，存储在 SQLite 数据库中。
<!-- END_BLOCK_20 -->

<!-- BLOCK_21 | doxcnDSNvVJBaNMyhLMXG9jIGXb -->
- **WAL 模式**：必须开启 `PRAGMA journal_mode=WAL;`。WAL (Write-Ahead Logging) 模式能显著提升并发性能，允许多个读操作和一个写操作同时进行，避免了 `DATABASE IS LOCKED` 的常见错误，对于 Electron 应用中可能存在的多进程访问场景至关重要。
<!-- END_BLOCK_21 -->

<!-- BLOCK_22 | doxcnxjxsjmjl4WxC7jmnGiacad -->
- **热备份策略**：
	- **在线备份 API**：利用 SQLite 的在线备份 API (`sqlite3.Connection.backup()`) 进行热备份。此方法可以在不锁死数据库的情况下，将当前数据库状态安全地复制到另一个文件。
	- **备份时机**：可在应用空闲时、退出前或按固定周期（如每日）触发。备份过程应在后台线程执行，避免阻塞主进程。
<!-- END_BLOCK_22 -->

<!-- BLOCK_23 | doxcnoemDr216hoFCOzpmnMRpIb -->
- **崩溃一致性**：WAL 模式本身提供了强大的崩溃恢复能力。即使在写入过程中应用崩溃，主数据库文件 `*.db` 仍保持一致状态，所有未完成的事务记录在 `*-wal` 文件中，下次连接时会自动恢复。
<!-- END_BLOCK_23 -->

<!-- BLOCK_24 | doxcnV5J0QRTPZ6fDBUyCntINtg -->
#### 1.2.2. 文档型内容 (Yjs + y-indexeddb)<!-- END_BLOCK_24 -->

<!-- BLOCK_25 | doxcnKcBUUWWFEl3MOqDnBnAV1d -->
对于 Tiptap 编辑器中的富文本文档（包括表格、列表等），其数据结构由 Yjs 管理。
<!-- END_BLOCK_25 -->

<!-- BLOCK_26 | doxcnpYeRItVKdS6owJRGvH9pNb -->
- **持久化层**：使用 `y-indexeddb` 适配器，将 Yjs 的 CRDT 文档状态直接存入浏览器的 IndexedDB。
<!-- END_BLOCK_26 -->

<!-- BLOCK_27 | doxcn8nxI6hxILVUstjOoQDvpCf -->
- **优势**：
	- **毫秒级加载**：`y-indexeddb` 实现了高效的增量加载，应用启动时几乎可以瞬时恢复文档状态。
	- **原生离线支持**：所有编辑操作都先应用到本地 Yjs 文档并存入 IndexedDB，无需任何网络请求。
	- **自动同步基础**：当网络恢复时，Yjs 的同步 Provider (如 `y-websocket`) 能自动与后端交换增量更新，无冲突地完成数据合并。
<!-- END_BLOCK_27 -->

<!-- BLOCK_28 | doxcnckZeUxOsKQPsY30ZYnizqg -->
#### 1.2.3. 向量数据 (ChromaDB v0.4+)<!-- END_BLOCK_28 -->

<!-- BLOCK_29 | doxcnc02jgbGR1dy6USNdd0kJEd -->
ChromaDB 用于存储文本块的嵌入向量，以支持语义搜索。
<!-- END_BLOCK_29 -->

<!-- BLOCK_30 | doxcnfUuOiGw1g8pTW4uOhOHVne -->
- **持久化后端**：自 v0.4.0 起，ChromaDB 默认使用 **SQLite** 作为其持久化后端（取代了之前的 DuckDB）。通过 `chromadb.PersistentClient(path="/path/to/db")` 指定的目录会包含一个 `chroma.sqlite3` 文件，用于存储所有元数据和集合信息。
<!-- END_BLOCK_30 -->

<!-- BLOCK_31 | doxcnJFXyy27Au1QYNmzZH6rQgb -->
- **路径规划**：向量数据库的存储路径应规划在应用的用户数据目录 (`app.getPath('userData')`)下，避免因应用更新或重装导致数据丢失。
<!-- END_BLOCK_31 -->

<!-- BLOCK_32 | doxcn58LG8YA4YQ1qhAwOREp1Nc -->
- **离线嵌入模型**：为保证离线可用性，必须选用可在本地运行的嵌入模型，如 `Sentence Transformers` 系列。模型文件需要随应用打包分发，或在首次运行时从可靠源下载。
<!-- END_BLOCK_32 -->

<!-- BLOCK_33 | doxcn917eaXejmNyyQplw58z8Th -->
### 1.3. 本地搜索与向量方案<!-- END_BLOCK_33 -->

<!-- BLOCK_34 | doxcnNkCMiHqkyDObKSvUwOwUyg -->
保留强大的本地搜索能力是核心需求。我们对比以下两种方案：
<!-- END_BLOCK_34 -->

<!-- BLOCK_35 | doxcn6KipeogzwOMKLHfsEciglh -->
#### 1.3.1. 保留 ChromaDB + 轻量嵌入模型 (推荐)<!-- END_BLOCK_35 -->

<!-- BLOCK_36 | doxcnQ6VAw5ljk0GNzw4776FBXc -->
- **方案**：继续在本地 Python 后端中集成 ChromaDB。使用轻量级的、可在 CPU 上高效运行的嵌入模型（如 `bge-small-zh-v1.5` 或 `paraphrase-multilingual-MiniLM-L12-v2`）。
<!-- END_BLOCK_36 -->

<!-- BLOCK_37 | doxcnA9FrZmpYti88dH0GcbZWde -->
- **优点**：
	- **强大的语义搜索**：能够理解用户自然语言查询，返回语义相关的结果，体验远超关键词搜索。
	- **技术栈统一**：与现有后端技术保持一致。
<!-- END_BLOCK_37 -->

<!-- BLOCK_38 | doxcnMQZsipp40nfj7QXYcRAd1g -->
- **挑战**：
	- **资源占用**：加载嵌入模型会带来额外的内存开销（通常为 200-500MB）。
	- **性能**：在没有 GPU 的普通用户设备上，首次建立索引或处理大量文档时可能会较慢。
<!-- END_BLOCK_38 -->

<!-- BLOCK_39 | doxcnIHENDuyA1gK4SddWBV9yKg -->
#### 1.3.2. 替代方案：纯全文索引<!-- END_BLOCK_39 -->

<!-- BLOCK_40 | doxcnRx8KkpaVhL9yzb4IgaEXDe -->
- **方案**：放弃向量搜索，转而使用基于 Rust -> WASM 的全文搜索引擎，如 `Tantivy`。
<!-- END_BLOCK_40 -->

<!-- BLOCK_41 | doxcnAmOZQal5glGzilGv7BfJAh -->
- **优点**：
	- **极致轻量**：资源占用极低，启动快，无模型加载开销。
	- **速度快**：对于关键词匹配场景，速度极快。
<!-- END_BLOCK_41 -->

<!-- BLOCK_42 | doxcnSALD5GTNXGQw5mYK3MtLAh -->
- **缺点**：
	- **功能降级**：无法理解语义，只能进行关键词和模糊匹配，搜索体验大幅下降。
	- **集成成本**：需要在前端（或主进程）集成 WASM 模块，并建立索引逻辑。
<!-- END_BLOCK_42 -->

<!-- BLOCK_43 | doxcnsBV0Ir0WZGGAlg06fRn94c -->
<callout icon="bulb" bgc="4" bc="4">
**决策**：**保留 ChromaDB**。虽然存在资源开销，但语义搜索是 `second-brain-ai` 的核心竞争力之一。我们可以通过提供选项让用户根据设备性能决定是否开启语义搜索，或者在应用空闲时进行索引来优化体验。
</callout>
<!-- END_BLOCK_43 -->

<!-- BLOCK_44 | doxcn5JOfIWxieivWOJ3tY9fcmd -->
## 2. Electron 封装与进程通信<!-- END_BLOCK_44 -->

<!-- BLOCK_45 | doxcnrplZrvFG6B5GuIpISTrD2e -->
本章详述如何将 React 前端与 Python 后端封装为统一的 Windows 客户端，并设计安全、高效的进程间通信机制。
<!-- END_BLOCK_45 -->

<!-- BLOCK_46 | doxcnke05O6IBKVMc6icWiex1Be -->
### 2.1. Electron-builder 打包与分发<!-- END_BLOCK_46 -->

<!-- BLOCK_47 | doxcn0ytmFxP8sSeHUVdg8vb6eb -->
我们选用 `electron-builder` 作为打包工具，因为它功能全面，支持 NSIS 安装包制作、自动更新和代码签名。
<!-- END_BLOCK_47 -->

<!-- BLOCK_48 | doxcnZWllQXQZbODWaJAziKZPLg -->
- **打包目标 (Target)**：
	- **nsis**：生成传统的 Windows 安装程序（`.exe`），提供完整的安装向导，允许用户选择安装路径。这是分发给普通用户的首选。
	- **portable**：生成便携版，无需安装，解压即用。适合高级用户或用作绿色版分发。
<!-- END_BLOCK_48 -->

<!-- BLOCK_49 | doxcnQTPXh4h91TLI4kphJOl3qe -->
- **安装与升级**：
	- **NSIS 配置** (`nsis` 字段):
		- `oneClick: false`：必须设置为 `false`，以提供安装向导。
		- `allowToChangeInstallationDirectory: true`：允许用户自定义安装路径。
		- `createDesktopShortcut: true`：创建桌面快捷方式。
		- `installerIcon`, `uninstallerIcon`: 定制安装和卸载图标。
	- **自动更新** (`publish` 字段):
		- 使用 `generic` Provider，将 `url` 指向一个可访问的服务器目录。`electron-builder` 打包时会生成 `latest.yml` 文件，`electron-updater` 会通过此文件检查更新。
<!-- END_BLOCK_49 -->

<!-- BLOCK_50 | doxcndw3A9JrArg6LPvAXxkp7Gg -->
- **代码签名 (Code Signing)**：
	- 为了通过 Windows Defender 和其他杀毒软件的校验，并提升应用信誉，**必须对应用进行代码签名**。
	- 需要购买有效的代码签名证书（EV 或 OV 证书）。
	- 在 `electron-builder` 配置的 `win` 字段中设置 `certificateFile`, `certificatePassword` 或通过环境变量 `CSC_LINK`, `CSC_KEY_PASSWORD` 来指定证书。
<!-- END_BLOCK_50 -->

<!-- BLOCK_51 | doxcnaaZr3tkjtU0K9wUO427eCf -->
- **WinDefender 兼容实践**：
	- **代码签名是前提**：未签名的应用极易被误报。
	- **避免可疑行为**：减少在运行时动态创建和执行脚本、向系统目录写入文件等行为。
	- **提交样本**：如果持续被误报，应向 Microsoft 安全智能中心提交应用样本进行分析，申请加入白名单。
<!-- END_BLOCK_51 -->

<!-- BLOCK_52 | doxcnbSe3m999z1vdvcQt96BVAh -->
### 2.2. Python 后端打包与生命周期管理<!-- END_BLOCK_52 -->

<!-- BLOCK_53 | doxcnj70iuTdkLtRwCgnaihsJUh -->
将 Python 后端与 Electron 应用捆绑分发，核心在于将 Python 代码及其依赖打包为可执行文件。
<!-- END_BLOCK_53 -->

<!-- BLOCK_54 | doxcnONpfHuTkphxJh9QQteJ8Td -->
#### 2.2.1. 打包工具对比与推荐<!-- END_BLOCK_54 -->

<!-- BLOCK_55 | doxcnnCtsjhQ6778VBBk4reM6qc -->
<table col-widths="200,200,200,200,200">
    <tr>
        <td>工具</td>
        <td>打包原理</td>
        <td>优点</td>
        <td>缺点</td>
        <td>推荐场景</td>
    </tr>
    <tr>
        <td>**PyInstaller&nbsp;(推荐)**</td>
        <td>将脚本和依赖项捆绑到单个目录或可执行文件中，运行时解压到临时目录。</td>
        <td>**最成熟，兼容性最好**，社区支持广泛，开箱即用支持绝大多数库。</td>
        <td>启动速度较慢，打包体积较大，易被反编译。</td>
        <td>绝大多数场景，尤其是项目依赖复杂（如包含 PyQt, numpy 等）时。</td>
    </tr>
    <tr>
        <td>**Nuitka**</td>
        <td>将 Python 代码编译为 C++ 代码，然后编译为原生可执行文件。</td>
        <td>**运行速度快**，接近原生性能；反编译难度高，代码安全性好。</td>
        <td>打包时间长，配置复杂，需要 C++ 编译器环境。</td>
        <td>对性能有极致要求、需要保护核心算法的计算密集型应用。</td>
    </tr>
    <tr>
        <td>**PyOxidizer**</td>
        <td>将 Python 解释器和应用代码嵌入到一个单一的原生二进制文件中。</td>
        <td>**启动速度极快**，分发的是真正的单个二进制文件，依赖管理更干净。</td>
        <td>学习曲线陡峭，需要 Rust 工具链，生态相对较小。</td>
        <td>对启动性能和包纯净度有极端要求的场景。</td>
    </tr>
</table>
<!-- END_BLOCK_55 -->

<!-- BLOCK_56 | doxcnBnta01oVtkVdkE6XFGsz5d -->
<callout icon="bulb" bgc="3" bc="3">
**决策**：首选 **PyInstaller**。其成熟度和社区支持能最大程度保证打包成功率。对于 `second-brain-ai` 项目，快速、可靠的打包比极致的运行性能更重要。未来若出现性能瓶颈，可再考虑迁移到 Nuitka。
</callout>
<!-- END_BLOCK_56 -->

<!-- BLOCK_57 | doxcnRGLSuncLqmpMZFpp1jyhed -->
#### 2.2.2. 目录结构与生命周期管理<!-- END_BLOCK_57 -->

<!-- BLOCK_58 | doxcnfvOlnlqVae9AFHX1Lhglkh -->
- **目录结构**：
	- 使用 PyInstaller 将 FastAPI 后端打包为单个可执行文件，例如 `backend.exe`。
	- 在 `electron-builder` 的配置中，使用 `extraResources` 字段将 `backend.exe` 包含到应用包的 `resources` 目录中。
```json
"build": {
  "extraResources": [
    {
      "from": "./backend/dist/backend.exe",
      "to": "backend.exe"
    }
  ]
}
```
<!-- END_BLOCK_58 -->

<!-- BLOCK_59 | doxcnX0zgDmzI0tg8NK1gmoLlBh -->
- **启动/退出生命周期**：
	- **启动**：在 Electron 主进程的 `app.whenReady()` 事件中，使用 `child_process.spawn` 启动后端服务。必须正确处理路径，在生产环境中使用 `process.resourcesPath` 定位 `backend.exe`。
```javascript
const { spawn } = require('child_process');
const path = require('path');

let backendProcess;

function startBackend() {
  const backendPath = app.isPackaged
    ? path.join(process.resourcesPath, 'backend.exe')
    : path.join(__dirname, '../backend/dist/backend.exe');

  backendProcess = spawn(backendPath);

  backendProcess.stdout.on('data', (data) => {
    console.log(`Backend: ${data}`);
  });
}

app.whenReady().then(startBackend);
```
	- **退出**：监听应用的 `before-quit` 事件，在应用退出前，使用 `backendProcess.kill()` 优雅地终止后端子进程，防止僵尸进程。
```javascript
app.on('before-quit', () => {
  if (backendProcess) {
    backendProcess.kill();
  }
});
```
<!-- END_BLOCK_59 -->

<!-- BLOCK_60 | doxcn4jGG8sqnu0TL37vHnQ3Veg -->
### 2.3. 主/渲染/预加载三层安全通信 (IPC 设计)<!-- END_BLOCK_60 -->

<!-- BLOCK_61 | doxcnCuUqFpsct1YCLhz8UNDNHf -->
为了保证应用的安全性，必须遵循 Electron 的最佳安全实践，严格隔离不同进程的权限。
<!-- END_BLOCK_61 -->

<!-- BLOCK_62 | doxcnm6XLVd3gekdnGD8bCnRjlh -->
- **核心安全原则**：
	- `nodeIntegration: false`：**严禁**在渲染进程中开启 Node.js 集成。
	- `contextIsolation: true`：**必须**开启上下文隔离，这是现代 Electron 安全的基石。它能确保 `preload` 脚本和网页的 JavaScript 运行在不同的上下文中，防止网页代码篡改 `preload` 脚本或 Electron 内部 API。
	- `sandbox: true`：开启渲染进程沙箱，限制其对系统资源的访问。
<!-- END_BLOCK_62 -->

<!-- BLOCK_63 | doxcnGqxvj7yaT5q0AugIOyAlug -->
- **通信桥梁：Preload 脚本**：`preload.js` 是唯一连接渲染进程和主进程（Node.js 环境）的桥梁。我们通过 `contextBridge` 向渲染进程暴露一个**受控的、白名单式的 API**，而不是直接暴露 `ipcRenderer`。
```javascript
// preload.js
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  // 白名单接口：从渲染进程到主进程
  searchNotes: (query) => ipcRenderer.invoke('search:notes', query),
  getNoteById: (id) => ipcRenderer.invoke('notes:get-by-id', id),

  // 白名单接口：从主进程到渲染进程
  onNoteUpdated: (callback) => ipcRenderer.on('note-updated', (event, ...args) => callback(...args))
});
```
<!-- END_BLOCK_63 -->

<!-- BLOCK_64 | doxcnWg9ldHrNYsQwUSkTTYHd7f -->
- **主进程 IPC 处理**：主进程使用 `ipcMain.handle` 响应 `invoke` 请求，并使用 `webContents.send` 主动向渲染进程推送事件。
```javascript
// main.js
ipcMain.handle('search:notes', async (event, query) => {
  // 参数校验
  if (typeof query !== 'string') {
    throw new Error('Invalid query');
  }
  // 调用本地后端服务...
  const results = await callBackendSearch(query);
  return results;
});

// 当笔记更新时，主动通知渲染进程
function notifyNoteUpdated(note) {
  mainWindow.webContents.send('note-updated', note);
}
```
<!-- END_BLOCK_64 -->

<!-- BLOCK_65 | doxcnVQfMw91fJkXDNx6Lha0K3f -->
- **渲染进程调用**：渲染进程中的 React 组件只能通过 `window.electronAPI` 访问暴露的接口，完全无法触及 Node.js 或 Electron 的其他部分。
```javascript
// MyReactComponent.jsx
async function handleSearch(query) {
  const results = await window.electronAPI.searchNotes(query);
  setResults(results);
}

useEffect(() => {
  const cleanup = window.electronAPI.onNoteUpdated((updatedNote) => {
    // ... 更新 UI
  });
  return cleanup; // 组件卸载时自动移除监听器
}, []);
```
<!-- END_BLOCK_65 -->

<!-- BLOCK_66 | doxcnBV1J4YkyRaSE0vG7Zykopf -->
### 2.4. 渲染层安全策略<!-- END_BLOCK_66 -->

<!-- BLOCK_67 | doxcnWudYsortg94keajzBghqKe -->
- **禁止直接运行 Node**：重申，渲染进程的 JavaScript 环境应被视为与普通网页同等的不受信任环境。所有需要 Node.js 能力（如文件读写）或 Electron 原生能力（如显示对话框）的操作，都必须通过 `preload` 桥接的 IPC 接口委托给主进程执行。
<!-- END_BLOCK_67 -->

<!-- BLOCK_68 | doxcnAKkiBK7ofw986pP0iXXi7d -->
- **远程内容加载策略**：
	- **严禁加载未知来源的远程内容**。所有 HTML/CSS/JS 资源都应是本地文件，随应用打包。
	- 如果必须展示外部网页，**必须**使用 `<webview>` 标签或 `BrowserView`，并为其配置严格的安全选项（`nodeIntegration: false`, `contextIsolation: true`），将其置于一个比应用自身渲染进程更受限的沙箱中。
	- 配置严格的**内容安全策略 (CSP)**，通过 `session.defaultSession.webRequest.onHeadersReceived` 拦截响应头，限制脚本执行、资源加载和网络请求的来源。
<!-- END_BLOCK_68 -->

<!-- BLOCK_69 | doxcnBUW74VeC2buMTWVfuAhjPd -->
通过以上设计，我们构建了一个职责清晰、边界明确、通信安全的 Electron 应用架构，能有效抵御常见的跨站脚本（XSS）和远程代码执行（RCE）攻击。
<!-- END_BLOCK_69 -->

<!-- BLOCK_70 | doxcnhGVg2eyHYDVIIOkIpDJR3d -->
## 3. 离线优先与数据一致性<!-- END_BLOCK_70 -->

<!-- BLOCK_71 | doxcnaBYpFWM5Mk8QOZF3r6ls3b -->
本章的核心是设计一个能够在断网环境下无缝工作，并在网络恢复时智能同步数据，确保最终一致性的健壮系统。
<!-- END_BLOCK_71 -->

<!-- BLOCK_72 | doxcnFSmHVudrkpjRPveqpj6YGd -->
![board_SUmiw7BlChCniCbermjcqt3on7b](board_SUmiw7BlChCniCbermjcqt3on7b_1.drawio)
<!-- END_BLOCK_72 -->

<!-- BLOCK_73 | doxcnAvOXjSyInd9YQBptLWiUUh -->
### 3.1. 文档型内容：Tiptap + Yjs (CRDT)<!-- END_BLOCK_73 -->

<!-- BLOCK_74 | doxcnMX0E4p2LgL6KMLTb0GVqMh -->
对于笔记的核心内容（富文本、表格、图片引用等），采用基于 CRDT 的方案是实现流畅离线编辑和无冲突合并的最佳实践。
<!-- END_BLOCK_74 -->

<!-- BLOCK_75 | doxcnCg5VHN06j0evpQrkn70mGd -->
- **技术栈**：
	- **编辑器**：`Tiptap`，提供强大的富文本编辑能力。
	- **协同引擎**：`Yjs`，一个高效的 CRDT 实现，负责处理数据结构的变更与合并。
	- **本地持久化**：`y-indexeddb`，将 Yjs 文档的二进制状态高效地存储在浏览器的 IndexedDB 中。
<!-- END_BLOCK_75 -->

<!-- BLOCK_76 | doxcnSuYXNob4bcreDQR1UCIXwg -->
- **工作流程**：
	1. **离线编辑**：用户的所有编辑操作（输入、删除、格式化）都被 Tiptap 捕获，并转换为对 Yjs 文档的操作。
	2. **本地持久化**：这些操作会立即更新内存中的 Yjs 文档，并通过 `y-indexeddb` 适配器**自动、增量地**写入本地 IndexedDB。这个过程是原子的，即使在写入中途关闭应用，数据也能保持一致。
	3. **网络恢复**：当网络连接恢复时，Yjs 的网络 Provider (如 `y-websocket`) 会被激活。
	4. **自动合并**：Provider 会自动与后端同步状态。由于 Yjs 基于 CRDT，它能将在离线期间发生的所有本地变更与云端的变更进行数学上可证明的无冲突合并。用户无需任何手动干预，所有设备上的内容最终会收敛到完全一致的状态。
<!-- END_BLOCK_76 -->

<!-- BLOCK_77 | doxcnWMroF8knY2uqtPamkY9dGe -->
- **支持表格与富文本**：Yjs 对嵌套的、复杂的富文本结构有良好的支持，能够正确处理表格、列表、内嵌块等在并发编辑场景下的冲突，确保文档结构不会被破坏。
<!-- END_BLOCK_77 -->

<!-- BLOCK_78 | doxcnpYKz6pNRDtsVRuU0qMvqah -->
### 3.2. 元数据/列表型：SQLite + 增量同步 (Delta Sync)<!-- END_BLOCK_78 -->

<!-- BLOCK_79 | doxcnS0ZYNr6YBrQk3bSe3uWwHc -->
对于笔记的元数据（如标题、标签、文件夹关系）和附件列表等结构化数据，我们使用 SQLite 进行本地存储，并通过自定义的增量同步协议与云端保持一致。
<!-- END_BLOCK_79 -->

<!-- BLOCK_80 | doxcnfEQZuFfKTySkJmFpR7cohh -->
- **本地存储**：
	- 使用本地 Python 后端操作的 SQLite 数据库。
	- **必须启用 WAL 模式** (`PRAGMA journal_mode=WAL;`)，以提高读写并发，降低数据库锁定的概率。
<!-- END_BLOCK_80 -->

<!-- BLOCK_81 | doxcnT9s6eH7Kvrswaz8fhdsWFb -->
- **增量同步协议 (Delta Sync)**：
	- **版本跟踪**：每条记录都需要增加 `version` 和 `last_modified_at` 两个字段。`version` 是一个递增的整数或版本向量，每次修改时更新；`last_modified_at` 记录服务器确认的修改时间戳。
	- **同步触发**：应用启动时、网络恢复时或定期（如每 5 分钟）触发同步流程。
	- **Pull 流程（下拉变更）**：
		1. 客户端向服务器发送 `pull` 请求，携带本地每个数据表的 `last_synced_at` 时间戳。
		2. 服务器返回自该时间戳以来所有发生变更（创建、更新、删除）的记录。
		3. 客户端将这些变更应用到本地 SQLite 数据库。
	- **Push 流程（推送变更）**：
		1. 客户端扫描本地数据库中所有待同步的变更（例如，可以设置一个 `is_synced` 标志位）。
		2. 将这些变更打包发送到服务器的 `push` 接口。
		3. 服务器处理这些变更，解决冲突，并返回成功或失败的结果。成功后，客户端更新本地记录的 `is_synced` 状态。
<!-- END_BLOCK_81 -->

<!-- BLOCK_82 | doxcnfgCHk9Mb8bPhAyLMTsVVOf -->
- **冲突解决策略矩阵**：当客户端和服务端同时修改了同一条记录时，必须有明确的冲突解决策略。
<!-- END_BLOCK_82 -->

<!-- BLOCK_83 | doxcnXr8nJJ4TzZSqc1ASSUy6zg -->
<table col-widths="250,250,250,250">
    <tr>
        <td>数据类型</td>
        <td>冲突场景</td>
        <td>解决策略</td>
        <td>备注</td>
    </tr>
    <tr>
        <td>**笔记标题、内容**</td>
        <td>A/B 用户同时修改</td>
        <td>**CRDT 自动合并**</td>
        <td>Yjs 负责处理，无需应用层干预。</td>
    </tr>
    <tr>
        <td>**标签、文件夹**</td>
        <td>A 用户重命名，B 用户删除</td>
        <td>**LWW (Last Write Wins)**</td>
        <td>以最后到达服务器的操作为准。简单有效，但可能丢失用户意图。</td>
    </tr>
    <tr>
        <td>**附件**</td>
        <td>A 用户替换文件，B 用户修改文件名</td>
        <td>**三方合并 (3-Way Merge)**</td>
        <td>如果有共同的祖先版本，可尝试自动合并（保留 B 的文件名和 A 的新文件）。</td>
    </tr>
    <tr>
        <td>**设置项**</td>
        <td>A/B 用户修改同一配置</td>
        <td>**LWW** 或 **服务器优先**</td>
        <td>通常配置项的冲突，以服务器的权威版本为准。</td>
    </tr>
    <tr>
        <td>**复杂结构冲突**</td>
        <td>无法自动合并</td>
        <td>**手动协商**</td>
        <td>在极少数情况下，如果自动策略失败，应将两个版本都保留，并在 UI 上提示用户手动选择或合并。</td>
    </tr>
</table>
<!-- END_BLOCK_83 -->

<!-- BLOCK_84 | doxcnI2fGauIly1V3M1tQ4w0Nkg -->
### 3.3. 备份与恢复<!-- END_BLOCK_84 -->

<!-- BLOCK_85 | doxcnQTMwa1efsGh8TNV461S6Fg -->
数据安全是最高优先级。必须提供健壮的本地备份和恢复机制。
<!-- END_BLOCK_85 -->

<!-- BLOCK_86 | doxcn4RPK1qYZN8HP9vzl22k1Hf -->
- **SQLite 备份**：
	- **在线备份 API**：利用 `sqlite3.Connection.backup()` 方法，可以在应用运行时对主数据库进行**热备份**，生成一个与当前状态完全一致的副本文件，而不会阻塞正在进行的读写操作。
	- **WAL Checkpoint 策略**：
		- 在执行文件系统级别的备份（如复制 `.db` 文件）之前，**必须**执行一次 `PRAGMA wal_checkpoint(TRUNCATE);`。
		- 此命令会强制将 `*-wal` 日志文件中的所有变更写入主数据库文件，并清空 WAL 文件。这确保了主 `.db` 文件本身是一个完整、一致的快照。不执行此操作而直接复制 `.db` 文件，会导致备份数据不完整，丢失最近的修改。
	- **备份策略**：
		- **定时备份**：每日或每周自动执行一次热备份，将备份文件存储在用户指定的目录或应用的备份文件夹中。可保留最近 3-5 个备份版本。
		- **应用退出时备份**：在应用关闭前，触发一次快速的 checkpoint 和备份。
<!-- END_BLOCK_86 -->

<!-- BLOCK_87 | doxcnwBPNQGMVhdwcIlzsWMuT1d -->
- **数据完整性风险与提示**：
	- **备份文件不完整**：必须教育用户，在手动备份或迁移数据时，如果数据库处于 WAL 模式，必须同时复制 `.db`, `.db-shm`, 和 `.db-wal` 三个文件，否则将导致数据丢失或损坏。
	- **恢复风险**：在从备份恢复数据前，应强烈建议用户先备份当前数据，以防恢复操作本身出现问题或恢复的是一个错误的版本。恢复操作应提供清晰的向导和不可逆操作的警告。
	- **跨版本恢复**：如果应用的版本迭代中涉及数据库 schema 的变更，旧版本的备份可能与新版应用不兼容。恢复流程需要能够检测版本差异，并尝试进行数据迁移，或者明确提示用户版本不兼容。
<!-- END_BLOCK_87 -->

<!-- BLOCK_88 | doxcnvuuVvIzkc55MXFYOYj1RUc -->
## 4. 同步机制基础 (接口规范草案)<!-- END_BLOCK_88 -->

<!-- BLOCK_89 | doxcnPUSvbKnfTSibXyfvmi0sgf -->
本章定义了客户端与云端同步服务之间的核心接口规范，为未来的跨端同步和云端存储功能奠定基础。该协议设计遵循 RESTful 原则，并采用增量同步（Delta Sync）思想以提高效率。
<!-- END_BLOCK_89 -->

<!-- BLOCK_90 | doxcnpawVxp3O3aJbaKVVzmEucf -->
### 4.1. 核心资源模型 (JSON Schema 草案)<!-- END_BLOCK_90 -->

<!-- BLOCK_91 | doxcnAfp7VMZYfHzOESElS9o3ob -->
所有通过 API 交换的数据都应遵循统一的资源模型。
<!-- END_BLOCK_91 -->

<!-- BLOCK_92 | doxcnsdn1LjZdVCRGuKmk8YlBye -->
- **Note (笔记)**
```json
{
  "id": "uuid",
  "title": "string",
  "content_crdt": "binary", // Yjs 文档的二进制表示
  "excerpt": "string",
  "tags": ["tag_id_1", "tag_id_2"],
  "asset_ids": ["asset_id_1"],
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "version": "integer"
}
```
<!-- END_BLOCK_92 -->

<!-- BLOCK_93 | doxcnmKPGjj4R8ziF5QruNgf6Qh -->
- **Block (块)注：在 CRDT 方案下，块级内容由&nbsp;content_crdt&nbsp;管理，独立的 Block 模型可能仅用于非 CRDT 内容的场景。**
<!-- END_BLOCK_93 -->

<!-- BLOCK_94 | doxcnO1UknPyKHrcLGk5U59H9Kc -->
- **Asset (附件)**
```json
{
  "id": "uuid",
  "note_id": "uuid",
  "filename": "string",
  "mime_type": "string",
  "size": "integer", // bytes
  "storage_path": "string", // 云存储路径
  "created_at": "timestamp",
  "version": "integer"
}
```
<!-- END_BLOCK_94 -->

<!-- BLOCK_95 | doxcnGHahw3XPvJAXbJlZkNafof -->
- **Embedding (向量)注：向量通常在客户端或服务端按需生成，是否需要独立同步取决于具体架构。**
<!-- END_BLOCK_95 -->

<!-- BLOCK_96 | doxcnx34Kgje4awEKn1SJYceH8f -->
- **Tag (标签)**
```json
{
  "id": "uuid",
  "name": "string",
  "color": "string",
  "version": "integer"
}
```
<!-- END_BLOCK_96 -->

<!-- BLOCK_97 | doxcnj8SdLHr1ooQSbyWhivr8Af -->
### 4.2. 增量同步协议 (Pull/Push)<!-- END_BLOCK_97 -->

<!-- BLOCK_98 | doxcnX3oF2z2XIoBu3ngMQLeLFe -->
#### 4.2.1. Pull (拉取云端变更)<!-- END_BLOCK_98 -->

<!-- BLOCK_99 | doxcnT283ExVjTTHhikJ4tqpB1c -->
客户端定期向服务器拉取自上次同步以来的所有变更。
<!-- END_BLOCK_99 -->

<!-- BLOCK_100 | doxcnrdAIeBAIJChXlJPCkNFlXg -->
- **Endpoint**: `GET /sync/pull`
<!-- END_BLOCK_100 -->

<!-- BLOCK_101 | doxcn7UdgtuDwvpTZ6xydRYwOWe -->
- **请求参数**:
	- `last_synced_at` (Timestamp): 客户端上次成功同步的时间戳。首次同步时为空。
	- `device_id` (String): 当前设备的唯一标识。
<!-- END_BLOCK_101 -->

<!-- BLOCK_102 | doxcnzUL6tPCBiyaq93Xh7B2WXc -->
- **响应体**:
```json
{
  "changes": {
    "notes": { "created": [...], "updated": [...], "deleted": ["id1", "id2"] },
    "tags": { "created": [...], "updated": [...], "deleted": ["id3"] },
    "assets": { "created": [...], "updated": [...], "deleted": ["id4"] }
  },
  "new_sync_timestamp": "timestamp" // 本次同步结束的服务器时间戳
}
```
<!-- END_BLOCK_102 -->

<!-- BLOCK_103 | doxcnKr2hgom7MlRmsyadP8AuVd -->
- **分页与过滤**: 对于初次同步或大量变更，响应应支持分页。服务器可在响应中包含 `next_page_token`，客户端需循环请求直至该 token 为空。
<!-- END_BLOCK_103 -->

<!-- BLOCK_104 | doxcnQhiw23mLiaxFDWrJwJnMzg -->
#### 4.2.2. Push (推送本地变更)<!-- END_BLOCK_104 -->

<!-- BLOCK_105 | doxcn7DGo1Ya53pYlVJB9nZRVuc -->
客户端将本地发生的所有变更推送到服务器。
<!-- END_BLOCK_105 -->

<!-- BLOCK_106 | doxcn0gp74ePbEa06NXv8KsBYXc -->
- **Endpoint**: `POST /sync/push`
<!-- END_BLOCK_106 -->

<!-- BLOCK_107 | doxcnpXtwHyVTwnmb2XxH25qolb -->
- **请求体**:
```json
{
  "device_id": "string",
  "changes": {
    "notes": { "created": [...], "updated": [...] },
    "tags": { "created": [...], "updated": [...] },
    "deleted": {
        "notes": ["id1", "id2"],
        "tags": ["id3"]
    }
  }
}
```
<!-- END_BLOCK_107 -->

<!-- BLOCK_108 | doxcnMZBKDi6x3lpF6LScKtd7fc -->
- **幂等性与重试**:
	- 每个变更对象应包含一个唯一的客户端生成的 `transaction_id`。服务器需要记录已处理的 `transaction_id`，在遇到重复 ID 时直接返回成功，从而保证 `push` 操作的幂等性，防止因网络重试导致重复创建。
<!-- END_BLOCK_108 -->

<!-- BLOCK_109 | doxcn4ZehNYXhDKqmv8PVR5oTcd -->
- **响应体**:
```json
{
  "status": "success",
  "processed_transactions": ["tid1", "tid2"],
  "conflicts": [
    {
      "type": "note",
      "id": "note_id_conflict",
      "server_version": 3,
      "client_version": 2,
      "resolution": "LWW_SERVER_WINS" // 冲突解决方法
    }
  ]
}
```
<!-- END_BLOCK_109 -->

<!-- BLOCK_110 | doxcnhD6bZn4jea9nSgm985G71e -->
### 4.3. 权限与鉴权<!-- END_BLOCK_110 -->

<!-- BLOCK_111 | doxcnr31XTdPrKlMAduUV96BAKg -->
- **设备注册**:
	1. 客户端首次启动时，生成一个唯一的设备 ID。
	2. 用户登录后，客户端使用用户凭证向服务器 `POST /devices/register` 接口注册该设备。
	3. 服务器返回一个与该设备绑定的长期有效的 `device_token`。
<!-- END_BLOCK_111 -->

<!-- BLOCK_112 | doxcnoZSE75pFfanFgweTLgTZLg -->
- **API 认证**:
	- 所有对同步 API 的请求，都必须在 HTTP Header 中包含 `Authorization: Bearer <device_token>`。
	- 服务器通过 `device_token` 验证请求的合法性，并将其与用户账户关联，确保数据隔离。
<!-- END_BLOCK_112 -->

<!-- BLOCK_113 | doxcnQuusDSoSwsU5QvNjPKcGHf -->
- **速率限制**:
	- 对 `pull` 和 `push` 接口实施基于设备 ID 或用户 IP 的速率限制（如每分钟不超过 60 次请求），防止滥用。
<!-- END_BLOCK_113 -->

<!-- BLOCK_114 | doxcn4kwabDjD9azYFwxyULX3ec -->
### 4.4. 云暴露策略 (预研)<!-- END_BLOCK_114 -->

<!-- BLOCK_115 | doxcnkbtzkS1fGCE4cxHWcAHCjf -->
当需要从外部设备（如手机）访问家中的 Windows 客户端数据时，需要一个安全的云暴露方案。
<!-- END_BLOCK_115 -->

<!-- BLOCK_116 | doxcnCwihQSBPZTlL3dEImD34nd -->
<table header-row="true" col-widths="200,200,200,200,200">
    <tr>
        <td>方案</td>
        <td>优点</td>
        <td>缺点</td>
        <td>典型用法</td>
        <td>何时选择</td>
    </tr>
    <tr>
        <td>**Cloudflare&nbsp;Tunnel**</td>
        <td>- **配置简单**，无需公网 IP。
- **安全性高**，自带 DDoS 防护和 WAF。
- 免费套餐满足基本需求。</td>
        <td>- 流量需经过 Cloudflare 全球网络，可能引入延迟。
- 免费版主要支持 HTTP/S，其他协议支持有限。</td>
        <td>在 Windows 客户端运行 `cloudflared` 守护进程，创建一个指向本地同步服务端口（如 8000）的隧道。外部设备通过 Cloudflare 分配的域名访问。</td>
        <td>**优先推荐**。当需要快速、安全地将 HTTP/S 服务暴露给公网，且对配置简易性要求高时。</td>
    </tr>
    <tr>
        <td>**Tailscale**</td>
        <td>- **P2P&nbsp;直连**，延迟低，速度快（打洞成功时）。
- **端到端加密**，安全性极高。
- 构建虚拟局域网，所有设备如同在同一内网。</td>
        <td>- 所有设备（包括手机）都**必须安装并登录 Tailscale&nbsp;客户端**。
- 在复杂的网络环境（如 NAT4）下可能打洞失败，回退到中继服务器，速度变慢。</td>
        <td>在 Windows 客户端和手机上都安装 Tailscale。手机端直接通过 Tailscale 分配的内网 IP 地址访问 Windows 客户端的同步服务。</td>
        <td>当所有需要同步的设备都能安装客户端，且追求极致的低延迟和网络隔离时。适合个人或小团队内部使用。</td>
    </tr>
</table>
<!-- END_BLOCK_116 -->

<!-- BLOCK_117 | doxcncLgpavL1vtmWLuDTN3KFXg -->
<callout icon="bulb" bgc="3" bc="3">
**集成方式建议：**
对于 `second-brain-ai`，**Cloudflare Tunnel** 是更现实的方案。它不要求移动端用户进行复杂的客户端安装和配置，只需通过一个安全的 URL 即可访问，用户体验更友好。未来可以在客户端设置中集成 `cloudflared` 的启动和隧道 Token 配置，实现一键开启远程访问。
</callout>
<!-- END_BLOCK_117 -->

<!-- BLOCK_118 | doxcngkqXUXZSlI6BwU5a2hyFSb -->
## 5. 开发计划与里程碑<!-- END_BLOCK_118 -->

<!-- BLOCK_119 | doxcngbJc3RMcM4efuASmanOcqh -->
本章旨在将整个 Windows 客户端的开发过程拆解为可执行、可衡量的里程碑，并明确各阶段的交付物、质量门槛及技术整合节点。
<!-- END_BLOCK_119 -->

<!-- BLOCK_120 | doxcn4RttMKFe7J0L4Netwwd8gb -->
![board_OpPdweNVFhowq5b7jM8c3EjhnBe](board_OpPdweNVFhowq5b7jM8c3EjhnBe_1.drawio)
<!-- END_BLOCK_120 -->

<!-- BLOCK_121 | doxcnyp7q7COFEwZTzRfTThg4ke -->
### 5.1. 里程碑拆解<!-- END_BLOCK_121 -->

<!-- BLOCK_122 | doxcn3ieRhGwxBBMAZd3kU0keIc -->
我们将项目分为三个主要里程碑：**PoC (概念验证)**、**Beta (公测版)** 和 **GA (正式发布)**。
<!-- END_BLOCK_122 -->

<!-- BLOCK_123 | doxcntDuAaLYVsx6cbDa2cGAsqe -->
<table col-widths="200,200,200,200,200">
    <tr>
        <td>里程碑</td>
        <td>周期</td>
        <td>核心目标</td>
        <td>交付物清单</td>
        <td>质量门槛</td>
    </tr>
    <tr>
        <td>**PoC**</td>
        <td>2 周</td>
        <td>验证核心技术可行性，打通关键路径。</td>
        <td>1. 可运行的 Electron 应用框架。
2. Tiptap 编辑器基本集成。
3. **路线 A**：Python 后端能被 Electron 启动并处理简单请求。
4. **路线 B**：Yjs 内容能持久化到 IndexedDB。</td>
        <td>- 功能可演示。
- 关键技术无阻塞性问题。</td>
    </tr>
    <tr>
        <td>**Beta**</td>
        <td>4 周</td>
        <td>实现完整的离线优先功能，并发布给内部或小范围用户测试。</td>
        <td>1. 完整的笔记创建、编辑、查看功能（离线可用）。
2. 本地数据持久化方案（SQLite + y-indexeddb）落地。
3. 初步的本地搜索功能（向量或全文）。
4. 可安装的 `.exe` 包（未签名）。
5. 基础的 UI/UX。</td>
        <td>- 稳定性：连续使用 4 小时无崩溃。
- 性能：应用冷启动时间 < 5s，笔记加载 < 1s。
- 无核心功能 Bug。</td>
    </tr>
    <tr>
        <td>**GA**</td>
        <td>3 周</td>
        <td>完善同步机制，加固安全性，优化性能和用户体验。</td>
        <td>1. 完整的增量同步功能（Pull/Push）。
2. 代码签名和 NSIS 安装包优化。
3. 完善的备份与恢复功能。
4. 完整的安全加固 checklist 落地。
5. 官方文档和帮助指南。</td>
        <td>- 回归测试通过率 100%。
- 数据一致性：经过 100 次“离线-在线”切换测试，无数据丢失或损坏。
- 性能：内存占用峰值 < 500MB。</td>
    </tr>
</table>
<!-- END_BLOCK_123 -->

<!-- BLOCK_124 | doxcni0Nwcr4hArpRl4lF2Q7NOe -->
### 5.2. 并行推进与整合节点<!-- END_BLOCK_124 -->

<!-- BLOCK_125 | doxcnSFdTThkkjQgFZUnxAWU0Sf -->
为了加快开发进度，我们将并行推进**本地后端方案 (A)** 和 **纯前端离线方案 (B)** 的关键模块，并在特定节点进行整合。
<!-- END_BLOCK_125 -->

<!-- BLOCK_126 | doxcnWpKRh2ICOVVBizP6QIOoHc -->
- **第一周 ~&nbsp;第二周 (PoC 阶段)**:
	- **团队 A (后端 & Electron)**：
		- **任务**: 专注于 **路线 A** 的 PoC。搭建 Electron + React 基础项目。使用 PyInstaller 打包一个最小化的 FastAPI "Hello World" 服务。在 Electron 主进程中实现该服务的启动和关闭。
		- **产出**: 一个能启动/关闭 Python 进程的 Electron 应用。
	- **团队 B (前端 & CRDT)**：
		- **任务**: 专注于 **路线 B** 的 PoC。在一个独立的 React 项目中，集成 Tiptap + Yjs + y-indexeddb，实现富文本内容的本地创建、编辑和持久化。
		- **产出**: 一个纯前端的、具备离线笔记编辑能力的 Web App。
<!-- END_BLOCK_126 -->

<!-- BLOCK_127 | doxcnWEWVKJy4VFMet1mlubEKte -->
- **第三周 (整合节点)**:
	- **任务**: 将团队 B 的前端成果整合进团队 A 的 Electron 项目中。此时，前端的富文本编辑部分使用其独立的持久化方案（y-indexeddb），而应用的元数据（如笔记列表）则通过 IPC 调用由 Python 后端管理的 SQLite。
	- **目标**: 验证混合架构的可行性。
<!-- END_BLOCK_127 -->

<!-- BLOCK_128 | doxcnPX6DGVDGRiT9LZkcwgIaLd -->
- **第四周 ~&nbsp;第七周 (Beta 阶段)**:
	- 在整合后的架构上，完善所有核心功能，包括 SQLite 的 CRUD 操作、本地搜索接口、附件管理等。
	- 完成 UI/UX 的主要设计和实现。
	- 进行内部测试和 Bug 修复。
<!-- END_BLOCK_128 -->

<!-- BLOCK_129 | doxcnnd22OFhIsYVBk2ZPaoMOSc -->
- **回退策略**:
	- 如果在整合节点发现混合架构存在难以解决的性能或稳定性问题，我们将基于 PoC 阶段的结论，迅速决策并完全转向其中一条路线。
	- **倾向于回退到路线 A (本地后端)**，因为它能更好地复用现有逻辑，虽然离线编辑体验可能需要降级（例如，放弃 CRDT，采用简单的本地缓存 + LWW 策略）。
<!-- END_BLOCK_129 -->

<!-- BLOCK_130 | doxcn0V1MsDcU9wrSKIY9ymcVVh -->
### 5.3. 安全加固 Checklist<!-- END_BLOCK_130 -->

<!-- BLOCK_131 | doxcnkbt3ayHWzqXHWakRqrGzye -->
在 **GA** 版本发布前，必须完成以下所有安全项的检查与加固。
<!-- END_BLOCK_131 -->

<!-- BLOCK_132 | doxcnrpCvyqlPnupCrbKDiYnpWc -->
#### IPC 安全<!-- 标题序号: 1 --><!-- END_BLOCK_132 -->

<!-- BLOCK_133 | doxcn72TDpDNIqycDXLUKsHV1Ae -->
- [ ] **IPC 接口白名单化**：所有通过 `contextBridge` 暴露的接口都经过严格审查，遵循最小权限原则。
<!-- END_BLOCK_133 -->

<!-- BLOCK_134 | doxcnHDepVv7RISS3BQ6Ix8QnRh -->
- [ ] **参数校验**：主进程中所有 `ipcMain.handle` 和 `ipcMain.on` 的监听器都对来自渲染进程的参数进行了类型、格式和范围的严格校验。
<!-- END_BLOCK_134 -->

<!-- BLOCK_135 | doxcnW0V3uWb0AuFN1tDyAUVNAh -->
- [ ] **禁止暴露原始&nbsp;ipcRenderer**：确认 `preload` 脚本没有将 `ipcRenderer` 对象或其方法直接暴露给渲染进程。
<!-- END_BLOCK_135 -->

<!-- BLOCK_136 | doxcn7yFBnBs5ZfzryA5cUPu2Hc -->
#### 核心配置安全<!-- 标题序号: 2 --><!-- END_BLOCK_136 -->

<!-- BLOCK_137 | doxcnCeHxprd9TAOQ7dLCTmRXbg -->
- [ ] `nodeIntegration: false`
<!-- END_BLOCK_137 -->

<!-- BLOCK_138 | doxcn9xSlxDP0LP9ST05HdQ0bsc -->
- [ ] `contextIsolation: true`
<!-- END_BLOCK_138 -->

<!-- BLOCK_139 | doxcnexO0B05WMzNNOwmMWRevMd -->
- [ ] `sandbox: true`
<!-- END_BLOCK_139 -->

<!-- BLOCK_140 | doxcnVnu0IuKjLqe0qzQNrCWxKh -->
- [ ] **内容安全策略 (CSP)**：已配置严格的 CSP，禁止内联脚本 (`unsafe-inline`) 和远程代码加载。
<!-- END_BLOCK_140 -->

<!-- BLOCK_141 | doxcnzLM7EdoIx4RTWXFI6QJR7c -->
- [ ] **URL 白名单**：所有外部链接（如果必须）都通过 `shell.openExternal` 打开，并对 URL 协议和域名进行白名单校验。
<!-- END_BLOCK_141 -->

<!-- BLOCK_142 | doxcnrO5ga3ayHpjwHipvq2lxFb -->
#### 分发与环境安全<!-- 标题序号: 3 --><!-- END_BLOCK_142 -->

<!-- BLOCK_143 | doxcnINfkWITit2IxbfnpCwNNwf -->
- [ ] **代码签名**：Windows 安装包已使用有效的证书进行签名。
<!-- END_BLOCK_143 -->

<!-- BLOCK_144 | doxcnc4iutgS3m0RiLlfNaYvKdh -->
- [ ] **依赖审查**：所有第三方 npm 和 Python 包都经过审查，无已知高危漏洞。
<!-- END_BLOCK_144 -->

<!-- BLOCK_145 | doxcnzRURlGKuaSjZWfcNvRDOqh -->
- [ ] **远程内容隔离**：如果应用内嵌了 `<webview>`，确保其运行在独立的、权限更低的进程中。
<!-- END_BLOCK_145 -->

<!-- BLOCK_146 | doxcnjrQOxoIyIljZAkfBp7gmih -->
#### 数据与恢复<!-- 标题序号: 4 --><!-- END_BLOCK_146 -->

<!-- BLOCK_147 | doxcnemupr614ed74mH8HhwPJff -->
- [ ] **崩溃恢复**：应用在异常崩溃后重启，能够恢复到上次的稳定状态，无数据丢失。
<!-- END_BLOCK_147 -->

<!-- BLOCK_148 | doxcnC8ILOc4PbdyqWEhbXjOdQf -->
- [ ] **日志与指标**：集成了基本的日志系统（如 `electron-log`），记录关键操作和错误，便于问题排查。敏感信息（如用户数据）不会被记入日志。
<!-- END_BLOCK_148 -->

<!-- BLOCK_149 | doxcnVJujv9n0E3pGWskFKpVjwf -->
- [ ] **备份可恢复性**：定期测试备份文件的可恢复性，确保备份流程可靠。
<!-- END_BLOCK_149 -->

<!-- BLOCK_150 | doxcnSHrTFqPf6OCvRhnSWO6R2b -->
## 6. 风险与规避<!-- END_BLOCK_150 -->

<!-- BLOCK_151 | doxcnHNHXHs588UGn28LOvk9D0b -->
在项目实施过程中，我们预见到以下潜在风险，并提前制定了相应的规避策略。
<!-- END_BLOCK_151 -->

<!-- BLOCK_152 | doxcnYfMyHXo2NXL8s5GIJs3zlh -->
<table col-widths="200,200,200,200,200">
    <tr>
        <td>风险类别</td>
        <td>风险描述</td>
        <td>可能性</td>
        <td>影响</td>
        <td>规避措施</td>
    </tr>
    <tr>
        <td>**打包与分发**</td>
        <td>**包体体积过大**：捆绑 Python 运行时和大量依赖（如 PyTorch, Pandas）可能导致安装包体积超过 500MB，影响下载和安装体验。</td>
        <td>高</td>
        <td>中</td>
        <td>1. **精简依赖**：定期审查 Python 依赖，移除不必要的库。
2. **延迟加载**：将大型模型或不常用的依赖设计为首次使用时按需下载。
3. **UPX 压缩**：在 `electron-builder` 中开启 `upx` 压缩，可有效减小可执行文件体积。
4. **分阶段打包**：考虑将核心功能与扩展功能分离，提供基础版和完整版。</td>
    </tr>
    <tr>
        <td></td>
        <td>**Windows Defender 误报**：由 PyInstaller 打包的未签名 `.exe` 文件极易被 Windows Defender 或其他杀毒软件误报为病毒，导致应用无法启动。</td>
        <td>极高</td>
        <td>高</td>
        <td>1. **强制代码签名**：所有公开发布的版本都**必须**使用有效的 OV/EV 代码签名证书进行签名。
2. **提交白名单**：在发布前，将已签名的应用提交给主流杀毒软件厂商（如 Microsoft）进行预分析，加入白名单。
3. **选择性打包**：避免使用可能触发启发式检测的打包选项（如过于激进的压缩）。</td>
    </tr>
    <tr>
        <td>**性能**</td>
        <td>**启动时长过长**：应用冷启动时，需要同时初始化 Electron 主进程、渲染进程和 Python 后端子进程，可能导致用户等待时间超过可接受范围（如 > 5-8 秒）。</td>
        <td>中</td>
        <td>中</td>
        <td>1. **优化主进程加载**：延迟非核心模块的 `require`，将耗时操作异步化。
2. **渲染进程优化**：采用代码分割（Code Splitting），按需加载路由和组件。显示启动画面（Splash Screen）以改善用户感知。
3. **Python 启动优化**：优化 Python 启动脚本，延迟导入大型模块。</td>
    </tr>
    <tr>
        <td>**依赖管理**</td>
        <td>**Python 依赖冲突**：在复杂的 Python 环境中，不同库之间可能存在版本冲突，导致打包失败或运行时错误。</td>
        <td>中</td>
        <td>高</td>
        <td>1. **锁定依赖版本**：使用 `pip freeze > requirements.txt` 或 `Poetry`/`Pipenv` 等工具锁定所有依赖（包括子依赖）的确切版本。
2. **虚拟环境**：在干净的虚拟环境中进行打包，确保环境纯净。
3. **持续集成 (CI)**：在 CI 环境中自动化构建和测试流程，及早发现依赖问题。</td>
    </tr>
    <tr>
        <td>**安全性**</td>
        <td>**Electron 安全边界被突破**：错误的 IPC 设计或配置（如 `nodeIntegration: true`）可能导致渲染进程获得过高权限，引发远程代码执行 (RCE) 漏洞。</td>
        <td>低</td>
        <td>极高</td>
        <td>1. **遵循安全 Checklist**：严格执行第 5.3 节中的所有安全加固措施。
2. **上下文隔离**：始终开启 `contextIsolation`，并通过 `contextBridge` 暴露有限的、经过参数校验的 API。
3. **代码审查**：对所有涉及 IPC 通信和 `preload` 脚本的代码进行严格的内部代码审查。</td>
    </tr>
    <tr>
        <td></td>
        <td>**远程加载风险**：若应用内需要加载外部网页或资源，可能因目标网站被攻击而引入恶意代码。</td>
        <td>低</td>
        <td>高</td>
        <td>1. **禁止加载未经验证的远程内容**：默认情况下，应用不应加载任何 HTTP/HTTPS 资源。
2. **使用&nbsp;<webview>&nbsp;或&nbsp;BrowserView**：如果必须加载，请使用这些标签/视图，并为其配置最严格的安全策略，将其运行在独立的、权限更低的沙箱中。
3. **配置内容安全策略 (CSP)**：限制资源加载的来源，禁止执行内联脚本。</td>
    </tr>
    <tr>
        <td>**数据一致性**</td>
        <td>**备份文件不可恢复**：用户可能因不理解 WAL 模式而只备份了 `.db` 文件，导致数据丢失；或者备份文件本身已损坏但未被发现。</td>
        <td>中</td>
        <td>高</td>
        <td>1. **明确的用户指引**：在备份/恢复功能的 UI 中，明确告知用户需要备份哪些文件，或提供一键打包备份的功能。
2. **备份校验**：备份完成后，可提供一个可选的“校验备份”功能，尝试从备份文件恢复到一个临时数据库，以验证其完整性。
3. **自动备份优先**：鼓励用户使用应用内置的自动、定时热备份功能，减少手动操作的风险。</td>
    </tr>
    <tr>
        <td></td>
        <td>**同步冲突导致数据丢失**：在 LWW (Last Write Wins) 策略下，用户的修改可能被其他设备的更新无声地覆盖，导致数据“丢失”的错觉。</td>
        <td>中</td>
        <td>中</td>
        <td>1. **CRDT 优先**：对于核心的文档内容，坚持使用 Yjs (CRDT) 方案，从根本上避免冲突。
2. **明智的冲突策略**：对于元数据，审慎选择冲突解决策略。对于关键操作（如删除），可考虑引入“回收站”机制或软删除，而不是物理删除。
3. **冲突提示**：在发生无法自动解决的复杂冲突时，应在 UI 上向用户明确展示冲突内容，并提供手动解决的选项。</td>
    </tr>
</table>
<!-- END_BLOCK_152 -->

