from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "RealWorld API"
    debug: bool = False
    database_url: str

    # Настройки CORS
    cors_origin: list[str] = [
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ]  # Значения по умолчанию для локальной разработки
    cors_allow_credentials: bool = True

    # Настройки для чтения .env файла
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Лишние переменные в .env игнорируем
        )

settings = Settings()
