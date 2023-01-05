from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

prayer = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Namoz Vaqtlari ☪️", callback_data="prayer_time")]
])    

regions = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Andijon"), KeyboardButton(text="Buxoro"), KeyboardButton(text="Qo'qon")],
    [KeyboardButton(text="Xiva"), KeyboardButton(text="Jizzax"), KeyboardButton(text="Namangan")],
    [KeyboardButton(text="Navoiy"), KeyboardButton(text="Nukus"), KeyboardButton(text="Guliston")],
    [KeyboardButton(text="Samarqand"), KeyboardButton(text="Qarshi"), KeyboardButton(text="Toshkent")],
    [KeyboardButton(text="🔙 Orqaga"), KeyboardButton(text="🏠 Bosh menyu")]
    ], resize_keyboard=True)