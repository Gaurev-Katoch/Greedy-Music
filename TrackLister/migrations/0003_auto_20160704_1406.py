# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-04 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackLister', '0002_auto_20160630_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='genre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
