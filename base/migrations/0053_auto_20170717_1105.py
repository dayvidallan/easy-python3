# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-17 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0052_ataregistropreco_fornecedor_adesao_arp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaolicitacao',
            name='tipo_aquisicao',
            field=models.CharField(choices=[('Licita\xe7\xe3o', 'Licita\xe7\xe3o'), ('Dispensa', 'Dispensa de Licita\xe7\xe3o (Outros)'), ('Dispensa de Licita\xe7\xe3o (At\xe9 R$ 8.000,00)', 'Dispensa de Licita\xe7\xe3o (At\xe9 R$ 8.000,00 - Aquisi\xe7\xe3o de Bens ou Servi\xe7os Comuns)'), ('Dispensa de Licita\xe7\xe3o (At\xe9 R$ 15.000,00)', 'Dispensa de Licita\xe7\xe3o (At\xe9 R$ 15.000,00 - Obras ou Servi\xe7os de Engenharia)'), ('Inexigibilidade', 'Inexigibilidade de Licita\xe7\xe3o'), ('Credenciamento', 'Credenciamento'), ('Chamada P\xfablica - Alimenta\xe7\xe3o Escolar', 'Chamada P\xfablica - Alimenta\xe7\xe3o Escolar'), ('Chamada P\xfablica - Outros', 'Chamada P\xfablica - Outros'), ('Chamada P\xfablica - PRONATER', 'Chamada P\xfablica - PRONATER')], default='Licita\xe7\xe3o', max_length=50, verbose_name='Tipo de Aquisi\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='solicitacaolicitacaotmp',
            name='tipo_aquisicao',
            field=models.CharField(choices=[('Licita\xe7\xe3o', 'Licita\xe7\xe3o'), ('Dispensa', 'Dispensa de Licita\xe7\xe3o (Outros)'), ('Dispensa de Licita\xe7\xe3o (At\xe9 R$ 8.000,00)', 'Dispensa de Licita\xe7\xe3o (At\xe9 R$ 8.000,00 - Aquisi\xe7\xe3o de Bens ou Servi\xe7os Comuns)'), ('Dispensa de Licita\xe7\xe3o (At\xe9 R$ 15.000,00)', 'Dispensa de Licita\xe7\xe3o (At\xe9 R$ 15.000,00 - Obras ou Servi\xe7os de Engenharia)'), ('Inexigibilidade', 'Inexigibilidade de Licita\xe7\xe3o'), ('Credenciamento', 'Credenciamento'), ('Chamada P\xfablica - Alimenta\xe7\xe3o Escolar', 'Chamada P\xfablica - Alimenta\xe7\xe3o Escolar'), ('Chamada P\xfablica - Outros', 'Chamada P\xfablica - Outros'), ('Chamada P\xfablica - PRONATER', 'Chamada P\xfablica - PRONATER')], default='Licita\xe7\xe3o', max_length=50, verbose_name='Tipo de Aquisi\xe7\xe3o'),
        ),
    ]
