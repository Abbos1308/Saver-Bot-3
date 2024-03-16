from aiogram import Bot , Dispatcher , types , F , Router
from handlers import start_answer , help_answer 
from aiogram.utils.keyboard import InlineKeyboardBuilder
#from musics.search_music_name import search_music_name
from youtube import youtube 
from instagram import instagram
from tiktok import tiktok
from notify_admin import startup,shutdown
from asyncio import run
from aiogram.filters import Command
import logging
import admin
#import musics
from loader import bot
from filters import UrlChecker
from check_user import User_checkMiddleware
yt_links = [
    "https://you",
    "https://m.you",
    "https://www.you",
    "http://you",
    "http://m.you",
    "http://www.you",
]
insta_links = [
    "https://insta",
    "https://www.insta",
]

tt_links = [
    "https://vt.tik",
    "https://vm.tik",
]


#Configure logging
logging.basicConfig(level=logging.INFO)



async def start():
    # set bot commands
    await bot.set_my_commands([
        types.BotCommand(command="/start",description="Botni ishga tushirish"),
        types.BotCommand(command="/help",description="Yordam"),
    ])
    
    #Middlaveres
    dp.update.middleware.register(User_checkMiddleware())
    
    
    # Register handlers
    dp.message.register(start_answer,Command("start"))
    dp.message.register(help_answer,Command("help"))
    dp.message.register(youtube,UrlChecker(yt_links))
    dp.message.register(instagram,UrlChecker(insta_links))
    dp.message.register(tiktok,UrlChecker(tt_links))
    #dp.message.register(search_music_name)
    
    # Admin Router
    dp.include_router(admin.admin_router)
    # Music Router
    #dp.include_router(musics.music_router)
    
    # Startup and Shutdown
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    
    # Start polling
    await dp.start_polling(bot,polling_timeout=1)
    
            
run(start())
