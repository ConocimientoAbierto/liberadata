# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liberacion', '0002_auto_20170111_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesforcebackup',
            name='instagram_user',
        ),
        migrations.AddField(
            model_name='salesforcebackup',
            name='appname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]