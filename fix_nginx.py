import re

with open("nova_repo/backend/api/routes.py", "r") as f:
    content = f.read()

# Make sure X-Accel-Buffering is explicitly no
old_headers = """                media_type="text/event-stream",
                headers={
                    "X-Accel-Buffering": "no",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "text/event-stream"
                }"""

new_headers = """                media_type="text/event-stream",
                headers={
                    "X-Accel-Buffering": "no",
                    "Cache-Control": "no-cache, no-transform",
                    "Connection": "keep-alive",
                    "Content-Type": "text/event-stream"
                }"""

content = content.replace(old_headers, new_headers)

with open("nova_repo/backend/api/routes.py", "w") as f:
    f.write(content)
