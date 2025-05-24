from aiogram import Dispatcher

from .client_handlers import register_client_handlers
from .admin_handlers import register_admin_handlers

def register_handlers(dp: Dispatcher):
    register_admin_handlers(dp)
    register_client_handlers(dp)
