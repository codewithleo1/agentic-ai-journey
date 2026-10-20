import os
import httpx
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {key}"}

messages = []

def ask(msgs):
    body = {"model": "openai/gpt-oss-20b", "messages": msgs}
    resp = httpx.post(url, headers=headers, json=body, timeout=60)
    if resp.status_code != 200:
        print("API ERROR:", resp.status_code, resp.text[:300])
        return "(error)"
    return resp.json()["choices"][0]["message"]["content"]

def summarize(old_msgs):
    text = "\n".join(m["content"] for m in old_msgs if m["role"] == "user")
    prompt = (
        "List only facts the user stated about themselves "
        "(name, age, job, family, city). Max 3 short lines. "
        "No other text.\n" + text
    )
    return ask([{"role": "user", "content": prompt}])

print(summarize([
    {"role": "user", "content": "my name is suraj"},
    {"role": "user", "content": "my wife is Pratiksha"},
]))

while True:
    user_text = input("You: ")
    if user_text == "quit":
        break
    messages.append({"role": "user", "content": user_text})

    recent = messages[-6:]
    old = messages[:-6]

    if old:
        facts = summarize(old)
        print("[DEBUG facts]:", facts)
        recent = [{"role": "system", "content": "Known facts: " + facts}] + recent

    reply = ask(recent)

    reply = ask(recent)

    print("Bot:", reply)
    messages.append({"role": "assistant", "content": reply})