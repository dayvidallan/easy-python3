# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-27 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0117_auto_20190124_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentosolicitacao',
            name='publico',
            field=models.BooleanField(default=False, help_text='Se sim, este documento ser\xe1 exibido publicamente', verbose_name='Documento P\xfablico'),
        ),
    ]