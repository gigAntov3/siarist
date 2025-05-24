import asyncio
from typing import Any

from aiogram import types
from aiogram.types import (
    FSInputFile,                 
    InputMediaPhoto, 
    InputMediaVideo
)
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput, MessageInput

from datetime import date, datetime

from .states import MainClient

from bot import db, bot


# async def on_enter_password(message: types.Message, widget: TextInput, manager: DialogManager, password: str):
#     await manager.switch_to(MainClient.main)
        
        
# async def on_click_(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
#     await manager.switch_to(MainAdmin.main)
        