# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_pregao_republicado'),
    ]

    operations = [
        migrations.CreateModel(
            name='CnaeSecundario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30, verbose_name='C\xf3digo')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'CNAE Secund\xe1rio',
                'verbose_name_plural': 'CNAES Secund\xe1rios',
            },
        ),
        migrations.CreateModel(
            name='FornecedorCRC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porte_empresa', models.CharField(choices=[('MEI - Microempreendedor Individual', 'MEI - Microempreendedor Individual'), ('Pequena empresa', 'Pequena empresa'), ('M\xe9dia empresa', 'M\xe9dia empresa'), ('M\xe9dia-grande empresa', 'M\xe9dia-grande empresa'), ('Grande empresa', 'Grande empresa')], max_length=100, verbose_name='Porte da Empresa')),
                ('data_abertura', models.DateField(verbose_name='Data de Abertura da Empresa')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=100, null=True, verbose_name='Inscri\xe7\xe3o Estadual')),
                ('inscricao_municipal', models.CharField(blank=True, max_length=100, null=True, verbose_name='Inscri\xe7\xe3o Municipal')),
                ('natureza_juridica', models.CharField(max_length=500, verbose_name='Natureza Jur\xeddica')),
                ('ramo_negocio', models.CharField(max_length=500, verbose_name='Ramo do Neg\xf3cio')),
                ('cnae_primario_codigo', models.CharField(max_length=30, verbose_name='C\xf3digo do CNAE Prim\xe1rio')),
                ('cnae_primario_descricao', models.CharField(max_length=500, verbose_name='Descri\xe7\xe3o do CNAE Prim\xe1rio')),
                ('objetivo_social', models.CharField(max_length=5000, verbose_name='Objetivo Social')),
                ('capital_social', models.CharField(blank=True, max_length=100, null=True, verbose_name='Capital Social (R$)')),
                ('data_ultima_integralizacao', models.DateField(blank=True, null=True, verbose_name='Data da \xdaltima Integraliza\xe7\xe3o')),
                ('banco', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banco')),
                ('agencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ag\xeancia')),
                ('conta', models.CharField(blank=True, max_length=200, null=True, verbose_name='Conta')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('nome', models.CharField(max_length=500, verbose_name='Nome')),
                ('rg', models.CharField(max_length=20, verbose_name='Carteira de Identidade')),
                ('rg_emissor', models.CharField(max_length=20, verbose_name='\xd3rg\xe3o Expedidor ')),
                ('data_expedicao', models.DateField(verbose_name='Data de Expedi\xe7\xe3o')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('email', models.CharField(max_length=200, verbose_name='Email ')),
                ('validade', models.DateField(verbose_name='Validade')),
            ],
            options={
                'verbose_name': 'Certificado de Registro Cadastral',
                'verbose_name_plural': 'Certificados de Registros Cadastrais',
            },
        ),
        migrations.CreateModel(
            name='SocioCRC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('nome', models.CharField(max_length=500, verbose_name='Nome')),
                ('rg', models.CharField(max_length=20, verbose_name='Carteira de Identidade')),
                ('rg_emissor', models.CharField(max_length=20, verbose_name='\xd3rg\xe3o Expedidor ')),
                ('data_expedicao', models.DateField(verbose_name='Data de Expedi\xe7\xe3o')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('email', models.CharField(max_length=200, verbose_name='Email ')),
                ('crc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.FornecedorCRC', verbose_name='CRC')),
            ],
            options={
                'verbose_name': 'S\xf3cio',
                'verbose_name_plural': 'S\xf3cios',
            },
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='agencia',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='banco',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='conta',
        ),
        migrations.AddField(
            model_name='fornecedorcrc',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Fornecedor', verbose_name='Fornecedor'),
        ),
        migrations.AddField(
            model_name='cnaesecundario',
            name='crc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.FornecedorCRC', verbose_name='CRC'),
        ),
    ]