# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 15:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ngrest', '0002_auto_20161021_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='birthday',
            field=models.DateField(default=datetime.datetime(1990, 1, 2, 6, 30, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='people',
            name='birthday_plus_time',
            field=models.DateTimeField(default=datetime.datetime(1990, 1, 2, 6, 30, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='people',
            name='secret_file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='people',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='what_time_is_it',
            field=models.TimeField(default=datetime.time(6, 30)),
        ),
    ]