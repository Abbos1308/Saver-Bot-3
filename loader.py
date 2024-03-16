from dotenv import load_dotenv
from aiogram import Bot , Dispatcher
from os import getenv
load_dotenv()
BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
bot = Bot(BOT_TOKEN)
ADMINS = getenv("ADMINS")