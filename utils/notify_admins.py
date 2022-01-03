import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен\nСпонсор данного бота: https://lolz.guru/threads/2904830/", disable_web_page_preview=True)

        except Exception as err:
            logging.exception(err)
