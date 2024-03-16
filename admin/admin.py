from aiogram import types , Bot , F 
from keyboards.inline import menu_builder,channels_kb
from aiogram.fsm.context import FSMContext
from admin.states import AdminState
from handlers import cursor , conn
import  sqlite3


db = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS channels
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, channel_id INTEGER)''')
db.commit()

cursor.execute("SELECT channel_id FROM channels")
result = cursor.fetchall()
kanallar = [row[0] for row in result]



async def admin_command(message:types.Message,state=FSMContext):
    await state.set_state(AdminState.base)
    await message.answer("Admin panelga xush kelibsiz, Menuni tanlang 👇",reply_markup=menu_builder.as_markup())

async def admin_callbacks(call:types.CallbackQuery,state:FSMContext):
    # Statistika
    if call.data == "statistika":
        cursorr.execute("SELECT user_id FROM users")
        result = cursorr.fetchall()
        user_ids = [row[0] for row in result]
        await call.message.answer(f"""
        Faol foydalanuvchilar : {len(result)}ta
        """)

    # Reklama
    if call.data == "reklama":
        await call.message.answer("Yaxshi. Reklama postini menga yuboring")
        await state.set_state(AdminState.reklama)

    # channel
    if call.data=="add_channel":
        await message.answer("Kanal ID sini yuboring.")
        await state.set_state(AdminState.add_channel)

async def reklama(message :types.Message,state:FSMContext):
    await message.answer("Reklama yuborish boshlandi.")
    cursorr.execute("SELECT user_id FROM users")
    result = cursorr.fetchall()
    user_ids = [row[0] for row in result]
    failed = 0
    succed = 0
    for _id in user_ids:
        try:
            await message.copy_to(_id)
            succed += 1
        except:
            failed += 1
            cursorr.execute("DELETE FROM users WHERE user_id=?",(_id,))
    await message.answer(f"Reklamalar yuborildi:\n{succed}ta ✅\n{failed}ta ❌")


async def adding(message:types.Message,state:FSMContext):
    channel_id = message.text
    cursor.execute("INSERT INTO channels (channel_id) VALUES (?)", (channel_id,))
    db.commit()
    await message_answer("Kanal qo'shildi")
    kb = await channels_kb(kanallar)
    await message.answer("Kanallarni o'chirish",reply_markup=kb.as_markup)