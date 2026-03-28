"""
WSGI entry point for production (e.g. gunicorn wsgi:app).
Uses the same app instance as `gunicorn app:app` (see app package).
DB setup: FLASK_APP=wsgi:app flask init-db && flask seed-db
"""
from app import app

if __name__ == "__main__":
    app.run()
