import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message , FSInputFile
from pytube import YouTube

# SQLite bazasiga ulanish
conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()

# Bazada video ma'lumotlarini saqlash uchun jadval yaratish
cursor.execute('''CREATE TABLE IF NOT EXISTS videos
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, youtube_link TEXT, message_id INTEGER,video_title TEXT)''')
conn.commit()


async def download_yt(link):

    # YouTube linkni pytube orqali yuklab olish
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()

    # Video yuklandi
    video_path = video.download()
    video_title = video.title
    video = FSInputFile(video_path)
    return video,video_title


async def youtube(message: types.Message,bot:Bot):
    # Foydalanuvchi yuborgan YouTube linkni olish
    youtube_link = message.text
    
    # Bazadan message_id ni olish
    cursor.execute("SELECT message_id FROM videos WHERE youtube_link=?", (youtube_link,))
    result = cursor.fetchone()
    cursor.execute("SELECT video_title FROM videos WHERE youtube_link=?", (youtube_link,))
    video_title = cursor.fetchone()
    
    if result:
        await message.answer("Please wait...")
        # Yuklangan videoni yuborish
        await bot.send_document(message.chat.id,str(result[0]), caption=str(video_title[0]))

    else:
        await message.answer("Please wait...")
        video , video_title = await download_yt(message.text)
        
        # Video faylini yuborish uchun boshqa foydalanuvchiga yuborish
        sent_message = await message.answer_document(video,caption=video_title)
        # Yuklangan videoning message_id sini bazaga saqlash
        cursor.execute("INSERT INTO videos (youtube_link, message_id , video_title) VALUES (?, ?, ?)", (youtube_link, sent_message.video.file_id,video_title))
        conn.commit()
        


# Ulanishni yopish
