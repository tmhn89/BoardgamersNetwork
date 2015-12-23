# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0017_auto_20151216_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
