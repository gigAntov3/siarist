import asyncio

from aiogram_dialog import setup_dialogs

from .handlers import register_handlers
from .dialogs import register_dialogs

from .__init__ import dp, bot, db

from .services import start_scheduler


async def run_bot():
    await db.init_db()
    
    register_dialogs(dp)
    register_handlers(dp)
    setup_dialogs(dp)

    print("✅ Бот запущен и готов к работе\n")
    
    await dp.start_polling(bot)


async def run():
    await asyncio.gather(run_bot(), start_scheduler())