from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

age_group_ikb = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Первая', callback_data='Первая'),
                                        # InlineKeyboardButton(text='Вторая', callback_data='Вторая'),
                                        # InlineKeyboardButton(text='Третья', callback_data='Третья'),
                                        # InlineKeyboardButton(text='Четвертая', callback_data='Четвертая'),
                                        # InlineKeyboardButton(text='Пятая', callback_data='Пятая')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Возврат меню', callback_data='cancel')
                                    ]
                                ])