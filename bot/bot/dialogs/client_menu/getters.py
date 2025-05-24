import asyncio

from datetime import timedelta

from aiogram_dialog import DialogManager, BaseDialogManager, ShowMode

from bot.__init__ import db, bot

from bot.config import messages
from bot.config.settings import SUPPORT_LINK

from .states import MainClient



async def get_main(dialog_manager: DialogManager, **kwargs):
    return {
        'text': messages.START_MESSAGE,
        "support": SUPPORT_LINK
    }