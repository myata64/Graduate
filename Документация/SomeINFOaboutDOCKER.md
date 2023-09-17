Создание:

docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 8000:5432 -d postgres

Подключение:

psql -h localhost -p 8000 -U postgres -W

Запуск(наверное):

sudo service postgresql start

Удаление: 

sudo docker stop my-postgres

sudo docker rm my-postgres


Просмотр контейнера:

docker ps -a

Открытие БД:

psql -h localhost -p 8000 -U postgres -d mydatabase


Создание БД + Таблицы:

CREATE DATABASE mydatabase;

CREATE TABLE users (
    id integer,
    name varchar(50)
);

Просмотр таблицы БД

SELECT * FROM users;
