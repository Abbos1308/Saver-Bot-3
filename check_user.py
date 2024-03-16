from aiogram.filters import BaseFilter
from aiogram.types import InlineKeyboardButton, Update
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import bot
import sqlite3
from channels_db import channel_db
DEFAULT_RATE_LIMIT = .1
kanallar = [-1002113453697]
class CheckSub(BaseFilter):
    async def __call__(self, message) -> bool:
        user_id = message.from_user.id
        k = []
        force = False
        for x in kanallar:
            kanals = await bot.get_chat(x)
            try:
                res = await bot.get_chat_member(chat_id=x, user_id=user_id)
            except:
                continue
            if res.status == 'member' or res.status == 'administrator' or res.status == 'creator':
                pass
            else:
                k.append(InlineKeyboardButton(text=f"{kanals.title}", url=f"{await kanals.export_invite_link()}"))
                force = True
        builder = InlineKeyboardBuilder()
        builder.add(*k)
        text = "Tasdiqlash"
        builder.add(InlineKeyboardButton(text=text, callback_data="check"))
        builder.adjust(1)
        if force:
            return True
        else:
            return False
