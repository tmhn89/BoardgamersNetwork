# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0006_auto_20151008_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
