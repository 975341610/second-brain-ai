"""
# `analyze_audio`

Call a multimodal LLM API to analyze and understand audio files. This tool ONLY accepts audio files (MP3/WAV/OGG/FLAC/AAC/M4A/WMA/AIFF/OPUS/WEBM).

Use cases:
- Transcription: Convert speech in audio to text, supporting multiple languages
- Summarization: Generate a concise summary of the audio content (meetings, lectures, podcasts, etc.)
- Translation: Transcribe and translate audio content into a specified target language

- DO NOT use this tool for non-audio files.


---

**Parameters Schema:**

{"type":"object","properties":{"path":{"type":"string","description":"the local path of the audio file","properties":{}},"task":{"type":"string","description":"the message to send to the LLM, e.g. 'transcribe this audio', 'summarize the meeting', 'translate to English'","properties":{}}},"required":["task","path"]}

"""
import sys
import json
from byted_aime_sdk import call_aime_tool

if __name__ == '__main__':
    try:
        print(call_aime_tool(toolset="analyze_media", tool_name="analyze_audio", parameters=json.loads(" ".join(sys.argv[1:])), response_format="text"))
    except Exception as e:
        print(e)
        sys.exit(1)