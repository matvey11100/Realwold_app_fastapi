"""Модуль запуска сервера"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Адрес запущенного фронтенда
origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
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
