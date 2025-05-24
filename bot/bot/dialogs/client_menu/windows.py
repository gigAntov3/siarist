from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Cancel, Back, Select, Calendar, SwitchTo, Url
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.common import Whenable

import operator

from .states import MainClient
# from .selected import (
    
# )
from .getters import (
    get_main,
)



def main_client_window():
    return Window(
        Format("{text}"),
        Url(
            id="support",
            text=Const("💬 Поддержка"),
            url=Format("{support}")
        ),
        getter=get_main,
        state=MainClient.main
    )