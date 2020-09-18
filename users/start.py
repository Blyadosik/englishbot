from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    file_words = open(f"dictionaries/{message.from_user.id}.txt", 'a')
    file_words.close()
    await message.answer(f'Привет, {message.from_user.first_name}!\nЯ бот, который поможет тебе с иностранным языком!\nНапиши /help, чтобы узнать подробнее!')
