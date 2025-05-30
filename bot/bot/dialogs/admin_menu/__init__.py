from aiogram_dialog import Dialog

from . import windows

def admin_menu_dialog():
    return Dialog(
        windows.main_admin_window(),
        windows.enter_password_window(),

        windows.categories_window(),
        windows.enter_category_name_window(),
        windows.category_window(),
        
        windows.product_window(),
        windows.enter_product_name_window(),
        windows.enter_product_description_window(),
        windows.enter_product_price_window(),
        windows.enter_product_tag_window(),
        windows.enter_product_photo_window(),


        windows.feedbacks_window(),
        windows.feedback_window(),
        windows.enter_feedback_content_window(),
        windows.enter_feedback_priority_window(),
    )   