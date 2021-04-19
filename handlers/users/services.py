from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp

from keyboards.inline.service_button import choice


@dp.message_handler(Command("service"))
async def show_items(message: Message):
    await message.answer(text="Выберите сервис для прослушивания",
                         reply_markup=choice)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы отменили эту функцию!", show_alert=True)

    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)