# aiogram (3.x)
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from .config import settings
from .handlers import routers

bot = Bot(settings.TOKEN)
dp = Dispatcher()

dp.include_routers(routers)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__": 
    asyncio.run(main=main())