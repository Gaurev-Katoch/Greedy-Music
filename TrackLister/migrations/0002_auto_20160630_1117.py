# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-30 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackLister', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracks',
            name='genres',
        ),
        migrations.AddField(
            model_name='tracks',
            name='genres',
            field=models.ManyToManyField(blank=True, to='TrackLister.Genres'),
        ),
    ]