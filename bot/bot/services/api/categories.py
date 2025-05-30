import asyncio
import aiohttp

from typing import List

from bot.services.api.schemas import Answer
from bot.services.api.schemas.categories import Category, AnswerCategories, AnswerCategory




class CategoriesAPI:
    BASE_URL = "http://127.0.0.1:8000/categories"


    async def get_categories(self, limit: int = 1, offset: int  = 0) -> List[Category]:
        url = "http://127.0.0.1:8000/categories"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params={"limit": limit, "offset": offset}) as response:
                return AnswerCategories(**await response.json()).categories
            

    async def add_category(self, name: str) -> Answer:
        url = "http://127.0.0.1:8000/categories"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={"name": name}) as response:
                return Answer(**await response.json())
            

    async def get_category(self, id: int) -> Category:
        url = f"http://127.0.0.1:8000/categories/{id}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return AnswerCategory(**await response.json()).category
            

    async def delete_category(self, id: int) -> Answer:
        url = f"http://127.0.0.1:8000/categories/{id}"

        async with aiohttp.ClientSession() as session:
            async with session.delete(url) as response:
                return Answer(**await response.json())



if __name__ == "__main__":
    api = CategoriesAPI()
    asyncio.run(api.get_categories(limit=3, offset=0))