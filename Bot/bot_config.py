import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand

from bots.Bot.handlers import reminder
from config import load_config

storage = MemoryStorage()
logger = logging.getLogger(__name__)

config = load_config(r'config/config.ini')

TOKEN = config.tg_bot.BOT_TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


async def set_commands(bot: Bot):
    """Установка команд для бота

    :param bot:
    :return:
    """
    commands = [
        BotCommand(command='/start', description='Начало работы'),
        BotCommand(command='/cancel', description='Отмена'),
        BotCommand(command='/bugreport', description='Отправить сообщение об ошибке')
    ]

    await bot.set_my_commands(commands)


async def main():
    """Запуск бота

    :return:"""

    logging.info('Bot started')

    reminder(dp)

    await set_commands(bot=bot)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
