# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0016_auto_20151216_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='lon',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='guild',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='guild',
            name='lon',
            field=models.FloatField(default=0),
        ),
    ]
