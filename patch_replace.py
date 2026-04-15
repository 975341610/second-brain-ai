with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the cleanup part too, it was likely searching for resizableImage or image object format
old_cleanup_1 = """            if (isFirstToken) {
              isFirstToken = false;
              const tr = editor.state.tr;
              let foundPos = -1;
              tr.doc.descendants((node, pos) => {
                if (node.type.name === 'image' && node.attrs['data-loading-placeholder'] === 'true') {
                  foundPos = pos;
                  return false;
                }
              });
              if (foundPos !== -1) {
                // Delete the placeholder
                tr.delete(foundPos, foundPos + 1);
                editor.view.dispatch(tr);
              }
            }"""

new_cleanup_1 = """            if (isFirstToken) {
              isFirstToken = false;
              const tr = editor.state.tr;
              let foundPos = -1;
              tr.doc.descendants((node, pos) => {
                if (node.type.name === 'image' && node.attrs.src === pixelMaidUrl) {
                  foundPos = pos;
                  return false;
                }
              });
              if (foundPos !== -1) {
                tr.delete(foundPos, foundPos + 1);
                editor.view.dispatch(tr);
              }
            }"""

content = content.replace(old_cleanup_1, new_cleanup_1)

old_cleanup_2 = """        // 清理可能残留的占位符
        let foundPos = -1;
        tr.doc.descendants((node, pos) => {
          if (node.type.name === 'image' && node.attrs['data-loading-placeholder'] === 'true') {
            foundPos = pos;
            return false;
          }
        });
        if (foundPos !== -1) {
          tr.delete(foundPos, foundPos + 1);
          editor.view.dispatch(tr);
        }"""

new_cleanup_2 = """        // 清理可能残留的占位符
        let foundPos = -1;
        tr.doc.descendants((node, pos) => {
          if (node.type.name === 'image' && node.attrs.src === pixelMaidUrl) {
            foundPos = pos;
            return false;
          }
        });
        if (foundPos !== -1) {
          tr.delete(foundPos, foundPos + 1);
          editor.view.dispatch(tr);
        }"""

content = content.replace(old_cleanup_2, new_cleanup_2)

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched cleanup!")
