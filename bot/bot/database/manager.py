import asyncio
import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .users import UserManager, BaseUsers


logging.getLogger('sqlalchemy.engine').setLevel(logging.CRITICAL)


# Главный класс для управления базой данных, который наследует функциональность модулей
class DatabaseManager(UserManager):
    def __init__(self, db_url: str = 'data/database.db'):
        # Инициализация подключения к базе данных
        self.engine = create_async_engine('sqlite+aiosqlite:///' + db_url, echo=False)
        self.async_session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )
        # Передача ссылки на себя в базовые классы
        UserManager.__init__(self, self)

    def get_session(self) -> AsyncSession:
        """Создает новую асинхронную сессию для работы с базой данных."""
        return self.async_session()

    async def init_db(self):
        """Создание таблиц, если они не существуют"""
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseUsers.metadata.create_all)
            
        print("🗂️  База данных инициализирована\n")

if __name__ == "__main__":
    async def main():
        # Создаем главный менеджер базы данных
        db_manager = DatabaseManager()

        # Инициализация базы данных
        await db_manager.init_db()

    asyncio.run(main())