from typing import Optional

from utils.repository import BaseRepository
from schemas.orders import OrderSchema


class OrdersService:

    def __init__(self, orders_repo: BaseRepository):
        self.orders_repo = orders_repo()

    async def add_order(self, order: OrderSchema):
        order_dict = order.model_dump()
        order_id = await self.orders_repo.add_one(order_dict)
        return order_id
    

    async def get_orders(self, limit: Optional[int] = None, offset: Optional[int] = None):
        orders = await self.orders_repo.find_all()
        return orders
    

    async def get_order(self, order_id: int):
        order = await self.orders_repo.find_one(order_id)
        return order
    

    async def update_payment_status(self, order_id: int, payment_status: str):
        return await self.orders_repo.update_payment_status(order_id, payment_status)