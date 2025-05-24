from typing import Optional

from abc import ABC, abstractmethod

from sqlalchemy import and_, insert, select, update, delete

from database import async_session_maker


class BaseRepository(ABC):

    @abstractmethod
    async def add_one(self):
        raise NotImplementedError
    

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError
    

    @abstractmethod
    async def update_one(self):
        raise NotImplementedError
    

    @abstractmethod
    async def delete_one(self):
        raise NotImplementedError
    

class SQLAlchemyRepository(BaseRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()
        

    async def find_one(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == id)
            result = await session.execute(stmt)
            result = result.scalar_one().to_read_model()
            return result
        
    
    async def find_all(self, limit: Optional[int] = None, offset: Optional[int] = None, **filters):
        async with async_session_maker() as session:
            stmt = select(self.model)

            if filters:
                conditions = [getattr(self.model, key) == value for key, value in filters.items()]
                stmt = stmt.where(and_(*conditions))

            if limit is not None:
                stmt = stmt.limit(limit)
            if offset is not None:
                stmt = stmt.offset(offset)

            result = await session.execute(stmt)
            return [row[0].to_read_model() for row in result.all()]
        
    
    async def update_one(self, id: int, data: dict) -> bool:
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(**data)
                .returning(self.model.id)
            )
            result = await session.execute(stmt)
            await session.commit()
            return True
        

    async def delete_one(self, id: int) -> bool:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == id)
            await session.execute(stmt)
            await session.commit()
            return True