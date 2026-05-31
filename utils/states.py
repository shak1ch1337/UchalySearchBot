from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    description = State()
    is_photo = State()
    photo = State()