# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-15 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0104_auto_20180424_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemataregistropreco',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]