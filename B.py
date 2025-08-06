# import logging
# import asyncio
# from aiogram import Bot, Dispatcher, types, F
# from aiogram.types import Message, CallbackQuery
# from aiogram.enums.chat_member_status import ChatMemberStatus
# from aiogram.filters import CommandStart
# from aiogram.utils.keyboard import InlineKeyboardBuilder
#
# # 🔐 Token va kanal sozlamalari
# BOT_TOKEN = "7733625396:AAHp-TawMtWLmXtGZ8xclq0dBXsynV4E9RM"
# MOVIE_CHANNEL = -1002562748114  # Bu maxfiy kanal — faqat video olish uchun ishlatiladi
#
# REQUIRED_CHANNELS = {
#     "@Kino_BM": "1 - kanal"
# }
#
# # 🔧 Logger sozlamasi
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
#
# # ✅ Obunani tekshiruvchi funksiya — faqat REQUIRED_CHANNELS ni tekshiradi
# async def check_user_subscription(user_id: int) -> bool:
#     for channel in REQUIRED_CHANNELS.keys():
#         try:
#             user = await bot.get_chat_member(chat_id=channel, user_id=user_id)
#             if user.status not in [
#                 ChatMemberStatus.MEMBER,
#                 ChatMemberStatus.ADMINISTRATOR,
#                 ChatMemberStatus.CREATOR
#             ]:
#                 return False
#         except Exception as e:
#             logging.warning(f"Obuna tekshiruvda xatolik ({channel}): {e}")
#             return False
#     return True
#
# # 🎬 /start komandasi
# @dp.message(CommandStart())
# async def start(message: Message):
#     builder = InlineKeyboardBuilder()
#
#     for channel, title in REQUIRED_CHANNELS.items():
#         builder.button(text=f"➕ {title}", url=f"https://t.me/{channel.lstrip('@')}")
#
#     builder.button(text="✅ Obunani tekshirish", callback_data="check_subs")
#     builder.adjust(1)
#
#     await message.answer(
#         "👋 Salom! Kino olish uchun raqam yuboring. Avval majburiy kanallarga obuna bo‘ling:",
#         reply_markup=builder.as_markup()
#     )
#
# # 🔁 Callback orqali obuna tekshirish
# @dp.callback_query(F.data == "check_subs")
# async def check_subscription(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     is_subscribed = await check_user_subscription(user_id)
#
#     if is_subscribed:
#         await callback.message.answer("✅ Obuna bo‘lgansiz!")
#         await callback.message.answer("🎬 Endi kino raqamini yuboring.")
#     else:
#         await callback.message.answer("❌ Obuna bo‘lmagansiz. Iltimos, majburiy kanallarga obuna bo‘ling.")
#
# # 🎥 Kino raqami yuborilganda faqat video/audio yuborish
# @dp.message()
# async def send_movie(message: Message):
#     if not message.text.isdigit():
#         await message.answer("❗ Iltimos, faqat raqam yuboring.")
#         return
#
#     is_subscribed = await check_user_subscription(message.from_user.id)
#     if not is_subscribed:
#         builder = InlineKeyboardBuilder()
#         for ch, title in REQUIRED_CHANNELS.items():
#             builder.button(text=f"➕ {title}", url=f"https://t.me/{ch.lstrip('@')}")
#         builder.button(text="✅ Obunani tekshirish", callback_data="check_subs")
#         builder.adjust(1)
#         await message.answer(
#             "📛 Iltimos, quyidagi kanallarga obuna bo‘ling va keyin raqam yuboring:",
#             reply_markup=builder.as_markup()
#         )
#         return
#
#     movie_id = int(message.text)
#     try:
#         # Har qanday kontentni yuborish uchun copy_message ishlatilmoqda
#         await bot.copy_message(chat_id=message.chat.id, from_chat_id=MOVIE_CHANNEL, message_id=movie_id)
#
#         # Hammasi muvaffaqiyatli bo‘lsa, reklama xabari chiqariladi
#         await message.answer(
#             "✅ Yana boshqa kinolar kerak bo‘lsa, bizning sahifalarimizga tashrif buyuring:\n"
#             "🎬 Instagram: @instagram\n"
#             "📺 TikTok: @tiktok\n"
#             "▶️ YouTube: @youtube"
#         )
#     except Exception as e:
#         logging.warning(f"Kino yuborishda xatolik: {e}")
#         await message.answer("❌ Kino topilmadi yoki raqam noto‘g‘ri.")
#
#
# # 🚀 Botni ishga tushirish
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())