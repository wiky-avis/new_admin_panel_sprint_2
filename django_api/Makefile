flake8:
	flake8 --config=.flake8

black:
	black . --config pyproject.toml

isort:
	isort .

linters: isort black flake8



up:
	docker-compose up -d

build:
	docker-compose up -d --build

makemigrations:
	docker-compose exec web python manage.py makemigrations

flush:
	docker-compose exec web python manage.py flush --no-input

migrate:
	docker-compose exec web python manage.py migrate --noinput

static:
	docker-compose exec web python manage.py collectstatic --no-input

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

down:
	docker-compose down -v
