# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-31 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetworkItemCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_items', models.PositiveIntegerField(verbose_name='Number of stored items')),
                ('response', models.TextField(verbose_name='Raw response of the API call')),
                ('creation_datetime', models.DateTimeField(verbose_name='When this cache was created')),
                ('type', models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('pinterest', 'Pinterest'), ('rss', 'RSS')], max_length=16, verbose_name='Type')),
                ('rss_url', models.URLField(blank=True, default=None, verbose_name='RSS URL')),
            ],
        ),
    ]
