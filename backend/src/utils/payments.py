import aiohttp
import asyncio

from pydantic import BaseModel

from schemas.payments import AnswerPallyCreateBillSchema, AnswerPallyGetBillStatusSchema


class PallyClient:
    BASE_URL = "https://pal24.pro/api/v1"

    def __init__(self, shop_id: str, api_key: str):
        self.shop_id = shop_id
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    async def create_payment(self, amount: int, currency: str, order_id: str) -> AnswerPallyCreateBillSchema:
        url = f"{self.BASE_URL}/bill/create"
        data = {
            "shop_id": self.shop_id,
            "amount": amount,
            "currency": currency,
            "order_id": order_id
        }

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(url, data=data) as response:
                data = await response.json()
                return PaymentSchema(url=data['link_page_url'])
            

    async def get_status(self, bill_id: str) -> AnswerPallyGetBillStatusSchema:
        url = f"{self.BASE_URL}/bill/status/"

        data = {
            'id': bill_id
        }
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url, params=data) as response:
                return AnswerPallyGetBillStatusSchema(**await response.json())
            



import time
import hmac
import hashlib
import aiohttp

from fastapi import HTTPException

from schemas.payments import PaymentSchema


class FreeKassaClient:
    BASE_URL = "https://api.fk.life/v1"

    def __init__(self, shop_id: int, api_key: str):
        self.shop_id = shop_id
        self.api_key = api_key

    def _generate_signature(self, data: dict) -> str:
        sorted_items = dict(sorted(data.items()))
        sign_string = '|'.join(str(value) for value in sorted_items.values())
        signature = hmac.new(self.api_key.encode("utf-8"), sign_string.encode("utf-8"), hashlib.sha256).hexdigest()
        return signature

    def _build_payment_data(self, order_id: int, amount: int, currency: str, email: str, ip: str) -> dict:
        data = {
            "shopId": self.shop_id,
            "nonce": int(time.time()),
            "i": 6,
            "email": email,
            "ip": ip,
            "amount": amount,
            "currency": currency,
            "us_order_id": order_id
        }
        data["signature"] = self._generate_signature(data)
        return data

    async def create_payment(
        self,
        order_id: int,
        amount: int,
        currency: str,
        email: str,
        ip: str
    ) -> PaymentSchema:
        url = f"{self.BASE_URL}/orders/create"

        json = {
            "shopId": self.shop_id,
            "nonce": int(time.time()),
            "i": 6,
            "email": email,
            "ip": ip,
            "amount": amount,
            "currency": currency,
            "us_order_id": order_id
        }
        json["signature"] = self._generate_signature(json)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json, timeout=10) as response:
                json_data = await response.json()
                return PaymentSchema(url=json_data["location"])