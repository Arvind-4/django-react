.PHONY: help test clean collectstatic migrations ui-install collectstatic-ui clean-static collect dev venv-activate activate export format bootstrap

help:
	@echo "test - run tests"
	@echo "clean - remove all .pyc files"
	@echo "collectstatic - collect static files"
	@echo "migrations - run migrations"
	@echo "ui-install - install ui dependencies"
	@echo "collectstatic-ui - collect static files from ui"
	@echo "clean-static - remove static files"
	@echo "collect - clean-static and collectstatic-ui"
	@echo "dev - run server"
	@echo "venv-activate - create virtual environment"
	@echo "activate - activate virtual environment"
	@echo "export - export requirements.txt"
	@echo "format - format code"
	@echo "bootstrap - install all dependencies"

test:
	python src/manage.py test

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	
collectstatic:
	python src/manage.py collectstatic --noinput --clear

migrations:
	python src/manage.py makemigrations
	python src/manage.py migrate --noinput

ui-install:
	pnpm install root=./src/ui

collectstatic-ui: 
	cd src/ui && pnpm collectstatic

clean-static:
	rm -rf static-cdn-local
	rm -rf src/staticfiles/js
	rm -rf src/staticfiles/css

collect: clean-static collectstatic-ui 

dev:
	python src/manage.py runserver & cd src/ui && pnpm dev

venv-activate:
	python3.10 -m venv .
	source bin/activate

activate:
	source bin/activate

export:
	bash src/commands/export.sh

format:
	bash src/commands/format.sh
	cd src/ui && pnpm format

bootstrap:
	cd src && poetry install 
	cd src/ui && pnpm install