# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cast_crew',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
    ]
