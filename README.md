

````markdown
# my-django-app

Простой Django проект с регистрацией, авторизацией и профилем пользователя.

---

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/jasperBLCK/my-django-app.git
   cd my-django-app-main
````

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/MacOS
   source venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции базы данных:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

---

## Основные URL пути

| URL              | Назначение               | Метод    | Описание                                     |
| ---------------- | ------------------------ | -------- | -------------------------------------------- |
| `/`              | Главная страница         | GET      | Отображает домашнюю страницу                 |
| `/register/`     | Регистрация пользователя | GET/POST | Форма регистрации нового пользователя        |
| `/login/`        | Вход пользователя        | GET/POST | Форма авторизации                            |
| `/profile/view/` | Профиль пользователя     | GET      | Просмотр профиля (только для авторизованных) |
| `/logout/`       | Выход из системы         | GET      | Выход пользователя и удаление cookie         |

---

## Рекомендуемое расширение для VSCode

Для удобной работы с Python в VSCode используйте [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack).

---

## Примечание

* Для корректной работы аутентификации требуется, чтобы в браузере были включены cookie.
* При разработке включен режим `DEBUG=True`. Для продакшена настройте `ALLOWED_HOSTS` и отключите режим отладки.

```
