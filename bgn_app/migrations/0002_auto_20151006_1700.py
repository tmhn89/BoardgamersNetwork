# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='gametags',
            old_name='game_id',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='gametags',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='participants',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='participants',
            old_name='user_id',
            new_name='user',
        ),
    ]
