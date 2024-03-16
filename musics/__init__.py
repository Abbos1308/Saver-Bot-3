from aiogram import F , Router
from . import music_search_name
from . import music_search_voice
music_router = Router()
music_router.message.register(music_search_name.search_by_voice)
music_router.message.register(music_search_voice.recieve_text,F.voice or F.audio)