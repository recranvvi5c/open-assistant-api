# Docker

`Dockerfile` builds the API image (poetry install, non-root user). The compose file at the
repository root starts Postgres and Redis for local development; it is not a production deployment.

The image expects the app to be served by uvicorn on `APP_SERVER_PORT` and does not run migrations
at start - run `alembic upgrade head` as a separate step.
