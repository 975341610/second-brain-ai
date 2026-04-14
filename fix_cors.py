import re

with open("nova_repo/backend/main.py", "r") as f:
    content = f.read()

# Make sure streaming response has the proper headers
if "CORSMiddleware" in content:
    # It already has CORSMiddleware, but let's check expose_headers
    pass

# What if the proxy is buffering the response? We can send a huge payload on the first ping
