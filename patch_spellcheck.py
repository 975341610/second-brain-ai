import re

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/extensions/AISpellcheck.ts', 'r', encoding='utf-8') as f:
    content = f.read()

old_apply = """            if (action && action.type === 'removeError') {
              const { from, to } = action;
              // Filter out the error from storage
              storage.errors = storage.errors.filter((e: any) => e.from !== from || e.to !== to);
              // Remove the specific decoration
              const decos = oldSet.find(from, to);
              let newSet = oldSet.remove(decos);
              return newSet.map(tr.mapping, tr.doc);
            }"""

new_apply = """            if (action && action.type === 'removeError') {
              // Completely clear the error state immediately when fixed
              storage.errors = [];
              return DecorationSet.empty;
            }"""

content = content.replace(old_apply, new_apply)

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/extensions/AISpellcheck.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("AISpellcheck patched!")
