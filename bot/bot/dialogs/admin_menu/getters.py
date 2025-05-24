from aiogram_dialog import DialogManager

from bot import db, bot
from bot.config import messages


async def get_main(dialog_manager: DialogManager, **kwargs):
    return {'text': messages.START_ADMIN_MESSAGE}


async def get_enter_password(dialog_manager: DialogManager, **kwargs):
    return {'text': messages.ENTER_PASSWORD_MESSAGE}