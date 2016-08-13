# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'ordering': ('periodo', 'grupo', 'nombre'),
            },
        ),
        migrations.CreateModel(
            name='MantenimientoGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='MantenimientoNombre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimientos.MantenimientoGrupo'),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimientos.MantenimientoNombre'),
        ),
    ]
