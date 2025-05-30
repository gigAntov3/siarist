from typing import Optional

from utils.repository import BaseRepository
from schemas.users import UserSchema, UserAddSchema


class UsersService:

    def __init__(self, users_repo: BaseRepository):
        self.users_repo = users_repo()

    async def add_user(self, user: UserSchema):
        user_dict = user.model_dump()
        product_id = await self.users_repo.add_one(user_dict)
        return product_id
    

    async def get_users(self, limit: Optional[int] = None, offset: Optional[int] = None):
        users = await self.users_repo.find_all(limit=limit, offset=offset)
        return users
    

    async def get_user(self, user_id: int):
        user = await self.users_repo.find_one(id=user_id)
        return user
    

    async def increase_balance(self, user_id: int, amount: int):
        await self.users_repo.increase_balance(user_id, amount)


    async def decrease_balance(self, user_id: int, amount: int):
        await self.users_repo.decrease_balance(user_id, amount)
    

    async def increase_purchases_count(self, user_id: int):
        await self.users_repo.increase_purchases_count(user_id)


    async def apply_purchase_bonuses(self, user_id: int):
        purchase_bonuses = await self.users_repo.get_purchases_count(user_id)
        
        bonuses = {
            1: 50,
            3: 75,
            5: 100,
            10: 50,
            15: 75,
            20: 200,
            30: 200,
            40: 250,
            50: 500,
            60: 350,
            70: 400,
            80: 500,
            90: 900,
            100: 1000,
        }

        if purchase_bonuses not in bonuses:
            return
        
        await self.increase_balance(user_id, bonuses[purchase_bonuses])