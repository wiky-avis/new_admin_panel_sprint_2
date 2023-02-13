import logging

from django.conf import settings
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from .mixins import MoviesApiMixin


logger = logging.getLogger(__name__)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = settings.PAGE_SIZE

    def get_context_data(self, *, object_list=None, **kwargs):
        paginator, page, queryset, _ = self.paginate_queryset(
            self.get_queryset(), self.paginate_by
        )
        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": page.previous_page_number()
            if page.has_previous()
            else None,
            "next": page.next_page_number() if page.has_next() else None,
            "results": list(queryset),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        return self.get_queryset()[0] if self.get_queryset() else {}
