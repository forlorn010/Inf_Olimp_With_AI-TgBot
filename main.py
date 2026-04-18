import asyncio
from aiogram import Dispatcher, Bot
from config import TOKEN
from handlers.menus import command_router, set_menu, set_commands
from handlers.callbacks import keyboard_router



dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(keyboard_router)
bot = Bot(token=TOKEN)



async def main():
    print('Bot is running...')

    #commands' menu left to the input line
    await set_menu(bot)
    await set_commands(bot)

    #start polling
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())