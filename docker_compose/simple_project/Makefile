up:
	docker-compose up -d

build:
	docker-compose up -d --build

makemigrations:
	docker-compose exec service python manage.py makemigrations

flush:
	docker-compose exec service python manage.py flush --no-input

migrate:
	docker-compose exec service python manage.py migrate --noinput

static:
	docker-compose exec service python manage.py collectstatic --no-input

createsuperuser:
	docker-compose exec service python manage.py createsuperuser

down:
	docker-compose down -v
