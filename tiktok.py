import requests
from aiogram import types
async def download_tt(link):
    api_url = "https://tiktokdownloaderapi.onrender.com/tiktok"
    params = {"url": link}
    response = requests.get(api_url, params=params)
    #print(dir(response))
    if response.status_code==200:
        return response.json()
    return None

async def tiktok(message:types.Message):
    await message.answer("Please, wait...")
    result = await download_tt(message.text)
    if result:
        #print(result)
        await message.answer_document(result["video_url"])
    else:
        await message.answer("Xatolik! Qayta urinib ko'ring.")