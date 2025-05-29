from sqlalchemy import insert, asc, and_
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from utils.repository import SQLAlchemyRepository

from typing import Optional

from models.orders import OrderModel, OrderProductsModel

from database import async_session_maker

class OrdersRepository(SQLAlchemyRepository):
    model = OrderModel

    async def add_one(self, order_data: dict) -> int:
        async with async_session_maker() as session:
            async with session.begin():  # одна транзакция
                # Отделяем продукты от основного заказа
                products_data = order_data.pop("order_products", [])

                # Создаём заказ
                stmt = insert(OrderModel).values(**order_data).returning(OrderModel.id)
                result = await session.execute(stmt)
                order_id = result.scalar_one()

                # Добавляем связанные продукты
                for product in products_data:
                    stmt = insert(OrderProductsModel).values(
                        order_id=order_id,
                        product_id=product["product_id"],
                        quantity=product["quantity"],
                    )
                    await session.execute(stmt)

            return order_id
        
    
    async def find_all(self, limit: Optional[int] = None, offset: Optional[int] = None, order_by: Optional[str] = None, **filters):
        async with async_session_maker() as session:
            stmt = (
                select(self.model)
                .options(
                    joinedload(self.model.order_products).joinedload(OrderProductsModel.product),
                    joinedload(self.model.user),
                    joinedload(self.model.order_products)
                    .joinedload(OrderProductsModel.product)
                )
            )

            if filters:
                conditions = [getattr(self.model, key) == value for key, value in filters.items()]
                stmt = stmt.where(and_(*conditions))

            if order_by:
                stmt = stmt.order_by(asc(getattr(self.model, order_by)))
            if limit is not None:
                stmt = stmt.limit(limit)
            if offset is not None:
                stmt = stmt.offset(offset)

            result = await session.execute(stmt)
            unique_result = result.unique()
            return [row.to_read_model() for row in unique_result.scalars().all()]


    async def find_one(self, id: int):
        async with async_session_maker() as session:
            stmt = (
                select(self.model)
                .options(
                    joinedload(self.model.order_products).joinedload(OrderProductsModel.product),
                    joinedload(self.model.user)
                )
                .where(self.model.id == id)
            )
            result = await session.execute(stmt)
            result = result.unique()
            return result.scalar_one().to_read_model()