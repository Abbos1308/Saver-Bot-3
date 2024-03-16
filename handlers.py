import sqlite3
from aiogram import types , Bot
from aiogram.types import FSInputFile
base_text = f"""
@username orqali Ijtimoiy tarmoqlardan video , rasm , qo'shiqlarni yuklab olishingiz mumkin
"""

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER)''')
conn.commit()



async def start_answer(message: types.Message,bot: Bot):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}. Xush kelibsiz!")
    try:
        cursor.execute("SELECT user_id FROM users WHERE user_id=?", (message.from_user.id,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO users (user_id) VALUES (?)", (message.from_user.id,))
            conn.commit()
    except :
        pass
async def help_answer(message: types.Message, bot: Bot):
    print(dir(message))
    await message.answer(f"""
    <b>Bot buyruqlari:</b>
    /start - Botni ishga tushirish
    /help - Yordam""", parse_mode="HTML")


