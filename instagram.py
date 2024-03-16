from aiogram import types , Bot
import requests
import asyncio

async def download_insta(link):
    api_url = "https://mediadownloaderapi-mkun.onrender.com/instagram"
    params = {"link": link}
    response = requests.get(api_url, params=params)
    return response.json()

async def instagram(message: types.Message, bot: Bot):
    await message.answer("Please, wait...")
    result = await download_insta(message.text)
    #print(result)
    if result['status'] == True:
        for i in result['data']:
        
            await message.answer_document(i['url'])
            asyncio.sleep(0.5)
    else:
        await message.answer("Yuklab bo'lmadi. Tekshirib qayta yuboring")
        
    