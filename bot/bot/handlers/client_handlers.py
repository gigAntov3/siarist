from aiogram import types
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from aiogram_dialog import DialogManager, StartMode

from bot.dialogs.client_menu.states import MainClient

from bot.services.api import API

from bot import db, bot
    
async def start_client(message: types.Message, dialog_manager: DialogManager):
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text='Подтвердить', callback_data='confirm:10')
    )

    builder.row(
        InlineKeyboardButton(text='Отменить', callback_data='cancel:10')
    )

    await bot.send_message(message.chat.id, 'Добро пожаловать в магазин!', reply_markup=builder.as_markup())





    
def register_client_handlers(dp: Dispatcher):
    dp.message.register(start_client, Command("start"))