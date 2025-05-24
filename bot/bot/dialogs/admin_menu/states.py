from aiogram.filters.state import State, StatesGroup

class MainAdmin(StatesGroup):
    main = State()
    
    enter_password = State()