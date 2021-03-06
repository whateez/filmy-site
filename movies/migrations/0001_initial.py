# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 02:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='movie_artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.artist')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='movie_artist',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.role'),
        ),
        migrations.AddField(
            model_name='movie',
            name='cast_crew',
            field=models.ManyToManyField(through='movies.movie_artist', to='movies.artist'),
        ),
    ]
