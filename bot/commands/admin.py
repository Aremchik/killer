from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
async def admin(message: types.Message) -> None:
    rand_markup = InlineKeyboardBuilder()
    rand_markup.button(
        text='Распределить участников',
        callback_data='random_users'
    )
    if message.from_user.id == 937448667:
        await message.answer("Добро пожаловать в админ панель", reply_markup=rand_markup.as_markup())

async def randomizer(callback: types.CallbackQuery) -> None:
    await callback.message.answer("Участники распределены")