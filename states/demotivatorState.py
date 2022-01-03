from aiogram.dispatcher.filters.state import State, StatesGroup


class StorageDemotivator(StatesGroup):
    Photo_id = State()
    Line_one = State()
    Line_two = State()