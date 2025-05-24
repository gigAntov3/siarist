from datetime import datetime, timedelta

from typing import Optional, List

from sqlalchemy import update, select

from .models import User


# Базовый класс для работы с пользователями
class UserManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def add_user(self, chat_id: str, first_name: str, username: str) -> bool:
        async with self.db_manager.get_session() as session:
            async with session.begin():
                # Проверяем существование пользователя с таким именем
                result = await session.execute(
                    User.__table__.select().where(User.username == username)
                )
                existing_user = result.scalar_one_or_none()
                
                if existing_user:
                    return False

                new_user = User(chat_id=chat_id, first_name=first_name, username=username)
                session.add(new_user)
            return True
        
    async def get_users(self, offset: int = 0, limit: int = 10) -> list:
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                User.__table__.select().offset(offset).limit(limit)
            )
            return result.all()

    async def get_user(self, chat_id: str) -> Optional[User]:
        async with self.db_manager.get_session() as session:
            result = await session.execute(
                User.__table__.select().where(User.chat_id == chat_id)
            )
            return result.fetchone()
    

    async def delete_user(self, username: str) -> bool:
        async with self.db_manager.get_session() as session:
            async with session.begin():
                result = await session.execute(
                    User.__table__.select().where(User.username == username)
                )
                user = result.scalar_one_or_none()
                if user:
                    await session.delete(user)
                    return True
            return False