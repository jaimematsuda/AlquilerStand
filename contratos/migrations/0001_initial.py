# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locales', '0001_initial'),
        ('inquilinos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('vencimiento', models.DateField()),
                ('monto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cobro', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contratos.Cobro')),
                ('inquilino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inquilinos.Inquilino')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales.Local')),
            ],
            options={
                'ordering': ('local', 'inquilino', 'vencimiento'),
            },
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vigencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='contrato',
            name='moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contratos.Moneda'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='vigencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contratos.Vigencia'),
        ),
        migrations.AlterUniqueTogether(
            name='contrato',
            unique_together=set([('local', 'inquilino', 'inicio')]),
        ),
    ]