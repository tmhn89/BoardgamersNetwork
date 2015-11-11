# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgn_app', '0009_auto_20151110_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_host', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='participants',
            name='event',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='user',
        ),
        migrations.RemoveField(
            model_name='event',
            name='host',
        ),
        migrations.DeleteModel(
            name='Participants',
        ),
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(related_name='memberships', to='bgn_app.Event'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(related_name='memberships', to='bgn_app.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='participant',
            field=models.ManyToManyField(blank=True, related_name='participants', through='bgn_app.Participant', to='bgn_app.User'),
        ),
    ]
