from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

arb_ikb = InlineKeyboardMarkup(row_width=5,
                               inline_keyboard=[
                                   [
                                        InlineKeyboardButton(text='Удовлетварительно', callback_data='3'),
                                   ],
                                   [
                                        InlineKeyboardButton(text='Хорошо', callback_data='4'),
                                   ],
                                   [
                                        InlineKeyboardButton(text='Отлично', callback_data='5'),
                                   ],
                                   [
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                   ]
                               ])
