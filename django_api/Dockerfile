FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install -y postgresql-client --no-install-recommends

WORKDIR /code
COPY . .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

CMD python3 manage.py runserver  0.0.0.0:8000
