# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20180205_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
