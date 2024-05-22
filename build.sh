#!/bin/bash

echo "Upgrade pip..."
python -m pip install --upgrade pip

echo "Installing dependencies..."
python -m pip install -r requirements.txt

# echo "Migrating database..."
# python manage.py makemigrations --noinput
# python manage.py migrate --noinput

# echo "Creating superuser..."

# DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
# DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
# DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

# python manage.py createsuperuser \
#     --email $DJANGO_SUPERUSER_EMAIL \
#     --noinput || true

echo "Running npm install..."
pnpm bootstrap

echo "Running npm Production..."
pnpm collect

echo "Collecting static files..."
python src/manage.py collectstatic --noinput --clear