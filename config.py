import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MOVIE_CHANNEL = int(os.getenv("MOVIE_CHANNEL"))
REQUIRED_CHANNELS = eval(os.getenv("REQUIRED_CHANNELS"))

ADMINS = {7419899223}
BANNED_USERS = set()
STATS = {"users": set(), "requests": 0}
