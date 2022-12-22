from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from table import speed_60m_list, speed_100m_list, speed_10x10_list

speed_category_ikb = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='60 метров', callback_data='60'),
                                        InlineKeyboardButton(text='100 метров', callback_data='100'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='10х10', callback_data='10x10'),
                                        InlineKeyboardButton(text='Назад', callback_data="speed_back")
                                    ],
                                    [
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                    ]
                                ])




list_60 = []
for key in speed_60m_list:
    list_60.append(key)
speed_60m_ikb_1 = InlineKeyboardMarkup(row_width=4,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_60[0]}', callback_data=f'{list_60[0]}'),
                                        InlineKeyboardButton(text=f'{list_60[1]}', callback_data=f'{list_60[1]}'),
                                        InlineKeyboardButton(text=f'{list_60[2]}', callback_data=f'{list_60[2]}'),
                                        InlineKeyboardButton(text=f'{list_60[3]}', callback_data=f'{list_60[3]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_60[4]}', callback_data=f'{list_60[4]}'),
                                        InlineKeyboardButton(text=f'{list_60[5]}', callback_data=f'{list_60[5]}'),
                                        InlineKeyboardButton(text=f'{list_60[6]}', callback_data=f'{list_60[6]}'),
                                        InlineKeyboardButton(text=f'{list_60[7]}', callback_data=f'{list_60[7]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_60[8]}', callback_data=f'{list_60[8]}'),
                                        InlineKeyboardButton(text=f'{list_60[9]}', callback_data=f'{list_60[9]}'),
                                        InlineKeyboardButton(text=f'{list_60[10]}', callback_data=f'{list_60[10]}'),
                                        InlineKeyboardButton(text=f'{list_60[11]}', callback_data=f'{list_60[11]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_60[12]}', callback_data=f'{list_60[12]}'),
                                        InlineKeyboardButton(text=f'{list_60[13]}', callback_data=f'{list_60[13]}'),
                                        InlineKeyboardButton(text=f'{list_60[14]}', callback_data=f'{list_60[14]}'),
                                        InlineKeyboardButton(text=f'{list_60[15]}', callback_data=f'{list_60[15]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='60m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='60m_next'),
                                    ]
                                ])
speed_60m_ikb_2 = InlineKeyboardMarkup(row_width=4,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_60[16]}', callback_data=f'{list_60[16]}'),
                                        InlineKeyboardButton(text=f'{list_60[17]}', callback_data=f'{list_60[17]}'),
                                        InlineKeyboardButton(text=f'{list_60[18]}', callback_data=f'{list_60[18]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_60[19]}', callback_data=f'{list_60[19]}'),
                                        InlineKeyboardButton(text=f'{list_60[20]}', callback_data=f'{list_60[20]}'),
                                        InlineKeyboardButton(text=f'{list_60[21]}', callback_data=f'{list_60[21]}'),
                                        InlineKeyboardButton(text=f'{list_60[22]}', callback_data=f'{list_60[22]}'),
                                    ],

                                    [
                                        InlineKeyboardButton(text=f'{list_60[23]}', callback_data=f'{list_60[23]}'),
                                        InlineKeyboardButton(text=f'{list_60[24]}', callback_data=f'{list_60[24]}'),
                                        InlineKeyboardButton(text=f'{list_60[25]}', callback_data=f'{list_60[25]}'),
                                        InlineKeyboardButton(text=f'{list_60[26]}', callback_data=f'{list_60[26]}'),
                                        InlineKeyboardButton(text=f'{list_60[27]}', callback_data=f'{list_60[27]}'),
                                    ],

                                    [
                                        InlineKeyboardButton(text=f'{list_60[28]}', callback_data=f'{list_60[28]}'),
                                        InlineKeyboardButton(text=f'{list_60[29]}', callback_data=f'{list_60[29]}'),
                                        InlineKeyboardButton(text=f'{list_60[30]}', callback_data=f'{list_60[30]}'),
                                        InlineKeyboardButton(text=f'{list_60[31]}', callback_data=f'{list_60[31]}'),

                                    ],

                                    [
                                        InlineKeyboardButton(text=f'{list_60[32]}', callback_data=f'{list_60[32]}'),
                                        InlineKeyboardButton(text=f'{list_60[33]}', callback_data=f'{list_60[33]}'),
                                        InlineKeyboardButton(text=f'{list_60[34]}', callback_data=f'{list_60[34]}'),
                                        InlineKeyboardButton(text=f'{list_60[35]}', callback_data=f'{list_60[35]}'),
                                    ],

                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='60m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='60m_next'),
                                    ]
                                ])


list_100 = []
for key in speed_100m_list:
    list_100.append(key)
speed_100m_ikb = InlineKeyboardMarkup(row_width=6,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_100[0]}', callback_data=f'{list_100[0]}'),
                                        InlineKeyboardButton(text=f'{list_100[1]}', callback_data=f'{list_100[1]}'),
                                        InlineKeyboardButton(text=f'{list_100[2]}', callback_data=f'{list_100[2]}'),
                                        InlineKeyboardButton(text=f'{list_100[3]}', callback_data=f'{list_100[3]}'),
                                        InlineKeyboardButton(text=f'{list_100[4]}', callback_data=f'{list_100[4]}'),
                                        InlineKeyboardButton(text=f'{list_100[5]}', callback_data=f'{list_100[5]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[6]}', callback_data=f'{list_100[6]}'),
                                        InlineKeyboardButton(text=f'{list_100[7]}', callback_data=f'{list_100[7]}'),
                                        InlineKeyboardButton(text=f'{list_100[8]}', callback_data=f'{list_100[8]}'),
                                        InlineKeyboardButton(text=f'{list_100[9]}', callback_data=f'{list_100[9]}'),
                                        InlineKeyboardButton(text=f'{list_100[10]}', callback_data=f'{list_100[10]}'),
                                        InlineKeyboardButton(text=f'{list_100[11]}', callback_data=f'{list_100[11]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[12]}', callback_data=f'{list_100[12]}'),
                                        InlineKeyboardButton(text=f'{list_100[13]}', callback_data=f'{list_100[13]}'),
                                        InlineKeyboardButton(text=f'{list_100[14]}', callback_data=f'{list_100[14]}'),
                                        InlineKeyboardButton(text=f'{list_100[15]}', callback_data=f'{list_100[15]}'),
                                        InlineKeyboardButton(text=f'{list_100[16]}', callback_data=f'{list_100[16]}'),
                                        InlineKeyboardButton(text=f'{list_100[17]}', callback_data=f'{list_100[17]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[18]}', callback_data=f'{list_100[18]}'),
                                        InlineKeyboardButton(text=f'{list_100[19]}', callback_data=f'{list_100[19]}'),
                                        InlineKeyboardButton(text=f'{list_100[20]}', callback_data=f'{list_100[20]}'),
                                        InlineKeyboardButton(text=f'{list_100[21]}', callback_data=f'{list_100[21]}'),
                                        InlineKeyboardButton(text=f'{list_100[22]}', callback_data=f'{list_100[22]}'),
                                        InlineKeyboardButton(text=f'{list_100[23]}', callback_data=f'{list_100[23]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[24]}', callback_data=f'{list_100[24]}'),
                                        InlineKeyboardButton(text=f'{list_100[25]}', callback_data=f'{list_100[25]}'),
                                        InlineKeyboardButton(text=f'{list_100[26]}', callback_data=f'{list_100[26]}'),
                                        InlineKeyboardButton(text=f'{list_100[27]}', callback_data=f'{list_100[27]}'),
                                        InlineKeyboardButton(text=f'{list_100[28]}', callback_data=f'{list_100[28]}'),
                                        InlineKeyboardButton(text=f'{list_100[29]}', callback_data=f'{list_100[29]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[30]}', callback_data=f'{list_100[30]}'),
                                        InlineKeyboardButton(text=f'{list_100[31]}', callback_data=f'{list_100[31]}'),
                                        InlineKeyboardButton(text=f'{list_100[32]}', callback_data=f'{list_100[32]}'),
                                        InlineKeyboardButton(text=f'{list_100[33]}', callback_data=f'{list_100[33]}'),
                                        InlineKeyboardButton(text=f'{list_100[34]}', callback_data=f'{list_100[34]}'),
                                        InlineKeyboardButton(text=f'{list_100[35]}', callback_data=f'{list_100[35]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[36]}', callback_data=f'{list_100[36]}'),
                                        InlineKeyboardButton(text=f'{list_100[37]}', callback_data=f'{list_100[37]}'),
                                        InlineKeyboardButton(text=f'{list_100[38]}', callback_data=f'{list_100[38]}'),
                                        InlineKeyboardButton(text=f'{list_100[39]}', callback_data=f'{list_100[39]}'),
                                        InlineKeyboardButton(text=f'{list_100[40]}', callback_data=f'{list_100[40]}'),
                                        InlineKeyboardButton(text=f'{list_100[41]}', callback_data=f'{list_100[41]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[42]}', callback_data=f'{list_100[42]}'),
                                        InlineKeyboardButton(text=f'{list_100[43]}', callback_data=f'{list_100[43]}'),
                                        InlineKeyboardButton(text=f'{list_100[44]}', callback_data=f'{list_100[44]}'),
                                        InlineKeyboardButton(text=f'{list_100[45]}', callback_data=f'{list_100[45]}'),
                                        InlineKeyboardButton(text=f'{list_100[46]}', callback_data=f'{list_100[46]}'),
                                        InlineKeyboardButton(text=f'{list_100[47]}', callback_data=f'{list_100[47]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[48]}', callback_data=f'{list_100[48]}'),
                                        InlineKeyboardButton(text=f'{list_100[49]}', callback_data=f'{list_100[49]}'),
                                        InlineKeyboardButton(text=f'{list_100[50]}', callback_data=f'{list_100[50]}'),
                                        InlineKeyboardButton(text=f'{list_100[51]}', callback_data=f'{list_100[51]}'),
                                        InlineKeyboardButton(text=f'{list_100[52]}', callback_data=f'{list_100[52]}'),
                                        InlineKeyboardButton(text=f'{list_100[53]}', callback_data=f'{list_100[53]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_100[54]}', callback_data=f'{list_100[54]}'),
                                        InlineKeyboardButton(text=f'{list_100[55]}', callback_data=f'{list_100[55]}'),
                                        InlineKeyboardButton(text=f'{list_100[56]}', callback_data=f'{list_100[56]}'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                    ],

                                ])


list_10x10 = []
for key in speed_10x10_list:
    list_10x10.append(key)
speed_10x10_ikb = InlineKeyboardMarkup(row_width=6,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[0]}', callback_data=f'{list_10x10[0]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[1]}', callback_data=f'{list_10x10[1]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[2]}', callback_data=f'{list_10x10[2]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[3]}', callback_data=f'{list_10x10[3]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[4]}', callback_data=f'{list_10x10[4]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[5]}', callback_data=f'{list_10x10[5]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[6]}', callback_data=f'{list_10x10[6]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[7]}', callback_data=f'{list_10x10[7]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[8]}', callback_data=f'{list_10x10[8]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[9]}', callback_data=f'{list_10x10[9]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[10]}', callback_data=f'{list_10x10[10]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[11]}', callback_data=f'{list_10x10[11]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[12]}', callback_data=f'{list_10x10[12]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[13]}', callback_data=f'{list_10x10[13]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[14]}', callback_data=f'{list_10x10[14]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[15]}', callback_data=f'{list_10x10[15]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[16]}', callback_data=f'{list_10x10[16]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[17]}', callback_data=f'{list_10x10[17]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[18]}', callback_data=f'{list_10x10[18]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[19]}', callback_data=f'{list_10x10[19]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[20]}', callback_data=f'{list_10x10[20]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[21]}', callback_data=f'{list_10x10[21]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[22]}', callback_data=f'{list_10x10[22]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[23]}', callback_data=f'{list_10x10[23]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[24]}', callback_data=f'{list_10x10[24]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[25]}', callback_data=f'{list_10x10[25]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[26]}', callback_data=f'{list_10x10[26]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[27]}', callback_data=f'{list_10x10[27]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[28]}', callback_data=f'{list_10x10[28]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[29]}', callback_data=f'{list_10x10[29]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[30]}', callback_data=f'{list_10x10[30]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[31]}', callback_data=f'{list_10x10[31]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[32]}', callback_data=f'{list_10x10[32]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[33]}', callback_data=f'{list_10x10[33]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[34]}', callback_data=f'{list_10x10[34]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[35]}', callback_data=f'{list_10x10[35]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[36]}', callback_data=f'{list_10x10[36]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[37]}', callback_data=f'{list_10x10[37]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[38]}', callback_data=f'{list_10x10[38]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[39]}', callback_data=f'{list_10x10[39]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[40]}', callback_data=f'{list_10x10[40]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[41]}', callback_data=f'{list_10x10[41]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[42]}', callback_data=f'{list_10x10[42]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[43]}', callback_data=f'{list_10x10[43]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[44]}', callback_data=f'{list_10x10[44]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[45]}', callback_data=f'{list_10x10[45]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[46]}', callback_data=f'{list_10x10[46]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[47]}', callback_data=f'{list_10x10[47]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[48]}', callback_data=f'{list_10x10[48]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[49]}', callback_data=f'{list_10x10[49]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[50]}', callback_data=f'{list_10x10[50]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[51]}', callback_data=f'{list_10x10[51]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[52]}', callback_data=f'{list_10x10[52]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[53]}', callback_data=f'{list_10x10[53]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_10x10[54]}', callback_data=f'{list_10x10[54]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[55]}', callback_data=f'{list_10x10[55]}'),
                                        InlineKeyboardButton(text=f'{list_10x10[56]}', callback_data=f'{list_10x10[56]}'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                    ],

                                ])







