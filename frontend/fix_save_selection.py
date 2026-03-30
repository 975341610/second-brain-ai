import os

store_path = os.path.join(os.path.dirname(__file__), 'src/store/useAppStore.ts')
with open(store_path, 'r', encoding='utf-8') as f:
    code = f.read()

old_selection = """      const currentSelectedId = get().selectedNoteId;
      // 只有在当前选中的正是被保存的笔记，或者是草稿转正时，才更新选中 ID
      const shouldUpdateSelection = (currentSelectedId === id) || isDraft;"""

new_selection = """      const currentSelectedId = get().selectedNoteId;
      // 必须严格判断当前选中的是不是刚刚正在保存的这个草稿！如果是，才更新它的选中状态为正式 ID。
      // 如果用户已经切走，绝不能强行把用户拉回来！
      const shouldUpdateSelection = currentSelectedId === id;"""

if old_selection in code:
    code = code.replace(old_selection, new_selection)
    with open(store_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Fixed selection bug in saveNote")
else:
    print("Could not find old_selection in saveNote")
