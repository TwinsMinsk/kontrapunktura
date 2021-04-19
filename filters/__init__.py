from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter

from aiogram import Dispatcher
from loguru import logger



from .group_chat import IsGroup



def setup(dp: Dispatcher):
    logger.info("Подключение filters...")
    text_messages = [
        dp.message_handlers,
        dp.edited_message_handlers,
        dp.channel_post_handlers,
        dp.edited_channel_post_handlers,
    ]


    dp.filters_factory.bind(IsGroup)



if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    pass
