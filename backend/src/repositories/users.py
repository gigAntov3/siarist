from utils.repository import SQLAlchemyRepository

from models.users import UserModel

from sqlalchemy import update, select

from database import async_session_maker


class UsersRepository(SQLAlchemyRepository):
    model = UserModel

    async def increase_balance(self, id: int, amount: int) -> bool:
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(balance=self.model.balance + amount)
                .returning(self.model.id)
            )
            result = await session.execute(stmt)
            await session.commit()
            return True

    async def decrease_balance(self, id: int, amount: int) -> bool:
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(balance=self.model.balance - amount)
                .returning(self.model.id)
            )
            result = await session.execute(stmt)
            await session.commit()
            return True
        

    async def increase_purchases_count(self, id: int) -> bool:
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(purchases_count=self.model.purchases_count + 1)
                .returning(self.model.id)
            )
            result = await session.execute(stmt)
            await session.commit()
            return True
        

    async def get_purchases_count(self, id: int) -> int:
        async with async_session_maker() as session:
            stmt = select(self.model.purchases_count).where(self.model.id == id)
            result = await session.execute(stmt)
            return result.scalar_one()