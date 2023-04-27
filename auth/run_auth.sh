#!/bin/sh

cd auth

python manage.py collectstatic --no-input --clear

python manage.py migrate

python manage.py createsuperuser --noinput

gunicorn auth.wsgi:application --bind 0.0.0.0:8000