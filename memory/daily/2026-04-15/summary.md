
## 11:25:17
- 用户要求将 Nova 项目版本升级至 0.17，并撰写完整的中文更新说明。
- 将 `package.json`、`frontend`、`nova-block` 及 `backend/ipc_bridge.py` 等 5 处文件中的版本号统一更新为 `0.17.0`，在项目根目录生成 `RELEASE_NOTES_0.17.md`，并将改动记录至 `DEVELOPMENT_LOG.md`。
- 用户要求将代码推送到 `main` 分支，并在设置中新增对 Slash 菜单、文字菜单和块菜单的透明度、色彩（背景色/前景色/边框色）及毛玻璃模糊度的自定义调节功能。
- 新增主题配置（JSON）的导入与导出功能，创建了 `ThemeConfig` 类型及 `themeUtils.ts`（包含校验、应用 CSS 变量及持久化逻辑），在 `SettingsDialog.tsx` 中新增“主题管理”标签页，并补充了测试用例 `src/test/theme-config.test.ts`。
- 用户反馈云端构建失败，出现 Vite/Oxc 解析报错（`SettingsDialog.tsx` 第 387 行提示 `Expected } but found :`）。
- 修复了 `SettingsDialog.tsx` 中 `activeTab` 三元表达式渲染链的解析错误（明确为 `activeTab === 'dictionary'` 并修正闭合兜底逻辑）；修复了 TS 编译报错，将 `ThemeConfig` 引入方式改为 `import type`；跑通了 `nova-block` 构建。
- 用户指出设置中关于“菜单面板外观调节”的具体功能并未实际实现。
- 确认当前代码仅完成了数据层（配置持久化及导入导出），缺失实际的 UI 调节控件（如滑块、颜色选择器）以及对应的组件 CSS 变量绑定。提出了补齐控制面板和实际样式接入的修复计划以待用户确认。
