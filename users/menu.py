from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from keyboards.inline.choice_buttons import choice
from loader import dp


@dp.message_handler(Command("items"))
async def show_message(message: Message):
    await message.answer(text="Кукуку", reply_markup=choice)