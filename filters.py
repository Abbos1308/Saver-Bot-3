from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message , CallbackQuery
from typing import Union

ADMIN_ID = [5053863236]
class UrlChecker(BaseFilter):
    def __init__(self, urls: Union[str, list]):
        self.urls = urls

    async def __call__(self, message: Message or CallbackQuery) -> bool:
        if message.text:
            text = message.text.lower()
            for url in self.urls:
                if url in text:
                    return True
        return False

class AdminIdFilter(BaseFilter):
    def __init__(self,ADMIN_ID : Union[int,list]):
        self.ADMIN_ID = ADMIN_ID
    
    async def __call__(self,message:Message) -> bool:
        if int(message.from_user.id) in self.ADMIN_ID:
            return True
        return False