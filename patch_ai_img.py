with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace resizableImage with image since that's what Tiptap Extension exports it as under the hood for schema naming
content = content.replace("type: 'resizableImage',", "type: 'image',")
content = content.replace("node.type.name === 'resizableImage'", "node.type.name === 'image'")

with open('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/novablock/NovaBlockEditor.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Patched node type successfully!")
