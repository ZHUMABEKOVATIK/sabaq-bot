from aiogram import F, Router
from aiogram.types import (
    Message
)

router = Router()


@router.message(F.contact)
async def get_contact(message: Message):
    await message.answer("get contact!")

@router.message(F.text)
async def text(message: Message):
    text = message.text
    await message.answer(f"Sen {text} dep jazdin'")