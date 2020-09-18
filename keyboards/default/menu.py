from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Показать слова"),
            KeyboardButton(text="Показать новые слова")
        ],
        [
            KeyboardButton(text="Показать количетво слов")
        ]
    ],
    resize_keyboard=True
)