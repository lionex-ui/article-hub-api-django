from django.urls import path

from .views import ArticleViewMixins

urlpatterns = [
    path("", ArticleViewMixins.as_view(), name="article-list-create"),
    path("<int:pk>/", ArticleViewMixins.as_view(), name="article-detail"),
]
