from services.products import ProductsService
from repositories.products import ProductsRepository


def products_service():
    return ProductsService(ProductsRepository)