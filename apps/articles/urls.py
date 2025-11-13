from django.urls import path

from .views import ArticleListAndCreateViewMixins, ArticleRetrieveAndUpdateAndDestroyViewMixins

urlpatterns = [
    path("", ArticleListAndCreateViewMixins.as_view(), name="article-list-create"),
    path("<int:pk>/", ArticleRetrieveAndUpdateAndDestroyViewMixins.as_view(), name="article-detail"),
]
