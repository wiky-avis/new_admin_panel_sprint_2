# API для кинотеатра

API возвращающий список фильмов и позволяющий получить информацию об одном фильме.

## Тестирование

### Установить зависимости
```bash
pip install poetry==1.1.13
poetry install --no-root && poetry shell
```

### Собрать контейнеры
```bash
make up
```

### Миграции
```bash
make migrate
```

### Запуск тестов:
```bash
cp .env.test .env
pytest
```

### Swagger
http://127.0.0.1:8080/
