import pytest
from django.urls import reverse_lazy

from django_api.tests.vars import MOVIES_DETAIL_RESPONSE


pytestmark = [pytest.mark.django_db]


def test_movies_detail(client, create_movie):
    create_movie()
    url = reverse_lazy(
        "movie_detail", kwargs={"id": "a61bf4b4-f8f2-43f4-993c-29aa15d5d307"}
    )
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == MOVIES_DETAIL_RESPONSE


@pytest.mark.django_db
def test_movies_list(client, create_movie):
    create_movie()
    url = reverse_lazy("movies")
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == {
        "count": 1,
        "next": None,
        "prev": None,
        "results": [MOVIES_DETAIL_RESPONSE],
        "total_pages": 1,
    }


@pytest.mark.parametrize(
    "params, prev_page, next_page",
    (
        ({}, None, 2),
        ({"page": 2}, 1, None),
        ({"page": "last"}, 1, None),
    ),
)
def test_movies_paginator(
    client, create_movies_list, params, prev_page, next_page
):
    create_movies_list(51)
    url = reverse_lazy("movies")
    response = client.get(url, params)
    assert response.status_code == 200
    result = response.json()
    assert result["count"] == 51
    assert result["total_pages"] == 2
    assert result["prev"] == prev_page
    assert result["next"] == next_page
