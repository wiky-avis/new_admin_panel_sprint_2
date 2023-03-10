#!/bin/sh

if [ "$DATABASE" = "Postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"

fi

python manage.py migrate
python manage.py collectstatic --no-input

uwsgi --strict --ini uwsgi.ini

exec "$@"
