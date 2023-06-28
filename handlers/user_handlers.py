from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import game_keyboard, yn_keyboard
from services.services import get_bot_choice, get_winner

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=yn_keyboard)


@router.message(Command(commands=['help']))
async def start_cmd(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=yn_keyboard)


@router.message(F.text == LEXICON_RU['yes_button'])
async def start_cmd(message: Message):
    await message.answer(text=LEXICON_RU['yes'],
                         reply_markup=game_keyboard)


@router.message(F.text == LEXICON_RU['no_button'])
async def start_cmd(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=game_keyboard)
