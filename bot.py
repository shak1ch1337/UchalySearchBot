import asyncio
from aiogram import Bot, Dispatcher
from handlers import commans_handler
from config_reader import config


bot = Bot(config.bot_token.get_secret_value())     # Create Bot
dp = Dispatcher()   #   Create Dispatcher


#   Include routers
dp.include_router(
    commans_handler.router
)


async def main():
    bot.delete_webhook(drop_pending_updates = True)
    dp.start_polling(bot)


if __name__ == "__main__":
    
    asyncio.run(main())