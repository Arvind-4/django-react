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

- Make Migrations

```bash
cd src
python manage.py makemigrations
python manage.py migrate
```
- Run Server

```bash
cd src
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
cd src/ui
pnpm dev
```

- For production 

```bash
cd src/ui
pnpm collectstatic
```
