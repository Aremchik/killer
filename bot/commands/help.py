from aiogram import types
from aiogram.filters import CommandObject
async def help_command(message: types.Message) -> None:
    await message.answer('Правила')