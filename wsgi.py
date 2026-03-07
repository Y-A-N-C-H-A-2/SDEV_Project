"""
WSGI entry point for Heroku deployment
"""
import sys
import os

# Add CrossPaths to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CrossPaths'))

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
