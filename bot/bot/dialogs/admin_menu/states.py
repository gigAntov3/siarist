from aiogram.filters.state import State, StatesGroup

class MainAdmin(StatesGroup):
    main = State()
    
    enter_password = State()


    categories = State()

    enter_category_name = State()

    category = State()

    product = State()

    enter_product_name = State()

    enter_product_description = State()

    enter_product_price = State()

    enter_product_tag = State()

    enter_product_photo = State()


    feedbacks = State()

    feedback = State()

    enter_feedback_content = State()

    enter_feedback_priority = State()

    enter_feedback_user_id = State()