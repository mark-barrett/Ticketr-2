# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_amount_resell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='amount_resell',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='when_resell',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
