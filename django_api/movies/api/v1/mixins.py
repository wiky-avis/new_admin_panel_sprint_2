import logging

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse

from movies.models import Filmwork


logger = logging.getLogger(__name__)


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ["get"]

    @staticmethod
    def array_agg_person(role: str):
        return ArrayAgg(
            "persons__full_name",
            filter=Q(personfilmwork__role=role),
            distinct=True,
        )

    def get_queryset(self):
        try:
            movies = (
                self.model.objects.prefetch_related("persons", "genres")
                .values(
                    "id",
                    "title",
                    "description",
                    "creation_date",
                    "rating",
                    "type",
                )
                .annotate(
                    genres=ArrayAgg("genres__name", distinct=True),
                    actors=self.array_agg_person(role="actor"),
                    directors=self.array_agg_person(role="director"),
                    writers=self.array_agg_person(role="writer"),
                )
            )
        except Exception:
            logger.warning("Couldn't get a list of movies", exc_info=True)
            return []
        return movies

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)