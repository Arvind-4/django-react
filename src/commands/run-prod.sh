#!/bin/bash

cd /app/src

APP_PORT=${GUNICORN_PORT:-8000}

if [ "$1" = "--debug" ]; then
  /opt/venv/bin/python /backend/manage.py runserver "0.0.0.0:$APP_PORT"
else
  /opt/venv/bin/gunicorn "backend.wsgi:application" --bind "0.0.0.0:$GUNICORN_PORT" --workers "$GUNICORN_WORKERS" --timeout "$GUNICORN_TIMEOUT" --log-level "$GUNICORN_LOG_LEVEL"
fi