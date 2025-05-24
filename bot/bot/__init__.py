from aiogram import Bot, Dispatcher

from bot.config import settings

from bot.database import DatabaseManager

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()
db = DatabaseManager()
