from random import randint
from aiogram.types import FSInputFile

from aiogram import Bot, Dispatcher, Router, types
from handlers.config_reader import config
from aiogram.filters.command import Command

# создаем экземпляр бота и диспатчер
dp = Dispatcher()
router = Router()
dp.include_router(router)
bot = Bot(token=config.bot_token.get_secret_value())


# Хэндлер на команду /example
@dp.message(Command("example"))
async def cmd_example_1(message: types.Message):
    # выбирается случайная картинка из архива sample
    #  и отправляется пользователю
    await message.answer("Вот случайная картинка из моей библиотеки")
    selection = randint(1, 10)
    file_name = f"./sample/{selection}.jpg"
    image_to_send = FSInputFile(file_name)
    await bot.send_photo(message.chat.id, image_to_send)
