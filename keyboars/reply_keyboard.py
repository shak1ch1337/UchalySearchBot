from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("Отправить анкету на поиск")
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)


fsm_buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Начнем"),
            KeyboardButton(text = "Позже")
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)


have_photo_buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Да, у меня есть фото"),
            KeyboardButton(text = "Нет, у меня нет фото")
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)