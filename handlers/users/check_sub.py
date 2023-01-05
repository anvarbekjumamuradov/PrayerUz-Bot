import requests
from loader import dp, bot
from aiogram import types

from data.config import CHANNELS
from utils.misc import subscription

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.prayer_time import prayer, regions


@dp.callback_query_handler(text="check_sub")
async def checker(call: types.CallbackQuery):
    await call.answer("Obunalar tekshirilmoqda")
    user_full_name = call.message.from_user.full_name
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n")
    if final_status:
        await call.message.delete()
        msg = f"Xush kelibsiz! {user_full_name}\n\nNamoz Vaqti Bot xizmatingizda!\n\nMeni Guruhlarda ham ishlata olasiz faqatgina guruhga qo'shsangiz bas 😉!" 
        await call.message.answer(msg, reply_markup=prayer)
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_sub"))
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=markup)
@dp.callback_query_handler(text="prayer_time")
async def reg(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Marhamat, viloyatni tanlang", reply_markup=regions)
@dp.message_handler(text="Andijon")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Buxoro")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Qo'qon")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Jizzax")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Xiva")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Namangan")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Navoiy")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Guliston")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Samarqand")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Nukus")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Qarshi")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="Toshkent")
async def get_all_messages(message: types.Message):
    try:
        user_full_name = message.from_user.full_name
        region = message.text
        URL = f"https://islomapi.uz/api/present/day?region={region}"
        response = requests.get(url=URL).json()
        # await message.reply(dictlar)
        await message.answer(f"<i><b>{region}</b></i> namoz vaqtlari🤲\n\n⏰ <i>Bomdod:</i>   {response['times']['tong_saharlik']}\n\n <i><b>Quyosh chiqishi:</b></i>   <b>{response['times']['quyosh']}</b>\n\n⏰ <i>Peshin:</i>   <b>{response['times']['peshin']}</b>\n\n⏰ <i>Asr:</i>   <b>{response['times']['asr']}</b>\n\n⏰ <i>Shom va iftorlik:</i>   <b>{response['times']['shom_iftor']}</b>\n\n⏰  <i>Xufton:</i>    <b>{response['times']['hufton']}</b>", parse_mode='html')
        
    except:
        await message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")
@dp.message_handler(text="🔙 Orqaga")
async def do_back(message: types.Message):
    user_full_name = message.from_user.full_name
    msgg = f"{user_full_name}. Siz asosiy menyudasiz!"
    msg = f"Namoz Vaqti Bot xizmatingizda!\n\nMeni Guruhlarda ham ishlata olasiz faqatgina guruhga qo'shsangiz bas 😉!"
    await message.answer(msgg)
    await message.answer(msg, reply_markup=prayer)
@dp.message_handler(text="🏠 Bosh menyu")
async def do_back(message: types.Message):
    await message.delete()
    user_full_name = message.from_user.full_name
    msgg = f"{user_full_name}. Siz asosiy menyudasiz!"
    msg = f"Namoz Vaqti Bot xizmatingizda!\n\nMeni Guruhlarda ham ishlata olasiz faqatgina guruhga qo'shsangiz bas 😉!"
    await message.answer(msgg)
    await message.answer(msg, reply_markup=prayer)