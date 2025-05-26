from services.basket import BasketService
from repositories.basket import BasketRepository


def basket_service():
    return BasketService(BasketRepository)