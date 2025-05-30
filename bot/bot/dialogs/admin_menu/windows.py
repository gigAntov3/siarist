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

    on_enter_category_name,
    on_click_category,
    on_click_delete_category,

    on_click_product,
    on_click_delete_product,
    on_enter_product_name,
    on_enter_product_description,
    on_enter_product_price,
    on_click_product_tag,
    on_enter_product_photo,


    on_click_feedback,
    on_click_delete_feedback,
    on_enter_feedback_content,
    on_enter_feedback_priority,

    on_click_set_offset,
    on_click_increase_offset,
    on_click_decrease_offset,

)
from .getters import (
    get_main,
    get_enter_password,

    get_categories,
    get_category,

    get_product,
    get_product_tags,


    get_feedbacks,
    get_feedback,
    get_priorities,
)



def main_admin_window():
    return Window(
        Format("{text}"),
        SwitchTo(
            id="categories",
            text=Const("📂 Каталог"),
            state=MainAdmin.categories
        ),
        SwitchTo(
            id="feedbacks",
            text=Const("💬 Отзывы"),
            state=MainAdmin.feedbacks,
            on_click=on_click_set_offset
        ),
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



def categories_window():
    return Window(
        Format("{text}"),
        Group(
            Select(
                id="category",
                text=Format("{item[1]}"),
                item_id_getter=operator.itemgetter(0),
                items="categories",
                on_click=on_click_category
            ),
            width=1
        ),
        SwitchTo(
            id="enter_category_name",
            text=Const("📂 Добавить категорию"),
            state=MainAdmin.enter_category_name
        ),
        SwitchTo(
            id="back_to_main",
            text=Const("🔙 Назад"),
            state=MainAdmin.main
        ),
        getter=get_categories,
        state=MainAdmin.categories
    )


def enter_category_name_window():
    return Window(
        Const("Введите название категории"),
        TextInput(
            id="enter_category_name",
            on_success=on_enter_category_name
        ),
        SwitchTo(
            id="back_to_categories",
            text=Const("🔙 Назад"),
            state=MainAdmin.categories
        ),
        state=MainAdmin.enter_category_name
    )

def category_window():
    return Window(
        Format("{text}"),
        Group(
            Select(
                id="product",
                text=Format("{item[1]}"),
                item_id_getter=operator.itemgetter(0),
                items="products",
                on_click=on_click_product
            ),
            width=1
        ),
        SwitchTo(
            id="enter_product_name",
            text=Const("📂 Добавить товар"),
            state=MainAdmin.enter_product_name
        ),
        Button(
            id="delete",
            text=Const("❌ Удалить категорию"),
            on_click=on_click_delete_category
        ),
        SwitchTo(
            id="back_to_categories",
            text=Const("🔙 Назад"),
            state=MainAdmin.categories
        ),
        getter=get_category,
        state=MainAdmin.category
    )



def product_window():
    return Window(
        StaticMedia(
            url=Format("{photo}"),
        ),
        Format("{text}"),
        Button(
            id="delete",
            text=Const("❌ Удалить товар"),
            on_click=on_click_delete_product
        ),
        SwitchTo(
            id="back_to_category",
            text=Const("🔙 Назад"),
            state=MainAdmin.category
        ),
        getter=get_product,
        state=MainAdmin.product
    )


def enter_product_name_window():
    return Window(
        Const("Введите название товара"),
        TextInput(
            id="enter_product_name",
            on_success=on_enter_product_name
        ),
        SwitchTo(
            id="back_to_category",
            text=Const("🔙 Назад"),
            state=MainAdmin.category
        ),
        state=MainAdmin.enter_product_name
    )


def enter_product_description_window():
    return Window(
        Const("Введите описание товара"),
        TextInput(
            id="enter_product_description",
            on_success=on_enter_product_description
        ),
        SwitchTo(
            id="back_to_name",
            text=Const("🔙 Назад"),
            state=MainAdmin.enter_category_name
        ),
        state=MainAdmin.enter_product_description
    )


def enter_product_price_window():
    return Window(
        Const("Введите цену товара"),
        TextInput(
            id="enter_product_price",
            on_success=on_enter_product_price
        ),
        SwitchTo(
            id="back_to_description",
            text=Const("🔙 Назад"),
            state=MainAdmin.enter_product_description
        ),
        state=MainAdmin.enter_product_price
    )


def enter_product_tag_window():
    return Window(
        Const("Введите количество товара"),
        Group(
            Select(
                id="product_tag",
                text=Format("{item[1]}"),
                item_id_getter=operator.itemgetter(0),
                items="product_tags",
                on_click=on_click_product_tag
            ),
            width=1
        ),
        SwitchTo(
            id="back_to_price",
            text=Const("🔙 Назад"),
            state=MainAdmin.enter_product_price
        ),
        getter=get_product_tags,
        state=MainAdmin.enter_product_tag
    )


def enter_product_photo_window():
    return Window(
        Const("Введите ссылку на изображение"),
        MessageInput(
            func=on_enter_product_photo
        ),
        SwitchTo(
            id="back_to_tag",
            text=Const("🔙 Назад"),
            state=MainAdmin.enter_product_tag
        ),
        state=MainAdmin.enter_product_photo
    )





####################################################################   FEEDBACKS   ############################################################################################



def feedbacks_window():
    return Window(
        Format("{text}"),
        Group(
            Select(
                id="feedback",
                text=Format("{item[1]}"),
                item_id_getter=operator.itemgetter(0),
                items="feedbacks",
                on_click=on_click_feedback
            ),
            width=2
        ),
        Group(
            Button(
                id="increase_feedback_offset",
                text=Const("◀️"),
                on_click=on_click_decrease_offset
            ),
            SwitchTo(
                id="enter_feedback_content",
                text=Const("📂 Добавить отзыв"),
                state=MainAdmin.enter_feedback_content
            ),
            Button(
                id="decrease_feedback_offset",
                text=Const("▶️"),
                on_click=on_click_increase_offset
            ),
            width=3
        ),
        SwitchTo(
            id="back_to_main",
            text=Const("🔙 Назад"),
            state=MainAdmin.main
        ),
        getter=get_feedbacks,
        state=MainAdmin.feedbacks
    )



def feedback_window():
    return Window(
        Format("{text}"),
        Button(
            id="delete",
            text=Const("❌ Удалить отзыв"),
            on_click=on_click_delete_feedback
        ),
        SwitchTo(
            id="back_to_feedbacks",
            text=Const("🔙 Назад"),
            state=MainAdmin.feedbacks
        ),
        getter=get_feedback,
        state=MainAdmin.feedback
    )


def enter_feedback_content_window():
    return Window(
        Const("Введите текст отзыва"),
        TextInput(
            id="enter_feedback_content",
            on_success=on_enter_feedback_content
        ),
        SwitchTo(
            id="back_to_feedbacks",
            text=Const("🔙 Назад"),
            state=MainAdmin.feedbacks
        ),
        state=MainAdmin.enter_feedback_content
    )


def enter_feedback_priority_window():
    return Window(
        Const("Выберите уровень приоретета"),
        Group(
            Select(
                id="priority",
                text=Format("{item[1]}"),
                item_id_getter=operator.itemgetter(0),
                items="priorities",
                on_click=on_enter_feedback_priority
            ),
            width=1,
        ),
        SwitchTo(
            id="back_to_content",
            text=Const("🔙 Назад"),
            state=MainAdmin.enter_feedback_content
        ),
        getter=get_priorities,
        state=MainAdmin.enter_feedback_priority
    )