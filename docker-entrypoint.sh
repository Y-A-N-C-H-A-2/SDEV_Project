#!/bin/sh
set -e
# One-shot DB setup for hosts without a shell (e.g. Render free tier). Safe to leave on:
# init-db is idempotent; seed-db no-ops once data exists.
#
# Runs when: AUTO_DB_SETUP is 1/true/yes, OR (AUTO_DB_SETUP unset and DATABASE_URL unset).
# SQLite-only deploys often omit AUTO_DB_SETUP → tables were never created → "no such table".
# Set AUTO_DB_SETUP=0 to skip (e.g. Postgres + only `flask db upgrade`).
_run_setup=0
case "${AUTO_DB_SETUP:-}" in
  1|true|TRUE|yes|YES) _run_setup=1 ;;
  0|false|FALSE|no|NO) _run_setup=0 ;;
  *)
    if [ -z "${DATABASE_URL:-}" ]; then
      _run_setup=1
    fi
    ;;
esac
if [ "$_run_setup" = 1 ]; then
  flask init-db
  flask seed-db
fi
exec gunicorn --bind "0.0.0.0:${PORT:-10000}" --workers "${WEB_CONCURRENCY:-2}" --timeout 120 wsgi:app
