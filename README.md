# Realwold_app_fastapi
Fastapi implementation of realworld app

Ссылка на используемую спецификацию OpenAPI
https://github.com/realworld-apps/realworld/blob/main/specs/api/openapi.yml

В качестве фронтенда для тестов пока что использую реализацию на Angular20:
https://github.com/TomislavVinkovic/realworld-app-angular-v20

Требования:
Python 3 (3.11.4 использую)

1. Clone the repository
git clone https://github.com/matvey11100/Realwold_app_fastapi.git
cd Realwold_app_fastapi

### Установка и запуск

**1. Установи uv**

Инструкции для Windows, macOS и Linux: https://docs.astral.sh/uv/getting-started/installation/

**2. Синхронизируй зависимости проекта**

```bash
uv sync
```

Команда создаст виртуальное окружение `.venv` (если его ещё нет) и установит зависимости из `pyproject.toml` и lock-файла.

**3. Запусти приложение**

```bash
uv run uvicorn src.main:app --reload
```

При необходимости предварительно настрой переменные окружения в соответствии с конфигурацией приложения.

Запуск фронтенда в формате разработки (angular) (node.js 18):
ng serve
