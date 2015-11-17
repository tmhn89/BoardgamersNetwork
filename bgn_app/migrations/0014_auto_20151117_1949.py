# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0013_auto_20151117_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participant',
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(to='bgn_app.User', through='bgn_app.Participant', blank=True),
        ),
    ]
