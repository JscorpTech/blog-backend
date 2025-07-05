#!/bin/bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

gunicorn  --workers 2 -b 0.0.0.0:8000 config.wsgi:application


exit $?


