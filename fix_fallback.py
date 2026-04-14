with open("nova_repo/backend/api/routes.py", "r") as f:
    content = f.read()

old_fallback = """                else:
                    # 如果插件开启但出错或未就绪，则回退到原始 AI
                    pass"""

new_fallback = """                else:
                    if status.get("error"):
                        import json
                        yield f'data: {json.dumps({"error": f"Local AI Error: {status['error']}. Please check your model file or disable Local AI."})}\\n\\n'
                        return
                    pass"""

content = content.replace(old_fallback, new_fallback)

with open("nova_repo/backend/api/routes.py", "w") as f:
    f.write(content)
