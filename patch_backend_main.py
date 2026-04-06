import re

with open('second-brain-ai/backend/main.py', 'r') as f:
    content = f.read()

protective_delete = """
@app.delete("/api/notes/{note_id}", response_model=dict)
def delete_note(note_id: int):
    if note_id < 0:
        return {"status": "success", "message": "Ignored negative draft ID"}
    success = db.soft_delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"status": "success"}
"""

# Replace the existing delete_note route
content = re.sub(
    r'@app\.delete\("/api/notes/\{note_id\}"[^)]*\)\s*def delete_note\(note_id: int\):\s*success = db\.soft_delete_note\(note_id\)\s*if not success:\s*raise HTTPException\(status_code=404, detail="Note not found"\)\s*return \{"status": "success"\}',
    protective_delete,
    content
)

with open('second-brain-ai/backend/main.py', 'w') as f:
    f.write(content)
