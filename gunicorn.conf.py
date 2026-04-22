"""Loaded by gunicorn for bind/timeout when the start command omits them (e.g. Render default)."""
import os

bind = f"0.0.0.0:{os.environ.get('PORT', '10000')}"
# Match Dockerfile: slow uploads / DB work should not hit gunicorn’s 30s default.
timeout = 120
