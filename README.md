
# Django-React-Typescript-Vite Starter Template

## Stack

- [React](https://reactjs.org/) - A JavaScript library for building user interfaces.
- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [Vite](https://vitejs.dev/) - Next Generation Frontend Tooling
- [Typescript](https://www.typescriptlang.org/) - JavaScript with syntax for types.

## Project structure

```
$PROJECT_ROOT
│   
├── web # backend file
│   
├── frontend # React files
│   
├── web/templates # Django Templates
│   
├── web/static-dev # Django Static Files
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
source bin/activate
```

- Install Dependencies

```
pip install -r requirements.txt
```

> **_NOTE:_**     To Install Latest Dependencies run command <br/>
> ``
> pip install -r required.txt
> ``

- Install Dependencies (For Poetry)

```
poetry install
```

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
cd frontend/
yarn
```
- Run Vite

```
yarn dev
```
<br/>


> **_NOTE:_**     To Use Django & React in With hot reload in Django Templates Run: <br/>
> ``` 
> cd web/
> python manage.py runserver
> ```
> and 
> ```
> cd frontend/
> yarn dev
> ``` 

