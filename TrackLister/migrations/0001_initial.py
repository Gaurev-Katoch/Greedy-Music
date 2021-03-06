# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-30 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=100)),
                ('artist', models.CharField(blank=True, max_length=100)),
                ('album', models.CharField(blank=True, max_length=100)),
                ('genres', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.CharField(blank=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')], max_length=1, null=True)),
            ],
        ),
    ]
