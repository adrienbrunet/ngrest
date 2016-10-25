import pytz
from datetime import datetime, time

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


COLORS = [
    ('red', 'red'),
    ('blue', 'blue')
]

DEFAULT_DATE = datetime(1990, 1, 2, 6, 30, 0, tzinfo=pytz.utc)
DEFAULT_TIME = time(6, 30, 0)


class People(models.Model):
    """Random model to test a few field inputs"""
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField()
    is_this_form_dumb = models.BooleanField(default=False)
    best_friend = models.ForeignKey('People', null=True, blank=True)
    favorite_color = models.CharField(max_length=50, choices=COLORS)
    favorite_int = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(100)],
                                       default=20,
                                       verbose_name="Favorite integer between 10 and 100")
    favorite_float = models.FloatField(validators=[MinValueValidator(-10), MaxValueValidator(10)],
                                       default=0,
                                       verbose_name="Favorite float between -10 and 10")
    birthday = models.DateField(default=DEFAULT_DATE)
    birthday_plus_time = models.DateTimeField(default=DEFAULT_DATE)
    secret_file = models.FileField(null=True)
    what_time_is_it = models.TimeField(default=DEFAULT_TIME)
    website = models.URLField(blank=True)
    my_image = models.ImageField(null=True)

    def __str__(self):
        return self.name

# TODO
# support:
# - DurationField
# - FileField
# - FilePathField
# - ImageField
# - GenericIPAddressField
# - SlugField
# - TimeField
# - URLField
# - UUIDField
# Adds a hide attributes on the serializer?
# Add extra attr to fields in serializer
# Add placeholder?