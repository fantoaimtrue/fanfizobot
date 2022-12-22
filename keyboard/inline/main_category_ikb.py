from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_category_ikb = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Сила', callback_data='Сила'),
                                        InlineKeyboardButton(text='Скорость', callback_data='Скорость'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Выносливость', callback_data='Выносливость'),
                                        InlineKeyboardButton(text='Военноприкладной', callback_data='Военноприкладной'),
                                        InlineKeyboardButton(text='cancel', callback_data='cancel')
                                    ]
                                ])