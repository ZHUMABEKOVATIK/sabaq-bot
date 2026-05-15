# aiogram (3.x)
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from .config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    await message.answer(f"Salem {u.full_name}, {u.id}")

@dp.message(F.text == "Qalay")
async def text(message: Message):
    text = message.text
    await message.answer(f"Sen 1")

@dp.message(F.text)
async def text(message: Message):
    text = message.text
    await message.answer(f"Sen 2")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__": 
    asyncio.run(main=main())