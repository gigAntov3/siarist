from aiogram import types
from aiogram.filters import Command
from aiogram import Dispatcher, types
from aiogram.filters import Command

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_dialog import DialogManager, StartMode

from bot.dialogs.admin_menu.states import MainAdmin

from bot.__init__ import bot, api

async def start_admin(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainAdmin.main, mode=StartMode.RESET_STACK)   



async def confirm_order(callback: types.CallbackQuery):
    order_id = callback.data.split(":")[1]

    order = await api.get_order(order_id)

    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text='✅ Выполнено', callback_data=f"done")
    )

    await bot.send_message(order.user.chat_id, f"✅ Заказ No{order_id} выполнен")

    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=builder.as_markup()
    )


async def cancel_order(callback: types.CallbackQuery):
    order_id = callback.data.split(":")[1]

    order = await api.get_order(order_id)

    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text='❌ Отменен', callback_data=f"canceled")
    )

    await bot.send_message(order.user.chat_id, f"❌ Заказ No{order_id} отменен")

    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=builder.as_markup()
    )

    
def register_admin_handlers(dp: Dispatcher):
    dp.message.register(start_admin, Command("admin"))
    dp.callback_query.register(confirm_order, lambda callback: callback.data.startswith("confirm:"))
    dp.callback_query.register(cancel_order, lambda callback: callback.data.startswith("cancel:"))