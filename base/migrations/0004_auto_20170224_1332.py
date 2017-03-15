# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_preenche_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemataregistropreco',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='itemataregistropreco',
            name='participante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ParticipantePregao'),
        ),
    ]