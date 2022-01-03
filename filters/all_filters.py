from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS

class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if str(message.chat.id) in ADMINS:
            return True
        else:
            return False