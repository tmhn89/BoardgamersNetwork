# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0003_game_player_max'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendShips',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('from_person', models.ForeignKey(related_name='from_people', to='bgn_app.User')),
                ('to_person', models.ForeignKey(related_name='to_people', to='bgn_app.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='friendships',
            field=models.ManyToManyField(related_name='related_to+', through='bgn_app.FriendShips', to='bgn_app.User'),
            preserve_default=True,
        ),
    ]
