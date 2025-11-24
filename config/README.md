# Configuration

Settings are declared in `app/core/config.py` and read from the environment (or `.env`).

- `APP_*` - process behaviour: prefix, debug flag, workers.
- `DATABASE_*` - SQLAlchemy URL and pool sizes.
- `REDIS_*` - stream and cache connection.
- `OPENAI_*` - upstream provider keys; a run uses the assistant's model unless overridden.

Nothing in this directory is secret. Keep credentials in `.env`, which is ignored.
