import asyncio
from aiogram import Dispatcher, Bot, F
from config import TOKEN
from handlers.commands import router

dp = Dispatcher()
bot = Bot(token=TOKEN)
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())