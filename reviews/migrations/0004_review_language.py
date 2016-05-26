# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='language',
            field=models.CharField(choices=[('ENG', 'English'), ('MAL', 'Malayalam'), ('TAM', 'Tamil'), ('HIN', 'Hindi'), ('UNK', 'Unknown')], default='UNK', max_length=3),
        ),
    ]