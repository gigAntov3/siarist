from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Cancel, Back, Select, Calendar, SwitchTo, Group
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.common import Whenable

import operator

from .states import MainAdmin
from .selected import (
    on_enter_password,

    on_click_mailings,
    on_click_statistics,
)
from .getters import (
    get_main,
    get_enter_password,
)



def main_admin_window():
    return Window(
        Format("{text}"),
        Button(
            id="mailings",
            text=Const("📲 Рассылки"),
            on_click=on_click_mailings
        ),
        Button(
            id="statistics",
            text=Const("📊 Статистика"),
            on_click=on_click_statistics
        ),
        getter=get_main,
        state=MainAdmin.main
    )


def enter_password_window():
    return Window(
        Format("{text}"),
        TextInput(
            id="enter_password",
            on_success=on_enter_password
        ),
        getter=get_enter_password,
        state=MainAdmin.enter_password
    )
