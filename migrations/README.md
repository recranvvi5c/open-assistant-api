# Migrations

Alembic revisions live here. Create one with:

```bash
poetry run alembic revision --autogenerate -m "add the column"
```

Review the generated file before committing - autogenerate does not see server defaults, indexes
added outside SQLAlchemy, or data backfills. Apply with `poetry run alembic upgrade head`.
