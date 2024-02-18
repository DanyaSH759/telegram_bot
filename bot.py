import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command

from handlers.config_reader import config
from handlers.h_start import cmd_start_1
from handlers.h_help import cmd_help_1
from handlers.h_example import cmd_example_1
from handlers.h_test import cmd_test_1
from handlers.h_load_data_user import process_photo_1, handle_csv_file_1


router = Router()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()
dp.include_router(router)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await cmd_start_1(message)


# Хэндлер на команду /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await cmd_help_1(message)


# Хэндлер на команду /example
@dp.message(Command("example"))
async def cmd_example(message: types.Message):
    await cmd_example_1(message)
    # await bot.send_photo(message.chat.id, example())


# Хэндлер на команду /test
@dp.message(Command("test"))
async def cmd_test(message: types.Message):
    await cmd_test_1(message)


# загрузка фотографии пользователя
@dp.message(F.photo)
async def process_photo(message: types.Message):
    await process_photo_1(message)


# загрузка файлов csv пользователя
@dp.message()
async def handle_csv_file(message: types.Message):
    await handle_csv_file_1(message)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
