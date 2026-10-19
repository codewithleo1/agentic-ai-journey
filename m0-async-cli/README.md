# M0: Async User Directory

Fetches 16 user IDs from a public API at the same time using `httpx` and `asyncio`, and validates each one with Pydantic. Bad IDs (like 0 or 999) return a "not found" message instead of crashing the batch.

## Run it (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python directory.py
```

## What I learned
- Async uses waiting time to run other tasks. 16 requests finish in about 1-3s instead of the sum of all of them. `time.sleep` blocks, `await asyncio.sleep` doesn't.
- `asyncio.gather` runs tasks together and returns results in the order I passed them.
- Pydantic validates data at the door and gives a clear error: which field, what's wrong, and the bad value.
- One failure must not crash the batch: `fetch_user` returns a message instead of raising, so `gather` keeps the other results.