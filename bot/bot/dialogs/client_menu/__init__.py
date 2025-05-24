from aiogram_dialog import Dialog

from . import windows

def client_menu_dialog():
    return Dialog(
        windows.main_client_window(),
    )   