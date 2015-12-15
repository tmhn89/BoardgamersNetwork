# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0015_auto_20151212_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img_url',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guild',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guild',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guild',
            name='main_game',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='main_game',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='guild',
            name='img_url',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
