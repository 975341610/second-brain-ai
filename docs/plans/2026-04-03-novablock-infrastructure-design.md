# NovaBlock (星核笔记) Infrastructure Design - Phase 1

## 1. Project Overview
NovaBlock is a local-first, zero-latency knowledge operating system. It features a block-based editor, infinite tree structure, canvas mode, and a plugin ecosystem compatible with Obsidian/Typora.

## 2. Technical Stack
- **Framework**: Electron + React + TypeScript
- **Bundler**: Vite (via electron-vite)
- **Styling**: TailwindCSS + Framer Motion
- **State Management**: Zustand (Global) + Yjs (Document CRDT)
- **Editor Engine**: Tiptap (Prosemirror-based)
- **Database**: Better-SQLite3 (Local metadata/indexing)
- **Testing**:
  - **Unit/Integration**: Vitest
  - **E2E**: Playwright
- **Storage**: Local Markdown files (SSOT)

## 3. Architecture Design
### 3.1 Process Separation
- **Main Process**: File system access (Node.js), window management, SQLite interaction, system tray.
- **Preload Process**: Secure IPC bridge using `contextBridge`.
- **Renderer Process**: React UI, Tiptap editor, Canvas engine.

### 3.2 File System SSOT (Single Source of Truth)
- All notes are stored as `.md` files in a user-defined "Vault" directory.
- `FSWatcher` (chokidar) in the Main process monitors changes and pushes updates to the Renderer via IPC.
- SQLite stores a shadow index (ID, title, tags, task status) for fast global search and relationship mapping.

### 3.3 Block Editor Concept
- Each note is a Tiptap document.
- Custom Tiptap Extensions will handle "Block" behavior:
  - Drag-and-drop handles.
  - Slash menu commands.
  - Embedded widgets (Task cards, Video, PDF).

## 4. Phase 1 Implementation Plan
### Task 1: Scaffolding & Testing Setup
- Reorganize directory structure.
- Configure Vitest for `frontend` and `src`.
- Configure Playwright for Electron E2E.
- Implement a "Hello World" test to verify the pipeline.

### Task 2: Core IPC & FSBridge
- Implement `FSBridge` in Main process for high-speed I/O.
- Expose `window.novablock.fs` to Renderer.
- TDD: Write tests for file reading/writing before implementation.

### Task 3: Base Editor Shell
- Initialize Tiptap with `StarterKit`.
- Implement a basic file explorer linked to a local directory.

## 5. Directory Structure
```text
novablock/
├── src/
│   ├── main/           # Electron Main process
│   │   ├── services/   # FS, SQLite, AI Sidecar
│   │   └── index.ts
│   ├── preload/        # Preload scripts
│   └── renderer/       # React Frontend
│       ├── src/
│       │   ├── components/ # Atomic components
│       │   ├── editor/     # Tiptap setup
│       │   ├── store/      # Zustand
│       │   └── views/      # Page layouts
├── tests/
│   ├── unit/
│   └── e2e/
├── package.json
└── vitest.config.ts
```
