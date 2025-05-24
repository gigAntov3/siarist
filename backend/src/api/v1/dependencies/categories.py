from services.categories import CategoriesService
from repositories.categories import CategoriesRepository


def categories_service():
    return CategoriesService(CategoriesRepository)