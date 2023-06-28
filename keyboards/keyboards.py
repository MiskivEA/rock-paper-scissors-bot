from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# инициализация клавиатуры с использованием билдера
yn_keyboard_builder = ReplyKeyboardBuilder()
yn_keyboard_builder.row(button_yes, button_no, width=2)
yn_keyboard = yn_keyboard_builder.as_markup(one_time_keyboard=True,
                                            resize_keyboard=True)

# инициализация игровой клавиатуры без использования билдера
rock_btn = KeyboardButton(text=LEXICON_RU['rock'])
scissors_btn = KeyboardButton(text=LEXICON_RU['scissors'])
paper_btn = KeyboardButton(text=LEXICON_RU['paper'])

game_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [rock_btn],
        [scissors_btn],
        [paper_btn]
    ],
    resize_keyboard=True
)
