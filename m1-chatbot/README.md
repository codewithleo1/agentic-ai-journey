# M1: CLI Chatbot with Memory

A command-line chatbot using the Groq API (`openai/gpt-oss-20b`) that remembers the conversation and keeps a summary of old messages.

## Run it (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file with `GROQ_API_KEY=your_key`, then:

```powershell
python chatbot.py
```

Type `quit` to exit.

## What I learned
- LLM APIs are stateless: my code keeps the `messages` list and resends it every turn.
- Long chats overflow the context window, so I send only the last 6 messages plus a summary of older ones.
- Models can hallucinate (wrong dates, wrong identity), so never trust them blindly.