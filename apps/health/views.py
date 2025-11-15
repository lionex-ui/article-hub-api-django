from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


@extend_schema(
    request=None,
    responses={
        200: {"type": "object", "properties": {"status": {"type": "string", "example": "OK"}}, "required": ["status"]}
    },
)
class HealthAPIView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        return Response({"status": "I'm Alive"}, status=status.HTTP_200_OK)
