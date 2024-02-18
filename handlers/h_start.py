from aiogram import Bot, Dispatcher, Router, types
from handlers.config_reader import config
from aiogram.filters.command import Command

# создаем экземпляр бота и диспатчер
dp = Dispatcher()
router = Router()
dp.include_router(router)
bot = Bot(token=config.bot_token.get_secret_value())


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start_1(message: types.Message):

    text = 'Привет! Это тестовый бот для тестирования \
работы разных фишек и кода. \n\n \
Для справки список всех команд:\n\n \
/help - отправит скриншоты как работает \
оригинал бота с определнием зверушки на фото.\n\n \
/example - отправит случайные фотографии из архива.\n\n \
/test - отрпалвяет тестовое сообщение в чат. \n\n \
Так же боту можно отправить офтографии \
или csv файл и они будут скачены'

    text = text.rstrip()

    await message.answer(text)
