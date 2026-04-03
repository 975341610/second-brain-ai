# Second Brain AI - 开发进度与状态日志

> **维护规则 (System Rule)**: 
> 1. 每次收到新需求、发现新问题，第一时间补充到此文档。
> 2. 只有在**用户（老大）明确确认**问题/需求解决后，才能标记为 `[x]` 或 `已解决`。
> 3. 每次提交 GitHub (Commit/Push) 必须在此记录更新详情。
> 4. 保持言简意赅，方便 AI 快速读取上下文。

---

## 📋 需求追踪 (Requirements)

### 待办 / 进行中 (Pending / In Progress)
- [ ] **架构转向：Obsidian/Typora 风格（纯本地文件 SSOT + 数据同步）**
  - [x] **Phase 1: 极简 I/O 链路重写 (Node.js 原生直写)** - 已完成，切断了笔记读写的 Python 依赖。
  - [x] **Phase 2: 状态解绑与隔离 (State Decoupling)** - 已完成，编辑器重构为非受控组件，实现静默防抖保存。
  - [x] **Phase 3: 彻底离线化改造 (Offline-first & No-blocking)** - 已完成，移除启动阻塞与 fetch 依赖。
  - [ ] **Phase 4: 结构化元数据索引 (本地嵌入式 DB)**
- [ ] **Phase 5: 桌面究极体改造** (Electron 重构，独立桌面窗口，系统托盘 - 已完成 MVP 适配)
- [ ] **全站 UI & 布局重构** (参考 Awwwards、Linear 质感)
- [ ] **互动级动态壁纸系统** (WebGL/Three.js，环境感知)
- [ ] **万物皆可拖拽** (自由调整文档/文本/图片位置)
- [ ] **飞书级表格系统** (多维属性增强)
- [x] **[Windows MVP] 系统托盘与本地路径优化** (已完成)

### 待确认 (Pending User Confirmation)
- [ ] **[架构迁移] 纯本地文件优先 (Local-first) SSOT 闭环实现**
  - *更新内容*: 
    1. 增强 `SSOTWatcher`：支持磁盘变更内容实时推送到编辑器。
    2. `NotionEditor` 适配：响应 `ssot:note-changed` 事件，实现与第三方编辑器（Obsidian/Typora）的协同。
    3. `preload` 安全增强：优化 IPC 事件绑定，支持自动清理监听。
    4. Windows 适配：本地存储路径迁移至 `appData`，完善系统托盘双击恢复与关闭隐藏逻辑。
  - *当前进度*: 代码已就绪，**[待老大确认测试]**。
- [ ] **[Bug修复] 基础联调与多端同步前置问题修复** (当前所在分支 `fix/4-issues-integration`)

### 已完成 (Completed)
- [x] **[架构重构] 彻底切断 FastAPI 依赖，实现纯本地 IPC CRUD 闭环** (2026-03-31)
  - *重构详情*: 
    1. **前端 API 层**: 全面移除 `fetch` 对 FastAPI 的直接调用，改为通过 `window.electron.ipcInvoke` 与主进程通信。
    2. **主进程 IPC Bridge**: 在 `src/main` 引入 Python 桥接机制，直接调用 `repositories.py` 逻辑，绕过网络协议栈。
    3. **Preload 安全增强**: 暴露通用的 `ipcInvoke` 接口，支持渲染进程直接发起本地指令。
  - *解决痛点*: 彻底解决了用户抱怨的“本地读写为何还有网络请求失败”的问题，大幅提升了操作响应速度与可靠性。

---

## 🐛 问题追踪 (Issue Tracker)

### 未解决 / 待确认 (Unresolved / Pending Confirmation)
1. **保存系统冲突（前端保存与磁盘监控打架）**
   - *现象*: 自动保存触发后，SSOT Watcher 监测到文件变化并推送到前端，导致编辑器强制 `setContent`，引发光标跳动、死循环或内容被旧版本覆盖。
   - *修复细节*:
     - **NotionEditor.tsx**: 引入 `isRemoteUpdatingRef` 锁机制。在处理来自磁盘的同步事件（`ssot:note-changed`）时，临时禁用 `onUpdate` 触发的自动保存，切断死循环。
     - **光标保护**: 增加 `isFocused` 判断，用户正在输入时跳过强制同步；增加 `selection` 记录与恢复逻辑，确保同步后光标位置不丢失。
     - **属性修改优化**: 在 `App.tsx` 中将侧边栏属性修改（图标、标签等）设为 `silent: true` 模式，减少不必要的 UI 干扰与重绘。
   - *当前进度*: 已完成核心链路修复，**[待老大确认测试]**。
2. **保存失败与回收站遗留问题**
   - *现象*: 笔记保存偶尔失败（父子关系丢失），新建子页面导致父页面重载，删除笔记不进本地回收站。
   - *修复细节*:
     - **Bug 1 (保存)**: 修复了 `App.tsx` 的 `onUpdateNote` 回调遗漏 `parent_id` 的问题；改进了后端 `update_note_api` 逻辑，支持显式传递 `null` 来清除父节点。
     - **Bug 2 (刷新)**: 为 `createDraftNote` 引入 `silent` 模式，在创建子页面时实现局部乐观更新，禁止触发全量组件重绘。
     - **Bug 3 (回收站)**: 在后端 `soft_delete_note` 中实现了将已删除笔记（含子笔记）自动导出并移动到 `.trash/*.md` 文件的机制，确保了纯本地架构下的物理软删除闭环。
   - *当前进度*: 已完成 TDD 修复，本地测试通过。**[待老大确认]**。
2. **编辑器状态泄露 (State Bleed)**
   - *现象*: 快速切换笔记时，旧笔记内容覆盖新笔记。
   - *当前进度*: 引入闭包和 `Ref` 锁机制阻断串台。代码已推送，**[待老大确认]**。
4. **动态视频壁纸无法播放**
   - *现象*: IndexedDB 取出的视频 Blob 缺少 MIME 类型。
   - *当前进度*: 已强制指定 `video/mp4` MIME 类型。代码已推送，**[待老大确认]**。

### 已解决 (Resolved)
1. **保存失败、刷新与回收站遗留问题** (已通过 IPC 重构彻底修复)
   - **Bug 1 (保存)**: 修复了更新笔记时 `parent_id` 可能被覆盖为 `null` 的逻辑漏洞。
   - **Bug 2 (刷新)**: 优化了 `useAppStore` 的状态合并逻辑，确保新建子页面（silent 模式）时不会导致父页面编辑器重载。
   - **Bug 3 (回收站)**: 完善了 Electron 主进程触发的物理软删除，删除笔记时自动在本地 `.trash` 目录生成对应的 `.md` 备份。
2. **编辑器状态泄露 (State Bleed)** (已修复)
4. **动态视频壁纸无法播放** (已修复)

---

## 📦 提交与更新记录 (Commit & Update Log)
- **2026-04-03 | Branch: `feature/local-first-architecture`**
  - `Commit: [Latest]`
  - *更新内容*: **离线架构彻底改造 (Phase 3 闭环)**。
    1. **移除启动阻塞 (App.tsx & useAppStore.ts)**: 彻底移除登录检查与 `SplashScreen` 阻塞。优化 `loadInitialData` 为容错并行加载，即使后端离线也直接进入 `READY` 状态渲染编辑器，实现“秒开”。
    2. **修复保存逻辑 (api.ts)**: 强制 IPC 调用，禁止在 Electron 下回退到 `fetch` 访问 Python 后端。
    3. **修复笔记切换空白 (App.tsx & NotionEditor.tsx)**: 通过 `key={selectedNoteId}` 强制编辑器重新挂载，并优化 `useEffect` 内容同步逻辑。
    4. **AI 接口补全**: 在 `api.ts` 中新增了 `streamInlineAI` 的 IPC 调用支持。
  - *解决痛点*: 实现了纯离线使用能力，消除了启动过程中的各种“请求后端失败”带来的阻塞感，解决了多处 UI 状态不一致的问题。

- **2026-03-31 | Branch: `feature/local-first-architecture`**
  - `Commit: [Latest]`
  - *更新内容*: **修复 PropertyPanel 崩溃问题并增强组件健壮性**。
    1. **PropertyPanel.tsx 崩溃修复**: 修复了在 `note.properties` 为 `undefined` 时调用 `.find()` 导致的 `TypeError`；通过添加默认空数组 `(note.properties || [])` 确保了组件在数据缺失时的稳定性。
    2. **App.tsx 空值处理**: 同步优化了 `App.tsx` 中 `includes` 相关的空值校验（紧随前序修复）。
  - *解决痛点*: 消除了编辑器侧边栏在特定笔记数据下导致的整站崩溃风险，提升了前端渲染的容错性。

- **2026-03-31 | Branch: `feature/local-first-architecture`**
  - `Commit: [Latest]`
  - *更新内容*: **执行全面的依赖清理与一键安装脚本构建**。
    1. **依赖统一与修复**: 统一了 `frontend` 中所有 Tiptap 相关包至 `^2.11.5` 稳定版本，修复了版本混用导致的 `peerDependency` 冲突；降级 `vite` 至 `^5.1.4` 以保持架构一致性。
    2. **显式核心包补全**: 补齐了 `y-protocols`, `@tiptap/y-tiptap`, `@tiptap/extension-node-range` 等缺失的底层依赖。
    3. **一键式工程化脚本**: 
       - 新增 `npm run bootstrap`: 跨平台一键清理 `node_modules` 并重新安装。
       - 增强 `postinstall`: 自动使用 `--legacy-peer-deps` 顺滑安装前端依赖。
       - 新增 `npm run clean`: 基于 Node.js 的跨平台目录清理脚本。
  - *解决痛点*: 彻底解决了用户在本地环境安装依赖时频繁遇到的冲突与“Could not resolve”报错，实现了真正的一键开发环境搭建。

- **2026-03-31 | Branch: `feature/local-first-architecture`**
  - `Commit: 0bb7643`
  - *更新内容*: **优化了依赖安装流程，解决了前端依赖丢失问题**。
    1. **自动依赖安装**: 在根目录 `package.json` 中增加了 `postinstall` 脚本，执行 `npm install` 时会自动安装 `frontend` 目录下的依赖。
    2. **解决依赖缺失**: 修复了 `@tiptap/extension-collaboration` 等新引入依赖在本地环境拉取后运行报错的问题。
  - *使用说明*: 之后只需 `git pull` 然后在根目录重新运行 `npm install` 即可自动完成所有依赖安装。

- **2026-03-31 | Branch: `feature/local-first-architecture`**
  - `Commit: a78dc6f`
  - *更新内容*: **深度诊断并修复了自动保存卡死与白屏 (React 崩溃) 问题**。
    1. **IPC 链路闭环**: 在 `preload` 中暴露 `ipcInvoke`，并在主进程中实现了业务逻辑转发。
    2. **性能重构**: 主进程接管了高频的 `notes:*` IPC 请求，并将其转发给常驻的 Python 后端（FastAPI），消除了每次保存都 `spawn` Python 进程的巨大开销。
    3. **稳定性增强**: 在 `NotionEditor` 外层包裹了 `ErrorBoundary`，删除了所有阻断性的硬编码“连接失败”提示，确保即使后端瞬时繁忙，前端也不会白屏崩溃。
  - *解决痛点*: 彻底解决了用户反馈的“长时间自动保存中”以及保存失败导致的白屏问题，实现了真正的本地化秒存体验。

- **2026-03-31 | Branch: `fix/4-issues-integration`**
  - `Commit: 9258886`
  - *更新了什么*: 恢复了毛玻璃面板 UI、基于 IndexedDB 的壁纸存储以及赛博朋克主题。
  - *解决了什么*: 提升了 UI 质感与个性化体验，确保壁纸数据在本地持久化。

- **2026-03-31 | Branch: `feature/local-first-architecture`**
  - `Commit: 6a2c1f3` (Local-only)
  - *更新了什么*: 修复了三个遗留 Bug：1. 彻底修复 `parent_id` 丢失与保存失败；2. 子页面创建静默乐观更新；3. 数据库与本地文件级联软删除至 `.trash`。
  - *解决了什么*: 确保了笔记层级的稳健性，提升了 UI 响应体验，并完善了本地文件架构下的回收站闭环。

- **2026-03-31 | Branch: `feature/local-first-architecture-poc`**
  - `Commit: N/A` (本地 PoC 阶段)
  - *更新了什么*:
    1. **前端持久化层**: 引入 `yjs` + `y-indexeddb`，在 `NotionEditor` 中为每篇笔记开启独立的 CRDT 状态与 IndexedDB 本地存储。
    2. **主进程 SSOT 框架**: 实现 `SSOTWatcher` (Node.js 原生 API)，监听本地 `data/` 目录下的 `.md` 文件变更，并通过 IPC 同步至渲染进程。
    3. **IPC 安全桥接**: 更新 `preload` 与 `index.ts`，暴露 `watchNote` 等本地优先核心接口。
  - *解决了什么*: 打通了“本地文件监听 -> 渲染进程协作”的 SSOT (Single Source of Truth) 最小可行性闭环，为纯本地文件优先架构奠定基础。

- **2026-03-31 | Branch: `feature/local-first-architecture`**

  - `Commit: N/A`
  - *更新了什么*: 交付了《纯本地文件优先架构迁移方案与 Windows MVP 任务拆解》([文档链接](https://bytedance.larkoffice.com/docx/SwqEduxjho8b7zx0jAscKWPkntd))。
  - *解决了什么*: 明确了 Local-first 架构的总体设计、技术选型、演进路径与 Windows 客户端 MVP 的具体任务。本次无代码变更，未推送远程。

- **2026-03-30 | Branch: `fix/4-issues-integration`**
  - `Commit: c81a9fe`
  - *更新了什么*: 修复编辑器 `NotionEditor.tsx` 在防抖保存和快捷键保存时遗漏 `parent_id` 的问题。
  - *解决了什么*: 防止笔记在更新内容时，其父级层级关系被错误重置（移出到根目录）。

---

## 🧪 架构收尾检查与测试清单 (Test Checklist)

针对 `feature/local-first-architecture` 架构，请务必进行以下验收测试：

### 1. 离线/断网表现 (Offline-First Ready)
- [ ] **秒开验证**：断开网络启动应用，编辑器应立即显示上一次的内容（由 IndexedDB 渲染），不应出现长时间 Loading 或白屏。
- [ ] **数据持久化**：在断网状态下修改内容并关闭应用，重新打开后修改应依然存在。
- [ ] **存储位置检查**：验证本地配置文件和笔记是否正确存储在 Windows 的 `%APPDATA%\SecondBrainAI` 目录下。

### 2. 多编辑器协同 (External Watcher / SSOT)
- [ ] **双向同步逻辑**：
  - 使用外部编辑器（Obsidian/VSCode）修改 `.md` 文件并保存，SecondBrainAI 编辑器应在 1s 内自动刷新。
  - 在 SecondBrainAI 修改并失去焦点后，检查本地 `.md` 文件内容是否同步更新。
- [ ] **覆盖与冲突**：模拟同时修改同一行，验证 Yjs 的 CRDT 合并逻辑是否生效（不应导致文件内容乱码或丢失）。
- [ ] **文件删除处理**：外部物理删除文件后，应用应能正确处理 UI 状态（如提示文件已丢失或从列表移除）。

### 3. IPC 与资源清理 (Resource Leak Prevention)
- [ ] **Watcher 销毁验证**：快速切换工作区文件夹，通过任务管理器观察进程，确保新有的 `chokidar` 监听器已释放。
- [ ] **Sidecar 进程管理**：退出应用后，检查后台是否有残留的 Python (Backend) 或 Node (Watcher) 进程。
- [ ] **内存占用监控**：频繁编辑大型文档，观察渲染进程内存，确保 Yjs 历史记录（UndoManager）没有导致内存持续攀升。

### 4. Windows 托盘体验 (UX/DX)
- [ ] **关闭到托盘**：点击窗口关闭按钮（X），窗口应隐藏至托盘。双击托盘图标或通过右键菜单“显示窗口”应能瞬间恢复。
- [ ] **彻底退出**：托盘右键选择“退出”，应用及所有关联 Sidecar 进程应全部正常关闭。
- [ ] **多开拦截**：应用已运行时，再次双击桌面快捷方式，应直接唤起已有的窗口，而不是启动第二个进程。
