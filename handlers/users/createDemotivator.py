from pathlib import Path

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from .demotivator import Demotivator

from loader import dp, bot
from states import StorageDemotivator

@dp.message_handler(text="🛠 Создать демотиватор")
async def createDemotivator(message: types.Message, state: FSMContext):
    await state.finish()

    await bot.send_message(message.chat.id, "❓ Отправьте мне фотографию")

    await StorageDemotivator.Photo_id.set()

@dp.message_handler(state=StorageDemotivator.Photo_id, content_types=["photo"])
async def getPhoto(message: types.message, state: FSMContext):
    await state.update_data(Photo_id=f"{message.chat.id}.jpg")

    await message.photo[1].download(Path("data", "Photo", f"{message.chat.id}.jpg"))

    await bot.send_message(message.chat.id, "❓ Введите текст для первой строки")

    await StorageDemotivator.Line_one.set()

@dp.message_handler(state=StorageDemotivator.Line_one)
async def getTextLineOne(message: types.message, state: FSMContext):
    await state.update_data(Line_one=message.text)

    await bot.send_message(message.chat.id, "❓ Введите текст для второй строки")

    await StorageDemotivator.Line_two.set()
    
@dp.message_handler(state=StorageDemotivator.Line_two)
async def getTextLineTwo(message: types.message, state: FSMContext):
    await state.update_data(Line_two=message.text)
    data = await state.get_data()

    await state.finish()

    dem = Demotivator(data["Line_one"], data["Line_two"])

    dem.create(file=Path("data", "Photo", f"{message.chat.id}.jpg"), result_filename=Path("data", "Photo", f"{message.chat.id}.jpg"))

    with open(Path("data", "Photo", f"{message.chat.id}.jpg"), "rb") as photo:
        await bot.send_photo(message.chat.id, photo)