
// 模拟 useAppStore.ts 的 saveNote 逻辑
function testSaveNoteMerge() {
    let notes = [
        { id: 101, title: '旧笔记1', parent_id: null },
        { id: 102, title: '旧笔记2', parent_id: null },
        { id: -12345, title: '未命名笔记', parent_id: null, is_draft: true } // 这是一个正在保存的草稿
    ];

    const draftId = -12345;
    const backendReturnedNote = { id: 101, title: '新笔记(转正)', parent_id: null }; // 假设后端返回了一个已存在的 ID

    console.log("原始状态:", JSON.stringify(notes, null, 2));

    // 模拟 saveNote 内部逻辑
    const id = draftId;
    const note = backendReturnedNote;
    const isDraft = true;

    const currentNotes = notes;
    const withoutOriginal = typeof id === 'number' ? currentNotes.filter((item) => item.id !== id) : currentNotes;
    
    // 更新所有子笔记的 parent_id
    const updatedNotesWithParentUpdate = isDraft && typeof id === 'number'
      ? withoutOriginal.map(n => n.parent_id === id ? { ...n, parent_id: note.id } : n)
      : withoutOriginal;

    const hasTarget = updatedNotesWithParentUpdate.some((item) => item.id === note.id);
    const finalNotes = hasTarget
      ? updatedNotesWithParentUpdate.map((item) => (item.id === note.id ? note : item))
      : [note, ...updatedNotesWithParentUpdate];

    console.log("合并后状态:", JSON.stringify(finalNotes, null, 2));
    
    const lostNote = finalNotes.find(n => n.id === 101 && n.title === '旧笔记1');
    if (!lostNote && hasTarget) {
        console.error("!!! 发现 BUG: 旧笔记 101 被新笔记覆盖了!");
    } else {
        console.log("未发现覆盖。");
    }
}

testSaveNoteMerge();
