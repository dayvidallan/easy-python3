# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-01 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0086_comissaolicitacao_data_designacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemcompra',
            name='tipo',
            field=models.CharField(choices=[('Compras', 'Compras'), ('Servi\xe7os', 'Servi\xe7os')], default='Compras', max_length=100, verbose_name='Tipo da Ordem'),
        ),
    ]
