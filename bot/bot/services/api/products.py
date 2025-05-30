import asyncio
import aiohttp

from typing import List

from bot.services.api.schemas import Answer
from bot.services.api.schemas.products import Product, AnswerProducts, AnswerProduct, AnswerProductAdd




class ProductsAPI:
    BASE_URL = "http://127.0.0.1:8000/products"

    async def get_products(self, category_id: int = None, limit: int = 1, offset: int  = 0) -> List[Product]:
        url = "http://127.0.0.1:8000/products"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params={"category_id": category_id, "limit": limit, "offset": offset}) as response:
                return AnswerProducts(**await response.json()).products
    

    async def get_product(self, id: int) -> Product:
        url = f"http://127.0.0.1:8000/products/{id}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return AnswerProduct(**await response.json()).product


    async def delete_product(self, id: int) -> Answer:
        url = f"http://127.0.0.1:8000/products/{id}"

        async with aiohttp.ClientSession() as session:
            async with session.delete(url) as response:
                return Answer(**await response.json())
            

    async def add_product(self, name: str, description: str, price: int, tag: str, photo: str, category_id: int) -> int:
        url = "http://127.0.0.1:8000/products"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={"name": name, "description": description, "price": price, "tag": tag, "photo": photo, "category_id": category_id}) as response:
                return AnswerProductAdd(**await response.json()).product_id



if __name__ == "__main__":
    api = ProductsAPI()
    asyncio.run(api.get_products(limit=3, offset=0))
