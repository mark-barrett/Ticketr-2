# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_organiser_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='paypal_email',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
