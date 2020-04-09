SHELL := /bin/bash

all: build test

build:
	cd deploy/ && docker-compose build  api

superuser:
	cd deploy/ && docker-compose exec api bash scripts/populate_user.sh

up:
	cd deploy/ && docker-compose up api

down:
	cd deploy/ && docker-compose down --remove-orphans

test:
	cd deploy/ && docker-compose exec api bash -c "export DJANGO_CONFIGURATION=Test; python manage.py test"

post:
	cd deploy/ && docker-compose exec api bash -c "scripts/./post.sh"


.PHONY: build up test clean
