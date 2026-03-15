#!/bin/bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

gunicorn config.asgi:application \
  -b 0.0.0.0:8000 \
  -k uvicorn.workers.UvicornWorker \
  --workers 4

exit $?
