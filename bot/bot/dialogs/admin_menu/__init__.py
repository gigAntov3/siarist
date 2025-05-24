from aiogram_dialog import Dialog

from . import windows

def admin_menu_dialog():
    return Dialog(
        windows.main_admin_window(),
        windows.enter_password_window(),
    )   