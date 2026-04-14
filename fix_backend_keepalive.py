with open("nova_repo/backend/main.py", "r") as f:
    content = f.read()

# Try to add explicit Keep-Alive timeout for uvicorn
if "uvicorn.run(" in content:
    content = content.replace("uvicorn.run(", "uvicorn.run(timeout_keep_alive=65, ")

with open("nova_repo/backend/main.py", "w") as f:
    f.write(content)
