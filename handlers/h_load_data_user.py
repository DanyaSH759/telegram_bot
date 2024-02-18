from aiogram import Bot, Dispatcher, Router, types
from pathlib import Path
from handlers.config_reader import config

# создаем экземпляр бота и диспатчер
dp = Dispatcher()
router = Router()
dp.include_router(router)
bot = Bot(token=config.bot_token.get_secret_value())


# загрузка фотографии пользователя
async def process_photo_1(message: types.Message):
    # счетчик файлов в папке
    folder = Path('./user_photo')
    count = len(list(folder.iterdir()))
    # получаем фотографию
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    # скачивания файла в папку
    file_path = file.file_path
    await bot.download_file(file_path,
                            f"./user_photo/{message.from_user.id}-{count}.jpg")
    await message.answer("Скачал фотографию себе")


# Загрузка файлов от пользователя
async def handle_csv_file_1(message: types.Message):

    folder = Path('./user_file')
    count = len(list(folder.iterdir()))

    file_id = message.document.file_id
    file = await bot.get_file(file_id)

    file_path = file.file_path
    await bot.download_file(file_path,
                            f"./user_file/{message.from_user.id}-{count}.csv")
    await message.answer("Скачиваю файл")
