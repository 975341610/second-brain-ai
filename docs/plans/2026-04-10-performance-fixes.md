# Performance Audit & Fix Implementation Plan

## 1. FastAPI Blocking Event Loop Fix
**Problem**: `async def` routes in `backend/api/routes.py` performing synchronous SQLAlchemy operations block the main event loop.
**Fix**: Convert these routes to regular `def` so FastAPI executes them in a thread pool.

## 2. Large Data Transfer Optimization
**Problem**: `GET /notes` and `GET /notes/tree` return the full `content` of all notes, causing excessive memory and network usage.
**Fix**: 
- Update `NoteResponse` to make `content` optional.
- Modify `list_notes` and `list_notes_tree` to exclude `content`.
- Add `GET /notes/{note_id}` for on-demand content loading.
- Update frontend `api.ts` and `App.tsx` to support lazy loading.

## 3. Base64 Media Storage Cleanup
**Problem**: `MoodboardView.tsx` and `HabitTrackerComponent.tsx` store media as Base64 in state/DB.
**Fix**: Replace `readAsDataURL` with `api.upload` and store URLs instead.

## 4. Frontend Persistence & Rendering
**Problem**: High-frequency `localStorage` writes in `App.tsx`.
**Fix**: Add debouncing to the `localStorage` sync logic.

---

### Implementation Details

#### Task 1: Backend Route Fixes
- File: `backend/api/routes.py`
- Change `async def` -> `def` for:
    - `quick_capture_api`
    - `upload_documents`
    - `create_folder_api`
    - `create_note_api`
    - `update_note_api`
    - `ask_question`
    - `search_api`
    - `inline_ai`
    - `global_chat`
    - `suggest_tags`
- For routes using `ai_client` (async), use `asyncio.run` or `loop.run_until_complete`.

#### Task 2: Data Optimization
- File: `backend/models/schemas.py`: `NoteResponse` -> `content: str | None = None`
- File: `backend/services/repositories.py`: 
    - Add `from sqlalchemy.orm import defer`
    - `list_notes` -> `select(Note).options(defer(Note.content))`
    - `list_notes_tree` -> `select(Note).options(defer(Note.content))`
- File: `backend/api/routes.py`: Add `get_note_api(note_id: int, db: Session = Depends(get_db))` returning `NoteResponse`.

#### Task 3: Base64 Removal
- File: `nova-block/src/components/moodboard/MoodboardView.tsx`: Use `api.upload` in `handleDrop`.
- File: `nova-block/src/components/widgets/HabitTrackerComponent.tsx`: Remove Base64 fallback in `onChange`.

#### Task 4: Frontend Lazy Loading & Debounce
- File: `nova-block/src/App.tsx`: 
    - Debounce `localStorage.setItem('nova-block-notes', ...)`
    - Add logic to fetch content if `currentNote.content` is missing.
