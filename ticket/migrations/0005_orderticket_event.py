# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_organiser_tagline'),
        ('ticket', '0004_auto_20180227_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderticket',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
            preserve_default=False,
        ),
    ]
