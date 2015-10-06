# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('venue', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('player_min', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GameTags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('game_id', models.ForeignKey(to='start.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.ForeignKey(to='start.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='participants',
            name='user_id',
            field=models.ForeignKey(to='start.User'),
        ),
        migrations.AddField(
            model_name='gametags',
            name='tag_id',
            field=models.ForeignKey(to='start.Tag'),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(to='start.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='main_game',
            field=models.ForeignKey(to='start.Game'),
        ),
        migrations.AddField(
            model_name='collection',
            name='game_id',
            field=models.ForeignKey(to='start.Game'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user_id',
            field=models.ForeignKey(to='start.User'),
        ),
    ]
