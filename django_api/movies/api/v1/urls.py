from django.urls import path

from . import views


urlpatterns = [
    path("movies/", views.MoviesListApi.as_view(), name="movies"),
    path(
        r"movies/<uuid:id>",
        views.MoviesDetailApi.as_view(),
        name="movie_detail",
    ),
]
