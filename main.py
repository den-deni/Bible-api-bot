import asyncio
import logging


from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession


from config import TOKEN, ADMIN_ID
from commands.bot_list_cmd import private, group
from handlers.main_handler import router_main_handler
from handlers.state_query_word import process_state_word
from handlers.start_books import constructor_index
from handlers.proces_weaher import weather_router
from handlers.index_search import index_start_router
from commands.run_stop import start_bot, stop_bot
from admin.admin_handler import admin_router
from commands.private_commands import commands_router
from commands.group_commands import grope_router
from filters.filter_main import filter_router
from filters.group_chat import user_group_router

TOKEN = TOKEN
router = Router()
dp = Dispatcher()
dp.startup()
dp.include_router(router_main_handler)
dp.include_router(process_state_word)
dp.include_router(constructor_index)
dp.include_router(weather_router)
dp.include_router(index_start_router)
dp.include_router(admin_router)
dp.include_router(commands_router)
dp.include_router(grope_router)
dp.include_router(filter_router)
dp.include_router(user_group_router)


async def main() -> None:
    # session = AiohttpSession(proxy=PROXY)
    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)
    bot.my_admins_list = [ADMIN_ID]
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=group, scope=types.BotCommandScopeAllGroupChats())
    await dp.start_polling(bot)
print('run')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())



