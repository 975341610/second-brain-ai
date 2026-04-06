# Data Import Feature Design

## Goal
Implement a data import feature that allows users to overwrite their current data (database, chroma store, uploads) with data from a source directory.

## Architecture
The feature consists of a backend API endpoint and a frontend UI component.

### Backend API
- **Endpoint**: `POST /api/system/import-data`
- **Payload**: `{"source_path": str}`
- **Logic**:
  1. Validate that `source_path` is a valid directory.
  2. Verify that `source_path / "second_brain.db"` exists.
  3. Release the current database connection using `engine.dispose()`.
  4. Copy (overwrite) the following from `source_path` to `settings.data_root`:
     - `second_brain.db`
     - `chroma_store/`
     - `uploads/`
     - `sample_docs/` (if present)
  5. Use `shutil.copy2` for files and `shutil.copytree` (with `dirs_exist_ok=True`) for directories.
  6. Catch and handle `OSError`, `PermissionError`, and other potential issues.
  7. Return a success response.

### Frontend UI
- **Location**: `SettingsPanel.tsx`, within the "Data Storage" or a new "Data Management" section.
- **Components**:
  - Label: "Import Data from Local Directory"
  - Input: Text field for `source_path`.
  - Button: "Import Data".
- **Interaction**:
  1. When "Import Data" is clicked, show a `window.confirm` or a custom modal with a warning:
     - "Warning: This operation will irreversibly overwrite all your current data! Are you sure you want to proceed?"
  2. If confirmed, call `api.importData(sourcePath)`.
  3. On success:
     - Show a success alert: "Data import successful! Please completely close and restart the software to apply changes."
  4. On failure:
     - Show an error alert with the message.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, Python `shutil` and `pathlib`.
- **Frontend**: React, Tailwind CSS, Lucide icons.

## Error Handling
- Invalid source path -> 400 Bad Request.
- Missing `second_brain.db` -> 400 Bad Request.
- File lock/Permission errors -> 500 Internal Server Error with descriptive message.

## Testing Strategy (TDD)
1. **RED**: Create `backend/api/import_data_test.py`. Define tests for success and failure cases. Run and see them fail.
2. **GREEN**: Implement the endpoint in `backend/api/routes.py`.
3. **VERIFY**: Run tests and confirm they pass.
4. **UI**: Manually verify the frontend changes.
