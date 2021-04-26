import logging

from loader import db
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)

    # Уведомляет про запуск
    logging.info("Создаем подключение к базе данных")
    await db.create()


    logging.info("Создаем таблицу пользователей")
    await db.create_table_users()
    logging.info("Готово.")

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)