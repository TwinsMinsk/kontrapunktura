from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from keyboards.default.menu import menu_button
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите действие из меню ниже", reply_markup=menu_button)


@dp.message_handler(Text(equals=["Музыка"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо")

@dp.message_handler(Text(equals=["Видео"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо")

@dp.message_handler(Text(equals=["Мероприятия"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо")

@dp.message_handler(Text(equals=["Афиши"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо")

@dp.message_handler(Text(equals=["СВязаться"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо")