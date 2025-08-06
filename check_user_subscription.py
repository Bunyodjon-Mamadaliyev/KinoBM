import logging
from aiogram import Bot
from aiogram.enums.chat_member_status import ChatMemberStatus
from config import REQUIRED_CHANNELS

# ✅ Obunani tekshiruvchi funksiya — faqat REQUIRED_CHANNELS ni tekshiradi
async def check_user_subscription(bot: Bot, user_id: int) -> bool:
    for channel in REQUIRED_CHANNELS.keys():
        try:
            user = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if user.status not in [
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.CREATOR
            ]:
                return False
        except Exception as e:
            logging.warning(f"Obuna tekshiruvda xatolik ({channel}): {e}")
            return False
    return True
