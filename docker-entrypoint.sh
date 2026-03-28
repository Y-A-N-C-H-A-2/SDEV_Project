#!/bin/sh
set -e
# One-shot DB setup for hosts without a shell (e.g. Render free tier). Safe to leave on:
# init-db is idempotent; seed-db no-ops once data exists.
case "${AUTO_DB_SETUP:-}" in
  1|true|TRUE|yes|YES)
    flask init-db
    flask seed-db
    ;;
esac
exec gunicorn --bind "0.0.0.0:${PORT:-10000}" --workers "${WEB_CONCURRENCY:-2}" --timeout 120 wsgi:app
