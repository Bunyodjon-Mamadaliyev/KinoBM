from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import REQUIRED_CHANNELS

router = Router()

# 🎬 /start komandasi
@router.message(CommandStart())
async def start_command(message: Message):
    builder = InlineKeyboardBuilder()
    for channel, title in REQUIRED_CHANNELS.items():
        builder.button(text=f"➕ {title}", url=f"https://t.me/{channel.lstrip('@')}")
    builder.button(text="✅ Obunani tekshirish", callback_data="check_subs")
    builder.adjust(1)
    await message.answer(
        "👋 Salom! Kino olish uchun raqam yuboring. Avval majburiy kanallarga obuna bo‘ling:",
        reply_markup=builder.as_markup()
    )
