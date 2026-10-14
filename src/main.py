"""Модуль запуска сервера"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=["*"],  # Разрешаем GET, POST, PUT, DELETE
    allow_headers=["*"],  # Разрешаем все заголовки (включая Authorization: Token...)
)

@app.get("/")
async def get_main_page():
    """Стандартная страница"""
    return "Успех"

@app.get("/api/tags")
async def get_tags():
    """Эндпоинт для проверки связи"""
    return {"tags": ["angular", "fastapi", "backend"]}
