from aiogram import Bot
from handlers import conn as user_db
from youtube import conn as yt_db
from loader import ADMINS
async def startup(bot: Bot):
    await bot.send_message(ADMINS,"Bot ishga tushdi ✔️")
    
async def shutdown(bot:Bot):
    yt_db.close()
    user_db.close()
    await bot.send_message(ADMINS,"Bot ishini to'xtatdi ❗")
    