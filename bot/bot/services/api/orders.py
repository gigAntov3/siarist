import asyncio
import aiohttp

from typing import List

from bot.services.api.schemas import Answer
from bot.services.api.schemas.orders import Order, AnswerOrder




class OrdersAPI:
    BASE_URL = "http://127.0.0.1:8000/products"
    
    async def get_order(self, id: int) -> Order:
        url = f"http://127.0.0.1:8000/orders/{id}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return AnswerOrder(**await response.json()).order
            

if __name__ == "__main__":
    api = OrdersAPI()
    asyncio.run(api.get_order(id=1))
