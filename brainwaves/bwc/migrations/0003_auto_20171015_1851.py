# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-15 18:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bwc', '0002_auto_20171015_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joined',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 10, 15, 18, 51, 17, 131267)),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 10, 15, 18, 51, 17, 134284)),
        ),
        migrations.AlterField(
            model_name='registered',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 10, 15, 18, 51, 17, 127256)),
        ),
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 10, 15, 18, 51, 17, 115558)),
        ),
    ]