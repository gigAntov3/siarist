from aiogram import types
from aiogram import Dispatcher
from aiogram.filters import Command

from aiogram_dialog import DialogManager, StartMode

from bot.dialogs.client_menu.states import MainClient

from bot.services.integrations import API

from bot import db, bot
    
async def start_client(message: types.Message, dialog_manager: DialogManager):
    api = API()
    await api.add_user(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, 0)
    await bot.send_message(chat_id=message.chat.id, text="✅ Вы успешно зарегистрировались!")


async def photo(message: types.Message, dialog_manager: DialogManager):
    file = await bot.get_file(message.photo[-1].file_id)

    await bot.send_message(chat_id=message.chat.id, text=file.file_path)

    file.
    

    
def register_client_handlers(dp: Dispatcher):
    dp.message.register(start_client, Command("start"))
    dp.message.register(photo)