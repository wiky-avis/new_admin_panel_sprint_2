import random
import uuid

import pytest

from django_api.tests.vars import GENRES, PERSONS, ROLES
from movies.models import (
    Filmwork,
    Genre,
    GenreFilmwork,
    Person,
    PersonFilmwork,
)


@pytest.fixture
def create_movie(db):
    def movie(
        id="a61bf4b4-f8f2-43f4-993c-29aa15d5d307",
        title="Star Slammer",
        rating=3.5,
        type="movie",
    ):
        Filmwork.objects.create(id=id, title=title, rating=rating, type=type)
        Genre.objects.bulk_create(
            (
                Genre(
                    id="120a21cf-9097-479e-904a-13dd7198c1dd", name="Adventure"
                ),
                Genre(
                    id="6c162475-c7ed-4461-9184-001ef3d9f26e", name="Sci-Fi"
                ),
            )
        )
        GenreFilmwork.objects.bulk_create(
            (
                GenreFilmwork(
                    id=uuid.uuid4(),
                    genre_id="120a21cf-9097-479e-904a-13dd7198c1dd",
                    film_work_id=id,
                ),
                GenreFilmwork(
                    id=uuid.uuid4(),
                    genre_id="6c162475-c7ed-4461-9184-001ef3d9f26e",
                    film_work_id=id,
                ),
            )
        )
        Person.objects.bulk_create(
            (
                Person(
                    id="d524fed5-3900-4ced-b448-83ae7e1c6bdd",
                    full_name="James Gleason",
                ),
                Person(
                    id="00d1e9e5-c569-4d09-a492-bb4ddec83b6f",
                    full_name="James Wallis",
                ),
                Person(
                    id="01820cd1-e5a9-46a5-a3f0-cf56abfcaa09",
                    full_name="Leyla Bolookat",
                ),
            )
        )
        PersonFilmwork.objects.bulk_create(
            (
                PersonFilmwork(
                    id=uuid.uuid4(),
                    person_id="d524fed5-3900-4ced-b448-83ae7e1c6bdd",
                    film_work_id=id,
                    role="actor",
                ),
                PersonFilmwork(
                    id=uuid.uuid4(),
                    person_id="00d1e9e5-c569-4d09-a492-bb4ddec83b6f",
                    film_work_id=id,
                    role="director",
                ),
                PersonFilmwork(
                    id=uuid.uuid4(),
                    person_id="01820cd1-e5a9-46a5-a3f0-cf56abfcaa09",
                    film_work_id=id,
                    role="writer",
                ),
            )
        )

    return movie


@pytest.fixture
def create_movies_list(db):
    def movies(movies_count=1, movies_genres=None, movies_persons=None):
        objs_filmworks = (
            Filmwork(
                id=uuid.uuid4(),
                title=f"Star Witness {i}",
                rating=5,
                type="movie",
            )
            for i in range(movies_count)
        )
        filmworks = Filmwork.objects.bulk_create(objs_filmworks)
        if movies_genres:
            objs_genres = (
                Genre(
                    id=genre.get("id"),
                    name=genre.get("name"),
                )
                for genre in GENRES
            )
            genres = Genre.objects.bulk_create(objs_genres)
            for film in filmworks[:movies_genres]:
                genrefilmworks = (
                    GenreFilmwork(
                        id=uuid.uuid4(),
                        genre_id=genre.id,
                        film_work_id=film.id,
                    )
                    for genre in genres
                )
                GenreFilmwork.objects.bulk_create(genrefilmworks)
        if movies_persons:
            objs_persons = (
                Person(
                    id=person.get("id"),
                    full_name=person.get("full_name"),
                )
                for person in PERSONS
            )
            persons = Person.objects.bulk_create(objs_persons)
            for film in filmworks[:movies_persons]:
                personfilmworks = (
                    PersonFilmwork(
                        id=uuid.uuid4(),
                        person_id=person.id,
                        film_work_id=film.id,
                        role=random.choice(ROLES),
                    )
                    for person in persons
                )
                PersonFilmwork.objects.bulk_create(personfilmworks)

    return movies
