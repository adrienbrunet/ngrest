from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


COLORS = [
    ('red', 'red'),
    ('blue', 'blue')
]


class People(models.Model):
    """Random model to test a few field inputs"""
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField()
    is_this_form_dumb = models.BooleanField()
    best_friend = models.ForeignKey('People', null=True, blank=True)
    favorite_color = models.CharField(max_length=50, choices=COLORS)
    favorite_int = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(100)],
                                       default=20,
                                       verbose_name="Favorite integer between 10 and 100")
    favorite_float = models.FloatField(validators=[MinValueValidator(-10), MaxValueValidator(10)],
                                       default=0,
                                       verbose_name="Favorite float between -10 and 10")

    def __str__(self):
        return self.name
