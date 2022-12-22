from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from table import endurance_1km, endurance_3km, endurance_5km

endurance_category_ikb = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='1 км', callback_data='1000'),
                                        InlineKeyboardButton(text='3 км', callback_data='3000'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='5 км', callback_data='5000'),

                                    ],

                                    [
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel')
                                    ]
                                ])


list_1000 = []
for key in endurance_1km:
    list_1000.append(key)

endurance_1000m_ikb_1 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[0]}', callback_data=f'{list_1000[0]}'),
                                        InlineKeyboardButton(text=f'{list_1000[1]}', callback_data=f'{list_1000[1]}'),
                                        InlineKeyboardButton(text=f'{list_1000[2]}', callback_data=f'{list_1000[2]}'),
                                        InlineKeyboardButton(text=f'{list_1000[3]}', callback_data=f'{list_1000[3]}'),
                                        InlineKeyboardButton(text=f'{list_1000[4]}', callback_data=f'{list_1000[4]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[5]}', callback_data=f'{list_1000[5]}'),
                                        InlineKeyboardButton(text=f'{list_1000[6]}', callback_data=f'{list_1000[6]}'),
                                        InlineKeyboardButton(text=f'{list_1000[7]}', callback_data=f'{list_1000[7]}'),
                                        InlineKeyboardButton(text=f'{list_1000[8]}', callback_data=f'{list_1000[8]}'),
                                        InlineKeyboardButton(text=f'{list_1000[9]}', callback_data=f'{list_1000[9]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[10]}', callback_data=f'{list_1000[10]}'),
                                        InlineKeyboardButton(text=f'{list_1000[11]}', callback_data=f'{list_1000[11]}'),
                                        InlineKeyboardButton(text=f'{list_1000[12]}', callback_data=f'{list_1000[12]}'),
                                        InlineKeyboardButton(text=f'{list_1000[13]}', callback_data=f'{list_1000[13]}'),
                                        InlineKeyboardButton(text=f'{list_1000[14]}', callback_data=f'{list_1000[14]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[15]}', callback_data=f'{list_1000[15]}'),
                                        InlineKeyboardButton(text=f'{list_1000[16]}', callback_data=f'{list_1000[16]}'),
                                        InlineKeyboardButton(text=f'{list_1000[17]}', callback_data=f'{list_1000[17]}'),
                                        InlineKeyboardButton(text=f'{list_1000[18]}', callback_data=f'{list_1000[18]}'),
                                        InlineKeyboardButton(text=f'{list_1000[19]}', callback_data=f'{list_1000[19]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[20]}', callback_data=f'{list_1000[20]}'),
                                        InlineKeyboardButton(text=f'{list_1000[21]}', callback_data=f'{list_1000[21]}'),
                                        InlineKeyboardButton(text=f'{list_1000[22]}', callback_data=f'{list_1000[22]}'),
                                        InlineKeyboardButton(text=f'{list_1000[23]}', callback_data=f'{list_1000[23]}'),
                                        InlineKeyboardButton(text=f'{list_1000[24]}', callback_data=f'{list_1000[24]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='1000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='1000m_next'),
                                    ]
                                ])


endurance_1000m_ikb_2 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[25]}', callback_data=f'{list_1000[25]}'),
                                        InlineKeyboardButton(text=f'{list_1000[26]}', callback_data=f'{list_1000[26]}'),
                                        InlineKeyboardButton(text=f'{list_1000[27]}', callback_data=f'{list_1000[27]}'),
                                        InlineKeyboardButton(text=f'{list_1000[28]}', callback_data=f'{list_1000[28]}'),
                                        InlineKeyboardButton(text=f'{list_1000[29]}', callback_data=f'{list_1000[29]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[30]}', callback_data=f'{list_1000[30]}'),
                                        InlineKeyboardButton(text=f'{list_1000[31]}', callback_data=f'{list_1000[31]}'),
                                        InlineKeyboardButton(text=f'{list_1000[32]}', callback_data=f'{list_1000[32]}'),
                                        InlineKeyboardButton(text=f'{list_1000[33]}', callback_data=f'{list_1000[33]}'),
                                        InlineKeyboardButton(text=f'{list_1000[34]}', callback_data=f'{list_1000[34]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[35]}', callback_data=f'{list_1000[35]}'),
                                        InlineKeyboardButton(text=f'{list_1000[36]}', callback_data=f'{list_1000[36]}'),
                                        InlineKeyboardButton(text=f'{list_1000[37]}', callback_data=f'{list_1000[37]}'),
                                        InlineKeyboardButton(text=f'{list_1000[38]}', callback_data=f'{list_1000[38]}'),
                                        InlineKeyboardButton(text=f'{list_1000[39]}', callback_data=f'{list_1000[39]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[40]}', callback_data=f'{list_1000[40]}'),
                                        InlineKeyboardButton(text=f'{list_1000[41]}', callback_data=f'{list_1000[41]}'),
                                        InlineKeyboardButton(text=f'{list_1000[42]}', callback_data=f'{list_1000[42]}'),
                                        InlineKeyboardButton(text=f'{list_1000[43]}', callback_data=f'{list_1000[43]}'),
                                        InlineKeyboardButton(text=f'{list_1000[44]}', callback_data=f'{list_1000[44]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[45]}', callback_data=f'{list_1000[45]}'),
                                        InlineKeyboardButton(text=f'{list_1000[46]}', callback_data=f'{list_1000[46]}'),
                                        InlineKeyboardButton(text=f'{list_1000[47]}', callback_data=f'{list_1000[47]}'),
                                        InlineKeyboardButton(text=f'{list_1000[48]}', callback_data=f'{list_1000[48]}'),
                                        InlineKeyboardButton(text=f'{list_1000[49]}', callback_data=f'{list_1000[49]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='1000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='1000m_next'),
                                    ]
                                ])


endurance_1000m_ikb_3 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[50]}', callback_data=f'{list_1000[50]}'),
                                        InlineKeyboardButton(text=f'{list_1000[51]}', callback_data=f'{list_1000[51]}'),
                                        InlineKeyboardButton(text=f'{list_1000[52]}', callback_data=f'{list_1000[52]}'),
                                        InlineKeyboardButton(text=f'{list_1000[53]}', callback_data=f'{list_1000[53]}'),
                                        InlineKeyboardButton(text=f'{list_1000[54]}', callback_data=f'{list_1000[54]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[55]}', callback_data=f'{list_1000[55]}'),
                                        InlineKeyboardButton(text=f'{list_1000[56]}', callback_data=f'{list_1000[56]}'),
                                        InlineKeyboardButton(text=f'{list_1000[57]}', callback_data=f'{list_1000[57]}'),
                                        InlineKeyboardButton(text=f'{list_1000[58]}', callback_data=f'{list_1000[58]}'),
                                        InlineKeyboardButton(text=f'{list_1000[59]}', callback_data=f'{list_1000[59]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[60]}', callback_data=f'{list_1000[60]}'),
                                        InlineKeyboardButton(text=f'{list_1000[61]}', callback_data=f'{list_1000[61]}'),
                                        InlineKeyboardButton(text=f'{list_1000[62]}', callback_data=f'{list_1000[62]}'),
                                        InlineKeyboardButton(text=f'{list_1000[63]}', callback_data=f'{list_1000[63]}'),
                                        InlineKeyboardButton(text=f'{list_1000[64]}', callback_data=f'{list_1000[64]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[65]}', callback_data=f'{list_1000[65]}'),
                                        InlineKeyboardButton(text=f'{list_1000[66]}', callback_data=f'{list_1000[66]}'),
                                        InlineKeyboardButton(text=f'{list_1000[67]}', callback_data=f'{list_1000[67]}'),
                                        InlineKeyboardButton(text=f'{list_1000[68]}', callback_data=f'{list_1000[68]}'),
                                        InlineKeyboardButton(text=f'{list_1000[69]}', callback_data=f'{list_1000[69]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[70]}', callback_data=f'{list_1000[70]}'),
                                        InlineKeyboardButton(text=f'{list_1000[71]}', callback_data=f'{list_1000[71]}'),
                                        InlineKeyboardButton(text=f'{list_1000[72]}', callback_data=f'{list_1000[72]}'),
                                        InlineKeyboardButton(text=f'{list_1000[73]}', callback_data=f'{list_1000[73]}'),
                                        InlineKeyboardButton(text=f'{list_1000[74]}', callback_data=f'{list_1000[74]}'),
                                    ],
[
                                        InlineKeyboardButton(text='⬅️', callback_data='1000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='1000m_next'),
                                    ]
                                ])


endurance_1000m_ikb_4 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[75]}', callback_data=f'{list_1000[75]}'),
                                        InlineKeyboardButton(text=f'{list_1000[76]}', callback_data=f'{list_1000[76]}'),
                                        InlineKeyboardButton(text=f'{list_1000[77]}', callback_data=f'{list_1000[77]}'),
                                        InlineKeyboardButton(text=f'{list_1000[78]}', callback_data=f'{list_1000[78]}'),
                                        InlineKeyboardButton(text=f'{list_1000[79]}', callback_data=f'{list_1000[79]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[80]}', callback_data=f'{list_1000[80]}'),
                                        InlineKeyboardButton(text=f'{list_1000[81]}', callback_data=f'{list_1000[81]}'),
                                        InlineKeyboardButton(text=f'{list_1000[82]}', callback_data=f'{list_1000[82]}'),
                                        InlineKeyboardButton(text=f'{list_1000[83]}', callback_data=f'{list_1000[83]}'),
                                        InlineKeyboardButton(text=f'{list_1000[84]}', callback_data=f'{list_1000[84]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_1000[85]}', callback_data=f'{list_1000[85]}'),
                                        InlineKeyboardButton(text=f'{list_1000[86]}', callback_data=f'{list_1000[86]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='1000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='1000m_next'),
                                    ]
                                ])


list_3000 = []
for key in endurance_3km:
    list_3000.append(key)

endurance_3000m_ikb_1 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[0]}', callback_data=f'{list_3000[0]}'),
                                        InlineKeyboardButton(text=f'{list_3000[1]}', callback_data=f'{list_3000[1]}'),
                                        InlineKeyboardButton(text=f'{list_3000[2]}', callback_data=f'{list_3000[2]}'),
                                        InlineKeyboardButton(text=f'{list_3000[3]}', callback_data=f'{list_3000[3]}'),
                                        InlineKeyboardButton(text=f'{list_3000[4]}', callback_data=f'{list_3000[4]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[5]}', callback_data=f'{list_3000[5]}'),
                                        InlineKeyboardButton(text=f'{list_3000[6]}', callback_data=f'{list_3000[6]}'),
                                        InlineKeyboardButton(text=f'{list_3000[7]}', callback_data=f'{list_3000[7]}'),
                                        InlineKeyboardButton(text=f'{list_3000[8]}', callback_data=f'{list_3000[8]}'),
                                        InlineKeyboardButton(text=f'{list_3000[9]}', callback_data=f'{list_3000[9]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[10]}', callback_data=f'{list_3000[10]}'),
                                        InlineKeyboardButton(text=f'{list_3000[11]}', callback_data=f'{list_3000[11]}'),
                                        InlineKeyboardButton(text=f'{list_3000[12]}', callback_data=f'{list_3000[12]}'),
                                        InlineKeyboardButton(text=f'{list_3000[13]}', callback_data=f'{list_3000[13]}'),
                                        InlineKeyboardButton(text=f'{list_3000[14]}', callback_data=f'{list_3000[14]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[15]}', callback_data=f'{list_3000[15]}'),
                                        InlineKeyboardButton(text=f'{list_3000[16]}', callback_data=f'{list_3000[16]}'),
                                        InlineKeyboardButton(text=f'{list_3000[17]}', callback_data=f'{list_3000[17]}'),
                                        InlineKeyboardButton(text=f'{list_3000[18]}', callback_data=f'{list_3000[18]}'),
                                        InlineKeyboardButton(text=f'{list_3000[19]}', callback_data=f'{list_3000[19]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[20]}', callback_data=f'{list_3000[20]}'),
                                        InlineKeyboardButton(text=f'{list_3000[21]}', callback_data=f'{list_3000[21]}'),
                                        InlineKeyboardButton(text=f'{list_3000[22]}', callback_data=f'{list_3000[22]}'),
                                        InlineKeyboardButton(text=f'{list_3000[23]}', callback_data=f'{list_3000[23]}'),
                                        InlineKeyboardButton(text=f'{list_3000[24]}', callback_data=f'{list_3000[24]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[25]}', callback_data=f'{list_3000[25]}'),
                                        InlineKeyboardButton(text=f'{list_3000[26]}', callback_data=f'{list_3000[26]}'),
                                        InlineKeyboardButton(text=f'{list_3000[27]}', callback_data=f'{list_3000[27]}'),
                                        InlineKeyboardButton(text=f'{list_3000[28]}', callback_data=f'{list_3000[28]}'),
                                        InlineKeyboardButton(text=f'{list_3000[29]}', callback_data=f'{list_3000[29]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[30]}', callback_data=f'{list_3000[30]}'),
                                        InlineKeyboardButton(text=f'{list_3000[31]}', callback_data=f'{list_3000[31]}'),
                                    ],

                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='3000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='3000m_next'),
                                    ]
                                    ])


endurance_3000m_ikb_2 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[32]}', callback_data=f'{list_3000[32]}'),
                                        InlineKeyboardButton(text=f'{list_3000[33]}', callback_data=f'{list_3000[33]}'),
                                        InlineKeyboardButton(text=f'{list_3000[34]}', callback_data=f'{list_3000[34]}'),
                                        InlineKeyboardButton(text=f'{list_3000[35]}', callback_data=f'{list_3000[35]}'),
                                        InlineKeyboardButton(text=f'{list_3000[36]}', callback_data=f'{list_3000[36]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[37]}', callback_data=f'{list_3000[37]}'),
                                        InlineKeyboardButton(text=f'{list_3000[38]}', callback_data=f'{list_3000[38]}'),
                                        InlineKeyboardButton(text=f'{list_3000[39]}', callback_data=f'{list_3000[39]}'),
                                        InlineKeyboardButton(text=f'{list_3000[40]}', callback_data=f'{list_3000[40]}'),
                                        InlineKeyboardButton(text=f'{list_3000[41]}', callback_data=f'{list_3000[41]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[42]}', callback_data=f'{list_3000[42]}'),
                                        InlineKeyboardButton(text=f'{list_3000[43]}', callback_data=f'{list_3000[43]}'),
                                        InlineKeyboardButton(text=f'{list_3000[44]}', callback_data=f'{list_3000[44]}'),
                                        InlineKeyboardButton(text=f'{list_3000[45]}', callback_data=f'{list_3000[45]}'),
                                        InlineKeyboardButton(text=f'{list_3000[46]}', callback_data=f'{list_3000[46]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[47]}', callback_data=f'{list_3000[47]}'),
                                        InlineKeyboardButton(text=f'{list_3000[48]}', callback_data=f'{list_3000[48]}'),
                                        InlineKeyboardButton(text=f'{list_3000[49]}', callback_data=f'{list_3000[49]}'),
                                        InlineKeyboardButton(text=f'{list_3000[50]}', callback_data=f'{list_3000[50]}'),
                                        InlineKeyboardButton(text=f'{list_3000[51]}', callback_data=f'{list_3000[51]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[52]}', callback_data=f'{list_3000[52]}'),
                                        InlineKeyboardButton(text=f'{list_3000[53]}', callback_data=f'{list_3000[53]}'),
                                        InlineKeyboardButton(text=f'{list_3000[54]}', callback_data=f'{list_3000[54]}'),
                                        InlineKeyboardButton(text=f'{list_3000[55]}', callback_data=f'{list_3000[55]}'),
                                        InlineKeyboardButton(text=f'{list_3000[56]}', callback_data=f'{list_3000[56]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[57]}', callback_data=f'{list_3000[57]}'),
                                        InlineKeyboardButton(text=f'{list_3000[58]}', callback_data=f'{list_3000[58]}'),
                                        InlineKeyboardButton(text=f'{list_3000[59]}', callback_data=f'{list_3000[59]}'),
                                        InlineKeyboardButton(text=f'{list_3000[60]}', callback_data=f'{list_3000[60]}'),
                                        InlineKeyboardButton(text=f'{list_3000[61]}', callback_data=f'{list_3000[61]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[62]}', callback_data=f'{list_3000[62]}'),
                                        InlineKeyboardButton(text=f'{list_3000[63]}', callback_data=f'{list_3000[63]}'),
                                    ],

                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='3000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='3000m_next'),
                                    ]
                                    ])

endurance_3000m_ikb_3 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[64]}', callback_data=f'{list_3000[64]}'),
                                        InlineKeyboardButton(text=f'{list_3000[65]}', callback_data=f'{list_3000[65]}'),
                                        InlineKeyboardButton(text=f'{list_3000[66]}', callback_data=f'{list_3000[66]}'),
                                        InlineKeyboardButton(text=f'{list_3000[67]}', callback_data=f'{list_3000[67]}'),
                                        InlineKeyboardButton(text=f'{list_3000[68]}', callback_data=f'{list_3000[68]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[69]}', callback_data=f'{list_3000[69]}'),
                                        InlineKeyboardButton(text=f'{list_3000[70]}', callback_data=f'{list_3000[70]}'),
                                        InlineKeyboardButton(text=f'{list_3000[71]}', callback_data=f'{list_3000[71]}'),
                                        InlineKeyboardButton(text=f'{list_3000[72]}', callback_data=f'{list_3000[72]}'),
                                        InlineKeyboardButton(text=f'{list_3000[73]}', callback_data=f'{list_3000[73]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[74]}', callback_data=f'{list_3000[74]}'),
                                        InlineKeyboardButton(text=f'{list_3000[75]}', callback_data=f'{list_3000[75]}'),
                                        InlineKeyboardButton(text=f'{list_3000[76]}', callback_data=f'{list_3000[76]}'),
                                        InlineKeyboardButton(text=f'{list_3000[77]}', callback_data=f'{list_3000[77]}'),
                                        InlineKeyboardButton(text=f'{list_3000[78]}', callback_data=f'{list_3000[78]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[79]}', callback_data=f'{list_3000[79]}'),
                                        InlineKeyboardButton(text=f'{list_3000[80]}', callback_data=f'{list_3000[80]}'),
                                        InlineKeyboardButton(text=f'{list_3000[81]}', callback_data=f'{list_3000[81]}'),
                                        InlineKeyboardButton(text=f'{list_3000[82]}', callback_data=f'{list_3000[82]}'),
                                        InlineKeyboardButton(text=f'{list_3000[83]}', callback_data=f'{list_3000[83]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[84]}', callback_data=f'{list_3000[84]}'),
                                        InlineKeyboardButton(text=f'{list_3000[85]}', callback_data=f'{list_3000[85]}'),
                                        InlineKeyboardButton(text=f'{list_3000[86]}', callback_data=f'{list_3000[86]}'),
                                        InlineKeyboardButton(text=f'{list_3000[87]}', callback_data=f'{list_3000[87]}'),
                                        InlineKeyboardButton(text=f'{list_3000[88]}', callback_data=f'{list_3000[88]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[89]}', callback_data=f'{list_3000[89]}'),
                                        InlineKeyboardButton(text=f'{list_3000[90]}', callback_data=f'{list_3000[90]}'),
                                        InlineKeyboardButton(text=f'{list_3000[91]}', callback_data=f'{list_3000[91]}'),
                                        InlineKeyboardButton(text=f'{list_3000[92]}', callback_data=f'{list_3000[92]}'),
                                        InlineKeyboardButton(text=f'{list_3000[93]}', callback_data=f'{list_3000[93]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_3000[94]}', callback_data=f'{list_3000[94]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='3000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='3000m_next'),
                                    ]
                                ])


list_5000 = []
for key in endurance_5km:
    list_5000.append(key)
    
endurance_5000m_ikb_1 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[0]}', callback_data=f'{list_5000[0]}'),
                                        InlineKeyboardButton(text=f'{list_5000[1]}', callback_data=f'{list_5000[1]}'),
                                        InlineKeyboardButton(text=f'{list_5000[2]}', callback_data=f'{list_5000[2]}'),
                                        InlineKeyboardButton(text=f'{list_5000[3]}', callback_data=f'{list_5000[3]}'),
                                        InlineKeyboardButton(text=f'{list_5000[4]}', callback_data=f'{list_5000[4]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[5]}', callback_data=f'{list_5000[5]}'),
                                        InlineKeyboardButton(text=f'{list_5000[6]}', callback_data=f'{list_5000[6]}'),
                                        InlineKeyboardButton(text=f'{list_5000[7]}', callback_data=f'{list_5000[7]}'),
                                        InlineKeyboardButton(text=f'{list_5000[8]}', callback_data=f'{list_5000[8]}'),
                                        InlineKeyboardButton(text=f'{list_5000[9]}', callback_data=f'{list_5000[9]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[10]}', callback_data=f'{list_5000[10]}'),
                                        InlineKeyboardButton(text=f'{list_5000[11]}', callback_data=f'{list_5000[11]}'),
                                        InlineKeyboardButton(text=f'{list_5000[12]}', callback_data=f'{list_5000[12]}'),
                                        InlineKeyboardButton(text=f'{list_5000[13]}', callback_data=f'{list_5000[13]}'),
                                        InlineKeyboardButton(text=f'{list_5000[14]}', callback_data=f'{list_5000[14]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[15]}', callback_data=f'{list_5000[15]}'),
                                        InlineKeyboardButton(text=f'{list_5000[16]}', callback_data=f'{list_5000[16]}'),
                                        InlineKeyboardButton(text=f'{list_5000[17]}', callback_data=f'{list_5000[17]}'),
                                        InlineKeyboardButton(text=f'{list_5000[18]}', callback_data=f'{list_5000[18]}'),
                                        InlineKeyboardButton(text=f'{list_5000[19]}', callback_data=f'{list_5000[19]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[20]}', callback_data=f'{list_5000[20]}'),
                                        InlineKeyboardButton(text=f'{list_5000[21]}', callback_data=f'{list_5000[21]}'),
                                        InlineKeyboardButton(text=f'{list_5000[22]}', callback_data=f'{list_5000[22]}'),
                                        InlineKeyboardButton(text=f'{list_5000[23]}', callback_data=f'{list_5000[23]}'),
                                        InlineKeyboardButton(text=f'{list_5000[24]}', callback_data=f'{list_5000[24]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='5000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='5000m_next'),
                                    ]
                                    ])

endurance_5000m_ikb_2 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[25]}', callback_data=f'{list_5000[25]}'),
                                        InlineKeyboardButton(text=f'{list_5000[26]}', callback_data=f'{list_5000[26]}'),
                                        InlineKeyboardButton(text=f'{list_5000[27]}', callback_data=f'{list_5000[27]}'),
                                        InlineKeyboardButton(text=f'{list_5000[28]}', callback_data=f'{list_5000[28]}'),
                                        InlineKeyboardButton(text=f'{list_5000[29]}', callback_data=f'{list_5000[29]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[30]}', callback_data=f'{list_5000[30]}'),
                                        InlineKeyboardButton(text=f'{list_5000[31]}', callback_data=f'{list_5000[31]}'),
                                        InlineKeyboardButton(text=f'{list_5000[32]}', callback_data=f'{list_5000[32]}'),
                                        InlineKeyboardButton(text=f'{list_5000[33]}', callback_data=f'{list_5000[33]}'),
                                        InlineKeyboardButton(text=f'{list_5000[34]}', callback_data=f'{list_5000[34]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[35]}', callback_data=f'{list_5000[35]}'),
                                        InlineKeyboardButton(text=f'{list_5000[36]}', callback_data=f'{list_5000[36]}'),
                                        InlineKeyboardButton(text=f'{list_5000[37]}', callback_data=f'{list_5000[37]}'),
                                        InlineKeyboardButton(text=f'{list_5000[38]}', callback_data=f'{list_5000[38]}'),
                                        InlineKeyboardButton(text=f'{list_5000[39]}', callback_data=f'{list_5000[39]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[40]}', callback_data=f'{list_5000[40]}'),
                                        InlineKeyboardButton(text=f'{list_5000[41]}', callback_data=f'{list_5000[41]}'),
                                        InlineKeyboardButton(text=f'{list_5000[42]}', callback_data=f'{list_5000[42]}'),
                                        InlineKeyboardButton(text=f'{list_5000[43]}', callback_data=f'{list_5000[43]}'),
                                        InlineKeyboardButton(text=f'{list_5000[44]}', callback_data=f'{list_5000[44]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[45]}', callback_data=f'{list_5000[45]}'),
                                        InlineKeyboardButton(text=f'{list_5000[46]}', callback_data=f'{list_5000[46]}'),
                                        InlineKeyboardButton(text=f'{list_5000[47]}', callback_data=f'{list_5000[47]}'),
                                        InlineKeyboardButton(text=f'{list_5000[48]}', callback_data=f'{list_5000[48]}'),
                                        InlineKeyboardButton(text=f'{list_5000[49]}', callback_data=f'{list_5000[49]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='5000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='5000m_next'),
                                    ]
                                    ])

endurance_5000m_ikb_3 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[50]}', callback_data=f'{list_5000[50]}'),
                                        InlineKeyboardButton(text=f'{list_5000[51]}', callback_data=f'{list_5000[51]}'),
                                        InlineKeyboardButton(text=f'{list_5000[52]}', callback_data=f'{list_5000[52]}'),
                                        InlineKeyboardButton(text=f'{list_5000[53]}', callback_data=f'{list_5000[53]}'),
                                        InlineKeyboardButton(text=f'{list_5000[54]}', callback_data=f'{list_5000[54]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[55]}', callback_data=f'{list_5000[55]}'),
                                        InlineKeyboardButton(text=f'{list_5000[56]}', callback_data=f'{list_5000[56]}'),
                                        InlineKeyboardButton(text=f'{list_5000[57]}', callback_data=f'{list_5000[57]}'),
                                        InlineKeyboardButton(text=f'{list_5000[58]}', callback_data=f'{list_5000[58]}'),
                                        InlineKeyboardButton(text=f'{list_5000[59]}', callback_data=f'{list_5000[59]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[60]}', callback_data=f'{list_5000[60]}'),
                                        InlineKeyboardButton(text=f'{list_5000[61]}', callback_data=f'{list_5000[61]}'),
                                        InlineKeyboardButton(text=f'{list_5000[62]}', callback_data=f'{list_5000[62]}'),
                                        InlineKeyboardButton(text=f'{list_5000[63]}', callback_data=f'{list_5000[63]}'),
                                        InlineKeyboardButton(text=f'{list_5000[64]}', callback_data=f'{list_5000[64]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[65]}', callback_data=f'{list_5000[65]}'),
                                        InlineKeyboardButton(text=f'{list_5000[66]}', callback_data=f'{list_5000[66]}'),
                                        InlineKeyboardButton(text=f'{list_5000[67]}', callback_data=f'{list_5000[67]}'),
                                        InlineKeyboardButton(text=f'{list_5000[68]}', callback_data=f'{list_5000[68]}'),
                                        InlineKeyboardButton(text=f'{list_5000[69]}', callback_data=f'{list_5000[69]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[70]}', callback_data=f'{list_5000[70]}'),
                                        InlineKeyboardButton(text=f'{list_5000[71]}', callback_data=f'{list_5000[71]}'),
                                        InlineKeyboardButton(text=f'{list_5000[72]}', callback_data=f'{list_5000[72]}'),
                                        InlineKeyboardButton(text=f'{list_5000[73]}', callback_data=f'{list_5000[73]}'),
                                        InlineKeyboardButton(text=f'{list_5000[74]}', callback_data=f'{list_5000[74]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='5000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='5000m_next'),
                                    ]
                                    ])
endurance_5000m_ikb_4 = InlineKeyboardMarkup(row_width=5,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[75]}', callback_data=f'{list_5000[75]}'),
                                        InlineKeyboardButton(text=f'{list_5000[76]}', callback_data=f'{list_5000[76]}'),
                                        InlineKeyboardButton(text=f'{list_5000[77]}', callback_data=f'{list_5000[77]}'),
                                        InlineKeyboardButton(text=f'{list_5000[78]}', callback_data=f'{list_5000[78]}'),
                                        InlineKeyboardButton(text=f'{list_5000[79]}', callback_data=f'{list_5000[79]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[80]}', callback_data=f'{list_5000[80]}'),
                                        InlineKeyboardButton(text=f'{list_5000[81]}', callback_data=f'{list_5000[81]}'),
                                        InlineKeyboardButton(text=f'{list_5000[82]}', callback_data=f'{list_5000[82]}'),
                                        InlineKeyboardButton(text=f'{list_5000[83]}', callback_data=f'{list_5000[83]}'),
                                        InlineKeyboardButton(text=f'{list_5000[84]}', callback_data=f'{list_5000[84]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[85]}', callback_data=f'{list_5000[85]}'),
                                        InlineKeyboardButton(text=f'{list_5000[86]}', callback_data=f'{list_5000[86]}'),
                                        InlineKeyboardButton(text=f'{list_5000[87]}', callback_data=f'{list_5000[87]}'),
                                        InlineKeyboardButton(text=f'{list_5000[88]}', callback_data=f'{list_5000[88]}'),
                                        InlineKeyboardButton(text=f'{list_5000[89]}', callback_data=f'{list_5000[89]}'),

                                    ],
                                    [
                                        InlineKeyboardButton(text=f'{list_5000[90]}', callback_data=f'{list_5000[90]}'),
                                        InlineKeyboardButton(text=f'{list_5000[91]}', callback_data=f'{list_5000[91]}'),
                                        InlineKeyboardButton(text=f'{list_5000[92]}', callback_data=f'{list_5000[92]}'),
                                        InlineKeyboardButton(text=f'{list_5000[93]}', callback_data=f'{list_5000[93]}'),
                                        InlineKeyboardButton(text=f'{list_5000[94]}', callback_data=f'{list_5000[94]}'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='⬅️', callback_data='5000m_back'),
                                        InlineKeyboardButton(text='Возврат в меню', callback_data='cancel'),
                                        InlineKeyboardButton(text='➡️', callback_data='5000m_next'),
                                    ]
                                ])