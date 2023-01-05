from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from filters import IsGroup


@dp.message_handler(CommandStart(), IsGroup())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f"Xush kelibsiz! {name}\nSiz guruhdasiz!")