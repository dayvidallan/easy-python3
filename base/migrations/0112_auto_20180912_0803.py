# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-12 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0111_auto_20180822_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='ataregistropreco',
            name='data_esgotamento',
            field=models.DateField(null=True, verbose_name='Data de Esgotamento da Ata'),
        ),
        migrations.AddField(
            model_name='itemataregistropreco',
            name='data_esgotamento',
            field=models.DateField(null=True, verbose_name='Data de Esgotamento do Item'),
        ),
    ]