from typing import Optional

from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy import and_, select, asc

from database import async_session_maker

from utils.repository import SQLAlchemyRepository

from models.feedbacks import FeedbackModel


class FeedbackRepository(SQLAlchemyRepository):
    model = FeedbackModel

    async def find_all(self, limit: Optional[int] = None, offset: Optional[int] = None, order_by: Optional[str] = None, **filters):
        async with async_session_maker() as session:
            stmt = select(self.model).options(joinedload(self.model.author))

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
        

    async def find_one(self, id: int):
        async with async_session_maker() as session:
            stmt = (
                select(self.model)
                .options(selectinload(self.model.author))  # 👈 загружаем связанного автора заранее
                .where(self.model.id == id)
            )
            result = await session.execute(stmt)
            feedback_obj = result.scalar_one()
            return feedback_obj.to_read_model()