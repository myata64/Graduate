# Pycharm пометки

### Поиск и замена
- `CTRL + R` - Замена внутри файла
- `CTRL + SHIFT + R` - Замена внутри директории.
- `CTRL + N` - Поиск внутри файла
- `CTRL + SHIFT + N` - Поиск внутри директории.

# Подключение к репозиторию

`git clone git@github.com:myata64/CredoRep.git` </br>
`git branch -M dev`</br>
`git push -u origin dev`

# Docker. Работа сервера

При запущенном контейнеры любые изменения(имена классов, ссылки, изображения) в html в браузере будут обновляться автоматически.
- Проверка на занятость портов: `sudo lsof -i :5433`</br>
- `sudo docker run --name my-postgres -e`
- Пересборка контейнера: `sudo docker-compose build` </br>
- Запуск контейнеров: </br>
  `sudo docker-compose up -d` </br>
  `sudo docker-compose exec web python manage.py migrate` </br>
  `sudo docker-compose exec web python manage.py runserver 0.0.0.0:8000`
- Проверка на занятость портов: `sudo lsof -i :5433`</br>
- Откройте веб-браузер и перейдите по адресу http://localhost:8000 </br>


- Работа внутри БД: </br>
`sudo docker-compose exec db psql -U myata64 -d clothing_store` </br>
`\dt` - просмотр таблиц </br>
`\d <table_name>` -  просмотр схемы таблицы


- интерфейс контейнера БД:
  `docker-compose exec db psql -U postgres` </br>
- вход в режим работы с БД:
  `psql` </br>

`sudo docker-compose stop` - остановить работу контейнеров </br>
`sudo docker-compose down` - удалить контейнеры </br>
`sudo docker-compose ps` - просмотр списка запущенных контейнеров

# Миграции

Скорее всего для работы с postgre придется установить модуль **psycopg2**.

- Но прежде чем это сделать нужно установить зависимости:</br>
  `sudo apt-get install libpq-dev python3-dev` </br>
- После можно устанавливать сам модуль **psycopg2**: </br>
  `pip3 install psycopg2` </br>
- Чтобы сделать миграции должен быть запущен postgres-контейнер: </br>
  `sudo docker-compose up -d` </br>
- Ну и теперь мы можем делать миграции (докер будет выводить в консоль журнал, потому следющую команду нужно выполнять в другой консоли): </br>
  `sudo docker-compose exec web python manage.py migrate`

### Ошибки
#### Ошибка создания таблиц
- Ни раз я сталкивался с ошибкой создания таблиц. По какой то причине, после успешных миграций, таблицы так и не создавались. Именно поэтому мне пришлось узнать о такой команде как: 
</br> `sudo docker-compose exec web python manage.py migrate credo zero` - эта команда откатывает миграции. А затем применял команду: </br> `sudo docker-compose exec web python manage.py migrate`


# Django Admin
login: `admin` </br> 
password: `pass1234`
# Создание БД и таблиц (не обязательно)

`CREATE DATABASE your_database;` </br>
`\c your_database` - переключение на бд </br>
`CREATE TABLE users (
id SERIAL PRIMARY KEY,
name VARCHAR(255)
);`

# Пометки по GIT

git checkout master - смена ветки </br>
git merge dev - обновить ветку master, путем слияния с dev веткой </br>
git commit -m "Merge dev into master" - коммит изменений </br>
git push origin master - отправка изменений </br>
</br># Graduate