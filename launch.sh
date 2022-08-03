#!/usr/bin/env bash

cd /app
pipenv run python3 manage.py collectstatic --no-input
pipenv run python3 manage.py migrate
pipenv run django-admin compilemessages
pipenv run gunicorn -w $GUNICORN_WORKERS -b unix:/var/run/gunicorn/gunicorn.sock project.wsgi
