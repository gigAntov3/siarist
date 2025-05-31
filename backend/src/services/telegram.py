from typing import Optional

from aiogram import Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from schemas.orders import OrderSchema

from utils.messages import get_order_message


class TelegramService:

    def __init__(self):
        self.bot = Bot(token="6637038952:AAEYo2vBYRThjt8sHG0_ccS10gPeGbUgIyA")
        self.admin_chat_id = -4700591030


    async def send_order_to_admin(self, order: OrderSchema):
        builder = InlineKeyboardBuilder()

        builder.row(
            InlineKeyboardButton(text='✅ Подтвердить выполнение', callback_data='confirm:10')
        )

        builder.row(
            InlineKeyboardButton(text='❌ Отменить заказ', callback_data='cancel:10')
        )

        await self.bot.send_message(
            chat_id=self.admin_chat_id, 
            text=get_order_message(order), 
            reply_markup=builder.as_markup(),
            parse_mode="Markdown"
        )


