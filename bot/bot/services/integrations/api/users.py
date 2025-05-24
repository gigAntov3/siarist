import asyncio
import aiohttp



class UsersAPI:
    BASE_URL = "http://127.0.0.1:8000/users"

    async def add_user(self, chat_id: str, first_name: str, last_name: str, username: str, balance: int) -> bool:
        async with aiohttp.ClientSession() as session:
            json = {
                "chat_id": chat_id,
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "balance": balance
            }
            async with session.post(self.BASE_URL, json=json) as response:
                print(await response.json())
                return await response.json()
            
    
    async def get_user(self, user_id: int) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.BASE_URL}/{user_id}") as response:
                print(await response.json())
                return await response.json()
            



if __name__ == "__main__":
    api = UsersAPI()

    asyncio.run(api.add_user())