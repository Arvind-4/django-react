
# Django-React-Typescript-Webpack Starter Template

## Stack

- [React](https://reactjs.org/) - A JavaScript library for building user interfaces.
- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [Webpack](https://webpack.js.org/) - Bundle Your Assets
- [Typescript](https://www.typescriptlang.org/) - JavaScript with syntax for types.

## Project structure

```
$PROJECT_ROOT
│   # backend file
├── backend
│   # React files
├── src
│   # Django Templates
├── templates
│   
```
---

### Get the Code

#### For Backend

- Clone Repo

```
mkdir django_react
cd django_react
git clone https://github.com/Arvind-4/django-react-typescript-webpack.git .
```
- Create Virtual Environment for Python

```
pip install virtualenv
python -m venv .
```

- Activate Virtual Environment

```
source Scripts/activate
```

- Install Dependencies

```
pip install -r requirements.txt
```

> **_NOTE:_**     To Install Latest Dependencies run command <br/>
> ``
> pip install -r required.txt
> ``

- Make Migrations

```
python manage.py makemigrations
python manage.py migrate
```
- Run Server

```
python manage.py runserver
```

####  For Frontend

- Install Dependencies

```
yarn install
```
- Run Webpack

```
yarn dev
```
