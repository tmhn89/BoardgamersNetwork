# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0005_remove_friendships_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gametags',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gametags',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='game',
        ),
        migrations.AddField(
            model_name='collection',
            name='game_id',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='main_game',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='GameTags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
