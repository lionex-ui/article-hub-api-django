from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.pagination import DefaultPagination

from .filters import ArticleFilter
from .models import Article
from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer


class ArticleViewMixins(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Article.objects.all().select_related()
    serializer_class = ArticleSerializer

    pagination_class = DefaultPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthorOrReadOnly]

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data["author"] = request.user.id
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
