from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Посчитать баллы'),
            KeyboardButton(text='Помощь при сдаче'),
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)