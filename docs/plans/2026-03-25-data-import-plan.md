# Data Import Implementation Plan
> **For agent:** REQUIRED SUB-SKILL: Use Section 4 or Section 5 to implement this plan.
**Goal:** Implement a data import feature with a backend API and frontend UI to overwrite current data with data from a source directory.
**Architecture:** Add a `POST /api/system/import-data` endpoint to `backend/api/routes.py` and update `frontend/src/components/SettingsPanel.tsx` with an import area and warning dialog.
**Tech Stack:** Python, FastAPI, SQLAlchemy, React, Tailwind CSS.

### Task 1: Create Backend API Test (RED)
**Files:**
- Create: `backend/api/import_data_test.py`
**Step 1:** Write failing test for `POST /api/system/import-data`.
- Test success case: valid `source_path` with `second_brain.db`.
- Test failure cases: invalid `source_path`, missing `second_brain.db`.
**Step 2:** Run test, verify fails.
```bash
pytest backend/api/import_data_test.py
```
Expected output: 404 Not Found (endpoint not created yet).

### Task 2: Implement Backend API (GREEN)
**Files:**
- Modify: `backend/api/routes.py`
**Step 1:** Implement the `import_data` endpoint logic.
- Verify `source_path` and `second_brain.db`.
- Call `engine.dispose()`.
- Use `shutil.copy2` and `shutil.copytree` to copy data.
**Step 2:** Run tests from Task 1, verify passes.
```bash
pytest backend/api/import_data_test.py
```
Expected output: 3 passed.
**Step 3:** Commit.
```bash
git add backend/api/routes.py
git commit -m "feat: add import-data backend API"
```

### Task 3: Update Frontend API Client
**Files:**
- Modify: `frontend/src/lib/api.ts`
**Step 1:** Add `importData` method to `api` object.
```typescript
importData: (sourcePath: string) => request<{ status: string; message: string }>('/system/import-data', {
  method: 'POST',
  body: JSON.stringify({ source_path: sourcePath }),
}),
```
**Step 2:** Commit.
```bash
git add frontend/src/lib/api.ts
git commit -m "feat: add importData to frontend API client"
```

### Task 4: Implement Frontend UI (GREEN)
**Files:**
- Modify: `frontend/src/components/SettingsPanel.tsx`
**Step 1:** Add "Data Import" area and button.
- Include a high-risk warning.
- Implement the click handler with confirmation and success/error alerts.
**Step 2:** Manually verify UI layout (no automated tests for UI in this task).
**Step 3:** Commit.
```bash
git add frontend/src/components/SettingsPanel.tsx
git commit -m "feat: add data import section to SettingsPanel"
```

### Task 5: Final Verification
**Step 1:** Run all tests in the project.
```bash
pytest backend/
```
**Step 2:** Perform a manual integration test if possible (or confirm with user).
**Step 3:** Commit any final fixes.
