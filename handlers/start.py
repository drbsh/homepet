from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear() # Сбрасываем состояние, если оно было
    await message.answer(
        f"Привет, {message.from_user.full_name}! 👋\n"
        "Я бот, который поможет нам завести нашего общего виртуального питомца. "
        "Готов начать?",
        # Здесь позже добавим кнопку "Выбрать питомца"
    )