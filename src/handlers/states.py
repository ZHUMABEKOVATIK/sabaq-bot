from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.states.auth import AuthStates

router = Router()

@router.message(AuthStates.name)
async def state_name(message: Message, state: FSMContext):
    name = message.text
    await state.set_data({'name': name})

    await message.answer(f"Atin'iz qabillandi, endi nomerin'iz")
    await state.set_state(AuthStates.phone)

@router.message(AuthStates.phone)
async def state_phone(message: Message, state: FSMContext):
    phone = message.text
    # Tekseriw

    await state.set_data({'phone': phone})

    await message.answer(f"Nomerin'iz qabillandi, endi jasin'iz")
    await state.set_state(AuthStates.age)

@router.message(AuthStates.age)
async def state_age(message: Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer(f"Jas tek sanlarda boladi")
        return

    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    await state.clear()

    # Save DB

    await message.answer(f"Jasin'iz qabillandi")