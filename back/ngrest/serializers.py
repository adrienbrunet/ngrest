from django.db.models.fields import NOT_PROVIDED

from rest_framework import serializers

from .models import People


class NgRestModelSerializer(serializers.ModelSerializer):
    def build_standard_field(self, field_name, model_field):
        """
        Create regular model fields.
        Adds field default
        """
        field_class, field_kwargs = super(NgRestModelSerializer, self).build_standard_field(field_name, model_field)
        if model_field.default is not NOT_PROVIDED:
            field_kwargs['default'] = model_field.default
        return field_class, field_kwargs


class PeopleSerializer(NgRestModelSerializer):
    class Meta:
        model = People
        fields = ('name', 'age', 'email', 'favorite_int', 'favorite_float',
                  'favorite_color', 'is_this_form_dumb', 'best_friend',
                  'website', 'what_time_is_it', 'birthday_plus_time',
                  'birthday',
                  # 'pk', 'id',
                  )
