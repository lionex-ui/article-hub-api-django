from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.pagination import DefaultPagination

from .filters import UserFilter
from .models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    pagination_class = DefaultPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
