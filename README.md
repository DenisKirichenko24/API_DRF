# Реализация API на базе Django Rest Framework

Доступ к сервису осуществляется по JWT токену. Создание,изменение, удаление контента по аутентификации. Без аутентификации разрешено только чтение. 

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/DenisKirichenko24/api_final_yatube.git

cd api_final_yatube

Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver


## Эндпоинты 

api/v1/token/ - получение JWT-токена

api/v1/token/refresh - обновление токена

api/v1/posts/ - получение всех постов

api/v1/posts/{post_id}/ - получение,удаление,редактирование поста по id

api/v1/group/ - получение списка всех групп

api/v1/follow/ - получение списка всех подписчиков или создание подписки
