from services.orders import OrdersService
from repositories.orders import OrdersRepository


def orders_service():
    return OrdersService(OrdersRepository)