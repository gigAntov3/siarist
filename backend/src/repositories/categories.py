from utils.repository import SQLAlchemyRepository

from models.categories import CategoryModel


class CategoriesRepository(SQLAlchemyRepository):
    model = CategoryModel