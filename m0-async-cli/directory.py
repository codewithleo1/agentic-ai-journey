from pydantic import BaseModel
import asyncio
import time
import httpx

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str

async def fetch_user(client, user_id):
    resp = await client.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if resp.status_code == 404:
        return f"User {user_id}: not found"
    data = resp.json()
    return User.model_validate(data)


async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        user = await asyncio.gather(*(fetch_user(client, user_id) for user_id in [*range(0,15), 999]))
    for u in user:
        if isinstance(u, str):
            print(u)
        else:
            print(f'{u.id} | {u.name} | {u.username} | {u.email}')
    print(f"Done in {time.time() - start:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())