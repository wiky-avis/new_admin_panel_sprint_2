flake8:
	flake8 --config=.flake8

black:
	black . --config pyproject.toml

isort:
	isort .

linters: isort black flake8

up_local:
	docker-compose up -d

build:
	docker-compose up -d --build
