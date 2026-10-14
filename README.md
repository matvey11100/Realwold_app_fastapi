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

**1. Создание виртуального окружения**

```bash
python -m venv venv
```

**2. Активация виртуального окружения**

Windows — CMD:

```bat
venv\Scripts\activate.bat
```

Windows — PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

macOS / Linux — Bash или Zsh:

```bash
source venv/bin/activate
```

**3. Установка зависимостей**

```bash
pip install uv
```

```bash
uv sync
```

3. Start the development server
```powershell
uvicorn src.main:app --reload
```

Запуск фронтенда в формате разработки (angular) (node.js 18):
ng serve
