from typing import Optional

from utils.repository import BaseRepository
from schemas.categories import CategoryAddSchema


class CategoriesService:

    def __init__(self, categories_repo: BaseRepository):
        self.categories_repo = categories_repo()

    async def add_category(self, category: CategoryAddSchema):
        category_dict = category.model_dump()
        category_id = await self.categories_repo.add_one(category_dict)
        return category_id
    

    async def get_category(self, category_id: int):
        category = await self.categories_repo.find_one(category_id)
        return category
    

    async def get_categories(self, limit: Optional[int] = None, offset: Optional[int] = None):
        categories = await self.categories_repo.find_all(limit=limit, offset=offset)
        return categories