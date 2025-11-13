from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.pagination import DefaultPagination

from .filters import ArticleFilter
from .models import Article
from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer
from .tasks import analyze_article


class ArticleListAndCreateViewMixins(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Article.objects.all().select_related("author")
    serializer_class = ArticleSerializer

    pagination_class = DefaultPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArticleRetrieveAndUpdateAndDestroyViewMixins(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Article.objects.all().select_related("author")
    serializer_class = ArticleSerializer

    pagination_class = DefaultPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ArticleAnalyzeAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    # noinspection PyMethodMayBeStatic
    def post(self, request, pk: int, *args, **kwargs):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(
                {"error": "Article matching query does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        if article.author != request.user:
            return Response(
                {"error": "You do not have permission to analyze this article."},
                status=status.HTTP_403_FORBIDDEN
            )

        analyze_article.delay(pk)

        return Response({"message": "success"}, status=status.HTTP_200_OK)
