import os
import httpx
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {key}"}
body = {
    "model": "openai/gpt-oss-20b",
    "messages": [
    {"role": "user", "content": "My name is Suraj."},
    {"role": "assistant", "content": "Nice to meet you, Suraj!"},
    {"role": "user", "content": "What's my name?"},
],
}

resp = httpx.post(url, headers=headers, json=body, timeout=30)
print(resp.status_code)
print(resp.json()["choices"][0]["message"]["content"])