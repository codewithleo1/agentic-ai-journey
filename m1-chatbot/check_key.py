import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GROQ_API_KEY")
print("Key loaded:", key is not None)
print("Starts with gsk_:", key.startswith("gsk_") if key else False)