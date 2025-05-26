from typing import Optional

from utils.repository import BaseRepository
from schemas.basket import BasketAddSchema


class BasketService:

    def __init__(self, basket_repo: BaseRepository):
        self.basket_repo = basket_repo()

    
    async def add_basket(self, basket: BasketAddSchema):
        basket_dict = basket.model_dump()
        basket_id = await self.basket_repo.add_one(basket_dict)
        return basket_id
    

    async def get_basket(self, basket_id: int):
        basket = await self.basket_repo.find_one(basket_id)
        return basket
    

    async def get_baskets(self, limit: Optional[int] = None, offset: Optional[int] = None):
        baskets = await self.basket_repo.find_all(limit=limit, offset=offset)
        return baskets
    

    async def increase_quantity(self, basket_id: int) -> bool:
        is_increased = await self.basket_repo.increase_quantity(basket_id)
        return is_increased
    

    async def decrease_quantity(self, basket_id: int) -> bool:
        is_decreased = await self.basket_repo.decrease_quantity(basket_id)
        return is_decreased