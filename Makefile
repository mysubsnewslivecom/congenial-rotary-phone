SHELL = /bin/bash
.PHONY: start dbbackup lint worker beat black cleanimports clean-lint checkmigrations

start:
	source ~/workspace/venv/venv@rotary_phone/bin/activate && \
	python3 manage.py start

startcelery:
	source ~/workspace/venv/venv@rotary_phone/bin/activate && \
	python3 -m celery -A rotary_phone worker --loglevel info -E

dbbackup:
	source ~/workspace/venv/venv@rotary_phone/bin/activate && \
	python3 manage.py dbbackup

worker:
	python3 -m celery -A adminlte worker --loglevel info --pool=solo

beat:
	python3 -m celery -A adminlte beat --loglevel info

lint:
	python3 -m flake8 --statistics --count .

black:
	python3 -m black .

cleanimports:
	python3 -m isort . --profile black
	python3 -m autoflake -r -i --remove-all-unused-imports --ignore-init-module-imports .

clean-lint: cleanimports black lint

checkmigrations:
	source /home/linux/workspace/venv@adminlte/.env.linux && \
	python3 manage.py makemigrations --check --no-input --dry-run

build: build-celery build-celery-beat build-portal

build-celery:
	docker build . -t celery:local \
		-f Dockerfiles/celery.Dockerfile \
		--build-arg IMAGE_NAME=python \
		--build-arg IMAGE_TAG=3.10-alpine \
		--build-arg DJANGO_PORT=9000 \
		--build-arg GUNICORN_WORKERS=1

build-celery-beat:
	docker build . -t celery-beat:local \
		-f Dockerfiles/celery-beat.Dockerfile \
		--build-arg IMAGE_NAME=python \
		--build-arg IMAGE_TAG=3.10-alpine

build-portal:
	docker build . -t rotary-phone:local \
		-f Dockerfiles/rotaryphone.Dockerfile \
		--build-arg IMAGE_NAME=python \
		--build-arg IMAGE_TAG=3.10-alpine \
		--build-arg DJANGO_PORT=9000 \
		--build-arg GUNICORN_WORKERS=1
