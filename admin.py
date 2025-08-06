# 📁 KinoBM_bot/admin.py
from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import ADMINS, BANNED_USERS, STATS, MOVIE_CHANNEL

router = Router()

def is_admin(user_id):
    return user_id in ADMINS

# /admin paneli
@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    await message.answer(f"🔐 Sizning ID: {message.from_user.id}")

    if not is_admin(message.from_user.id):
        await message.answer("⛔ Siz admin emassiz!")
        return

    kb = InlineKeyboardBuilder()
    kb.button(text="📈 Statistika", callback_data="admin_stats")
    kb.button(text="🚫 Ban", callback_data="admin_ban")
    kb.button(text="➕ Unban", callback_data="admin_unban")
    kb.button(text="🎬 Kino yuklash", callback_data="admin_upload")
    kb.adjust(2)

    await message.answer("🛠 Admin panelga xush kelibsiz:", reply_markup=kb.as_markup())

# Statistika ko‘rsatish
@router.callback_query(F.data == "admin_stats")
async def show_stats(callback: types.CallbackQuery):
    users = len(STATS["users"])
    reqs = STATS["requests"]
    await callback.message.answer(f"📊 Statistika:\n👥 Foydalanuvchilar: {users}\n🎬 So‘rovlar: {reqs}")

# /ban user_id
@router.message(Command("ban"))
async def ban_user(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Siz admin emassiz!")
        return
    try:
        user_id = int(message.text.split()[1])
        BANNED_USERS.add(user_id)
        await message.answer(f"🚫 Foydalanuvchi {user_id} bloklandi.")
    except:
        await message.answer("⚠️ Foydalanuvchi ID noto‘g‘ri formatda.")

# /unban user_id
@router.message(Command("unban"))
async def unban_user(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Siz admin emassiz!")
        return
    try:
        user_id = int(message.text.split()[1])
        BANNED_USERS.discard(user_id)
        await message.answer(f"✅ Foydalanuvchi {user_id} ochildi.")
    except:
        await message.answer("⚠️ Foydalanuvchi ID noto‘g‘ri formatda.")

# Kino fayl yuborish
@router.message(lambda m: m.video and is_admin(m.from_user.id))
async def handle_upload(message: types.Message):
    sent = await message.forward(chat_id=MOVIE_CHANNEL)
    await message.answer(f"🎞 Kino muvaffaqiyatli yuklandi! Kino ID: {sent.message_id}")