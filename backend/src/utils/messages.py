
from schemas.orders import OrderSchema


def get_order_message(order: OrderSchema) -> str:
    message = (
        "🛒 *Новый заказ!*\n\n"
        f"👤 *Пользователь:* @{order.user.username}\n\n"
        "📦 *Товары:*\n"
    )

    for order_product in order.order_products:
        message += (
            f"   ▫️ *{order_product.product.name}*\n"
            f"      💵 Цена: `{order_product.product.price} ₽`\n"
            f"      🔢 Кол-во: `{order_product.quantity}`\n"
        )

    message += f"\n💰 *Сумма заказа:* *{order.total_amount} ₽*\n"

    if order.withdrawn_bonuses > 0:
        message += f"🎁 *Бонусов использовано:* `{order.withdrawn_bonuses} ₽`\n"

    message += "\n"
    message += (
        f"🎮 *Платформа:* {order.platform}\n"
        f"📧 *Почта:* `{order.email}`\n"
    )

    if order.password:
        message += f"🔐 *Пароль:* `{order.password}`\n"

    message += f"🕹️ *Ник в игре:* `{order.nickname}`\n\n"

    message += f"🕒 *Время заказа:* `{order.created_at.strftime("%d.%m.%Y, %H:%M")}`"

    return message
