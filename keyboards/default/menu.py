from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Музыка"),
            KeyboardButton(text="Видео"),
        ],
        [
            KeyboardButton(text="Мероприятия"),
            KeyboardButton(text="Афиши")
        ],
        [
            KeyboardButton(text="Связаться"),
        ],
    ],
    resize_keyboard=True
)
