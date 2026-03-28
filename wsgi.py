"""
WSGI entry point for production (e.g. gunicorn wsgi:app).
App lives at repo root; no path hacks needed.
Create and seed the database manually when deploying:
  FLASK_APP=wsgi:app flask init-db && FLASK_APP=wsgi:app flask seed-db
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
