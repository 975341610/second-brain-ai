import re

with open("nova_repo/backend/services/local_ai.py", "r") as f:
    content = f.read()

# In generate_chat_stream_messages, update the while loop to use wait_for
old_loop = """        while True:
            chunk = await async_queue.get()
            if chunk is None:
                break
            yield chunk"""

new_loop = """        while True:
            try:
                # Wait for data with a timeout to send keep-alive pings
                chunk = await asyncio.wait_for(async_queue.get(), timeout=2.0)
                if chunk is None:
                    break
                yield chunk
            except asyncio.TimeoutError:
                # Yield an empty string to keep the proxy connection alive
                yield ""
"""

content = content.replace(old_loop, new_loop)

# Also let's yield an immediate empty ping in generate_chat_stream
old_gen = """        async for chunk in self.generate_chat_stream_messages(messages):
            import json
            yield f'data: {json.dumps({"text": chunk}, ensure_ascii=False)}\\n\\n'"""

new_gen = """        # Yield an immediate ping to satisfy reverse proxy TTFB
        yield 'data: {"text": ""}\\n\\n'

        async for chunk in self.generate_chat_stream_messages(messages):
            import json
            if chunk == "":
                # Keep-alive ping, we can just send an empty SSE comment
                yield ': ping\\n\\n'
            else:
                yield f'data: {json.dumps({"text": chunk}, ensure_ascii=False)}\\n\\n'"""

content = content.replace(old_gen, new_gen)

with open("nova_repo/backend/services/local_ai.py", "w") as f:
    f.write(content)
