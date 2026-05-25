from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.states.auth import AuthStates

router = Router()

@router.message(AuthStates.name)
async def get_message(message: Message, state: FSMContext):
    await message.answer(f"Bul state xabar")