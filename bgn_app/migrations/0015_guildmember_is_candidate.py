# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20151008184735 on 2015-12-09 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0014_auto_20151117_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildmember',
            name='is_candidate',
            field=models.BooleanField(default=False),
        ),
    ]
