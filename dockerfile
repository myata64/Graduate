# Базовый образ Python
FROM python:3.9

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории
WORKDIR /code

# Установка зависимостей проекта
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копирование файлов проекта в рабочую директорию
COPY . /code/

RUN python manage.py makemigrations

# Запуск сервера Django
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000

