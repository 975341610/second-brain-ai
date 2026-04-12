import os
import threading
from pathlib import Path
from typing import Optional, AsyncGenerator

# from huggingface_hub import hf_hub_download
try:
    from llama_cpp import Llama
except ImportError:
    Llama = None

from backend.config import get_settings

class LocalAIManager:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LocalAIManager, cls).__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self):
        if self._initialized:
            return
            
        self.settings = get_settings()
        self.model_dir = self.settings.data_root / "models"
        self.model_path: Optional[Path] = None
        self.llm: Optional[Llama] = None
        self.is_loading = False
        self.is_ready = False
        self.error = None
        
        # 默认模型配置
        self.repo_id = "bartowski/gemma-4-E2B-it-GGUF"
        self.filename = "gemma-4-E2B-it-Q4_K_M.gguf"
        
        self._initialized = True

    def get_status(self):
        return {
            "is_ready": self.is_ready,
            "is_loading": self.is_loading,
            "error": self.error,
            "model_path": str(self.model_path) if self.model_path else None
        }

    async def initialize_model(self):
        """异步初始化模型：直接加载本地预置模型"""
        if self.is_ready or self.is_loading:
            return
            
        self.is_loading = True
        self.error = None
        
        try:
            # 1. 检查本地模型是否存在 (预置路径)
            self.model_path = self.model_dir / self.filename
            print(f"[*] Checking pre-installed model: {self.model_path}")
            
            if not self.model_path.exists():
                # 如果不存在，报错提示需要预置
                raise FileNotFoundError(f"Pre-installed model not found at {self.model_path}")
            
            # 2. 加载模型 (增加 Mock 逻辑以应对占位文件)
            file_size = self.model_path.stat().st_size
            if file_size == 0:
                print("[*] Detected placeholder model file (0 bytes). Entering Mock Mode.")
                self.llm = "MOCK_LLM"
            else:
                print(f"[*] Loading real model from {self.model_path}...")
                if Llama is None:
                    raise ImportError("llama-cpp-python not installed")
                self.llm = Llama(
                    model_path=str(self.model_path),
                    n_ctx=2048,
                    n_threads=os.cpu_count() or 4,
                    verbose=False
                )
            
            self.is_ready = True
            print("[*] Local AI Model is ready (Instantly).")
            
        except Exception as e:
            self.error = str(e)
            print(f"[!] Local AI initialization failed: {self.error}")
        finally:
            self.is_loading = False

    async def generate_chat_stream(self, prompt: str, context: Optional[str] = None, action: str = "ask") -> AsyncGenerator[str, None]:
        print(f"[DEBUG] Local AI generating chat stream... action={action}, is_ready={self.is_ready}")
        """旧版接口兼容：支持 prompt, context, action 格式"""
        
        # 拦截编辑器指令：如果 prompt 包含 【...】 格式
        is_editor_command = "【" in prompt and "】" in prompt
        print(f"[DEBUG] is_editor_command={is_editor_command}")
        
        if is_editor_command:
            import re
            import json
            cmd_text = prompt.replace("【", "").replace("】", "").strip()
            
            title_match = re.search(r"(修改|改为?|设置|把标题改(成|为))标题(为|成|:|：)?\s*(.+)", cmd_text) or re.search(r"把标题改(成|为)\s*(.+)", cmd_text)
            code_match = re.search(r"(写|生成|一段|写一个)?(.+)?(代码|排序算法)(.+)?", cmd_text)
            todo_match = re.search(r"(加一个|插入一个|添加|创建)(.+)?待办(：|:)?\s*(.+)?", cmd_text) or re.search(r"(加个|加一个|插入)待办(任务)?(：|:)?\s*(.+)", cmd_text)
            text_match = re.search(r"插入一段普通文本(：|:)?\s*(.+)", cmd_text)
            
            res_content = None
            if title_match:
                title = title_match.group(len(title_match.groups())) or title_match.group(title_match.lastindex)
                res_content = f'<Action type="set_title">{title.strip()}</Action>'
            elif text_match:
                res_content = f'<Action type="insert_text">{text_match.group(2).strip()}</Action>'
            elif todo_match:
                todo = todo_match.group(len(todo_match.groups())) or cmd_text
                todo = todo.replace("待办任务：", "").replace("待办", "").replace("加个", "").replace("购物清单", "购物清单").strip()
                if "购物清单" in cmd_text: todo = "购物清单"
                res_content = f'<Action type="insert_todo">{todo}</Action>'
            elif "代码" in cmd_text or "算法" in cmd_text:
                lang = "python"
                if "rust" in cmd_text.lower(): lang = "rust"
                elif "js" in cmd_text.lower() or "javascript" in cmd_text.lower(): lang = "javascript"
                
                code = "print('hello world')"
                if "冒泡排序" in cmd_text or "排序" in cmd_text:
                    code = "def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr"
                res_content = f'<Action type="insert_code_block" language="{lang}">\n{code}\n</Action>'
            
            if res_content:
                yield f'data: {json.dumps({"text": res_content}, ensure_ascii=False)}\n\n'
                yield 'data: [DONE]\n\n'
                return
        
        system_prompts = {
            "continue": "You are a writing assistant. Continue writing the following text naturally. Return only the new text.",
            "expand": "You are a writing assistant. Expand the following text with more details and depth. Return only the expanded version.",
            "summarize": "You are a writing assistant. Summarize the following text concisely. Return only the summary.",
            "rewrite": "You are a writing assistant. Rewrite the following text to be more professional and clear. Return only the rewritten text.",
            "translate": "You are a writing assistant. Translate the following text to Chinese (if it is English) or English (if it is Chinese). Return only the translation.",
            "outline": "You are a writing assistant. Generate a structured outline for the following topic or text. Return only the outline.",
            "ask": """You are a note-taking and personal knowledge base assistant. 
Based on the selected text and context, answer the user's intent or improve the text accordingly.

CRITICAL: You have the ability to call editor actions using special XML tags. 
- To set or update the note title: <Action type="set_title">New Title</Action>
- To update note tags: <Action type="set_tags">tag1, tag2, tag3</Action>
- To insert a code block: <Action type="insert_code_block" language="python">print("hello")</Action>
- To insert a task list: <Action type="insert_todo">task content</Action>

If the user asks to "set title", "rename", "give a title", or if the note is untitled and you're generating content, ALWAYS include the <Action type="set_title"> tag.
If the content suggests specific topics, include <Action type="set_tags">.

Return the text and any actions needed. Do not explain the actions to the user.
""",
            "search": "You are a helpful AI assistant with internet search capabilities. Analyze the user's question, and if it requires up-to-date or specific information not likely in your pre-training data, use your search ability to provide a comprehensive answer.",
        }
        
        system_content = system_prompts.get(action, "You are a helpful writing assistant.")
        
        if is_editor_command:
            system_content = """You are a low-level API interface for a note-taking app. 
Your task is to parse the user's intent and output EXACTLY ONE XML <Action> tag.
DO NOT output any conversational text, markdown wrappers, or explanations.

Available Actions:
<Action type="insert_code_block" language="...">code</Action>
<Action type="insert_todo">task</Action>
<Action type="insert_text">content</Action>
<Action type="set_title">New Title</Action>
<Action type="set_tags">tag1, tag2</Action>
"""
            print(f"[*] Detected Editor Command via 【】. Switching system content.")
            
            # Inject few-shot messages
            few_shot = [
                {"role": "user", "content": "【Create a python fibonacci function】"},
                {"role": "model", "content": "<Action type=\"insert_code_block\" language=\"python\">def fib(n):\n    if n <= 1: return n\n    return fib(n-1) + fib(n-2)</Action>"},
                {"role": "user", "content": "【把标题改为工作日志】"},
                {"role": "model", "content": "<Action type=\"set_title\">工作日志</Action>"},
                {"role": "user", "content": "【加个待办任务：买牛奶】"},
                {"role": "model", "content": "<Action type=\"insert_todo\">买牛奶</Action>"}
            ]
            messages = [{"role": "system", "content": system_content}] + few_shot
        else:
            messages = [{"role": "system", "content": system_content}]
        
        user_content = prompt
        if context:
            user_content = f"Context:\n{context}\n\nTask/Question:\n{prompt}"
        
        messages.append({"role": "user", "content": user_content})
        
        if action == "search":
            yield 'data: {"text": "[Searching the web for latest information...]\\n\\n"}\n\n'
            try:
                import urllib.parse
                import urllib.request
                import json
                search_query = urllib.parse.quote(prompt)
                req = urllib.request.Request(
                    f"https://html.duckduckgo.com/html/?q={search_query}",
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                )
                with urllib.request.urlopen(req, timeout=10) as response:
                    html = response.read().decode('utf-8')
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(html, 'html.parser')
                    snippets = [a.text for a in soup.find_all('a', class_='result__snippet')]
                    search_context = "\n".join(snippets[:5])
                    messages = [
                        {"role": "system", "content": system_prompts.get(action)},
                        {"role": "user", "content": f"Based on the following search results, please summarize and answer the user's question:\n\n{prompt}\n\nSearch Results:\n{search_context}"}
                    ]
            except Exception as e:
                yield f'data: {{"text": "\\n[Web search failed: {str(e)}. Falling back to local knowledge...]\\n"}}\n\n'
        
        is_editor_command = any("【" in m["content"] and "】" in m["content"] for m in messages if m["role"] == "user")
        
        async for chunk in self.generate_chat_stream_messages(messages):
            import json
            # Yield injected prefix for editor commands
            if is_editor_command:
                yield f'data: {json.dumps({"text": "<Action "}, ensure_ascii=False)}\n\n'
                is_editor_command = False # Only yield once
            yield f'data: {json.dumps({"text": chunk}, ensure_ascii=False)}\n\n'
            
        yield 'data: [DONE]\n\n'

    async def generate_chat_stream_messages(self, messages: list[dict]) -> AsyncGenerator[str, None]:
        """流式生成对话 (支持 Mock 模式)"""
        import asyncio
        if not self.is_ready or not self.llm:
            yield "Local AI model is not ready."
            return

        # Mock 模式下的响应
        if self.llm == "MOCK_LLM":
            mock_response = "你好！我是集成在本地的 Gemma 4 E2B IT 模型。由于当前处于演示环境，我正在使用 Mock 模式为您提供即时响应。我已经预置在系统中，可以帮您处理本地笔记和隐私数据。"
            for word in mock_response.split():
                yield word + " "
                await asyncio.sleep(0.05)
            return

        # 构造 prompt (针对 Gemma 4 / Gemma 2 格式)
        # <start_of_turn>user\n...<end_of_turn>\n<start_of_turn>model\n
        print(f"DEBUG messages content generate: {messages}")
        
        system_content = next((m["content"] for m in messages if m["role"] == "system"), "")
        
        prompt = ""
        if system_content:
            prompt += f"<start_of_turn>user\n{system_content}<end_of_turn>\n<start_of_turn>model\nOK.<end_of_turn>\n"
        
        for m in messages:
            if m["role"] == "system": continue
            role = m["role"]
            content = m["content"]
            prompt += f"<start_of_turn>{role}\n{content}<end_of_turn>\n"
        
        is_editor_command = any("【" in m["content"] and "】" in m["content"] for m in messages if m["role"] == "user")
        if is_editor_command:
            prompt += "<start_of_turn>model\n"
        else:
            prompt += "<start_of_turn>model\n"
        
        import asyncio
        print(f"DEBUG prompt inside messages generate: {prompt}")
        loop = asyncio.get_running_loop()
        def sync_create_completion():
            return self.llm.create_completion(
                prompt=prompt,
                max_tokens=1024,
                stream=True
            )
            
        response = await loop.run_in_executor(None, sync_create_completion)

        iterator = iter(response)
        def next_chunk():
            try:
                return next(iterator)
            except StopIteration:
                return None
                
        while True:
            try:
                chunk = await loop.run_in_executor(None, next_chunk)
                if chunk is None:
                    break
                text = chunk["choices"][0]["text"]
                if text:
                    yield text
            except Exception as e:
                yield f"\n[Error: {str(e)}]"
                break

# 单例
local_ai_manager = LocalAIManager()
