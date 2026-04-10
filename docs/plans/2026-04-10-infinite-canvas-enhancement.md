# Infinite Canvas Implementation Plan

**Goal:** Implement advanced "Infinite Canvas" features in `nova_repo/nova-block` using `@xyflow/react`.
**Architecture:** Use a `BaseNode` wrapper for common node features, a custom `groupNode` for grouping, and a global `onDrop` handler for versatile uploads.
**Tech Stack:** React, @xyflow/react, Framer Motion, Tailwind CSS, Lucide React.

## Tasks

### Task 1: Create BaseNode Wrapper and update existing nodes
**Files:**
- Create: `nova_repo/nova-block/src/components/canvas/BaseNode.tsx`
- Modify: `nova_repo/nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Implement `BaseNode` component. It should:
- Take `children`, `id`, `selected`, `type`, `data` as props.
- Render 4 `Handle` components (Top, Right, Bottom, Left).
- Render an `Info` icon (Lucide) that calls a prop `onInfoClick`.
- Render `NodeResizer` (visible when selected).
- Add styles to show handles on hover/selection.

**Step 2:** Update `CanvasBoard` in `CanvasEditor.tsx` to include `BaseNode` in node definitions or use it within `TextCardNode` and `ReferenceCardNode`.

### Task 2: Advanced Selection and Panning Experience
**Files:**
- Modify: `nova_repo/nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Change `ReactFlow` props:
- `panOnDrag={false}`
- `selectionOnDrag={true}`
- `panOnScroll={true}`
- `selectionMode="partial"` (optional, for partial selection)
- Enable panning via middle/right click using `panOnDrag={[1, 2]}` (Middle=1, Right=2).

### Task 3: Grouping System
**Files:**
- Modify: `nova_repo/nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Define `groupNode` type and its component.
**Step 2:** Implement a floating `SelectionToolbar` that appears when `selection.nodes.length >= 2`.
**Step 3:** Implement `handleGroupSelection` logic:
- Calculate bounds of selected nodes.
- Create a new node of type `groupNode`.
- Move selected nodes inside it (set `parentId`, calculate relative `position`).

### Task 4: Memo Drawer (Info Panel)
**Files:**
- Modify: `nova_repo/nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Add `memoOpenId` state to `CanvasBoard`.
**Step 2:** Implement `MemoDrawer` component using `framer-motion`.
**Step 3:** Bind `data.memo` to a textarea in the drawer with bi-directional update logic.

### Task 4: Universal Drag-and-Drop
**Files:**
- Modify: `nova_repo/nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Enhance `handleCanvasDrop` to handle:
- `event.dataTransfer.files`: call `api.upload`, then create nodes based on file type.
- `event.dataTransfer.getData('text/plain')`: check if it's a URL, if so, create `linkNode`.
**Step 2:** Ensure nodes are placed at the correct flow position using `screenToFlowPosition`.

### Task 5: Context Menu Positioning Fix
**Files:**
- Modify: `nova_repo/nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Use `screenToFlowPosition` or appropriate bounding client rect mapping to ensure the context menu doesn't offset when the canvas is zoomed/panned.

### Task 6: Final Verification & Commit
**Step 1:** Verify all features manually (as much as possible in this environment).
**Step 2:** Update `DEVELOPMENT_LOG.md` in Chinese.
**Step 3:** Local commit with Chinese message.
