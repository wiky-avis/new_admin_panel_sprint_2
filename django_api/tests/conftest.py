import uuid

import pytest

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
            [
                Genre(
                    id="120a21cf-9097-479e-904a-13dd7198c1dd", name="Adventure"
                ),
                Genre(
                    id="6c162475-c7ed-4461-9184-001ef3d9f26e", name="Sci-Fi"
                ),
            ]
        )
        GenreFilmwork.objects.bulk_create(
            [
                GenreFilmwork(
                    id="001dd75b-85b7-40b0-8317-328c86ff7d12",
                    genre_id="120a21cf-9097-479e-904a-13dd7198c1dd",
                    film_work_id=id,
                ),
                GenreFilmwork(
                    id="f808f59a-f7ba-4440-8a5b-801651e69376",
                    genre_id="6c162475-c7ed-4461-9184-001ef3d9f26e",
                    film_work_id=id,
                ),
            ]
        )
        Person.objects.bulk_create(
            [
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
            ]
        )
        PersonFilmwork.objects.bulk_create(
            [
                PersonFilmwork(
                    id="d2a4bdaa-b767-4d4e-b623-3f3fbac7e8da",
                    person_id="d524fed5-3900-4ced-b448-83ae7e1c6bdd",
                    film_work_id=id,
                    role="actor",
                ),
                PersonFilmwork(
                    id="d2a4bdaa-b767-4d4e-b623-3f3fbac7e8d1",
                    person_id="00d1e9e5-c569-4d09-a492-bb4ddec83b6f",
                    film_work_id=id,
                    role="director",
                ),
                PersonFilmwork(
                    id="d2a4bdaa-b767-4d4e-b623-3f3fbac7e8d2",
                    person_id="01820cd1-e5a9-46a5-a3f0-cf56abfcaa09",
                    film_work_id=id,
                    role="writer",
                ),
            ]
        )

    return movie


@pytest.fixture
def create_movies_list(db):
    def movies(count_movies=5):
        objs = [
            Filmwork(
                id=uuid.uuid4(),
                title=f"Star Witness {i}",
                rating=5,
                type="movie",
            )
            for i in range(count_movies)
        ]
        Filmwork.objects.bulk_create(objs)

    return movies
