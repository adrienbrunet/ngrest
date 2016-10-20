from rest_framework import viewsets

from .models import People
from .serializers import PeopleSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
