from _tracemalloc import stop
import re

from aiogram.bot import bot
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import menu
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Text
import random
from loader import dp
from utils.misc import rate_limit
import sys

@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def show_menu(message: Message):
    await message.answer(text=
                         "Команды для пользования:\n"
                         "👉 Для взаимодействия со словами, напишите слово латинскими буквами и выберите нужное действие\n"
                         "👉 Чтобы добавить перевод, напишите его русскими буквами после сохранения иностранного\n"
                         "👉 Для вывода слов (5 слов) на клавиатуре выберите 'Показать слова'\n"
                         "👉 Чтобы узнать общее количество слов, на клавиатуре выберите 'Показать количество слов'",
                         reply_markup=menu
                         )

@dp.callback_query_handler(text_contains="entered")
async def enteredWord(call: CallbackQuery):
    await call.answer(cache_time=10)
    txt = call.message.text
    print(txt)
    # >>> Добавляем новое слово

    file_words = open(f"dictionaries/{call.message.chat.id}.txt", 'a')  # Открываем для записи

    with open(f"dictionaries/{call.message.chat.id}.txt") as file:  # Отрываем для чтения - with автоматический закрывает файл
        reads_words = [row.strip() for row in file]

    get_button = txt  # Вводим желаемое слово
    if get_button in reads_words:  # Ищем если уже существует
        await call.message.answer(f"Такое слово уже сохранено")
    else:
        file_words.write(get_button + ' - ')  # Записываем слово, если новое
        await call.message.answer(f"Слово - " + get_button + " успешно добавлено \n"
                                                             "Введите пожалуйста перевод")
        print(get_button)
        file_words.close()
    await call.message.edit_reply_markup()

@dp.callback_query_handler(text_contains="deleted")
async def deletedWord(call: CallbackQuery):
    await call.answer(cache_time=10)
    txt = call.message.text
    print(txt)
    file = open(f"dictionaries/{call.message.chat.id}.txt")  # Открываем для чтения
    lines = file.readlines()  # Записываем в массив
    file.close()  # Закрываем
    file = open(f"dictionaries/{call.message.chat.id}.txt", "w")  # Открываем для записи
    deletedWord = txt
    for line in lines:
        if line != deletedWord + "\n":  # Удаляем если нашли
            file.write(line)  # Записываем в файл, то что вышло
    await call.message.answer(f"Слово - " + deletedWord + " успешно удалено")
    file.close()
    await call.message.edit_reply_markup()

@dp.callback_query_handler(text_contains="translate")
async def enteredWord(call: CallbackQuery):
    await call.answer(cache_time=10)
    txt = call.message.text

    with open(f"dictionaries/{call.message.chat.id}.txt") as file:  # Отрываем для чтения - with автоматический закрывает файл
        for line in file:
            if txt in line:
                print(line)
                await call.message.answer(line)

    await call.message.edit_reply_markup()

@dp.message_handler(Text(equals=["Показать слова"]))
async def get_button(message: Message):
    file_words = open(f"dictionaries/{message.chat.id}.txt", 'a')
    with open(f"dictionaries/{message.chat.id}.txt") as file:  # Открываем для чтения
        read_words = [row.strip() for row in file]  # Записываем в массив
    read = []
    new_words = []
    i = 0
    while i < 10:  # Ищем 10 слов
        if read_words == []:
            await message.answer(f"Ваш словарь пустой, добавьте слово")
            i = 10
        else:
            read.append(random.choice(read_words))  # Выводим рандомно 10 слов
            i += 1
    [new_words.append(item) for item in read if item not in new_words]  # Фильтруем, чтобы не было схожих слов

    enterdWord = new_words[:5]
    # print(enterdWord)
    if len(enterdWord) < 5:
        await message.answer(f"В вашем словаре меньше 5 слов, добавьте еще")
    else:
        str1 = enterdWord[0]
        str2 = enterdWord[1]
        str3 = enterdWord[2]
        str4 = enterdWord[3]
        str5 = enterdWord[4]
        file_words.close()
        if read_words == []:
            print()
        else:
            await message.answer(f"Ваши слова:\n{str1.split('-')[0]}\n{str2.split('-')[0]}\n"
                                 f"{str3.split('-')[0]}\n{str4.split('-')[0]}\n{str5.split('-')[0]}")
    # print(str1.split('-')[0])
    # print(str2.split('-')[0])
    # print(str3.split('-')[0])
    # print(str4.split('-')[0])
    # print(str5.split('-')[0])

@dp.message_handler(Text(equals=["Показать новые слова"]))
async def get_button(message: Message):
    file_words = open(f"dictionaries/{message.chat.id}.txt", 'a')
    with open(f"dictionaries/{message.chat.id}.txt") as file:  # Открываем для чтения
        read_words = [row.strip() for row in file]  # Записываем в массив
    read = []
    new_words = []
    print(read_words)
    enterdWord = read_words[-5:]
    print(enterdWord)
    if len(enterdWord) < 5:
        await message.answer(f"В вашем словаре меньше 5 слов, добавьте еще")
    else:
        str1 = enterdWord[0]
        str2 = enterdWord[1]
        str3 = enterdWord[2]
        str4 = enterdWord[3]
        str5 = enterdWord[4]
        file_words.close()
        if read_words == []:
            print()
        else:
            await message.answer(f"Ваши слова:\n{str1.split('-')[0]}\n{str2.split('-')[0]}\n"
                                 f"{str3.split('-')[0]}\n{str4.split('-')[0]}\n{str5.split('-')[0]}")


@dp.message_handler(Text(equals=["Показать количетво слов"]))
async def get_button(message: Message):
    with open(f"dictionaries/{message.chat.id}.txt") as file:  # Открываем для чтения
        len_words = [row.strip() for row in file]  # Записываем в массив
    print(f"Количество слов в вашем словаре - {len(len_words)}")  # Выводим общее количество
    await message.answer(f"Количество слов в вашем словаре - {len(len_words)}")

