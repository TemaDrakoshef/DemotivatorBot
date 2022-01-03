from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def menu():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(KeyboardButton("🛠 Создать демотиватор"))

    return menu