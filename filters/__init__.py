from aiogram import Dispatcher

from loader import dp
from .all_filters import IsAdmin

if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    pass
