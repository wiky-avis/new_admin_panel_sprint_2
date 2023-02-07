from django.urls import path

from django_api.movies.api.v1.views import MoviesListApi

urlpatterns = [
    path('movies/', MoviesListApi.as_view()),
    # path('movies/<uuid:pk>/', views.MoviesDetailApi.as_view()),
]
