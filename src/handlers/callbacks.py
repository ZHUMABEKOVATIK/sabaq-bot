from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data)
async def callback(call: CallbackQuery):
    data = call.data
    await call.message.answer(f"Button: {data}")