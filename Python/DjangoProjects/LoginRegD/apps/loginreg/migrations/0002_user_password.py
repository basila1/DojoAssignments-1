# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
