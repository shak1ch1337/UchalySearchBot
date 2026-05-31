from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.states import Form
from keyboars.reply_keyboard import have_photo_buttons
from config_reader import config


router = Router()


@router.message(F.text.lower() == "начнем")
async def fill_form(message: Message, state: FSMContext):
    await state.set_state(Form.description)
    await message.answer("Сначала введи описание: кого ищешь, где, когда и т.п.")


@router.message(Form.description)
async def form_description(message: Message, state: FSMContext):
    if len(message.text) > 10:
        await state.update_data(description = message.text)
        await state.set_state(Form.is_photo)
        await message.answer(text = "Отлично! Теперь ответь на вопрос: у тебя есть фото?", reply_markup = have_photo_buttons)
    else:
        await message.answer("Слишком маленькое описание, опиши подробнее")


@router.message(Form.is_photo, F.text.casefold().in_(["да, у меня есть фото", "нет, у меня нет фото"]))
async def form_is_photo(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(is_photo = message.text)
    if message.text.lower() == "да, у меня есть фото":
        await state.set_state(Form.photo)
        await message.answer("Теперь пришли фото того, кого ты ищешь")
    elif message.text.lower() == "нет, у меня нет фото":
        data = await state.get_data()
        await state.clear()
        await message.answer("Ничего страшного. Твоя заявка отправляется на модерацию. Если все хорошо, то скоро она появится в чате")
        await bot.send_message(chat_id = config.chat_id.get_secret_value(), text = data["description"])
    else:
        await message.answer(text = "Неопознанная ошибка!")


@router.message(Form.is_photo)
async def incorrect_form_is_photo(message: Message, state: FSMContext):
    await message.answer("Нажми на кнопку")


@router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext, bot: Bot):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()
    await message.answer("Замечательно! Твоя заявка отправляется на модерацию. Если все хорошо, то скоро она появится в чате")
    await bot.send_photo(
        chat_id = config.chat_id.get_secret_value(),
        photo = photo_file_id,
        caption = data["description"]
    )


@router.message(Form.photo, ~F.photo)
async def incorrect_form_photo(message: Message, state: FSMContext):
    await message.answer(text = "Нужно отправить фото!")