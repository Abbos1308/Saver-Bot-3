from aiogram import types , Bot , F 
from keyboards.inline import menu_builder,channels_kb
from aiogram.fsm.context import FSMContext
from admin.states import AdminState
from handlers import cursor , conn
import  sqlite3
from channels_db import channel_db


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
        pass

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


