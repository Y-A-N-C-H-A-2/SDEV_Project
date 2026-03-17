web: gunicorn --bind 0.0.0.0:$PORT wsgi:app
release: set -e && FLASK_APP=wsgi:app flask init-db && FLASK_APP=wsgi:app flask seed-db
