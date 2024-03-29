from aiogram.filters.base import Filter
from aiogram.types import Message


class MyFilters(Filter):
    def __init__(self, my_text: list):
        self.my_text = my_text

    async def __call__(self, message: Message):
        return message.text == self.my_text
