from django.views.generic import FormView

from rest_framework import viewsets

from .forms import PeopleForm
from .models import People
from .serializers import PeopleSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class FormView(FormView):
    template_name = 'form.html'
    form_class = PeopleForm
