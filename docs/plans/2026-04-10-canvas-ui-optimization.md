# Canvas UI/UX Optimization Implementation Plan

Goal: Optimize the canvas interface with a dark theme, collapsible toolbars, icon-only buttons with tooltips, and customizable background image persistence.

## Task 1: Update Types and Persistence Logic
**Files:**
- Modify: `nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Update `CanvasSerialized` type to include `backgroundUrl`.
**Step 2:** Update `parseCanvasContent` to extract `backgroundUrl`.
**Step 3:** Add `backgroundUrl` state to `CanvasBoard`.
**Step 4:** Initialize `backgroundUrl` from the parsed note content.
**Step 5:** Update `saveSnapshot` to include the current `backgroundUrl`.

## Task 2: Implement Background UI and Styles
**Files:**
- Modify: `nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Add a hidden file input for background upload.
**Step 2:** Implement `handleBackgroundUpload` using `api.upload`.
**Step 3:** Update the main container styles to a dark theme (`#121212` or `bg-slate-900`) and apply `backgroundImage` from `backgroundUrl`.
**Step 4:** Remove old background effects (radial gradients, paper texture).
**Step 5:** Update the `Background` (grid/dots) component for the dark theme.

## Task 3: Optimize Top Navigation Bar
**Files:**
- Modify: `nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Add `isNavCollapsed` state.
**Step 2:** Refactor `Panel position="top-center"`:
  - Add a collapse/expand toggle button.
  - Convert "Add Text Card" and "Reference Note" buttons to icon-only with tooltips.
  - Add "Change Background" icon button.
  - Apply a compact, dark-friendly design to the toolbar.
**Step 3:** (Optional) Refactor `Panel position="top-left"` to be more compact or collapsible.

## Task 4: Final Cleanups
**Files:**
- Modify: `nova-block/src/components/canvas/CanvasEditor.tsx`

**Step 1:** Remove the "Delete Selected" button at the bottom right.
**Step 2:** Ensure all text/icons in panels are visible against the new dark background.

## Task 5: Build and Verify
**Steps:**
1. Run `npm run build` in `nova-block`.
2. Copy output to `frontend_dist`.
3. Update `DEVELOPMENT_LOG.md`.
4. Commit changes.
