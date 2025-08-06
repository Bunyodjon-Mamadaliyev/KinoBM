import asyncio
import logging

from loader import dp, bot  # ❗ faqat bu yerda Dispatcher va Bot chaqiriladi

from start import router as start_router
from movie import router as movie_router
from check_subscription import router as check_subs_router
from admin import router as admin_router

# Log yozish
logging.basicConfig(level=logging.INFO)

# ✅ Routerlar ulanmoqda
dp.include_router(start_router)
dp.include_router(check_subs_router)
dp.include_router(admin_router)
dp.include_router(movie_router)

# 🚀 Botni ishga tushirish
async def main():
    print("✅ Bot serveri ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
