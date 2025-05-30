from aiogram_dialog import DialogManager

from bot import db, bot, api
from bot.config import messages


async def get_main(dialog_manager: DialogManager, **kwargs):
    return {'text': messages.START_ADMIN_MESSAGE}


async def get_enter_password(dialog_manager: DialogManager, **kwargs):
    return {'text': messages.ENTER_PASSWORD_MESSAGE}



import aiohttp



async def get_categories(dialog_manager: DialogManager, **kwargs):
    categories = await api.get_categories(limit=10, offset=0)

    categories = [(category.id, category.name) for category in categories]

    return {
        'text': messages.CATEGORIES_MESSAGE,
        'categories': categories
    }


async def get_category(dialog_manager: DialogManager, **kwargs):
    category = await api.get_category(dialog_manager.dialog_data['category'])

    products = await api.get_products(limit=10, offset=0, category_id=category.id)

    products = [(product.id, "🛍 " + product.name) for product in products]

    return {
        'text': messages.CATEGORY_MESSAGE.format(name=category.name),
        'products': products
    }



async def get_product(dialog_manager: DialogManager, **kwargs):
    product = await api.get_product(dialog_manager.dialog_data['product'])

    return {
        'text': messages.PRODUCT_MESSAGE.format(name=product.name),
        'photo': product.photo
    }


async def get_product_tags(dialog_manager: DialogManager, **kwargs):
    tags = [
        ("new", "🆕 Новый"),
        ("hit", "🔥 Хит продаж"),
        ("best", "🤑 Лучшая цена"),
        ("none", "❌ Без тега")
    ]
    return {
        'text': messages.PRODUCT_TAGS_MESSAGE,
        'product_tags': tags
    }




async def get_feedbacks(dialog_manager: DialogManager, **kwargs):
    feedbacks = await api.get_feedbacks(limit=10, offset=dialog_manager.dialog_data['offset'])

    feedbacks = [(feedback.id, feedback.content) for feedback in feedbacks]

    return {
        'text': messages.FEEDBACKS_MESSAGE,
        'feedbacks': feedbacks
    }


async def get_feedback(dialog_manager: DialogManager, **kwargs):
    feedback = await api.get_feedback(dialog_manager.dialog_data['feedback'])

    return {
        'text': messages.FEEDBACK_MESSAGE.format(content=feedback.content)
    }


async def get_priorities(dialog_manager: DialogManager, **kwargs):

    return {
        'priorities': [
            ("1", "⏫ Очень высокий"),
            ("2", "▶️ Высокий"),
            ("3", "▶️ Средний"),
            ("4", "⏬ Низкий"),
            ("5", "⏬ Очень низкий")
        ]
    }