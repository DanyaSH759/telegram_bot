
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):

    # токен бота
    bot_token: SecretStr

    # Чтение .env файла с кодировйкой с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file='bot/.env',
                                      env_file_encoding='utf-8')


# При импорте файла сразу создастся файл настроек
config = Settings()
