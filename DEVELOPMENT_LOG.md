# Development Log

## v0.08 - 贴纸系统完全体 (修复全局404、实现拖拽与体验微调)

### 核心修复与优化 (Sticker System & API)
- **后端 API 全面修复**：解决了后端 IPv6/IPv4 端口冲突导致的 404 错误，重构了 SPA 拦截逻辑，确保 API 请求（如 `/api/stickers/list`）不再被错误重定向至 `index.html`。
- **内网穿透适配**：改写前端 fetch 请求逻辑，引入 `getApiBase()` 动态识别环境，完美适配内网穿透与远程访问场景。
- **原生拖拽上墙 (Drag & Drop)**：在贴纸面板实现 HTML5 原生拖拽，支持将贴纸库资源直接拖拽至编辑器任意位置，并实现“落点即中心”的精准放置。
- **解决无限循环渲染**：重构了 `StickerLayer` 与 `NovaBlockEditor` 的通讯机制，将回调函数移出 React 状态更新周期，彻底消除了由于状态竞争导致的崩溃与白屏报错。
- **独立透明度与样式分离**：为贴纸引入独立的透明度调节功能，并与便利贴（Sticky Notes）实现架构层面的彻底分离，互不干扰。
- **防状态重置保护**：优化了数据保存与读取逻辑，确保在编辑器重渲染或切换笔记时，贴纸的位置、旋转角度、缩放比例及透明度得到持久化保留。

### UI/UX 体验升级
- **悬浮操作菜单**：将贴纸操作从“悬停触发”改为“点击选中”，避免鼠标经过时的视觉干扰。选中后唤起带有毛玻璃效果的精致控制面板。
- **头部按钮 Hover 菜单**：在编辑器顶部工具栏新增 Hover 悬浮菜单，集成一键清理、层级切换等快捷操作。
- **视觉反馈增强**：为选中的贴纸添加蓝色光晕外框与动态高层级阴影，提升交互的确定感。

## [2026-04-04] - 高级极简主义大纲目录 (TOC) 组件实现

### 核心功能
- **极简设计**：在静止状态下仅显示代表标题等级的水平横线，不占用正文空间。
- **动态交互**：鼠标悬停时平滑展开，显示标题文字，伴随毛玻璃效果和贝塞尔曲线动画。
- **自动提取**：集成 Tiptap 的标题提取逻辑，自动构建 H1-H3 层级树。
- **同步高亮**：利用 `IntersectionObserver` 实现滚动时的实时位置跟踪与高亮。
- **平滑滚动**：点击目录项可平滑跳转至对应正文位置。

### 技术栈
- **React**: 组件化开发。
- **Framer Motion**: 高级补间动画与状态切换。
- **Tailwind CSS**: 基础布局与响应式样式。
- **IntersectionObserver API**: 高性能的可见性追踪。

### 视觉细节 (ui-ux-pro-max)
- 使用 `cubic-bezier(0.4, 0, 0.2, 1)` 贝塞尔曲线。
- 采用 1.5px 的精致线条和 `text-[11px]` 的极简字体。
- 实现了展开时的模糊滤镜 (`backdrop-blur`) 和文字渐入 (`opacity + blur`) 效果。

## [2026-04-06] - 修复组件输入消失问题 & 还原 Blockquote 样式

### 核心修复
- **修复组件消失**: 修复了在 CodeBlock、Sticky Note 和 Footnote 中输入时导致组件消失的 Bug。主要原因是 `NovaBlockEditor.tsx` 中的状态同步逻辑在每次按键时不断调用 `setContent`，导致 ProseMirror 销毁并重建 NodeViews。现已将同步逻辑改为仅在 `note.id` 改变时触发。
- **严格 DOM 映射**: 重构了 `CodeBlockComponent.tsx` 和 `FootnoteComponent.tsx`，使其 React `NodeViewWrapper` 和 `NodeViewContent` 严格使用 `code` 和 `span` 标签，与 Tiptap 的 `renderHTML` 架构定义完美匹配，防止 ProseMirror 丢弃“无效”的嵌套节点。
- **拖拽事件冒泡**: 在 `StickyNoteComponent.tsx` 中重写了拖拽手柄的事件处理逻辑，严格执行 `e.preventDefault()` 和 `e.stopPropagation()`，并确保 `draggable={true}` 以允许正常拖拽。

### 样式调整
- **Blockquote 还原**: 更新了 `novablock-core.css`，将 Blockquote 的样式还原为最初的设计（`font-style: italic !important;` 以及固定的段落边距），符合用户的“初始实现样式”偏好。

## [2026-04-06] - Tiptap 注脚 (Footnote) 组件重构与自动序号系统实现

### 核心功能
- **全自动序号重排**: 实现 ProseMirror 插件 `footnote-reindexer`，通过 `appendTransaction` 实时监听文档变更。无论是插入、删除还是移动注脚，所有序号都会在毫秒级内自动重新计算并同步（[1], [2], [3]...）。
- **交互状态分离**: 
  - **View Mode**: 默认仅显示蓝色的数字序号 `[n]`，保持正文排版极致整洁。
  - **Edit Mode**: 双击序号即可唤起精致的编辑气泡框，支持实时内容修改。
- **高级悬停提示 (Tooltip)**: 鼠标悬停在序号上时，显示带有 **毛玻璃背景 (`backdrop-blur`)** 和 **平滑缩放/淡入动画** 的 Tooltip，优雅呈现注脚全文。
- **内联排版优化**: 严格遵循行内元素规范，采用 `inline-flex` 布局，确保在不同字号和行高下均能完美对齐。

### 技术栈与 UI/UX 设计
- **ProseMirror Plugin**: 负责底层文档树遍历与属性原子化更新。
- **Framer Motion**: 处理 Tooltip 和编辑框的所有补间动画，采用 `easeOut` 曲线。
- **UI-UX Pro Max**: 
  - 编辑框支持 `Cmd/Ctrl + Enter` 快捷保存。
  - Tooltip 采用 `bg-white/90` 半透明设计，增加 `shadow-[0_20px_50px_rgba(0,0,0,0.15)]` 增强悬浮感。
  - 蓝色序号在悬停时具备 `scale-110` 的动态反馈。

### 热修复
- **修复加粗字体颜色与主题适配**: 重构了 `strong` / `b` 标签在 `novablock-core.css` 中的样式，使其不再被不当的全局规则继承为白色。使用了可扩展的主题语义变量（`color: var(--text-primary, #111827)`）来保证其在当前的浅色背景（如 `bg-white`）下保持清晰可读，同时也能完美向前兼容后续即将开发的深浅色/自定义主题系统。不再依赖写死的白字或强制的 `!important`。

### UI 优化
- **待办事项完成动画**: 为 Tiptap TaskList 添加了纯 CSS 的完成效果。当勾选待办事项（`[data-checked="true"]`）时，文字会带有丝滑的过渡动画（`cubic-bezier`）并显示删除线、颜色变浅和透明度降低，增强“划掉待办”的视觉反馈。

### UI 优化
- **TOC 语义化主题变量与可见性修复**: 修复了 TOC（大纲目录）在浅色背景下非悬停状态横线几乎不可见的问题。通过引入语义化 CSS 变量（`--toc-line-muted` / `--toc-line-hover` / `--toc-line-active` 等），并结合 `@media (prefers-color-scheme: dark)` 为不同模式提供合理的默认值。
  - **设计提升**: 浅色模式下，非激活状态的横线可见度从 30% 提升至 40% (rgba(120, 113, 108, 0.4))，确保在白色背景下依然清晰可辨。
  - **健壮性**: 采用 CSS 变量方案，支持未来一键切换主题或自定义背景，且改动仅局限在 TOC 容器内，不影响全局。
  - **性能**: 保持原有的 `IntersectionObserver` 逻辑，无冗余 re-render。

### 热修复
- **TOC 静默状态对比度微调**: 重新调整了浅色模式下目录横线的基准变量（从使用 `stone-500` 透明度调整为直接使用基于黑色的 `rgba(0,0,0,0.15)`），解决部分浅色背景下横线对比度依旧偏低的问题。深色模式则使用 `rgba(255,255,255,0.3)` 来确保良好的辨识度。

### 热修复
- **TOC 悬停状态恢复**: 响应用户反馈，恢复了 TOC 在【鼠标悬停展开时】的高级视觉效果（毛玻璃背板 `backdrop-blur`、投影、以及圆角背景框），确保展开后目录层级清晰且具有原先受青睐的美感。同时保留了【非悬停静默状态】下无背景的极简设定，并进一步固化了主题 token 对深浅色双模式的支持。

### 热修复
- **TOC 非悬停可见度终极调整**: 彻底去除了 TOC 的所有背景颜色（无论是悬停还是非悬停），在悬停时仅保留纯净的 `backdrop-blur(12px)` 毛玻璃滤镜。同时，大幅提升了非悬停状态下的横线不透明度（达到 `0.35`），确保在没有背景衬托的浅色环境中也能清晰辨认。

### 热修复
- **TOC 非悬停可见度终极修复**: 找到了导致 TOC 在非悬停状态下隐藏横线的底层原因——原先的组件由于内部强加的 `overflow-hidden` 和固定宽度在失去背景板后导致了元素的布局截断。我们解除了强制隐藏与冗余 `padding`，将非悬停宽度从 40px 微调到 48px，并在内层 `div` 取消了 `overflow-hidden`，确保横线能够自然展现而不被裁剪缩回。

### UI 微调
- **TOC 静默状态视觉弱化**: 听取用户对于极简美学的要求，将非活跃状态的横线透明度降至极低的 `0.12`（深色模式 `0.15`），呈现“隐隐约约”的视觉边缘存在感。当用户滚动到特定区域时，当前标题的横线高亮才会真正脱颖而出，从而在“指示”与“不打扰”之间找到了最优雅的平衡。

### 交互优化
- **侧边栏悬停展示完整标题**: 解决了侧边栏笔记标题过长被隐藏的问题。添加了浏览器原生的 `title` 属性，当鼠标悬停在被截断的标题上时，可以显示出完整的笔记名称，既保持了侧边栏的整洁，又提升了信息可读性。

## [2026-04-06] - Sticky Note (便利贴) 体验优化

### 核心功能与交互
- **光标处流式插入**: 将便利贴的默认定位从绝对定位 (`position: absolute`) 改为相对流式定位 (`position: relative` + `inline-block`)。现在通过 `/` 斜杠菜单插入便利贴时，它会完美出现在当前光标所在的文档流位置，无需再从顶部固定位置拖拽。
- **内部滚动条 (防溢出)**: 为便利贴的内容区域添加了 `max-h-[260px]` 和优雅的内部滚动条 (`overflow-y-auto custom-scrollbar`)。当输入超长文本时，便利贴本身的大小不再无限撑大，而是保持精致的卡片比例。
- **隐藏式多巴胺/马卡龙色卡**: 
  - 在便利贴右上角新增了一个悬浮呼出的调色板图标 (`Palette`)。
  - 点击即可展开带有 Framer Motion 平滑动画的色卡面板。
  - 内置 12 种精心调配的马卡龙/多巴胺配色（阳光黄、樱花粉、薄荷绿、海冻蓝、香芋紫、蜜桃橘），每种颜色均提供“纯色”与“微透 (0.6 opacity)”两种质感，并支持实时无缝切换。

## [2026-04-06] - 修复文件拖拽功能 Bug 与 Heading 稳定性增强

### 核心修复
- **修复 `ensureHeadingIds` 报错**：在 `CollapsibleHeading.tsx` 扩展中显式实现了 `ensureHeadingIds` 命令，通过遍历文档树为缺失 ID 的标题自动生成基于内容的 Safe Slug 或随机 ID，解决了 `NovaBlockEditor.tsx` 在 `onCreate` 阶段因找不到该命令导致的崩溃。
- **修复 `NodeViewWrapper` 缺失报错**：重构了 `tiptapExtensions.ts` 中的 `FilePlaceholder` 组件，将原始 `div` 渲染修改为使用 `@tiptap/react` 提供的 `NodeViewWrapper` 包裹。这符合 Tiptap React NodeView 的架构要求，消除了控制台中的 `Please use the NodeViewWrapper component` 错误。
- **修复上传接口路径与多文件支持**：
  - 修正了 `api.ts` 中 `upload` 方法的请求路径（从 `/api/upload` 更改为后端实际挂载的 `/api/media/upload`）。
  - 重构了上传逻辑，支持并发处理多文件上传，并将字段名统一为后端期望的 `file`。
  - 在 `handleFilesUpload` 中添加了详细的错误处理和用户提示（Alert），当后端未启动或连接失败（`ERR_CONNECTION_REFUSED`）时，能够自动清理无效的占位符并告知用户。

### 细节优化
- **增强 ID 生成逻辑**：标题 ID 生成现在支持中文字符过滤（Safe Slug），并具备自动冲突检测（Counter 递增），确保 TOC 锚点跳转的唯一性。
- **文件卡片元数据同步**：修复了上传完成后 `FileNode` 属性（size, type）未能正确从后端返回结果中同步的问题。
- **UI/UX 鲁棒性**：增强了上传失败时的回滚机制，确保编辑器状态在网络异常时仍能保持干净、一致。

## [2026-04-06] - 万物皆可拖拽与本地文件预览 (Universal Drag & Drop)

### 核心功能
- **智能拖拽与粘贴 (Drag & Paste)**：深度集成 Tiptap 扩展，支持从系统资源管理器直接拖入文件或从剪贴板粘贴。
- **分类自动化处理**：
  - **图片/视频/音频**：上传后自动识别 MIME 类型，分别渲染为 `ResizableImage`、`VideoNode` 或 `AudioNode`，实现即时预览。
  - **通用文件 (PDF/Word/Excel 等)**：渲染为精美的 **「文件卡片 (File Card)」**，展示图标、文件名和格式化大小。
- **上传占位加载 UX (Placeholder)**：在文件上传期间，在编辑器内插入带有**脉冲动画 (Pulse Animation)** 和进度条提示的临时卡片，上传完成后无缝替换为实际内容，确保流畅的写作节奏。
- **本地程序唤起 (Open-in-System)**：点击文件卡片时，通过后端 `open-file` API 调用操作系统默认关联程序（Windows: `os.startfile`, macOS: `open`, Linux: `xdg-open`）打开文件，实现真正的本地联动。

### 技术栈与 UI/UX 设计
- **后端 (Python/FastAPI)**：
  - 新增 `/api/system/open-file` 接口，支持绝对路径与相对上传目录的安全解析。
  - 已有 `/api/media/upload` 与静态文件挂载逻辑。
- **前端 (NovaBlock/React)**：
  - **ProseMirror Plugin**: 拦截 `drop` 和 `paste` 事件，处理 `File` 对象队列。
  - **Tailwind CSS & Lucide**: 
    - File Card 采用 **Notion/Linear 风格** 的现代极简设计：`rounded-xl` 大圆角、`shadow-sm` 微阴影。
    - 增加 Hover 时的 `scale-105` 缩放反馈与背景色微变 (`transition-all duration-200`)。
    - 支持暗色模式 (`dark:bg-stone-900`)，保持灰阶克制。

### 细节优化
- **安全性**: 限制 `open-file` 仅能访问本地已存在的文件，并优先匹配上传目录。
- **UI Pro Max**: 文件类型标签 (Type Tag) 采用全大写字母与 `tracking-wider` 间距，增强专业感。
- **交互**: 在 File Card 右侧添加 `ExternalLink` 图标，暗示点击即可在外部打开。

## [2026-04-08] - 修复后端 API 全面 404 与 SPA 拦截逻辑重构 (核心修复)

### 1. 根因分析与环境治理
- **多版本冲突修复**：发现环境中存在两套 `backend` 代码（根目录 `backend/` 与 `nova_repo/backend/`）。由于 `PYTHONPATH` 优先级问题，系统实际运行的是根目录下残缺的旧版代码，导致 `nova_repo` 中的修复始终无效。本次修复实现了两套代码的**深度同步与固化**。
- **配置属性补全**：修复了根目录 `backend/config.py` 中缺失的 `music_path` 和 `stickers_path` 属性，解决了因配置缺失导致的后端启动崩溃并退化至 SPA 拦截的问题。

### 2. 路由逻辑与静态挂载优化
- **消除 Mount 路径冲突**：将静态文件挂载路径从 `/api/media/music` 和 `/api/media/files` 迁移至 `/api/media/static/music` 和 `/api/media/static/files`。这彻底解决了 FastAPI `mount` 前缀匹配劫持 `/api/media/music-library` 等 API 路由导致的 404 遗留问题。
- **补全缺失 API 路由**：在 `backend/api/routes.py` 中手工补全了被遗漏的 `/api/media/music-library`、`/api/stickers/list` 等核心业务路由，确保所有前端功能均有对应的后端接口支撑。

### 3. SPA Fallback 安全拦截 (防止 JSON 解析报错)
- **严格 API 过滤**：重构了 `main.py` 中的 `spa` 路径拦截逻辑。现在所有以 `/api` 开头的请求，如果未匹配到具体路由，将**强制返回标准 404 JSON** (`{"detail": "API endpoint not found"}`)，而不再错误地返回 `index.html`。
- **解决 Unexpected token '<'**：这一重构从根本上杜绝了前端因收到 HTML 响应而导致的 `JSON.parse` 报错（如 `StickerPanel.tsx:29`）。

### 4. 权限与自动化
- **鉴权豁免同步**：更新了 `auth_middleware` 的豁免列表，确保 `/api/media/music-library` 和 `/api/stickers` 相关的合法请求在未配置 Token 的本地开发环境下也能正常通行。
- **实机验证**：通过内存 TestClient 模拟请求，证实 `/api/stickers/list` 和 `/api/media/music-library` 均已恢复 `200 OK` 状态并正确返回 JSON 数据。

## [2026-04-08] - 修复 StickerLayer (贴纸层) 拖拽导致的白屏报错 (TypeError: Cannot read properties of null)

### 1. 核心修复：StickerLayer.tsx 稳定性增强
- **修复 null 指针引用**：修复了在 `StickerItem` 组件的拖拽 (`mousemove`) 事件处理中，由于 `setLocalSticker` 异步状态回调执行时 `dragRef.current` 可能已在 `mouseup` 中被重置为 `null` 导致的白屏报错。
- **快照式状态访问**：在 `handleMouseMove` 开头通过 `const currentDrag = dragRef.current` 获取引用快照，并移除所有非空断言 (`!`)，确保在整个事件周期内即使 `ref` 被置空，回调逻辑依然能安全运行或静默退出。
- **防御性编程**：在 `setLocalSticker` 回调内部增加了对快照的闭包引用，彻底杜绝了 `Cannot read properties of null (reading 'initialX')` 这一类型的运行时错误。

### 2. 交互逻辑优化
- **清理逻辑加固**：确保在 `handleMouseUp` 中先完成所有必要的父组件状态同步 (`onUpdate`)，再清理 `dragRef.current` 和移除事件监听，保证了数据流的完整性。
- **响应性能**：维持了 `localSticker` 的局部状态更新策略，确保在拖拽、缩放、旋转和透明度调整时拥有极致的丝滑体验，同时避免了高频触发父组件重渲染。

### 3. 技术细节
- **React Hooks**: `useRef` + `useEffect` + `useCallback`。
- **Event Listeners**: 动态监听 `mousemove` 与 `mouseup`，并在结束后及时销毁。
- **Framer Motion**: 配合 `AnimatePresence` 处理控制面板的淡入淡出。

## [2026-04-08] - 修复 StickerItem 渲染触发 NovaBlockEditor 报错 (React 竞态修复)

### 1. 核心修复：消除跨组件更新报错 (Cannot update a component while rendering...)
- **修复状态更新器副作用**：在 `StickerLayer.tsx` 的 `StickerItem` 组件中，修复了 `onUpdate` (父组件回调) 在 `setLocalSticker` 的**状态更新函数 (updater function)** 内部被非法调用的问题。
- **逻辑解耦**：将所有导致父组件重渲染的回调函数（`onUpdate`, `onRemove`）移出 React 状态更新周期。现在这些回调仅在确定的事件处理程序（如 `handleMouseUp`）中被调用，且直接访问当前的闭包变量，确保符合 React 的纯函数状态更新规范。
- **闭包安全**：在 `handleMouseUp` 触发时，直接使用 `localSticker` 最新的值同步给父组件，消除了渲染期间产生的副作用。

### 2. 性能与稳定性优化
- **引用稳定性控制 (Memoization)**：在 `StickerLayer` 组件中，为 `handleUpdate` 和 `handleRemove` 增加了 `useCallback` 封装。这确保了在父组件 `NovaBlockEditor` 重渲染时，传递给子组件的函数引用保持稳定，防止了不必要的子组件大规模重渲染。
- **渲染链路清理**：经过全量搜索排查，确认 `StickerItem` 的所有渲染路径中不再包含任何裸露的父组件状态更新调用。

### 3. 技术栈
- **React**: `useCallback`, `useState`, `useRef`。
- **状态管理**: 局部状态 (`localSticker`) 与全局状态 (`onUpdate`) 的分阶段同步策略。

## [2026-04-08] - 贴纸系统交互体验深度升级与原生拖拽支持

### 1. 核心修复：解决贴纸“裂图”问题
- **路径解析逻辑对齐**：修复了 `StickerLayer.tsx` 中贴纸图片的 `src` 拼接逻辑。现在它能正确识别并转换以 `/api` 开头的本地路径（将其映射到 `/api/stickers/files/...`），确保贴纸从库中添加到画布后能正常显示，不再出现图片破碎。
- **一致性增强**：使贴纸图层与贴纸面板（StickerPanel）使用完全一致的 `getApiBase()` 转换逻辑。

### 2. 交互革命：实现原生拖拽添加 (Drag & Drop)
- **StickerPanel 升级**：在贴纸库的每个贴纸元素上启用了 HTML5 原生拖拽 (`draggable={true}`)。
- **数据负载传输**：在 `onDragStart` 中封装了贴纸的 JSON 元数据（URL、类型、名称），并设置了 50x50 的居中拖拽预览图，提供直观的视觉反馈。
- **精准落点放置**：
  - 在 `NovaBlockEditor.tsx` 的主滚动容器上实现了 `onDragOver` 和 `onDrop` 监听。
  - **局部坐标计算**：在 `onDrop` 时精准计算鼠标相对于编辑器容器的局部坐标 `(x, y)`，并自动减去偏移量实现“落点即中心”。
  - **流式分发**：直接触发 `add-sticky-note` 自定义事件并携带坐标参数，实现从工具栏拖出、在鼠标位置瞬间生成的丝滑闭环。

### 3. UI 交互：从“悬停”进化为“点击选中”
- **干扰消除**：将贴纸的操作菜单和控制手柄从 `onMouseEnter` 触发改为 `onClick` 选中触发。这彻底解决了拖拽鼠标路过其他贴纸时菜单乱跳、遮挡视线的痛点。
- **选中状态管理**：
  - 在 `StickerLayer` 中引入了 `selectedStickerId` 状态。
  - **自动取消选中**：实现了全局点击监听，当用户点击编辑器空白处或其他非贴纸区域时，自动清空选中状态，保持画布整洁。
  - **视觉反馈**：仅在选中状态下显示蓝色光晕外框 (`ring-2 ring-blue-400/50`)、高层级阴影及功能手柄（移动、缩放、旋转、透明度、删除）。

### 4. 技术栈
- **HTML5 Drag and Drop API**: 处理跨组件的数据传输。
- **React State & Effects**: 管理复杂的交互状态与全局点击捕获。
- **Framer Motion**: 配合 `AnimatePresence` 提供菜单弹出与消失的顺滑过渡。
- **Tailwind CSS**: 动态处理 `z-index` 与选中视觉反馈。

## [2026-04-08] - Tiptap 自定义表情包系统 (Emoticons) 前端功能实现

### 1. 自定义 Tiptap Node (`Emoticon.ts`)
- **内联渲染**：创建了继承自 `Node` 的 `Emoticon` 节点，配置为 `inline: true` 和 `group: 'inline'`。这使得表情包能像文字一样在段落中自然排版。
- **性能冻结魔法**：渲染为带有 `data-emoticon="true"` 属性的 `<img>` 标签，方便后续在列表摘要等只读场景下通过 CSS 或 Canvas 进行特定处理。
- **属性支持**：支持 `src`、`alt` 和 `title` 属性，并内置了 `1.5em` 的标准表情包尺寸样式。

### 2. 表情包选择面板 (`EmoticonPanel.tsx`)
- **微缩设计**：采用类似微信表情包的网格布局，适配 Popover 弹出显示。
- **后端联动**：集成表情包列表获取 (`GET /api/emoticons/list`)、上传 (`POST /api/emoticons/upload`) 和删除 (`DELETE /api/emoticons/files/{filename}`) 功能。
- **体验优化**：内置搜索过滤、上传进度状态提示及删除二次确认逻辑。

### 3. 编辑器集成与工具栏增强
- **Popover 集成**：在 `NovaBlockEditor.tsx` 的浮动菜单（BubbleMenu）中集成表情包按钮，使用 `Smile` 图标。
- **斜杠菜单支持**：在 `/` 命令菜单中新增“表情”选项，点击可快速唤起选择面板。
- **注册扩展**：在 `NovaBlockEditor` 的 `extensions` 数组中正式注册 `Emoticon` 扩展，使其在整个编辑器中可用。

### 4. 技术细节与安全性
- **API 基准适配**：所有图片请求和接口调用均通过 `getApiBase()` 进行动态 URL 包装，确保在内网穿透和不同部署环境下均能正常加载。
- **UI 库集成**：使用了 `@/components/ui/popover` 实现非侵入式的弹出层交互。
- **Lucide Icons**: 引入 `Smile` 图标作为表情系统的视觉入口。

---


## [2026-04-08] - 紧急修复：Vite 构建报错 (Popover 未定义) 与 UI 鲁棒性增强

### 1. 核心修复：清理非法 UI 组件引入
- **移除不存在的 Popover 导入**：修复了 `NovaBlockEditor.tsx` 中由于错误引入不存在的 `../ui/popover` 组件导致的 Vite 构建崩溃（`Failed to resolve import`）。
- **原生悬浮实现重构**：将编辑器浮动菜单（BubbleMenu）中的表情包面板（EmoticonPanel）触发逻辑从 Shadcn `Popover` 替换为基于 React 状态和 Tailwind CSS 的**原生绝对定位 `div` 实现**。
- **视觉一致性保持**：利用 `AnimatePresence` 和 `framer-motion` 还原了平滑的弹出与缩放动画（`scale-90 -> 100`），并确保 z-index 层级（`z-[120]`）正确覆盖在编辑器之上。

### 2. 项目全局清理
- **全面排查**：经全局搜索确认，项目中所有其他 `Popover` 引用（如 `PlaylistPopover.tsx`、`FootnoteComponent.tsx`）均已采用原生 `motion.div` 实现，不存在类似的非法引入隐患。

### 3. 技术栈
- **React**: 状态驱动的条件渲染。
- **Framer Motion**: 高级交互动画。
- **Tailwind CSS**: 响应式定位与阴影/背景滤镜。

---


### 1. 核心架构重构：分离“贴纸 (Stickers)”与“便利贴 (Sticky Notes)”
- **三层架构逻辑纠偏**：
  - **Layer 2 (Middle Layer / StickerLayer)**：恢复为纯装饰性的贴纸层，仅包含图片资源（SVG/PNG 等）。该层位于文字之下、背景之上，受“贴纸模式”开关控制（开启时可编辑，关闭时不可点击并带有模糊/低透明度效果）。
  - **Layer 1 (Editor Layer / Tiptap)**：核心文字编辑层。
  - **Layer 0 (Top Layer / StickyNotesLayer)**：恢复为独立的便利贴层，位于最顶层，**不受贴纸模式模糊滤镜影响**。便利贴现在被视为笔记内容的一部分，而非纯装饰。
- **数据结构独立化**：
  - 在 `types.ts` 中彻底分离 `StickerData` (仅限 image 类型) 与 `StickyNoteData` (含 HTML 内容)。
  - `Note` 对象现在拥有独立的 `stickers` 和 `sticky_notes` 属性，避免了保存时的属性覆盖和逻辑混淆。
- **交互逻辑修复**：
  - 在 `NovaBlockEditor.tsx` 中重新分发 `add-sticky-note` 事件。根据事件携带的是 `url` (贴纸) 还是 `content` (便利贴) 自动分发到对应的状态数组中。

### 2. 贴纸预置图库显示修复
- **后端静态挂载**：在 `backend/main.py` 中新增 `/api/stickers/files` 路径的静态文件挂载，确保前端能直接访问 `data/stickers/` 目录下的资源。
- **自动初始化逻辑**：在 `backend/api/routes.py` 的 `list_stickers` 接口中增加了路径自动纠偏逻辑。如果运行时 `stickers_path` 找不到预置图，会自动尝试从项目根目录的 `data/stickers` 初始化，解决了开发环境下路径不一致导致面板空白的问题。
- **前端渲染优化**：`StickerPanel.tsx` 现在能正确显示 `tape.svg`, `note.svg`, `star.svg`, `heart.svg` 等预设矢量图，并支持直接选中插入。

### 3. 技术栈
- **FastAPI**: 静态文件挂载与路径纠便逻辑。
- **React/Tiptap**: 多层级状态同步与事件分发重构。
- **CSS/Tailwind**: 修复了 `z-index` 层级冲突，确保便利贴始终在最上方可点击。




## [2026-04-08] - 修复表情面板点击无法弹出（脱离 BubbleMenu 的重构方案）

### 根因
- Tiptap `BubbleMenu` 内部存在原生 `mousedown/click` 拦截与失焦隐藏机制：当用户点击菜单内按钮时，容易触发编辑器失焦，导致 `BubbleMenu` 立刻销毁，从而把其 DOM 树内的 `<EmoticonPanel>` 一并卸载（表现为“点不出来/闪一下就没了”）。

### 修复方案（彻底脱离 BubbleMenu）
- **将挂载点抽离**：不再把 `<EmoticonPanel>` 渲染在 `<BubbleMenu>` 内部，改为在 `NovaBlockEditor` 返回结构中与 `BubbleMenu` 平级挂载。
- **固定定位兜底**：面板使用 `fixed top-1/2 left-1/2 ... z-[99999]` 居中展示，彻底摆脱 `BubbleMenu` 生命周期影响。
- **事件纪律**：表情按钮增加 `onMouseDown/onClick` 的 `e.preventDefault(); e.stopPropagation();`，避免触发 `BubbleMenu` 的隐藏/失焦链路。
