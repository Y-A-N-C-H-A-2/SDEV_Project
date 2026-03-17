web: gunicorn --bind 0.0.0.0:$PORT wsgi:app
release: FLASK_APP=wsgi:app flask init-db && FLASK_APP=wsgi:app flask seed-db
