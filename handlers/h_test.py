from aiogram import Bot, Dispatcher, Router, types
from handlers.config_reader import config
from aiogram.filters.command import Command


# создаем экземпляр бота и диспатчер
dp = Dispatcher()
router = Router()
dp.include_router(router)
bot = Bot(token=config.bot_token.get_secret_value())


# Хэндлер на команду /test
@dp.message(Command("test"))
async def cmd_test_1(message: types.Message):
    await message.answer("Это тест для pytest")
