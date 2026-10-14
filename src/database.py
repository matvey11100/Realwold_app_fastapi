"""Настройка подключения базы данных"""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

# Ссылка на базу PostgreSQL
DATABASE_URL = settings.database_url

# Создаем асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика для создания сессий базы данных
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    """Базовый класс, от которого будут наследоваться все наши модели (таблицы)"""

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Функция-зависимость (Dependency), которую мы будем передавать в эндпоинты FastApi"""
    async with async_session_maker() as session:
        yield session
