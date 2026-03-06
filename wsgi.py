"""
WSGI entry point for Heroku deployment
"""
import sys
import os

# Add CrossPaths to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CrossPaths'))

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
