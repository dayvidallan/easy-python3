# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-25 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0081_auto_20170822_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregao',
            name='objeto',
            field=models.TextField(null=True, verbose_name='Objeto'),
        ),
    ]
