from aiogram.utils.keyboard import InlineKeyboardBuilder
import sqlite3
menu_builder = InlineKeyboardBuilder()
menu_builder.button(text=f"Reklama berish🔊", callback_data="reklama")
menu_builder.button(text=f"Statistika📊", callback_data="statistika")
menu_builder.button(text=f"Kanal qo'shish📢", callback_data="add_channel")
menu_builder.adjust(1)


async def channels_kb(channels):
    kb = InlineKeyboardBuilder()
    for i in channels:
        kb.button(text=f"{await bot.get_chat(i).title}",callback_data={i})
    kb.adjust(1)
    return kb