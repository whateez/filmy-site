# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20160606_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=movies.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='movie',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]