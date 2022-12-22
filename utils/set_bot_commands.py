from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('profile', "Мой профиль"),
        types.BotCommand('result', "Мои результаты"),
        types.BotCommand('menu', 'Меню'),
    ])