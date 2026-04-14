with open("nova_repo/backend/services/local_ai.py", "r") as f:
    content = f.read()

# Make the TTFB ping larger to flush any proxy buffers
old_ping = """        # Yield an immediate ping to satisfy reverse proxy TTFB
        yield 'data: {"text": ""}\\n\\n'"""

# sending 4KB of empty spaces inside a comment
new_ping = """        # Yield an immediate ping to satisfy reverse proxy TTFB and flush any intermediate proxy buffers
        buffer_flush = " " * 4096
        yield f': ping {buffer_flush}\\n\\n'
        yield 'data: {"text": ""}\\n\\n'"""

content = content.replace(old_ping, new_ping)

with open("nova_repo/backend/services/local_ai.py", "w") as f:
    f.write(content)
