#!/bin/bash

set -e

if [ -z ${POSTGRES_DB+x} ]; then
  echo "PostgreSQL is not used. Skipping wait-for-it...";
  echo "Using SQLite. Creating database...";
else
  echo "Using PostgreSQL. Waiting for it to be ready...";
  /opt/venv/bin/wait-for-it -s "$POSTGRES_HOST:$POSTGRES_PORT" -t 60
  echo "PostgreSQL is ready.";
fi

echo "Running makemigrations..."
/opt/venv/bin/python /app/src/manage.py makemigrations --noinput
echo "Completed makemigrations."

echo "Running migrate..."
/opt/venv/bin/python /app/src/manage.py migrate --noinput
echo "Completed migrate."

echo "Running CreateSuperUser..."
USER_EXISTS="from django.contrib.auth import get_user_model; User = get_user_model(); exit(User.objects.exists())"
/opt/venv/bin/python /app/src/manage.py shell -c "$USER_EXISTS" && /opt/venv/bin/python /app/src/manage.py createsuperuser --noinput
echo "Completed CreateSuperUser."

echo "Running collectstatic..."
/opt/venv/bin/python /app/src/manage.py collectstatic --noinput
echo "Completed collectstatic."

exec "$@"