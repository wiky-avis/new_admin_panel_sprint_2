# Проектное задание: Docker-compose

### Запуск
```bash
cd simple_project
```

- Создать env файл
```bash
cp .env.example .env
```

- Собрать контейнеры
для локальной разработки
```bash
make up-local
```
для прода
```bash
make up-prod
```

### Доступные эндпойнты
 - /admin/
 - /api/v1/movies/
