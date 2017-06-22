# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_auto_20170606_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregao',
            name='recurso_estadual',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Recurso Transferido (Estadual)'),
        ),
        migrations.AlterField(
            model_name='pregao',
            name='recurso_federal',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Recurso Transferido (Federal)'),
        ),
        migrations.AlterField(
            model_name='pregao',
            name='recurso_municipal',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Recurso Transferido (Municipal)'),
        ),
        migrations.AlterField(
            model_name='pregao',
            name='recurso_proprio',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Recurso Pr\xf3prio'),
        ),
        migrations.AlterField(
            model_name='pregao',
            name='valor_total',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Valor Total Or\xe7ado'),
        ),
    ]