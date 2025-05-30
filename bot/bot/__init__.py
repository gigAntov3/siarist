from aiogram import Bot, Dispatcher

from bot.config import settings

from bot.database import DatabaseManager

from bot.services.api import API

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()
db = DatabaseManager()
api = API()
