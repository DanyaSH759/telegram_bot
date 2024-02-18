import pytest
from aiogram_tests import MockedBot
from aiogram_tests.handler import MessageHandler
from aiogram_tests.types.dataset import MESSAGE
from handlers.h_test import cmd_test_1
from handlers.h_start import cmd_start_1


# тестирование ручки /test
@pytest.mark.asyncio
async def test_message_handler_1():
    requester = MockedBot(request_handler=MessageHandler(
        cmd_test_1, auto_mock_success=True))
    calls = await requester.query(MESSAGE.as_object(text="/test"))
    answer_message = calls.send_message.fetchone().text
    assert answer_message == "Это тест для pytest"


# тестирование ручки /start
@pytest.mark.asyncio
async def test_message_handler_2():
    requester = MockedBot(request_handler=MessageHandler(
        cmd_start_1, auto_mock_success=True))
    calls = await requester.query(MESSAGE.as_object(text="/start"))
    answer_message = calls.send_message.fetchone().text
    text = 'Привет! Это тестовый бот для тестирования \
работы разных фишек и кода. \n\n \
Для справки список всех команд:\n\n \
/help - отправит скриншоты как работает \
оригинал бота с определнием зверушки на фото.\n\n \
/example - отправит случайные фотографии из архива.\n\n \
/test - отрпалвяет тестовое сообщение в чат. \n\n \
Так же боту можно отправить офтографии \
или csv файл и они будут скачены'
    assert answer_message == text
