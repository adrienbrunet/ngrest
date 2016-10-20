from rest_framework import serializers

from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('name', 'email', 'favorite_int', 'favorite_float', 'favorite_color', 'is_this_form_dumb', 'best_friend')
