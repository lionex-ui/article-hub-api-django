from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from common.pagination import DefaultPagination
from common.tasks import log_event_to_sentry

from .filters import UserFilter
from .models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerializer

    pagination_class = DefaultPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            user_id = response.data["id"]
            email = response.data["email"]

            log_event_to_sentry.delay("USER_CREATED", f"id: {user_id} | email: {email}")

        return response
