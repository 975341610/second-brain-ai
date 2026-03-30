import os

store_path = os.path.join(os.path.dirname(__file__), 'src/store/useAppStore.ts')
with open(store_path, 'r', encoding='utf-8') as f:
    code = f.read()

old_delete = """  deleteNote: async (noteId) => {
    try {
      if (noteId > 0) {
        await api.deleteNote(noteId);
      }
      
      const [backendNotes, trash] = await Promise.all([api.listNotes(), api.getTrash()]);
      
      // 简单直观：后端返回什么，前端就显示什么。
      // 后端 repositories.py:192 已经处理了递归软删除，前端不需要重复计算子树。
      // 只有对于负数 ID（尚未持久化的草稿），后端不知道它们，需要前端手动过滤。
      // 修复“删除连坐”：在合并后端数据时，必须保留本地现有的其他草稿（负数 ID）
      const localDrafts = get().notes.filter(n => n.id < 0 && n.id !== noteId);
      const finalNotes = [...localDrafts, ...backendNotes];
      
      set({ 
        notes: finalNotes, 
        trash, 
        selectedNoteId: get().selectedNoteId === noteId ? finalNotes[0]?.id ?? null : get().selectedNoteId, 
        toast: { id: Date.now(), tone: 'success', text: noteId < 0 ? '草稿已移除。' : '笔记已移入垃圾桶。' } 
      });
      setCachedData(STORE_NOTES, finalNotes);
    } catch (error) {
      set({ toast: { id: Date.now(), tone: 'error', text: `删除笔记失败：${error instanceof Error ? error.message : '请稍后重试'}` } });
    }
  },"""

new_delete = """  deleteNote: async (noteId) => {
    try {
      const getDescendantDraftIds = (parentId: number, notes: Note[]): number[] => {
        const children = notes.filter(n => n.parent_id === parentId && n.id < 0);
        let ids = children.map(c => c.id);
        for (const child of children) {
          ids = [...ids, ...getDescendantDraftIds(child.id, notes)];
        }
        return ids;
      };

      if (noteId < 0) {
        // Purely local draft deletion
        const allNotes = get().notes;
        const idsToRemove = new Set([noteId, ...getDescendantDraftIds(noteId, allNotes)]);
        
        const finalNotes = allNotes.filter(n => !idsToRemove.has(n.id));
        set({ 
          notes: finalNotes, 
          selectedNoteId: idsToRemove.has(get().selectedNoteId!) ? (finalNotes[0]?.id ?? null) : get().selectedNoteId, 
          toast: { id: Date.now(), tone: 'success', text: '草稿已移除。' } 
        });
        return;
      }

      await api.deleteNote(noteId);
      
      const [backendNotes, trash] = await Promise.all([api.listNotes(), api.getTrash()]);
      
      const allNotes = get().notes;
      const draftIdsToRemove = new Set(getDescendantDraftIds(noteId, allNotes));
      
      const localDrafts = allNotes.filter(n => n.id < 0 && n.id !== noteId && !draftIdsToRemove.has(n.id));
      const finalNotes = [...localDrafts, ...backendNotes];
      
      set({ 
        notes: finalNotes, 
        trash, 
        selectedNoteId: get().selectedNoteId === noteId ? finalNotes[0]?.id ?? null : get().selectedNoteId, 
        toast: { id: Date.now(), tone: 'success', text: '笔记已移入垃圾桶。' } 
      });
      setCachedData(STORE_NOTES, finalNotes);
    } catch (error) {
      set({ toast: { id: Date.now(), tone: 'error', text: `删除笔记失败：${error instanceof Error ? error.message : '请稍后重试'}` } });
    }
  },"""

code = code.replace(old_delete, new_delete)

with open(store_path, 'w', encoding='utf-8') as f:
    f.write(code)
print("Fixed deleteNote")
