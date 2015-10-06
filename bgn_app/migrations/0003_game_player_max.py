# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0002_auto_20151006_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player_max',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
