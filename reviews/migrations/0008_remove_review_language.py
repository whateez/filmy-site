# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 02:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_review_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='language',
        ),
    ]