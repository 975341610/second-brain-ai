with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace editor.chain().focus().insertContent with editor.commands.insertContent in case chain causes issues
# Or better, just fix the type since Image node expects specific attributes or format
old_code = """      // 在当前光标位置插入像素女仆动图加载占位
      editor.chain().focus().insertContent({
        type: 'image',
        attrs: {
          src: pixelMaidUrl,
          width: 80,
          height: 80,
          alt: 'AI Thinking...',
          'data-loading-placeholder': 'true' // 用于后续查找并移除
        }
      }).run();"""

new_code = """      // 在当前光标位置插入像素女仆动图加载占位
      try {
        editor.commands.insertContent(`<img src="${pixelMaidUrl}" width="80" height="80" alt="AI Thinking..." data-loading-placeholder="true" />`);
      } catch(e) {
        console.error('Failed to insert AI placeholder:', e);
      }"""

content = content.replace(old_code, new_code)

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched insert content!")
