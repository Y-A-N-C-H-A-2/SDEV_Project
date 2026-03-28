"""Used automatically by gunicorn when the start command omits --bind (e.g. Render default)."""
import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
