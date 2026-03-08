"""
WSGI entry point for Heroku deployment.
App lives at repo root; no path hacks needed.
"""
from app import create_app, db

app = create_app()

# Create tables and seed on startup so Heroku (gunicorn) has a working database
with app.app_context():
    from app import models  # noqa: F401 – ensure all models are registered
    db.create_all()
    from app.seed import seed_database
    seed_database()

if __name__ == "__main__":
    app.run()
