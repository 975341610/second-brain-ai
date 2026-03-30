import os

store_path = os.path.join(os.path.dirname(__file__), 'src/store/useAppStore.ts')
with open(store_path, 'r', encoding='utf-8') as f:
    code = f.read()

old_bulk = """  bulkDeleteNotes: async () => {
    const noteIds = get().selectedNoteIds;
    if (noteIds.length === 0) return;
    try {
      const notesToFilter = new Set<number>(noteIds);
      const findChildren = (pids: number[]) => {
        const nextPids: number[] = [];
        get().notes.forEach(n => {
          if (n.parent_id && pids.includes(n.parent_id) && !notesToFilter.has(n.id)) {
            notesToFilter.add(n.id);
            nextPids.push(n.id);
          }
        });
        if (nextPids.length > 0) findChildren(nextPids);
      };
      findChildren(noteIds);

      const realNoteIds = noteIds.filter(id => id > 0);
      
      if (realNoteIds.length > 0) {
        await api.bulkDeleteNotes({ note_ids: realNoteIds });
      }
      
      const [backendNotes, trash] = await Promise.all([api.listNotes(), api.getTrash()]);
      
      // 修复“删除连坐”：在合并后端数据时，保留未被删除的本地草稿
      const localDrafts = get().notes.filter(n => n.id < 0 && !notesToFilter.has(n.id));
      const finalNotes = [...localDrafts, ...backendNotes.filter(n => !notesToFilter.has(n.id))];
      
      set({ notes: finalNotes, trash, selectedNoteIds: [], toast: { id: Date.now(), tone: 'success', text: '已批量移入垃圾桶。' } });
      setCachedData(STORE_NOTES, finalNotes);
    } catch (error) {
      set({ toast: { id: Date.now(), tone: 'error', text: `批量删除失败：${error instanceof Error ? error.message : '请稍后重试'}` } });
    }
  },"""

new_bulk = """  bulkDeleteNotes: async () => {
    const noteIds = get().selectedNoteIds;
    if (noteIds.length === 0) return;
    try {
      const notesToFilter = new Set<number>(noteIds);
      const findChildren = (pids: number[]) => {
        const nextPids: number[] = [];
        get().notes.forEach(n => {
          if (n.parent_id && pids.includes(n.parent_id) && !notesToFilter.has(n.id)) {
            notesToFilter.add(n.id);
            nextPids.push(n.id);
          }
        });
        if (nextPids.length > 0) findChildren(nextPids);
      };
      findChildren(noteIds);

      const realNoteIds = noteIds.filter(id => id > 0);
      
      if (realNoteIds.length > 0) {
        await api.bulkDeleteNotes({ note_ids: realNoteIds });
        const [backendNotes, trash] = await Promise.all([api.listNotes(), api.getTrash()]);
        const localDrafts = get().notes.filter(n => n.id < 0 && !notesToFilter.has(n.id));
        const finalNotes = [...localDrafts, ...backendNotes.filter(n => !notesToFilter.has(n.id))];
        
        set({ notes: finalNotes, trash, selectedNoteIds: [], toast: { id: Date.now(), tone: 'success', text: '已批量移入垃圾桶。' } });
        setCachedData(STORE_NOTES, finalNotes);
      } else {
        const finalNotes = get().notes.filter(n => !notesToFilter.has(n.id));
        set({ notes: finalNotes, selectedNoteIds: [], toast: { id: Date.now(), tone: 'success', text: '草稿已批量移除。' } });
      }
    } catch (error) {
      set({ toast: { id: Date.now(), tone: 'error', text: `批量删除失败：${error instanceof Error ? error.message : '请稍后重试'}` } });
    }
  },"""

if old_bulk in code:
    code = code.replace(old_bulk, new_bulk)
    with open(store_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Fixed bulkDeleteNotes")
else:
    print("Could not find old_bulk")
