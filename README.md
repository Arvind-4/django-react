# Django-React Starter Template

## Stack

- [React](https://reactjs.org/) - A JavaScript library for building user interfaces.
- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [Vite](https://vitejs.dev/) - Next Generation Frontend Tooling
- [Typescript](https://www.typescriptlang.org/) - JavaScript with syntax for types.

## Project structure

```
$PROJECT_ROOT
│   
├── src/backend # backend file
│   
├── src/ui # React files
│   
├── src/templates # Django Templates
│   
├── src/staticfiles # Django Static Files
```
---

### Get the Code

#### For Backend

- Clone Repo

```bash
mkdir django-react
cd django-react
git clone https://github.com/Arvind-4/django-react.git .
```

- Create Virtual Environment for Python

```bash
python3.10 -m pip install virtualenv
python3.10 -m virtualenv .
```

- Activate Virtual Environment

```bash
source bin/activate
```

- Install Dependencies

```bash
cd src
pip install -r requirements.txt
```

- Install Dependencies (For Poetry)

```bash
cd src
poetry install
```

- Generate the secret key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

- Create a `.env` file and copy the contents of the `.env.sample` file into it

```properties
# Django settings
DJANGO_DEBUG=False
DJANGO_LIVE=0
DJANGO_SECRET_KEY=your_secret_key
DJANGO_ALLOWED_HOSTS=*
DJANGO_ADMIN_URL=admin
DJANGO_EMAIL_HOST_USER=your_email
DJANGO_EMAIL_HOST_PASSWORD=your_password
DJANGO_VERCEL=1
DJANGO_IN_REACT=1

# Django superuser credentials
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@gmail.com

# Gunicorn settings
GUNICORN_PORT=8000
GUNICORN_WORKERS=4
GUNICORN_TIMEOUT=120
GUNICORN_LOG_LEVEL=INFO

# Email settings
DJANGO_EMAIL_PORT=
DJANGO_EMAIL_USE_TLS=
DJANGO_EMAIL_HOST_USER=
DJANGO_EMAIL_HOST_PASSWORD=

# HSTS settings
DJANGO_HSTS_SECONDS=
```

- Make Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

- Run Server

```bash
python manage.py runserver
```

####  For Frontend

- Install Dependencies

```bash
cd src/ui
pnpm i
```
- Run Vite

```bash
pnpm dev
```

- For production 

```bash
pnpm collectstatic
```
