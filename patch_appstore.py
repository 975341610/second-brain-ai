import re

with open('second-brain-ai/frontend/src/store/useAppStore.ts', 'r') as f:
    content = f.read()

# Replace the createDraftNote implementation to be async and call the real API immediately
new_createDraftNote = """
  createDraftNote: async (notebookId, parentId, title, content, icon) => {
    const targetNotebookId = notebookId ?? get().notebooks[0]?.id ?? null;
    const initialTitle = title ?? '未命名笔记';
    const initialContent = content ?? '<h1>新建笔记</h1><p>从这里开始记录你的想法。</p>';
    
    try {
        const newNote = await api.createNote({
            title: initialTitle,
            content: initialContent,
            notebook_id: targetNotebookId,
            parent_id: parentId,
            icon: icon ?? '📝'
        });
        
        const [notes] = await Promise.all([api.listNotes()]);
        set({
            notes,
            selectedNoteId: newNote.id,
            recentNoteIds: [newNote.id, ...get().recentNoteIds.filter((id) => id !== newNote.id)].slice(0, 8),
            toast: { id: Date.now(), tone: 'success', text: '已创建新笔记。' }
        });
    } catch (error) {
        set({ toast: { id: Date.now(), tone: 'error', text: `创建笔记失败：${error instanceof Error ? error.message : '请稍后重试'}` } });
    }
  },
"""

content = re.sub(
    r'createDraftNote:\s*\([^)]*\)\s*=>\s*\{.*?(?=saveNote:)', 
    new_createDraftNote, 
    content, 
    flags=re.DOTALL
)

# Fix the signature in the interface definition
content = re.sub(
    r'createDraftNote:\s*\(notebookId\?:.*?\) => void;',
    r'createDraftNote: (notebookId?: number | null, parentId?: number | null, title?: string, content?: string, icon?: string) => Promise<void>;',
    content
)

with open('second-brain-ai/frontend/src/store/useAppStore.ts', 'w') as f:
    f.write(content)
