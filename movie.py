import logging
from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import REQUIRED_CHANNELS, MOVIE_CHANNEL
from check_user_subscription import check_user_subscription

router = Router()  # 🔹 Router orqali handlerni tashqi faylga o'tkazamiz

# 🎥 Kino raqami yuborilganda faqat video/audio yuborish
@router.message(lambda msg: msg.text and msg.text.isdigit())
async def send_movie(message: Message):
    if not message.text.isdigit():
        await message.answer("❗ Iltimos, faqat raqam yuboring.")
        return

    is_subscribed = await check_user_subscription(message.bot, message.from_user.id)
    if not is_subscribed:
        builder = InlineKeyboardBuilder()
        for ch, title in REQUIRED_CHANNELS.items():
            builder.button(text=f"➕ {title}", url=f"https://t.me/{ch.lstrip('@')}")
        builder.button(text="✅ Obunani tekshirish", callback_data="check_subs")
        builder.adjust(1)

        await message.answer(
            "📛 Iltimos, quyidagi kanallarga obuna bo‘ling va keyin raqam yuboring:",
            reply_markup=builder.as_markup()
        )
        return

    movie_id = int(message.text)
    try:
        await message.bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=MOVIE_CHANNEL,
            message_id=movie_id
        )

        await message.answer(
            "✅ Yana boshqa kinolar kerak bo‘lsa, bizning sahifalarimizga tashrif buyuring:\n"
            "🎬 Instagram: https://instagram.com/kino.bm\n"
        )
    except Exception as e:
        logging.warning(f"Kino yuborishda xatolik: {e}")
        await message.answer("❌ Kino topilmadi yoki raqam noto‘g‘ri.")
