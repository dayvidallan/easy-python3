# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0060_pregao_categoria_suspensao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregao',
            name='categoria_suspensao',
            field=models.CharField(blank=True, choices=[('', '--------------'), ('An\xe1lise de Amostras', 'An\xe1lise de Amostras'), ('Documenta\xe7\xe3o Complementar', 'Documenta\xe7\xe3o Complementar'), ('Impugna\xe7\xe3o', 'Impugna\xe7\xe3o'), ('Parecer T\xe9cnico', 'Parecer T\xe9cnico'), ('Prazo de Recurso', 'Prazo de Recurso'), ('Proposta Final', 'Proposta Final'), ('Revis\xe3o do Processo', 'Revis\xe3o do Processo')], max_length=100, null=True, verbose_name='Situa\xe7\xe3o'),
        ),
    ]
