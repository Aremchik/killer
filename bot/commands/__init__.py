__all__ = ['register_user_commands']

from aiogram import Router
from aiogram.filters import Command

from bot.commands.admin import admin, randomizer
from bot.commands.start import start
from bot.commands.fsm import registration, fio_handler, RegistrationState
from bot.commands.help import help_command
from aiogram import F

def register_user_commands(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(admin, Command(commands=['admin']))
    router.callback_query.register(registration, F.data == 'registr')
    router.callback_query.register(randomizer, F.data == 'random_users')
    router.message.register(fio_handler, RegistrationState.wait_fio)
