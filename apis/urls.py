from django.urls import path

from .views import InfoAPIView

urlpatterns = [
    path("", InfoAPIView.as_view(), name="info_list")
]