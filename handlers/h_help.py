from aiogram import Bot, Dispatcher, Router, types
from handlers.config_reader import config
from aiogram.filters.command import Command

# создаем экземпляр бота и диспатчер
dp = Dispatcher()
router = Router()
dp.include_router(router)
bot = Bot(token=config.bot_token.get_secret_value())


# хендлер для комманды help
@dp.message(Command("help"))
async def cmd_help_1(message: types.Message):
    await message.answer("Вот пример того, как cо мной взаимодейстовавать...")
    photo_1 = "https://disk.yandex.ru/i/0nJvrpXn1mjSyg"
    photo_2 = "https://disk.yandex.ru/i/QvJuz5j3Kimg9g"
    await bot.send_photo(message.chat.id, photo_1)
    await message.answer('Выбираем модель и нажимаем кнопку "Подтвердить"')
    await bot.send_photo(message.chat.id, photo_2)
    await message.answer('Если хочешь протестировать, вот команда /example, \
                         отправлю тебе фотографию, которую ты можешь \
                         использовать для моего тестирования.')
