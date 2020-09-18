from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import word_callback

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Добавить слово", callback_data=word_callback.new(
#                 word="word", config="entered"
#             )),
#             InlineKeyboardButton(text="Удалить слово", callback_data=word_callback.new(
#                 word="word", config="deleted"
#             )),
#         ],
#         [
#             InlineKeyboardButton(text="Отмена", callback_data="cancel")
#         ]
#     ]
# )

choice = InlineKeyboardMarkup(row_width=2)

entered_word = InlineKeyboardButton(text="Добавить слово",callback_data=word_callback.new(
                word="word", config="entered"))
choice.insert(entered_word)
deleted_word = InlineKeyboardButton(text="Удалить слово", callback_data=word_callback.new(
                word="word", config="deleted"))
choice.insert(deleted_word)

cancel_button = InlineKeyboardButton(text="Показать перевод", callback_data="translate")
choice.insert(cancel_button)