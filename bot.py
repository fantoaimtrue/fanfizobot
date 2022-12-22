from pprint import pprint

from aiogram.types import CallbackQuery

from config import *  # конфиг с значениями
from data.config import NGROK_TOKEN

from db import Db  # подключение к БД
import logging

from data import config

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from pyngrok import ngrok
import datetime
from filters import IsPrivate # Подключение фильтров для чата
from keyboard.default import kb_menu # Подключение базовой клавиатуры
from states import Calc # Подключение машины состояний

from keyboard.inline import speed_60m_ikb_1, speed_100m_ikb, arb_ikb, speed_10x10_ikb, endurance_category_ikb, \
     main_category_ikb, age_group_ikb, power_category_ikb, \
    speed_category_ikb, pull_up_ikb, rise_with_coup_ikb, rise_with_force_ikb, speed_60m_ikb_2 # Подключение инлайн клавиатуры


from keyboard.inline.endurance_ikb import endurance_1000m_ikb_1, endurance_1000m_ikb_2, endurance_1000m_ikb_3, \
    endurance_1000m_ikb_4, endurance_3000m_ikb_1, endurance_3000m_ikb_2, endurance_3000m_ikb_3, endurance_5000m_ikb_1, \
    endurance_5000m_ikb_2, endurance_5000m_ikb_3, endurance_5000m_ikb_4 # Подключение инлайн клавиатуры


from table import speed_60m_list, speed_100m_list, speed_10x10_list, V_P_N, endurance_1km, endurance_3km, endurance_5km, \
    pull_up, rise_with_coup, rise_with_force # Подключение инлайн клавиатуры

# подключение к серверу NGROK
ngrok.set_auth_token(NGROK_TOKEN)
http_tunnel = ngrok.connect(5000, bind_tls=True)

# webhook settings
WEBHOOK_HOST = http_tunnel.public_url
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 5000


now = datetime.datetime.now()


#  Настройки логирования

logging.basicConfig(
    filename='HISTORYlistener.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware()) # Логирование хэндлеров

# open database
db = Db()


## Обработчик текстовых сообщений

@dp.message_handler(text='/start')
async def cmd_start(message: types.Message):

    user = db.select("SELECT * FROM `user` WHERE `chat_id` = ?", [message.from_user.id], False) # выбрать из таблицы 'user' id = chat_id

    if not user:  # добавляем в БД, если нет
        db.query("INSERT INTO user (chat_id, last_username, registration_date) VALUES (?, ?, CURDATE())",
                 [message.from_user.id, message.from_user.username.lower()])
        text = 'Добро пожаловать! Выбери меню ниже'
        await bot.send_message(message.from_user.id, text, reply_markup=kb_menu)
    else:  # если есть - проверяем соответствие логина с тем, что в бд и меняем в случае его не совпадения
        if message.from_user.username.lower() != user.last_username:
            db.query("UPDATE user SET `last_username` = ? WHERE chat_id = ?",
                     [message.from_user.username.lower(), message.from_user.id])
        text = 'Ты уже зарегистрирован! Выбери меню ниже'
        await bot.send_message(message.from_user.id, text, reply_markup=kb_menu)


@dp.message_handler(text='/profile')
async def cmd_profile(message: types.Message):
    profile = db.select("SELECT registration_date FROM `user` WHERE chat_id = ? ",
                        [message.from_user.id]) # выбрать из таблицы 'user' дату регистрации и сравнить ее по чату айди пользователя
    await message.answer(f'Дата регистрации: {profile[0][0]}')

@dp.message_handler(text='/result')
async def cmd_profile(message: types.Message):
    user_id = message.chat.id
    print(user_id)
    force = db.select("SELECT exercises_force FROM `exercises` WHERE user_id = ?", [user_id])
    speed = db.select("SELECT exercises_speed FROM `exercises` WHERE user_id = ?", [user_id])
    endurance = db.select("SELECT exercises_endurance FROM `exercises` WHERE user_id = ?", [user_id])
    arb = db.select("SELECT exercises_arb FROM `exercises` WHERE user_id = ?", [user_id])
    result = db.select("SELECT exercises_result FROM `exercises` WHERE user_id = ?", [user_id])
    date = db.select("SELECT exercises_date FROM `exercises` WHERE user_id = ?", [user_id])
    pprint(force)
    try:
        await message.answer(f'Ваши результаты: СИЛА: {(force)[-1][-1]}\nСКОРОСТЬ: {speed[-1][-1]}\nВЫНОСЛИВОСТЬ: {endurance[-1][-1]}\nАРБ: {arb[-1][-1]}\nРЕЗУЛЬТАТ: {result[-1][-1]}\nДАТА: {date[-1][-1]}')
        await message.answer(f'Ваши результаты: СИЛА: {(force)[-2][0]}\nСКОРОСТЬ: {speed[-2][0]}\nВЫНОСЛИВОСТЬ: {endurance[-2][0]}\nАРБ: {arb[-2][0]}\nРЕЗУЛЬТАТ: {result[-2][0]}\nДАТА: {date[-2][0]}')
        await message.answer(f'Ваши результаты: СИЛА: {(force)[-3][0]}\nСКОРОСТЬ: {speed[-3][0]}\nВЫНОСЛИВОСТЬ: {endurance[-3][0]}\nАРБ: {arb[-3][0]}\nРЕЗУЛЬТАТ: {result[-3][0]}\nДАТА: {date[-3][0]}')
    except:
        pass
# HELP
@dp.message_handler(IsPrivate(), text='/help')
async def cmd_help(message: types.Message):
    await message.reply(f'Для началы работы нажми <b>/menu</b>')


# Сброс состояния FSM
@dp.callback_query_handler(text='cancel', state='*')
async def cancel_handler(call: CallbackQuery, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await call.message.reply('Возврат в меню.', reply_markup=kb_menu)
    await call.answer()


# MENU
@dp.message_handler(text='/menu')
async def menu(message: types.Message):
    await message.answer('приступим?', reply_markup=kb_menu)


""" SCORE COUNTER """


@dp.message_handler(text='Посчитать баллы')
async def count_ball(message: types.Message):
    await message.answer('Выбери свою возрастную группу', reply_markup=age_group_ikb)
    await Calc.ScoreCounter.set()


""" AGE GROUP """


###FIRSTGROUP
@dp.callback_query_handler(text='Первая', state=Calc.ScoreCounter)
async def age_group_1(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Выбери упражнение на силу!', reply_markup=power_category_ikb)
    await state.set_state(Calc.FirstGroup)
    await callback.answer()

@dp.callback_query_handler(text='power_back', state=Calc.FirstGroup)
async def age_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Возврат назад', reply_markup=age_group_ikb)
    await state.set_state(Calc.ScoreCounter)
    await callback.answer()



"""FORCE"""


###PULLUP
@dp.callback_query_handler(text='Подтягивания', state=Calc.FirstGroup)
async def force_pull_ups(call: CallbackQuery, state: FSMContext):
    try:
        if call.data == 'Подтягивания':
            await state.set_state(Calc.PullUp)
        elif call.data == 'Подъем_с_переворотом':
            await state.set_state(Calc.RiseWithCoup)
        elif call.data == 'Выход_с_силой':
            await state.set_state(Calc.RiseWithForce)
        else:
            print('ERROR')
    except Exception as ex:
        await call.message.answer(f'ERROR: {ex}')
    await call.message.edit_text('Выбери количество раз')
    await call.message.edit_reply_markup(pull_up_ikb)
    await call.answer()


@dp.callback_query_handler(text='power_back', state=[Calc.PullUp, Calc.RiseWithForce, Calc.RiseWithCoup])
async def power_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Возврат назад', reply_markup=power_category_ikb)
    await state.set_state(Calc.FirstGroup)
    await callback.answer()


@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.PullUp)
async def count_next(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    try:
        await call.message.answer(f"Выбери следующее упражнение, результат {pull_up[int(call.data)]} баллов",
                                  reply_markup=speed_category_ikb)
        async with state.proxy() as data:
            data['force'] = pull_up[int(call.data)]
    except Exception as ex:
        print(ex)
    await state.set_state(Calc.speed)
    await call.answer()



###RISEWITHCOUP
@dp.callback_query_handler(text='Подъем_с_переворотом', state=Calc.FirstGroup)
async def force_rise_with_coup(call: CallbackQuery, state: FSMContext):
    try:
        if call.data == 'Подтягивания':
            await state.set_state(Calc.PullUp)
        elif call.data == 'Подъем_с_переворотом':
            await state.set_state(Calc.RiseWithCoup)
        elif call.data == 'Выход_с_силой':
            await state.set_state(Calc.RiseWithForce)
        else:
            print('ERROR')
    except Exception as ex:
        await call.message.answer(f'ERROR: {ex}')
    await call.message.edit_text('Выбери количество раз')
    await call.message.edit_reply_markup(rise_with_coup_ikb)
    await call.answer()

@dp.callback_query_handler(text='power_back', state=[Calc.PullUp, Calc.RiseWithForce, Calc.RiseWithCoup])
async def power_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Возврат назад', reply_markup=power_category_ikb)
    await state.set_state(Calc.FirstGroup)
    await callback.answer()

@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.RiseWithCoup)
async def count_next(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Выбери следующее упражнение, результат {rise_with_coup[int(call.data)]} баллов",
                              reply_markup=speed_category_ikb)
    async with state.proxy() as data:
        data['force'] = rise_with_coup[int(call.data)]
    await state.set_state(Calc.speed)
    await call.answer()


###RISEWITHFORCE
@dp.callback_query_handler(text='Выход_с_силой', state=Calc.FirstGroup)
async def force_rise_with_force(call: CallbackQuery, state: FSMContext):
    try:
        if call.data == 'Подтягивания':
            await state.set_state(Calc.PullUp)
        elif call.data == 'Подъем_с_переворотом':
            await state.set_state(Calc.RiseWithCoup)
        elif call.data == 'Выход_с_силой':
            await state.set_state(Calc.RiseWithForce)
        else:
            print('ERROR')
    except Exception as ex:
        await call.message.answer(f'ERROR: {ex}')
    await call.message.edit_text('Выбери количество раз')
    await call.message.edit_reply_markup(rise_with_force_ikb)
    await call.answer()


@dp.callback_query_handler(text='power_back', state=[Calc.PullUp, Calc.RiseWithForce, Calc.RiseWithCoup])
async def power_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Возврат назад', reply_markup=power_category_ikb)
    await state.set_state(Calc.FirstGroup)
    await callback.answer()


@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.RiseWithForce)
async def count_next_force(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Выбери следующее упражнение, результат {rise_with_force[int(call.data)]} баллов",
                              reply_markup=speed_category_ikb)
    async with state.proxy() as data:
        data['force'] = rise_with_force[int(call.data)]
    await state.set_state(Calc.speed)
    await call.answer()


"""SPEED"""

@dp.callback_query_handler(text='speed_back', state=[Calc.speed, Calc.speed_60m, Calc.speed_10x10, Calc.speed_100m])
async def power_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Возврат назад', reply_markup=power_category_ikb)
    await state.set_state(Calc.FirstGroup)
    await callback.answer()

###60m
@dp.callback_query_handler(text='60', state=Calc.speed)
async def speed(call: CallbackQuery, state: FSMContext):
    if call.data == '60':
        await state.set_state(Calc.speed_60m)
        await call.message.edit_text('Выбери время за которое пробежал')
        await call.message.edit_reply_markup(speed_60m_ikb_1)
    await call.answer()


@dp.callback_query_handler(text='60m_next', state=Calc.speed_60m)
async def next_table_speed(call: CallbackQuery):
    if call.data == '60m_next':
        try:
            await call.message.edit_reply_markup(speed_60m_ikb_2)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='60m_back', state=Calc.speed_60m)
async def back_table_speed(call: CallbackQuery):
    if call.data == '60m_back':
        try:
            await call.message.edit_reply_markup(speed_60m_ikb_1)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.speed_60m)
async def count_next_60m(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Выбери оценку за АРБ",
                              reply_markup=arb_ikb)
    async with state.proxy() as data:
        data['speed'] = speed_60m_list[float(call.data)]
    await state.set_state(Calc.Arb)
    await call.answer()


###100m
@dp.callback_query_handler(text='100', state=Calc.speed)
async def speed_100_m(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text('Выбери время за которое пробежал')
    await call.message.edit_reply_markup(speed_100m_ikb)
    await state.set_state(Calc.speed_100m)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.speed_100m)
async def count_next(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Выбери оценку за АРБ",
                              reply_markup=arb_ikb)
    async with state.proxy() as data:
        data['speed'] = speed_100m_list[float(call.data)]
    await state.set_state(Calc.Arb)
    await call.answer()


###10x10
@dp.callback_query_handler(text='10x10', state=Calc.speed)
async def speed_10x10(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text('Выбери время за которое пробежал')
    await call.message.edit_reply_markup(speed_10x10_ikb)
    await state.set_state(Calc.speed_10x10)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.speed_10x10)
async def count_next(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Выбери оценку за АРБ", reply_markup=arb_ikb)
    async with state.proxy() as data:
        data['speed'] = speed_10x10_list[float(call.data)]
    await state.set_state(Calc.Arb)
    await call.answer()


## ARB
@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.VPN)
async def VPN_arb(call: CallbackQuery, state: FSMContext):
    await state.set_state(Calc.Arb)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data.isdigit, state=Calc.Arb)
async def count_next_arb(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Выбери следующее упражнение, результат {V_P_N[int(call.data)]} баллов",
                              reply_markup=endurance_category_ikb)
    async with state.proxy() as data:
        data['arb'] = V_P_N[int(call.data)]
    await state.set_state(Calc.endurance)
    await call.answer()


"""ENDURANCE"""

"""Первая таблица"""


###1000m
@dp.callback_query_handler(lambda call: call.data == '1000' or call.data == '3000' or call.data == '5000', state=Calc.endurance)
async def endurance_1000_m(call: CallbackQuery, state: FSMContext):
    if call.data == '1000':
        await state.set_state(Calc.endurance_1000)
        await call.message.edit_text('Выбери время за которое пробежал')
        await call.message.edit_reply_markup(endurance_1000m_ikb_1)
    elif call.data == '3000':
        await state.set_state(Calc.endurance_3000)
        await call.message.edit_text('Выбери время за которое пробежал')
        await call.message.edit_reply_markup(endurance_3000m_ikb_1)
    elif call.data == '5000':
        await state.set_state(Calc.endurance_5000)
        await call.message.edit_text('Выбери время за которое пробежал')
        await call.message.edit_reply_markup(endurance_5000m_ikb_1)
    await call.answer()


"""Вторая таблица"""


@dp.callback_query_handler(text='1000m_next', state=Calc.endurance_1000)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_next':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_2)
            await state.set_state(Calc.endurance_1000_2)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='1000m_back', state=Calc.endurance_1000_2)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_back':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_1)
            await state.set_state(Calc.endurance_1000)
        except Exception as ex:
            await call.answer()
    await call.answer()


"""Третья таблица"""


@dp.callback_query_handler(text='1000m_next', state=Calc.endurance_1000_2)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_next':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_3)
            await state.set_state(Calc.endurance_1000_3)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='1000m_back', state=Calc.endurance_1000_3)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_back':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_2)
            await state.set_state(Calc.endurance_1000_2)
        except Exception as ex:
            await call.answer()
    await call.answer()


"""Четвертая таблица"""


@dp.callback_query_handler(text='1000m_next', state=Calc.endurance_1000_3)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_next':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_4)
            await state.set_state(Calc.endurance_1000_4)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='1000m_back', state=Calc.endurance_1000_4)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_back':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_3)
            await state.set_state(Calc.endurance_1000_3)
        except Exception as ex:
            await call.answer()
    await call.answer()


"""Из четвертой таблицы в первую"""


@dp.callback_query_handler(text='1000m_next', state=Calc.endurance_1000_4)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_next':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_1)
            await state.set_state(Calc.endurance_1000)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='1000m_back', state=Calc.endurance_1000)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '1000m_back':
        try:
            await call.message.edit_reply_markup(endurance_1000m_ikb_4)
            await state.set_state(Calc.endurance_1000_4)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(lambda call: call.data.isdigit,
                           state=[Calc.endurance_1000, Calc.endurance_1000_2, Calc.endurance_1000_3, Calc.endurance,
                                  Calc.endurance_1000_4])
async def count_next(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    async with state.proxy() as data:
        data['endurance'] = endurance_1km[float(call.data)]
    async with state.proxy() as data:
        force = data['force']
        speed = data['speed']
        endurance = data['endurance']
        arb = data['arb']
        result = force + speed + endurance + arb
        data['endurance'] = endurance_1km[float(call.data)]


        if result >= 320:
            level = 'Высший уровень'
        elif 310 <= result < 320:
            level = 'Первый уровень'
        elif 300 <= result < 310:
            level = 'Второй уровень'
        elif 280 <= result < 300:
            level = 'Третий уровень'
        else:
            level = 'Нет уровня'
        await call.message.answer(f'<b>РЕЗУЛЬТАТ</b>\n'
                                  f'СИЛА - {data["force"]}\n'
                                  f'СКОРОСТЬ - {data["speed"]}\n'
                                  f'ВЫНОСЛИВОСТЬ - {data["endurance"]}\n'
                                  f'ВПН - {data["arb"]}\n'
                                  f'<b>ОБЩИЙ РЕЗУЛЬТАТ</b>: {result}\n'
                                  f'<b>УРОВЕНЬ:</b> {level}')
        data = str(now.strftime("%Y-%m-%d"))
        user_id = call.message.chat.id
        db.query(
            "INSERT INTO exercises (user_id, exercises_force, exercises_speed, exercises_endurance, exercises_arb, exercises_result, exercises_date) VALUE (?, ?, ?, ?, ?, ?, ?)",
            [user_id, force, speed, endurance, arb, result, data])
    await state.finish()
    await call.answer()



"""Вторая таблица"""


@dp.callback_query_handler(text='3000m_next', state=Calc.endurance_3000)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '3000m_next':
        try:
            await call.message.edit_reply_markup(endurance_3000m_ikb_2)
            await state.set_state(Calc.endurance_3000_2)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='3000m_back', state=Calc.endurance_3000_2)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '3000m_back':
        try:
            await call.message.edit_reply_markup(endurance_3000m_ikb_1)
            await state.set_state(Calc.endurance_3000)
        except Exception as ex:
            await call.answer()


"""Третья таблица"""


@dp.callback_query_handler(text='3000m_next', state=Calc.endurance_3000_2)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '3000m_next':
        try:
            await call.message.edit_reply_markup(endurance_3000m_ikb_3)
            await state.set_state(Calc.endurance_3000_3)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='3000m_back', state=Calc.endurance_3000_3)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '3000m_back':
        try:
            await call.message.edit_reply_markup(endurance_3000m_ikb_2)
            await state.set_state(Calc.endurance_3000_2)
        except Exception as ex:
            await call.answer()
    await call.answer()


"""Из третьей таблицы в первую"""


@dp.callback_query_handler(text='3000m_next', state=Calc.endurance_3000_3)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '3000m_next':
        try:
            await call.message.edit_reply_markup(endurance_3000m_ikb_1)
            await state.set_state(Calc.endurance_3000)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='3000m_back', state=Calc.endurance_3000)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '3000m_back':
        try:
            await call.message.edit_reply_markup(endurance_3000m_ikb_3)
            await state.set_state(Calc.endurance_3000_3)
        except Exception as ex:
            await call.answer()
    await call.answer()



@dp.callback_query_handler(lambda call: call.data.isdigit,
                           state=[Calc.endurance_3000, Calc.endurance_3000_2, Calc.endurance_3000_3])
async def count_next(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    async with state.proxy() as data:
        data['endurance'] = endurance_3km[float(call.data)]
    async with state.proxy() as data:
        force = data['force']
        speed = data['speed']
        endurance = data['endurance']
        arb = data['arb']
        result = force + speed + endurance + arb
        data['endurance'] = endurance_3km[float(call.data)]
        if result >= 320:
            level = 'Высший уровень'
        elif 310 <= result < 320:
            level = 'Первый уровень'
        elif 300 <= result < 310:
            level = 'Второй уровень'
        elif 280 <= result < 300:
            level = 'Третий уровень'
        else:
            level = 'Нет уровня'
        await call.message.answer(f'<b>РЕЗУЛЬТАТ</b>\n'
                                  f'СИЛА - {data["force"]}\n'
                                  f'СКОРОСТЬ - {data["speed"]}\n'
                                  f'ВЫНОСЛИВОСТЬ - {data["endurance"]}\n'
                                  f'ВПН - {data["arb"]}\n'
                                  f'<b>ОБЩИЙ РЕЗУЛЬТАТ</b>: {result}\n'
                                  f'<b>УРОВЕНЬ:</b> {level}')
        data = str(now.strftime("%Y-%m-%d"))
        user_id = call.message.chat.id
        db.query("INSERT INTO exercises (user_id, exercises_force, exercises_speed, exercises_endurance, exercises_arb, exercises_result, exercises_date) VALUE (?, ?, ?, ?, ?, ?, ?)", [user_id, force, speed, endurance, arb, result, data])

    await state.finish()
    await call.answer()


"""Вторая таблица"""


###5000m
@dp.callback_query_handler(text='5000m_next', state=Calc.endurance_5000)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_next':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_2)
            await state.set_state(Calc.endurance_5000_2)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='5000m_back', state=Calc.endurance_5000_2)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_back':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_1)
            await state.set_state(Calc.endurance_5000)
        except Exception as ex:
            await call.answer()
    await call.answer()


"""Третья таблица"""


@dp.callback_query_handler(text='5000m_next', state=Calc.endurance_5000_2)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_next':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_3)
            await state.set_state(Calc.endurance_5000_3)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='5000m_back', state=Calc.endurance_5000_3)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_back':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_2)
            await state.set_state(Calc.endurance_5000_2)
        except Exception as ex:
            await call.answer()
    await call.answer()


"""Четвертая таблица"""


@dp.callback_query_handler(text='5000m_next', state=Calc.endurance_5000_3)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_next':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_4)
            await state.set_state(Calc.endurance_5000_4)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='5000m_back', state=Calc.endurance_5000_4)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_back':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_3)
            await state.set_state(Calc.endurance_5000_3)
        except Exception as ex:
            await call.answer()
    await call.answer()


"""Из четвертой таблицы в первую"""


@dp.callback_query_handler(text='5000m_next', state=Calc.endurance_5000_4)
async def next_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_next':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_1)
            await state.set_state(Calc.endurance_5000)
        except Exception as ex:
            await call.answer()
    await call.answer()


@dp.callback_query_handler(text='5000m_back', state=Calc.endurance_5000)
async def back_table_endurance(call: CallbackQuery, state: FSMContext):
    if call.data == '5000m_back':
        try:
            await call.message.edit_reply_markup(endurance_5000m_ikb_4)
            await state.set_state(Calc.endurance_5000_4)
        except Exception as ex:
            await call.answer()
    await call.answer()



@dp.callback_query_handler(lambda call: call.data.isdigit,
                           state=[Calc.endurance_5000, Calc.endurance_5000_2, Calc.endurance_5000_3, Calc.endurance_5000_4])
async def count_next(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    async with state.proxy() as data:
        data['endurance'] = endurance_5km[float(call.data)]
    async with state.proxy() as data:
        force = data['force']
        speed = data['speed']
        endurance = data['endurance']
        arb = data['arb']
        result = force + speed + endurance + arb
        data['endurance'] = endurance_5km[float(call.data)]
        if result >= 320:
            level = 'Высший уровень'
        elif 310 <= result < 320:
            level = 'Первый уровень'
        elif 300 <= result < 310:
            level = 'Второй уровень'
        elif 280 <= result < 300:
            level = 'Третий уровень'
        else:
            level = 'Нет уровня'
        await call.message.answer(f'<b>РЕЗУЛЬТАТ</b>\n\n'
                                  f'СИЛА - {data["force"]}\n'
                                  f'СКОРОСТЬ - {data["speed"]}\n'
                                  f'ВЫНОСЛИВОСТЬ - {data["endurance"]}\n'
                                  f'ВПН - {data["arb"]}\n'
                                  f'<b>ОБЩИЙ РЕЗУЛЬТАТ</b>: {result}\n\n'
                                  f'<b>УРОВЕНЬ:</b> {level}')
        data = str(now.strftime("%Y-%m-%d"))
        user_id = call.message.chat.id
        db.query(
            "INSERT INTO exercises (user_id, exercises_force, exercises_speed, exercises_endurance, exercises_arb, exercises_result, exercises_date) VALUE (?, ?, ?, ?, ?, ?, ?)",
            [user_id, force, speed, endurance, arb, result, data])
    await state.finish()
    await call.answer()


###SECOND GROUP###
@dp.callback_query_handler(text='Вторая', state=Calc.ScoreCounter)
async def age_group_2(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Выбери упражнение!')
    await callback.message.edit_reply_markup(main_category_ikb)
    await state.set_state(Calc.SecondGroup)
    await callback.answer()


@dp.callback_query_handler(text='Третья', state=Calc.ScoreCounter)
async def age_group_3(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Выбери упражнение!')
    await callback.message.edit_reply_markup(main_category_ikb)
    await state.set_state(Calc.ThirdGroup)
    await callback.answer()


@dp.callback_query_handler(text='Четвертая', state=Calc.ScoreCounter)
async def age_group_4(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Выбери упражнение!')
    await callback.message.edit_reply_markup(main_category_ikb)
    await state.set_state(Calc.FourthGroup)
    await callback.answer()


@dp.callback_query_handler(text='Пятая', state=Calc.ScoreCounter)
async def age_group_5(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Выбери упражнение!')
    await callback.message.edit_reply_markup(main_category_ikb)
    await state.set_state(Calc.FifthGroup)
    await callback.answer()


# @dp.message_handler() # ответы от бота в группе
# async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.from_user.id, message.text)

    # or reply INTO webhook
    # return SendMessage(message.chat.id, message.text)


""""DONT'T TOUCH"""


### Запуск бота
async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)


### Остановка бота
async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown
    db.close()

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    ngrok.disconnect(http_tunnel.public_url)

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
