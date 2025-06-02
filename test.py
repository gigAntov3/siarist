import aiohttp
import asyncio

from pydantic import BaseModel


class AnswerPallyCreateBill(BaseModel):
    success: bool
    bill_id: str
    link_url: str
    link_page_url: str

    class Config:
        from_attributes = True



class PallyClient:
    BASE_URL = "https://pal24.pro/api/v1"

    def __init__(self, shop_id: str, api_key: str):
        self.shop_id = shop_id
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    async def create_bill(self, amount: int, currency: str, order_id: str) -> AnswerPallyCreateBill:
        url = f"{self.BASE_URL}/bill/create"
        data = {
            "shop_id": self.shop_id,
            "amount": amount,
            "currency": currency,
            "order_id": order_id
        }

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(url, data=data) as response:
                return AnswerPallyCreateBill(**await response.json())
            

    async def get_status(self, bill_id: str) -> dict:
        url = f"{self.BASE_URL}/bill/status/"

        data = {
            'id': "rvNw9Lxrm0"
        }
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url, params=data) as response:
                return await response.json()

# Пример использования
async def main():
    shop_id = "kd71ZWyv1K"
    api_key = "23212|1bUrTxfWReibMVjlqUdfYkBroGbDDmCuYzFYgw6L"

    bill_id = "R2Pa9g197w"
    
    client = PallyClient(shop_id, api_key)

    # payment = await client.create_bill(amount=100, currency="RUB", order_id="1")
    # print(payment)

    response = await client.get_status("rvNw9Lxrm0")
    print(response)

# Запуск
if __name__ == "__main__":
    asyncio.run(main())