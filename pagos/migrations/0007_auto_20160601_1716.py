# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0006_auto_20160601_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagotipo',
            options={'ordering': ('id',)},
        ),
        migrations.RemoveField(
            model_name='pago',
            name='tipo',
        ),
    ]