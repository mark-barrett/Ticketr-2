# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_organiser_tagline'),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderticket',
            name='ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.Ticket'),
            preserve_default=False,
        ),
    ]
