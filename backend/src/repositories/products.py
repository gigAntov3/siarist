from utils.repository import SQLAlchemyRepository

from models.products import ProductModel


class ProductsRepository(SQLAlchemyRepository):
    model = ProductModel