import uuid
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
from aiogram.utils.media_group import MediaGroupBuilder

from aiogram_dialog import DialogManager, ShowMode, BaseDialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput, MessageInput

from datetime import date, datetime

from bot.services.reports.excel import UsersExcel

from .states import MainAdmin

from bot import db, bot
from bot.config import messages
from bot.config.settings import ADMIN_PASSWORD



async def on_enter_password(message: types.Message, widget: TextInput, manager: DialogManager, password: str):
    if password == ADMIN_PASSWORD:
        await manager.switch_to(MainAdmin.main)
    else:
        await manager.switch_to(MainAdmin.password)


async def on_click_mailings(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    await callback.answer(messages.NOT_CONNECTED_FUNCTIONALITY, show_alert=True)


async def on_click_statistics(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    excel = UsersExcel()
    await excel.create()

    file = types.FSInputFile("data/statistics.xlsx", "Пользователи.xlsx")

    await bot.send_document(chat_id=callback.message.chat.id, document=file)

    await manager.switch_to(MainAdmin.main, show_mode=ShowMode.DELETE_AND_SEND)