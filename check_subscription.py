from aiogram import Router, F
from aiogram.types import CallbackQuery
from check_user_subscription import check_user_subscription

router = Router()

# 🔁 Callback orqali obuna tekshirish
@router.callback_query(F.data == "check_subs")
async def check_subscription(callback: CallbackQuery):
    user_id = callback.from_user.id
    is_subscribed = await check_user_subscription(callback.bot, user_id)

    if is_subscribed:
        await callback.message.answer("✅ Obuna bo‘lgansiz!")
        await callback.message.answer("🎬 Endi kino raqamini yuboring.")
    else:
        await callback.message.answer("❌ Obuna bo‘lmagansiz. Iltimos, majburiy kanallarga obuna bo‘ling.")
