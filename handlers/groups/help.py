from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, db, bot
from filters import IsGroup


@dp.message_handler(CommandHelp(), IsGroup())
async def bot_help(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f"Sizga guruhda qanday yordam ko'rsata olaman {name} ?")