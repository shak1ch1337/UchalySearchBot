from aiogram import Router, F
from aiogram.types import Message

from keyboars.reply_keyboard import fsm_buttons


router = Router()


@router.message(F.text.lower() == "отправить анкету на поиск")
async def send_post(message: Message):
    await message.answer(text = "Итак, для отправки анкеты по поиску тебе нужно указать описание (кого ищешь, где видел (-а), в какой время и т.д), а также " \
    "фото (но если у тебя его нет, то ничего страшного). Начнем?", reply_markup = fsm_buttons)