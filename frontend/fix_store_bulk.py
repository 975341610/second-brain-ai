import os

store_path = os.path.join(os.path.dirname(__file__), 'src/store/useAppStore.ts')
with open(store_path, 'r', encoding='utf-8') as f:
    code = f.read()

old_bulk = """  bulkDeleteNotes: async () => {
    const { selectedNoteIds, notes } = get();
    if (!selectedNoteIds.length) return;
    
    set({ isDeletingNote: true });
    try {
      const realIds = selectedNoteIds.filter(id => id > 0);
      if (realIds.length > 0) {
        await api.bulkDeleteNotes(realIds);
      }
      
      const notesToFilter = new Set(selectedNoteIds);
      
      // 前端只需要过滤选中的 ID，因为后端会处理那些被选中父节点的子节点
      // 这里只需要保证前端显示的列表和选中状态一致即可
      for (const note of notes) {
        if (note.parent_id && notesToFilter.has(note.parent_id)) {
          notesToFilter.add(note.id);
        }
      }
      
      const [backendNotes, trash] = await Promise.all([api.listNotes(), api.getTrash()]);
      
      // 修复“删除连坐”：在合并后端数据时，保留未被删除的本地草稿
      const localDrafts = get().notes.filter(n => n.id < 0 && !notesToFilter.has(n.id));
      const finalNotes = [...localDrafts, ...backendNotes.filter(n => !notesToFilter.has(n.id))];
      
      set({ notes: finalNotes, trash, selectedNoteIds: [], toast: { id: Date.now(), tone: 'success', text: '已批量移入垃圾桶。' } });
      setCachedData(STORE_NOTES, finalNotes);
    } catch (error) {
      set({ toast: { id: Date.now(), tone: 'error', text: '批量删除失败' } });
    } finally {
      set({ isDeletingNote: false });
    }
  },"""

new_bulk = """  bulkDeleteNotes: async () => {
    const { selectedNoteIds, notes } = get();
    if (!selectedNoteIds.length) return;
    
    set({ isDeletingNote: true });
    try {
      const realIds = selectedNoteIds.filter(id => id > 0);
      
      const notesToFilter = new Set(selectedNoteIds);
      
      // Recursively find all descendants to delete
      let added = true;
      while (added) {
        added = false;
        for (const note of notes) {
          if (note.parent_id && notesToFilter.has(note.parent_id) && !notesToFilter.has(note.id)) {
            notesToFilter.add(note.id);
            added = true;
          }
        }
      }
      
      if (realIds.length > 0) {
        await api.bulkDeleteNotes(realIds);
        const [backendNotes, trash] = await Promise.all([api.listNotes(), api.getTrash()]);
        
        const localDrafts = get().notes.filter(n => n.id < 0 && !notesToFilter.has(n.id));
        const finalNotes = [...localDrafts, ...backendNotes];
        
        set({ notes: finalNotes, trash, selectedNoteIds: [], toast: { id: Date.now(), tone: 'success', text: '已批量移入垃圾桶。' } });
        setCachedData(STORE_NOTES, finalNotes);
      } else {
        // Only drafts were selected
        const finalNotes = notes.filter(n => !notesToFilter.has(n.id));
        set({ 
          notes: finalNotes, 
          selectedNoteIds: [], 
          toast: { id: Date.now(), tone: 'success', text: '草稿已批量移除。' } 
        });
      }
    } catch (error) {
      set({ toast: { id: Date.now(), tone: 'error', text: '批量删除失败' } });
    } finally {
      set({ isDeletingNote: false });
    }
  },"""

if old_bulk in code:
    code = code.replace(old_bulk, new_bulk)
    with open(store_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Fixed bulkDeleteNotes")
else:
    print("Could not find old_bulk")

