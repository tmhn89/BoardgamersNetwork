# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0004_auto_20151007_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendships',
            name='status',
        ),
    ]
