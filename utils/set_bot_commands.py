from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Начать диалог"),
        types.BotCommand("help", "Получить справку"),
        types.BotCommand("menu", "Главное меню"),
        types.BotCommand("service", "Сервисы для прослуживания музыки"),
        types.BotCommand("channels", "Список каналов на подписку"),
        types.BotCommand("create_post", "Предложить пост в канале"),
    ])
