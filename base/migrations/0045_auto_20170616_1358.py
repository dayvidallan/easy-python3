# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-16 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_auto_20170607_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aditivo',
            options={'verbose_name': 'Aditivo do Contrato', 'verbose_name_plural': 'Aditivos do Contrato'},
        ),
        migrations.AlterModelOptions(
            name='ataregistropreco',
            options={'verbose_name': 'Ata de Registro de Pre\xe7o', 'verbose_name_plural': 'Atas de Registro de Pre\xe7o'},
        ),
        migrations.AlterModelOptions(
            name='contrato',
            options={'verbose_name': 'Contrato', 'verbose_name_plural': 'Contratos'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='itemquantidadesecretaria',
            options={'verbose_name': 'Pedido de Itens da Secretaria', 'verbose_name_plural': 'Pedidos de Itens da Secretaria'},
        ),
        migrations.AlterModelOptions(
            name='opcaolcn',
            options={'verbose_name': 'Op\xe7\xe3o da LCN', 'verbose_name_plural': 'Op\xe7\xf5es da LCN'},
        ),
        migrations.AlterModelOptions(
            name='pesquisamercadologica',
            options={'verbose_name': 'Pesquisa Mercadol\xf3gica', 'verbose_name_plural': 'Pesquisas Mercadol\xf3gicas'},
        ),
        migrations.AlterField(
            model_name='documentosolicitacao',
            name='nome',
            field=models.CharField(max_length=500, verbose_name='Nome do Arquivo'),
        ),
    ]
