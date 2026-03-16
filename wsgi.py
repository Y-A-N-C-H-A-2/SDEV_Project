"""
WSGI entry point for Heroku deployment.
App lives at repo root; no path hacks needed.
Database tables and seed are run via release phase (Procfile) or manually:
  flask init-db && flask seed-db
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
