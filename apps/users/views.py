from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from common.pagination import DefaultPagination

from .filters import UserFilter
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    pagination_class = DefaultPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
