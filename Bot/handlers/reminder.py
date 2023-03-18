from datetime import datetime

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import callback_query

from ..bot_config import bot
from ..buttons import start_kb


async def start_message(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\n Я бот который может напомнить о важных событиях.',reply_markup=start_kb)

def remind_register_handlers(dp: Dispatcher):
    """Функиция для регистрации хэндлеров

    :param dp:
    :return:
    """

    dp.register_message_handler(start_message, commands=['start'])