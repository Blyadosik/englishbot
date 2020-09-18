import logging
import re
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import choice
from loader import dp
from array import *




@dp.message_handler()
async def echo_bot(message: Message):
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    for one_char in message.text:
        if one_char in alphabet:
            await message.answer(text=f"{message.text.lower()}", reply_markup=choice)
            break
    alphabet = {"а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я","А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О",
                "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"}
    for one_char in message.text:
        if one_char in alphabet:
            file_words = open(f"dictionaries/{message.chat.id}.txt", 'a')  # Открываем для записи

            with open(f"dictionaries/{message.chat.id}.txt") as file:  # Отрываем для чтения - with автоматический закрывает файл
                reads_words = [row.strip() for row in file]

            get_button = message.text  # Вводим желаемое слово
            if get_button in reads_words:  # Ищем если уже существует
                await message.answer(f"Такое слово уже сохранено")
            else:
                file_words.write(get_button + '\n')  # Записываем слово, если новое
                await message.answer(f"Перевод - " + get_button + " успешно сохранен")
                print(get_button)
                file_words.close()
            break
    # if f"{message.text}" != re.search('[а-яА-Я]'):
    #     await message.answer(f"ERDfd")
