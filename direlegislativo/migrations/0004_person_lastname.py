# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direlegislativo', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='LastName',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
