# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-19 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0090_auto_20170919_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelodocumento',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.TipoModelo'),
        ),
        migrations.AddField(
            model_name='modelodocumento',
            name='tipo_objeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.TipoObjetoModelo'),
        ),
    ]
