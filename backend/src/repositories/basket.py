from models.basket import BasketModel

from sqlalchemy import asc
from sqlalchemy import and_, select, update
from sqlalchemy.orm import joinedload

from database import async_session_maker

from models.basket import BasketModel
from utils.repository import SQLAlchemyRepository


class BasketRepository(SQLAlchemyRepository):
    model = BasketModel

    async def find_all(self, limit = None, offset = None, order_by = None, **filters):
        async with async_session_maker() as session:
            stmt = select(self.model).options(joinedload(self.model.product))

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
            return [row[0].to_read_model() for row in result.all()]
        

    async def increase_quantity(self, id: int) -> bool:
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(quantity=self.model.quantity + 1)
                .returning(self.model.id)
            )
            result = await session.execute(stmt)
            await session.commit()
            return True
        

    async def decrease_quantity(self, id: int) -> bool:
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(quantity=self.model.quantity - 1)
                .returning(self.model.id)
            )
            result = await session.execute(stmt)
            await session.commit()
            return True