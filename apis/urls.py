from django.urls import path

from .views import InfoAPIView

urlpatterns = [
    path("<pk>", InfoAPIView.as_view(), name="info_list")
]