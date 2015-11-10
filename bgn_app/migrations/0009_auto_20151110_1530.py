# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0008_auto_20151110_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='guildmembers',
            name='is_leader',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='participants',
            name='is_host',
            field=models.BooleanField(default=False),
        ),
    ]
