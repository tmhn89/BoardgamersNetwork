# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0007_auto_20151103_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
                ('hq', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GuildMembers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_leader', models.BooleanField()),
                ('guild', models.ForeignKey(to='bgn_app.Guild')),
            ],
        ),
        migrations.RemoveField(
            model_name='friendships',
            name='from_person',
        ),
        migrations.RemoveField(
            model_name='friendships',
            name='to_person',
        ),
        migrations.RemoveField(
            model_name='user',
            name='friendships',
        ),
        migrations.AddField(
            model_name='participants',
            name='is_host',
            field=models.BooleanField(default=datetime.datetime(2015, 11, 10, 8, 25, 11, 581331, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FriendShips',
        ),
        migrations.AddField(
            model_name='guildmembers',
            name='user',
            field=models.ForeignKey(to='bgn_app.User'),
        ),
    ]
