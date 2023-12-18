# 🐈 QRkot | Сat сharity fund

## 📝 Описание

Учебный проект для изучения работы во фреймворке FastAPI.

**QRkot** - это API сервиса по сбору средств для финансирования благотворительных проектов. В сервисе реализована возможность регистрации пользователей, добавления благотворительных проектов и пожертвований, которые распределяются по открытым проектам.

Настроено автоматическое создание первого суперпользователя при запуске проекта.

## ⚙️ Создайте в корневой директории файл .env со следующим наполнением:
```
APP_TITLE=Приложение QRKot.
APP_DESC=Спасем котиков вместе!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=secretcat
FIRST_SUPERUSER_EMAIL=user@example.com
FIRST_SUPERUSER_PASSWORD=admin
```

## ⚙️ Инструкция по развёртыванию проекта

* клонировать проект на компьютер `git clone https://github.com/tapp41k/cat_charity_fund.git`
* создание виртуального окружения `python3 -m venv venv`
* запуск виртуального окружения `. venv/bin/activate`
* установить зависимости из файла requirements.txt `pip install -r requirements.txt`
* запуск сервера `uvicorn main:app`
* запуск сервера с автоматическим рестартом `uvicorn main:app --reload`
* инициализируем Alembic в проекте `alembic init --template async alembic`
* создание файла миграции `alembic revision --autogenerate -m "migration name"`
* применение миграций `alembic upgrade head`
* отмена миграций `alembic downgrade`
* запуск тестов `pytest`

<h2> Автор проекта </a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32" width="32"/></h2>

[Илья Осадчий](https://github.com/tapp41k)
