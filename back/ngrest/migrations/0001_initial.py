# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 14:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_this_form_dumb', models.BooleanField()),
                ('favorite_color', models.CharField(choices=[('red', 'red'), ('blue', 'blue')], max_length=50)),
                ('favorite_int', models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)], verbose_name='Favorite integer between 10 and 100')),
                ('favorite_float', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(-10), django.core.validators.MaxValueValidator(10)], verbose_name='Favorite float between -10 and 10')),
                ('best_friend', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngrest.People')),
            ],
        ),
    ]
