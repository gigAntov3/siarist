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