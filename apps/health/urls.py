from django.urls import path

from apps.health.views import HealthAPIView

urlpatterns = [
    path("", HealthAPIView.as_view(), name="health"),
]
