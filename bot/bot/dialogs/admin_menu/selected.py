import os
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

from bot import db, bot, api
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




async def on_enter_category_name(message: types.Message, widget: TextInput, manager: DialogManager, category_name: str):
    await api.add_category(category_name)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await manager.switch_to(MainAdmin.categories, show_mode=ShowMode.DELETE_AND_SEND)


async def on_click_category(callback: types.CallbackQuery, widget: Any,  manager: DialogManager, category_id: str):
    manager.dialog_data['category'] = int(category_id)
    await manager.switch_to(MainAdmin.category, show_mode=ShowMode.DELETE_AND_SEND)


async def on_click_delete_category(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    await api.delete_category(manager.dialog_data['category'])
    await manager.switch_to(MainAdmin.categories, show_mode=ShowMode.DELETE_AND_SEND)




async def on_click_product(callback: types.CallbackQuery, widget: Any,  manager: DialogManager, product_id: str):
    manager.dialog_data['product'] = int(product_id)
    await manager.switch_to(MainAdmin.product, show_mode=ShowMode.DELETE_AND_SEND)


async def on_click_delete_product(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    await api.delete_product(manager.dialog_data['product'])
    await manager.switch_to(MainAdmin.category, show_mode=ShowMode.DELETE_AND_SEND)


async def on_enter_product_name(message: types.Message, widget: TextInput, manager: DialogManager, product_name: str):
    manager.dialog_data['product_name'] = product_name
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await manager.switch_to(MainAdmin.enter_product_description, show_mode=ShowMode.DELETE_AND_SEND)


async def on_enter_product_description(message: types.Message, widget: TextInput, manager: DialogManager, product_description: str):
    manager.dialog_data['product_description'] = product_description
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await manager.switch_to(MainAdmin.enter_product_price, show_mode=ShowMode.DELETE_AND_SEND)


async def on_enter_product_price(message: types.Message, widget: TextInput, manager: DialogManager, product_price: str):
    manager.dialog_data['product_price'] = int(product_price)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await manager.switch_to(MainAdmin.enter_product_tag, show_mode=ShowMode.DELETE_AND_SEND)


async def on_click_product_tag(message: types.Message, widget: TextInput, manager: DialogManager, product_tag: str):
    manager.dialog_data['product_tag'] = product_tag
    await manager.switch_to(MainAdmin.enter_product_photo, show_mode=ShowMode.DELETE_AND_SEND)


async def on_enter_product_photo(message: types.Message, widget: MessageInput, manager: DialogManager):
    if message.photo:
        file = await bot.get_file(file_id=message.photo[-1].file_id)
        file_path = f"data/files/{message.photo[-1].file_id}.jpg"

        await bot.download_file(file.file_path, file_path)

        file = await api.upload_file(file_path)
        
        os.remove(file_path)

        await api.add_product(
            manager.dialog_data['product_name'],
            manager.dialog_data['product_description'],
            manager.dialog_data['product_price'],
            manager.dialog_data['product_tag'],
            file.url,
            manager.dialog_data['category']
        )

        await manager.switch_to(MainAdmin.category, show_mode=ShowMode.DELETE_AND_SEND)

    else:
        await manager.switch_to(MainAdmin.enter_product_photo, show_mode=ShowMode.DELETE_AND_SEND)







async def on_click_feedback(callback: types.CallbackQuery, widget: Any,  manager: DialogManager, feedback_id: str):
    manager.dialog_data['feedback'] = int(feedback_id)
    await manager.switch_to(MainAdmin.feedback, show_mode=ShowMode.DELETE_AND_SEND)


async def on_click_delete_feedback(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    await api.delete_feedback(manager.dialog_data['feedback'])
    await manager.switch_to(MainAdmin.feedbacks, show_mode=ShowMode.DELETE_AND_SEND)


async def on_enter_feedback_content(message: types.Message, widget: TextInput, manager: DialogManager, feedback_content: str):
    manager.dialog_data['content'] = feedback_content
    await manager.switch_to(MainAdmin.enter_feedback_priority, show_mode=ShowMode.DELETE_AND_SEND)


async def on_enter_feedback_priority(message: types.Message, widget: TextInput, manager: DialogManager, feedback_priority: str):
    manager.dialog_data['priority'] = int(feedback_priority)

    await api.add_feedback(
        manager.dialog_data['content'],
        manager.dialog_data['priority'],
        1
    )

    await manager.switch_to(MainAdmin.feedbacks, show_mode=ShowMode.DELETE_AND_SEND)












async def on_click_set_offset(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    await manager.update({'offset': 0})


async def on_click_increase_offset(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    await manager.update({'offset': manager.dialog_data['offset'] + 10})


async def on_click_decrease_offset(callback: types.CallbackQuery, widget: Any,  manager: DialogManager):
    await manager.update({'offset': manager.dialog_data['offset'] - 10})