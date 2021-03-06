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
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.PositiveIntegerField()),
                ('numero', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('piso', 'tipo', 'numero', 'division'),
            },
        ),
        migrations.CreateModel(
            name='LocalDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='LocalTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.AddField(
            model_name='local',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='locales.LocalDivision'),
        ),
        migrations.AddField(
            model_name='local',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales.LocalTipo'),
        ),
        migrations.AlterUniqueTogether(
            name='local',
            unique_together=set([('tipo', 'numero', 'division')]),
        ),
    ]
