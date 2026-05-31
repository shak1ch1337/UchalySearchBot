from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboars import reply_keyboard


#   Create router
router = Router()


#   Start command
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text = "Добро пожаловать в бота по поиску людей в городе Учалы! Жми на кнопку, чтобы найти человека", 
                         reply_markup = reply_keyboard.start_buttons)