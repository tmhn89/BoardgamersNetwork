# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bgn_app', '0014_auto_20151117_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('location', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(to='bgn_app.UserProfile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, to='bgn_app.UserProfile', through='bgn_app.Participant'),
        ),
        migrations.AlterField(
            model_name='guild',
            name='member',
            field=models.ManyToManyField(blank=True, to='bgn_app.UserProfile', related_name='members', through='bgn_app.GuildMember'),
        ),
        migrations.AlterField(
            model_name='guildmember',
            name='user',
            field=models.ForeignKey(to='bgn_app.UserProfile', related_name='memberships'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(to='bgn_app.UserProfile', related_name='players'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
