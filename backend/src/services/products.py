from typing import Optional

from utils.repository import BaseRepository
from schemas.products import ProductSchema, ProductUpdateSchema


class ProductsService:

    def __init__(self, products_repo: BaseRepository):
        self.products_repo = products_repo()

    async def add_product(self, product: ProductSchema):
        product_dict = product.model_dump()
        product_id = await self.products_repo.add_one(product_dict)
        return product_id
    
    async def get_product(self, product_id: int):
        product = await self.products_repo.find_one(product_id)
        return product
    
    async def get_products(self, limit: Optional[int] = None, offset: Optional[int] = None):
        products = await self.products_repo.find_all(limit=limit, offset=offset)
        return products
    
    async def update_product(self, product_id: int, product: ProductUpdateSchema):
        product_dict = product.model_dump(exclude_unset=True)
        await self.products_repo.update_one(product_id, product_dict)
        return product_dict
    
    async def delete_product(self, product_id: int):
        product = await self.products_repo.delete_one(product_id)
        return product