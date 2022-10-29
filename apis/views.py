from rest_framework import generics

from info.models import Info
from .serializers import InfoSerializer

class InfoAPIView(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
