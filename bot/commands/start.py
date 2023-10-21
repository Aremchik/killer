from aiogram import Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
async def start(message: types.Message) -> None:
    reg_markup = InlineKeyboardBuilder()
    reg_markup.button(
        text='Регистрация',
        callback_data='registr'
    )
    await message.answer("Добро пожаловать в процесс регистрации! Пожалуйста, Пройдите регистрацию", reply_markup=reg_markup.as_markup())



