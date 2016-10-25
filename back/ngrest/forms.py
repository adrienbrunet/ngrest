from django.forms import ModelForm

from .models import People


class PeopleForm(ModelForm):
    class Meta:
        model = People
        exclude = ['id', ]
