# import requests

# from loader import dp, bot
# from aiogram import types


# from keyboards.inline.prayer_time import regions

# @dp.callback_query_handler(text="prayer_time")
# async def reg(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Marhamat, viloyatni tanlang", reply_markup=regions)
# @dp.callback_query_handler()
# async def get_all_messages(call: types.Message):
#     try:
#         # user_full_name = call.message.from_user.full_name
#         region = call.message.text
#         URL = f"https://islomapi.uz/api/present/day?region={region}"
#         response = requests.get(url=URL).json()
#         # await message.reply(dictlar)
#         await call.message.answer(f"{region} namoz vaqtlari🤲\n\n🌄Bomdod: {response['times']['tong_saharlik']}\n\n🌅Quyosh chiqishi: {response['times']['quyosh']}\n\n🌇Peshin: {response['times']['peshin']}\n\n🌆Asr: {response['times']['asr']}\n\n🏙Shom va iftorlik: {response['times']['shom_iftor']}\n\n🌃Xufton: {response['times']['hufton']}")
#     except:
#         await call.message.answer(f"Kechirasiz bizda {region} haqida ma'lumot yo'q❌")