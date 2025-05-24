from aiogram import types
from aiogram.filters import Command
from aiogram import Dispatcher, types
from aiogram.filters import Command

from aiogram_dialog import DialogManager, StartMode

from bot.dialogs.admin_menu.states import MainAdmin

from bot.__init__ import bot

async def start_admin(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainAdmin.enter_password, mode=StartMode.RESET_STACK)   
    
def register_admin_handlers(dp: Dispatcher):
    dp.message.register(start_admin, Command("admin"))