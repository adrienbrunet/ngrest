from django.db.models.fields import NOT_PROVIDED
from rest_framework import serializers

from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('name', 'email', 'favorite_int', 'favorite_float', 'favorite_color', 'is_this_form_dumb', 'best_friend')

    def build_standard_field(self, field_name, model_field):
        """
        Create regular model fields.
        """
        field_class, field_kwargs = super(PeopleSerializer, self).build_standard_field(field_name, model_field)
        if model_field.default is not NOT_PROVIDED:
            field_kwargs['default'] = model_field.default
        return field_class, field_kwargs
