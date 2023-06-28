import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
import logging

from config_data.config import load_config
from handlers.other_handlers import router as other_router
from handlers.user_handlers import router as user_router
from keyboards.menu import main_menu_commands

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting BOT')

    config = load_config()
    bot = Bot(token=config.bot.token,
              parse_mode='HTML')

    dp = Dispatcher()
    dp.include_router(user_router)
    dp.include_router(other_router)

    await bot.set_my_commands(main_menu_commands)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
