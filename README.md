# Incident API

Минимальный FastAPI сервис для учёта инцидентов.

---

## 1. Настройка окружения

1. Скопируйте пример файла `app/backend/main/src/core/env_files/.env.example` в `app/backend/main/src/core/env_files/.env`:

2. Отредактируйте .env, указав свои значения для переменных, например:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
POSTGRES_DB=incidents_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

## 2. Сборка образов

```bash
docker compose build
```


## 3. Применение миграций Alembic

```bash
docker compose run --rm main_alembic
docker compose run --rm main_alembic upgrade head
```

## 4. Запуск сервиса
```bash
docker compose up
```

теперь сервис доступен по адрессу `localhost:9092`

чтобы получить документацию перейдите по адрессу `localhost:9092/api/docs`

## 5. Пример эндпоинтов

1. Создать инцидент
```bash
POST /api/v1/incidents/
Content-Type: application/json

{
  "description": "Самокат не отвечает",
  "status": "new",
  "source": "operator"
}
```
2. Получить список инцидентов по фильтру
```bash
POST /api/v1/incidents/list
Content-Type: application/json

{
  "status": "NEW"
}

```


3. Частично обновить инцидент
```bash
PATCH /api/v1/incidents/{uuid}
Content-Type: application/json

{
  "status": "CLOSED"
}

```