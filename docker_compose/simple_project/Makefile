up-local:
	docker-compose -f docker-compose-local.yml up -d --build

up-prod:
	docker-compose -f docker-compose-local.yml -f docker-compose-prod.yml up -d --build

build-local:
	docker-compose -f docker-compose-local.yml up -d --build

build-prod:
	docker-compose -f docker-compose-local.yml up -d --build

makemigrations:
	docker-compose -f docker-compose-local.yml exec service python manage.py makemigrations

flush:
	docker-compose -f docker-compose-local.yml exec service python manage.py flush --no-input

migrate:
	docker-compose -f docker-compose-local.yml exec service python manage.py migrate --noinput

static:
	docker-compose -f docker-compose-local.yml exec service python manage.py collectstatic --no-input

createsuperuser:
	docker-compose -f docker-compose-local.yml exec service python manage.py createsuperuser

down:
	docker-compose -f docker-compose-local.yml down -v
