from aiogram import types

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import ScalarResult
from bot.db import User
class RegistrationState(StatesGroup):
    wait_fio = State()


async def registration(callback: types.CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer('Введите свое ФИО')
    await state.set_state(RegistrationState.wait_fio)

async def fio_handler(message: types.Message) -> None:
    session_maker: sessionmaker = 'session_maker'
    async with session_maker() as session:
        async with session.begin():
            session: AsyncSession
            result = await session.execute(select(User).where(User.user_id == message.from_user.id))
            result: ScalarResult
            user: User - result.one_or_none()

            if user is not None:
                pass
            else:
                user = User(
                    user_id=message.from_user.id,
                    username=message.text
                )
                await session.merge(user)
                await message.answer(f"Регистрация завершена! Ожидайте совю жертву. {message.text}" )