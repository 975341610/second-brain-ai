# BGM 播放器与启动页状态机设计方案

## 1. BGM 播放器骨架

### 1.1 后端逻辑 (Python/FastAPI)
- **目标**：提供音频文件索引和流式读取。
- **功能点**：
    - `GET /api/bgm/list`：扫描 `data/bgm` 目录下的音频文件（mp3, wav），返回列表。
    - `GET /api/bgm/stream/{filename}`：流式返回音频文件内容。
- **存储**：默认使用 `second-brain-ai/data/bgm` 作为存放路径。

### 1.2 前端逻辑 (React/Zustand)
- **目标**：实现一个简洁的音频控制面板。
- **功能点**：
    - 状态管理：集成到 `useAppStore`，管理 `isPlaying`, `volume`, `currentTrack`, `tracks` 等状态。
    - UI 组件：`BGMPlayer.tsx` 包含播放/暂停按钮、音量滑动条、曲目选择（或下一首）。
    - 自动索引：应用启动后自动拉取列表并随机/顺序播放。

## 2. 启动页 (SplashScreen) 状态机

### 2.1 状态定义
我们将替换现有的白屏/简单加载，定义如下状态：
1. `INIT` (初始化)
2. `LOADING_BACKEND` (检查/连接后端服务)
3. `LOADING_FRONTEND` (加载本地数据、配置、资源)
4. `READY` (进入主界面)
5. `ERROR` (加载失败，显示重试/诊断信息)

### 2.2 实现策略
- **SplashScreen 组件**：全屏覆盖，展示进度条和当前状态文案。
- **状态机控制**：在 `App.tsx` 中引入 `appStatus` 状态。
- **流程流转**：
    - `useEffect` 触发加载链。
    - 检查后端 API 可用性。
    - 调用 `loadInitialData` 并等待完成。
    - 全部完成后设置 `READY`，淡出 SplashScreen。

## 3. TDD 开发流程
1. **后端测试**：编写 `routes_test.py` 验证 BGM 接口。
2. **后端代码**：实现 BGM 路由。
3. **前端测试**：编写 `useAppStore.test.ts` 验证状态机和 BGM 逻辑。
4. **前端代码**：实现 `SplashScreen` 和 `BGMPlayer` 组件。
