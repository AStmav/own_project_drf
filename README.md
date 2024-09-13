# ## Стек технологий
- Backend: Django 4.x, Django REST Framework 3.x
- Аутентификация: JWT (Django Simple JWT) или Session-based Auth
- База данных: PostgreSQL или SQLite (по умолчанию)
- Документация API: Swagger/OpenAPI (drf-yasg)
- Тестирование: Django Test Framework

## Установка и запуск проекта

### Предварительные требования
- Python 3.8+
- Pip
- Виртуальное окружение (рекомендуется использовать virtualenv или venv)
- PostgreSQL (если не используете SQLite)

### Инструкция по установке

1. Клонируйте репозиторий:

    
    git clone https://github.com/your-username/your-project.git
    cd your-project
    

2. Создайте виртуальное окружение и активируйте его:

    
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
    

3. Установите зависимости:

    
    pip install -r requirements.txt
    

4. Настройте переменные окружения (например, добавьте в проект файл .env):

    - DEBUG: True/False
    - SECRET_KEY: Ваш секретный ключ
    - DATABASE_URL: Строка подключения к базе данных (если не используете SQLite)
    - ALLOWED_HOSTS: Разрешенные хосты

5. Выполните миграции базы данных:

    
    python manage.py migrate
    

6. Создайте суперпользователя:

    
    python manage.py createsuperuser
    

7. Запустите локальный сервер разработки:

    
    python manage.py runserver
    

8. Откройте API-документацию (если настроена):

    - Swagger UI: http://localhost:8000/swagger/
    - Redoc: http://localhost:8000/redoc/

## Примеры использования API

### Аутентификация

- POST /api/token/ — получение JWT токена.
- POST /api/token/refresh/ — обновление токена.

### Пример запроса для создания записи

```bash
POST /api/items/