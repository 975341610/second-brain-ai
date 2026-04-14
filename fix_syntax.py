with open("nova_repo/backend/main.py", "r") as f:
    content = f.read()

content = content.replace("uvicorn.run(timeout_keep_alive=65, app, host=host, port=port)", "uvicorn.run(app, host=host, port=port, timeout_keep_alive=65)")

with open("nova_repo/backend/main.py", "w") as f:
    f.write(content)
