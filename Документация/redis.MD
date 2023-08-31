# Redis 
## docker-compose.yml
```python
# до этого идет другой код
 redis:
    image: redis:6.0.7
    container_name: redis
    restart: always
    volumes:
      - redis_volume_data:/data
    ports:
      - '6379:6379'
  redis_insight:
    image: redislabs/redisinsight:latest
    container_name: redis_insight
    restart: always
    ports:
      - '8001:8001'
    volumes:
      - redis_insight_volume_data:/db
volumes:
  redis_volume_data:
  redis_insight_volume_data:
```


Давай разберём этот docker-compose файл по строкам:

- `redis`: - определяет сервис с именем redis. Всё ниже относится к настройкам этого сервиса.
- `image: redis:6.0.7` - указывает, что для сервиса будет использоваться образ redis версии 6.0.7. Этот образ будет скачан с Docker Hub.
- `container_name: redis` - задаёт имя контейнера, который будет запущен.
- `restart: always` - перезапускать контейнер всегда, если он упадёт.
- `volumes:` - примонтировать тома (папки на хост машине) в контейнер:
- `redis_volume_data:/data` - примонтировать том redis_volume_data в папку /data контейнера.
- `ports:` - опубликовать порты контейнера на хост машине:
- `'6379:6379'` - снаружи порт 6379, внутри контейнера тоже 6379.
Далее аналогично настраивается второй сервис redis_insight для запуска RedisInsight.
- `volumes:` в конце - определяет сами тома, которые монтируются в контейнеры.
- `redis_volume_data:` - том для данных Redis.
- `redis_insight_volume_data:` - том для данных RedisInsight.

В целом, это запустит два контейнера - сам Redis и RedisInsight для управления. Данные будут храниться в томах на хост машине.


- Откройте веб-браузер и перейдите по адресу http://localhost:8001
- 'HOST': redis
- Port: 6379
- Name: redis-local
