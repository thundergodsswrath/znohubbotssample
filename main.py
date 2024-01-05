from logging import basicConfig, INFO
from os import getenv
from dotenv import load_dotenv

from asyncio import run
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

load_dotenv()

TOKEN_HIST = getenv('TOKEN_HIST')
TOKEN_MATH = getenv('TOKEN_MATH')
TOKEN_ENG = getenv('TOKEN_ENG')
TOKEN_UKR = getenv('TOKEN_UKR')
TOKEN_BIO = getenv('TOKEN_BIO')
TOKEN_GEO = getenv('TOKEN_GEO')

bot_hist = Bot(token=TOKEN_HIST)
bot_math = Bot(token=TOKEN_MATH)
bot_eng = Bot(token=TOKEN_ENG)
bot_ukr = Bot(token=TOKEN_UKR)
bot_bio = Bot(token=TOKEN_BIO)
bot_geo = Bot(token=TOKEN_GEO)
dp = Dispatcher()


class UserState(StatesGroup):
    START_STATE = State()
    DONE_STATE = State()


@dp.message(CommandStart())
async def start_view(message: types.Message, state: FSMContext):
    await state.set_state(UserState.START_STATE)
    start_message = ('Привіт! Для реєстрації напиши, будь ласка:\n'
                     '1. ПІБ\n'
                     '2. Пошту(email)\n'
                     '3. Персональний код підтвердження покупки')
    await message.answer(text=start_message)


@dp.message(UserState.START_STATE)
async def manager_message(message: types.Message, state: FSMContext):
    reply_message = 'Менеджер скоро тобі відповість😉'
    if message.text:
        await message.answer(text=reply_message)
        await state.set_state(UserState.DONE_STATE)


async def main():
    basicConfig(level=INFO)
    await dp.start_polling(bot_hist, bot_math, bot_eng, bot_ukr, bot_bio, bot_geo)


if __name__ == '__main__':
    run(main())
