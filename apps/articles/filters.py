import django_filters
from django.db.models import Q

from .models import Article


class ArticleFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(method="filter_by_tag")
    search = django_filters.CharFilter(method="filter_by_search")

    class Meta:
        model = Article
        fields = ["tag", "search"]

    # noinspection PyMethodMayBeStatic
    def filter_by_tag(self, queryset, name, value):
        return queryset.filter(tags__contains=[value])

    # noinspection PyMethodMayBeStatic
    def filter_by_search(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(content__icontains=value))
