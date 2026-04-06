import re

with open('second-brain-ai/backend/routers/notes.py', 'r') as f:
    content = f.read()

# Add a protective hook to DELETE method to just return 200 on negative IDs
protective_delete = """
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int, current_user=Depends(get_current_user)):
    if note_id < 0:
        return # Ignore negative IDs from frontend sync bugs
    return repositories.soft_delete_note(note_id, current_user.id)
"""

content = re.sub(
    r'@router\.delete\("/\{note_id\}"[^)]*\)\s*async def delete_note\(note_id: int, current_user=Depends\(get_current_user\)\):\s*return repositories\.soft_delete_note\(note_id, current_user\.id\)',
    protective_delete,
    content
)

with open('second-brain-ai/backend/routers/notes.py', 'w') as f:
    f.write(content)
