# Local development

1. `cp .env.example .env` and set `DATABASE_URL` if you are not using the compose stack.
2. `docker compose -f docker-compose.middleware.yml up -d` starts Postgres and Redis.
3. `poetry install` then `poetry run alembic upgrade head`.
4. `poetry run uvicorn app.main:app --reload --port 8086`.

Run `make test` for the unit tests that do not need either service. The API prefix defaults to
`/api`, so the generated docs are at `http://localhost:8086/docs`.
