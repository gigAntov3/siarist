from aiogram import Dispatcher

from .admin_menu import admin_menu_dialog
from .client_menu import client_menu_dialog

def register_dialogs(dp: Dispatcher):
    dp.include_router(admin_menu_dialog())
    dp.include_router(client_menu_dialog())