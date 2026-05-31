import asyncio
from aiogram import Bot, Dispatcher
from handlers import commans_handler, messages_handler, questionare
from config_reader import config


bot = Bot(config.bot_token.get_secret_value())     # Create Bot
dp = Dispatcher()   #   Create Dispatcher


#   Include routers
dp.include_routers(
    commans_handler.router,
    messages_handler.router,
    questionare.router
)


async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    
    asyncio.run(main())