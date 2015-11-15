# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0010_auto_20151111_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_leader', models.BooleanField(default=False)),
                ('guild', models.ForeignKey(to='bgn_app.Guild', related_name='memberships')),
                ('user', models.ForeignKey(to='bgn_app.User', related_name='memberships')),
            ],
        ),
        migrations.RemoveField(
            model_name='guildmembers',
            name='guild',
        ),
        migrations.RemoveField(
            model_name='guildmembers',
            name='user',
        ),
        migrations.AlterField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(to='bgn_app.Event', related_name='players'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(to='bgn_app.User', related_name='players'),
        ),
        migrations.DeleteModel(
            name='GuildMembers',
        ),
        migrations.AddField(
            model_name='guild',
            name='member',
            field=models.ManyToManyField(to='bgn_app.User', through='bgn_app.GuildMember', related_name='members', blank=True),
        ),
    ]
